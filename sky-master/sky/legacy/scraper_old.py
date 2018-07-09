import sys
sys.path.append("/Users/pascal/egoroot/sky_package/sky/")
from utils import *
from training import *
from findLeaf import *
from bs4 import BeautifulSoup

def uniqifyOverTraining(list_of_lists):
    uniques = []    
    for x in list_of_lists[0]: 
        if all([bool(x in y) for y in list_of_lists]):
            uniques.append(x)
        return uniques        

def findParentIdentifiers(x, soup, nLevel=3):
    parents = [] 
    try:
        for parent_attrs in [parent.attrs for parent in x.parents][:nLevel]:
            if len(soup.findAll(**{"attrs" : parent_attrs})) == 1:
                parents.append({"attrs" : parent_attrs})
        for parent_attrs in [{"name" : parent.name} for parent in x.parents][:nLevel]:
            if len(soup.findAll(**{"name" : parent.name})) == 1:
                parents.append({"name" : parent.name})
    except:
        pass
    return parents
    
def findSharedKeyValues(training, trainingLeafs):    
    case_options = [] 
    for soup, case in zip(training.soups, trainingLeafs): 
        options = [] 
        for leaf in case: 
            options.extend(findParentIdentifiers(leaf, soup)) 
            options.extend(findByTag(leaf, soup)) 
        case_options.append(options) 
    shared_options = [] 
    for option in case_options[0]: 
        if all([bool(option in case) for case in case_options]): 
            shared_options.append(option)
    return shared_options        
                        
def findByTag(node, soup, nLevel=5): 
    goodTags = []
    tags = []
    tags.extend([x.name for x in node.parents][:nLevel])
    try:
        tags.append(node.name)
    except:
        pass    
    for tag in tags: 
        if len(soup.findAll(tag)) == 1:
            goodTags.append({"name" : tag}) 
    return goodTags        

def secondLevelDown(soup, outcome, unique_keys): 
    solution = []
    num = 0
    for unique_key in unique_keys:
        num += 1 
        #attempt = soup
        #for key in unique_key: ik denk dat ik hier bedoedle dat ik ook halve matches kan doen
        attempt = soup.find(**unique_key)
        if attempt.text == outcome:
            solution.append([unique_key, BeautifulSoup.get_text])
            
        if stripReasonableWhite(attempt.text) == stripReasonableWhite(outcome):
            solution.append([unique_key, BeautifulSoup.get_text, stripReasonableWhite])

        splitting = splitN(attempt.text, outcome)    
        if splitting:
            for splitable in splitting:    
                solution.append([unique_key, BeautifulSoup.get_text, splitSolution(splitable)]) 
    return solution

def stripReasonableWhite(x):
    return re.sub(r"\s+", " ", x).strip()
    
def splitN(txt, outcome):
    # consider splitting to get result
    txt = stripReasonableWhite(txt)
    outcome = stripReasonableWhite(outcome)
    splitables = set(txt.replace(outcome, '', 1)) - set(' ') 
    options = set()
    for s in splitables:
        for i, x in enumerate(txt.split(s)):
            if stripReasonableWhite(x) == stripReasonableWhite(outcome):
                options.add((s, i))
    return options            

def splitSolution(how):
    def solution(txt):
        return txt.split(how[0])[how[1]]
    return solution    
    
def asNumeric(x): 
    return re.sub("[^0-9]", "", x)


def applySolutionChain(solution, x): 
    for sol in solution: 
        if isinstance(sol, dict):
            x = x.find(**sol)
        else:    
            x = sol(x)
    return x    

def buildSolution(training):
    res = findLeaf(training)
    print("len(res)", len(res))
    x = findSharedKeyValues(training, res)
    print("len(shared)", len(x))
    solutions = secondLevelDown(training.soups[0], training.targets[0], x)
    print("len(solutions)", len(solutions))
    return solutions

def testAutoScraperSolutions(autoScraper, training, verbose = False):
    num = 0
    any_succes = False
    for solution in autoScraper: 
        num += 1
        if all([applySolutionChain(solution, soup) == target for soup, target in zip(training.soups, training.targets)]):
            result = "SUCCESFULL" 
            any_succes = True
        else: 
            result = "UNSUCCESFULL"
        if verbose:    
            print("Scraper method: ", num, " was ", result)
    return any_succes    

def tryUniqueID(c, sp):
    return len(sp.findAll(c.name, attrs=c.attrs)) == 1

