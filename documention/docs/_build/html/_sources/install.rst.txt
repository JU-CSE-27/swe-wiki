Installation
============

Ecommerce is hosted on github and publically available at https://github.com/JU-CSE-27/swe-wiki.
The entire repository can be cloned to your machine directly from github, downloaded as a compressed folder,
or individual files can be downloaded. Repository directories and files are described below.


Operating systems
-----------------

The Ecommerce python code is cross platform (Windows, Mac, Linux), and code for the :code:`View` and :code:`Model` packages has been
tested on Windows (10) and Ubuntu (16.04) operating systems.
Dependencies
------------

1. Python version 3.7.x is recommended.
2. Python IDE:`vs code`.
3. Executable:repo:`ecom`

Installing python
-----------------

Python can be installed from a number of sources, including https://www.python.org/downloads/. Anaconda is another option which
provides additional tools for python https://www.anaconda.com/download/. This is a recommended option for novice users.
Python version 2.7.x is recommended.

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