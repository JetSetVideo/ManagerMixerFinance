# Installation Guide:

### Virtual Environment on Windows:
py -3 -m venv .venv
.venv\scripts\activate


**Note:** MMF requires Python 3.9+

ManagerMixerFinance can be installed from PyPi. (It's recommended that you install in a virtual environment of your choice).

    pip install ManagerMixerFinance

ManagerMixerFinance has optional dependencies, depending on the backends used. You can install them individually, or all at once. To install ManagerMixerFinance along with all its optional dependencies in one bundle:

    pip install ManagerMixerFinance[all]

If you wish to clone the repository and install from source, run this command from the root of the cloned repository

    python setup.py install

Alternatively, you can install in 'edit' mode (also called development mode):

    python setup.py develop