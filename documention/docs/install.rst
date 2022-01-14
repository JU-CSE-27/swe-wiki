Installation
============

Ecommerce is hosted on github and publically available at https://github.com/JU-CSE-27/swe-wiki.
The entire repository can be cloned to your machine directly from github, downloaded as a compressed folder,
or individual files can be downloaded. Repository directories and files are described below.


Operating systems
-----------------

The Ecommerce python code is cross platform (Windows, Mac, Linux), and code for the :code:`View` and :code:`Model` packages has been
tested on Windows (10) operating systems.

Dependencies
------------

1. Python version 3.7.x is recommended.
2. Python IDE:`Visual Studio Code`.
3. Executable:repo:`ecom`

Installing python
-----------------

Python can be installed from a number of sources, including https://www.python.org/downloads/. Anaconda is another option which
provides additional tools for python https://www.anaconda.com/download/. This is a recommended option for novice users.
Python version 3.7.x is recommended.
::
	>> Step 1: Select Version of Python to Install.
	>> Step 2: Download Python Executable Installer.
	>> Step 3: Run Executable Installer.
	>> Step 4: Verify Python Was Installed On Windows.
	>> Step 5: Verify Pip Was Installed.
	>> Step 6: Add Python Path to Environment Variables (Optional)
	>> Step 7: Install virtualnv (Optional)

Check Python Version on Windows
-------------------------------
To check if you already have Python on your Windows machine, first open a command-line application, such as PowerShell.
With the command line open, type in the following command and press :code:`enter`
::	
	>>> python --version
	or
	>>> python -v

Installing modules
------------------

Python modules can be installed with :code:`pip`.

1. Make sure :code:`pip` is up-to-date. From a terminal or the Anaconda command prompt enter the following.
::	
	>>> pip install --upgrade pip

2. Install any dependencies as follows.
::	
	>>> pip install gdal


Full documentation for module dependencies can be found at the following sources.

- gdal http://gdal.org/python/
- numpy https://docs.scipy.org/doc/


Installing Visual Studio Code
-----------------------------
:code:`follow the link` https://code.visualstudio.com/docs

Installing Django in Visual Studio Code
----------------------------------------
:code:`follow the link` https://code.visualstudio.com/docs/python/tutorial-django

Installing Our Django Project
-----------------------------
Download the progect from the github at https://github.com/JU-CSE-27/swe-wiki.

1. In the VS Code Terminal where your virtual environment is activated, run the following command:
::	
	>>> django-admin startproject ecom
	
2. Make development database migrations by running the following command:
::	
	>>> python manage.py makemigrations

3. Make development database models by running the following command:
::	
	>>> python manage.py migrate

4. Reset Django admin password.
::	
	>>> python manage.py createsuperuser
	
5. Run This Django project.
::	
	>>> python manage.py runserver