def buildNewSolution(tr):
    childs = []
    num = 0
    options = []
    for soup, target in zip(tr.soups, tr.targets):
        print('num',num)
        num+=1
        for c in soup.findChildren():
            try:
                if c.name not in ['body', 'html']:
                    if target in c.text:
                        childs.append([c,  len(c.text)])
            except:
                pass        

        tmp = []            
        for i,x in enumerate(childs[::-1]): 
            if tryUniqueID(x[0], soup):
                attrs = x[0].attrs
                attrs['name'] = x[0].name
                attrs = {'attrs' : attrs}
                if x[0].text == target:
                    tmp.append((attrs, BeautifulSoup.get_text))
                elif stripReasonableWhite(x[0].text) == stripReasonableWhite(target):     
                    tmp.append((attrs, BeautifulSoup.get_text, stripReasonableWhite))
                elif splitN(x[0].text, target):    
                    for splitable in splitN(x[0].text, target):
                        tmp.append((attrs, BeautifulSoup.get_text, splitSolution(splitable)))
                else: 
                    print(len([y for y in x[0].children]))
            else:
                print('not unique', len([y for y in x[0].children])) 
        options.append(tmp)
    good_options = [] 
    if options: 
        for x in options[0]:
            if all(x in y for y in options[1:]): 
                good_options.append(x)
    return good_options    
    
#testAutoScraperSolutions(buildSolution(tr), tr, False)

    

# tr1 = Training("marktplaats-testcase1", "/Users/pascal/egoroot/sky_package/sky/tests/").load()

# tr2 = Training("nieuwsdumper-testcase1", "/Users/pascal/egoroot/sky_package/sky/tests/").load()

# tr3 = Training("nieuwsdumper-testcase2", "/Users/pascal/egoroot/sky_package/sky/tests/").load()

# tr4 = Training("bouwmaterieel-testcase1", "/Users/pascal/egoroot/sky_package/sky/tests/").load()

# tr5 = Training("marktplaats-testcase2", "/Users/pascal/egoroot/sky/sky/tests/")

# tr5.addLinks(["http://www.marktplaats.nl/a/telecommunicatie/mobiele-telefoons-samsung/m861980349-hdc-galaxy-s5-nieuw-in-doos.html?c=a2384ef0ece270f44503df9f8598c624&previousPage=lr",
#               "http://www.marktplaats.nl/a/telecommunicatie/mobiele-telefoons-samsung/m862001039-samsung-galaxy-s3-neo.html?c=a2384ef0ece270f44503df9f8598c624&previousPage=lr", "http://www.marktplaats.nl/a/telecommunicatie/mobiele-telefoons-toebehoren-en-onderdelen/m862001036-iphone-3-4-4s-usb-oplaad-snoer.html?c=a2384ef0ece270f44503df9f8598c624&previousPage=lr"])

# tr5.viewAll()

# tr6 = Training("pypi-author", "/Users/pascal/egoroot/sky_package/sky/tests/").load()


# links = ["http://www.forbes.com/sites/rogerkay/2014/11/10/sparkcognition-meets-ibms-watson-starts-conversation/"]


# import justext

# url = "http://www.forbes.com/sites/rogerkay/2014/11/10/sparkcognition-meets-ibms-watson-starts-conversation/"
# html = urllib.urlopen(url).read()
# paragraphs = justext.justext(html, justext.get_stoplist('English'))


# title = "SparkCognition Meets IBM's Watson, Starts Conversation"
# res = []
# for x in paragraphs:
#     if not x.is_boilerplate:
#         res.append(x.text)

# newres = []
# for x in res[res.index(title)+1:]:
#     newres.append(x)

# for x in newres:
#     print(x.encode("ascii", "ignore"))

# res = findLeaf(tr3)

# x = findSharedKeyValues(tr3, res)

# secondLevelDown(tr3.soups[0], tr3.targets[0], x)
        




tr1 = Training("marktplaats-testcase1", "/Users/pascal/egoroot/sky_package/sky/tests/").load()


from collections import Counter        

class SoupStats():
    def __init__(self, soup):
        self.soup = soup
        self.counter = Counter()
        for child in soup.findChildren():
            for atts in child.attrs.items():
                k,v = atts
                self.counter[atts] += 1
                self.counter[k] += 1
                self.counter[v] += 1

z = SoupStats(soup)        
        



counter = Counter()
for child in soup.findChildren():
    for atts in child.attrs.items():
        k,v = atts
        counter[k] += 1
        if isinstance(v, list):
            for l in v:
                counter[(k, l)] += 1
                counter[l] += 1
            counter[(k, " ".join(v))] += 1
        else:    
            counter[atts] += 1
            counter[v] += 1
r
import lxml.html

lxml.html.tostring()

html = 'html'
tree = lxml.html.fromstring(html)

tree.findall('.//*')

from lxml.html import HtmlComment # or similar

no_comments=[element for element in tree if not isinstance(element, HtmlComment)]



tr = Training('betterdoctor-doctor-referalls', '/Users/pascal/egoroot/sky_package/sky/tests/').load()

