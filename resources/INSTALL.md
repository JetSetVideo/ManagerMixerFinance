# Installation Guide:

### Virtual Environment on Windows:

#### Run the script below within the directory to create the virtual environment:
> py -3 -m venv env

#### Start the virtual environment run the script below:
> source env/bin/activate
On cmd Windows within the main file:
>.\env\Scripts\activate 
#### Then, to stop it:
> deactivate

### Git Hub, to track dependencies:

#### Install all python libraries from requirements.txt:
py -m pip install -r requirements.txt

#### To export a list of all installed packages:
py -m pip freeze

### The routine for a python project on GitHub:
<ol>
<li>While in the virtual environment, start by installing a python library: </li>
> pip install library
<li>Then stop the virtual environment: </li>
> deactivate
<li>Initialize the repository: </li>
> git init
<li>To include the "env" folder in the .gitignore file so the virtual environment is ignored by source control: </li>
> echo ‘env' > .gitignore
<li>To place the dependencies in a text file to be committed (Freezing reads all the installed dependencies and then produces a text file with the name of the dependency and the installed version number.): </li>
> pip freeze > requirements.txt
<li>To check the file into source control : </li>
> git add requirements.txt
<li>Finally, commit the files and push to a repo. </li>
</ol>

**Note:** MMF requires Python 3.9+

ManagerMixerFinance can be installed from PyPi. (It's recommended that you install in a virtual environment of your choice).

    pip install ManagerMixerFinance

ManagerMixerFinance has optional dependencies, depending on the backends used. You can install them individually, or all at once. To install ManagerMixerFinance along with all its optional dependencies in one bundle:

    pip install ManagerMixerFinance[all]

If you wish to clone the repository and install from source, run this command from the root of the cloned repository

    python setup.py install

Alternatively, you can install in 'edit' mode (also called development mode):

    python setup.py develop