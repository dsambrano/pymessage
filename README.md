## First Time Users

If you are unfamilar with the general python package structure and/or don't know what a requirments.txt file is or a virtual environment continue reading, otherwise skip to the [installation section](##installation). When you are working on different projects in python, you often want to install packages (or code that other have created) as such, you might do something like `pip install super-helpful-package`. The problem is you might have a project that requires version 1.2 of super-helpful-package and another project that requires 1.4 uhh ohh... 

This is where the idea of virtual environments come in. You can create virtual environments so that each project has the specific version of each package and the specific version of python that is required. Moreover, since each environment is separate, you don't have to worry about one overwritting another.

The two most common ways are with the [built in](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) `venv` and [Anaconda](https://anaconda.org/) with the [command](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) `conda create`. If you already are using Anaconda to create manage your python/R installation I would use the later, otherwise, the former is pretty easy. When setting up the virtual environment, do not set up with both methods, just pick one of the following then continue onto [Requirments.txt](###requirments.txt) section.



### venv
Using your preferred terminal emulator, `cd` to the directory you will like to store the project. Once there type:

```python3 -m venv tutorial-env```

where tutorial-env is the name you with to give your virtual environment. Next you need to activate your evironment with 

**Unix or MacOS**

```source tutorial-env/bin/activate```

**Windows**

```tutorial-env\Scripts\activate.bat```

Once you complete that step you should notice at the start of each line of your terminal, you should not see your virtual environments name in parentheses like `(tutorial-env) ~/Documents/project`. If you see this you have completed the virtual environment. You can exit a virtual environment at any time with the following command: `deactivate` sometimes `source deactivate` is needed however. Finally, you can remove any environment by first deactivating it and then typing: `rm -r ENV_NAME`, where ENV_NAME is the name of the virtual environment that needs to be removed. 

### Anaconda Environment
Anaconda environments can be accessed from anywhere so you don't need to `cd` to your poject directory, but it is a good idea anyways. Once you are their you can type: 

```conda create -n tutorial-env python=3.10```

This will create a virutal environment called `tutorial-env` and it will automatically install python version 3.10 (latest version at the time of writing). You can specify any version of python after the equal sign (or leave it off for the latest version). Next you need to activate your virtual environment with the following command: 

```conda activate tutorial-env```

Once you complete that step you should notice at the start of each line of your terminal, you should not see your virtual environments name in parentheses like `(tutorial-env) ~/Documents/project`. If you see this you have completed the virtual environment. You can exit a virtual environment at any time with the following command: `conda deactivate` sometimes `source deactivate` is needed however. Finally, you can remove any environment by first deactivating it and then typing: `conda env remove -n ENV_NAME`, where ENV_NAME is the name of the virtual environment that needs to be removed. 

### Requirments.txt

A `requirments.txt` is a file that allows you to install several packages all at once and for them all to be a specific version of each package. This is extremely helpful when you are trying to reproduce another persons virtual environment to allow you to run their code. If you made your own package you could create your `requirments.txt` file from your virtual evironment with one simple command: 

```pip freeze > requirements.txt```

This will use all the packages that have been installed in the active virtual environment and store them into the  `requirments.txt` file. Since it automatically installs all the packages from a virtual environment, its important to have each virtual environment clean (i.e., only include the necessary packages and not have dozens of unused packages). Continue to learn how to install packages from the `requirments.txt` file


## Installation

Once you made your virtual environment, make sure that environment is active, and then install the required packages with the following command (*Note this should go inside the terminal emulator not inside of a python session):

```pip install -r requirements.txt```

This will install all the necessary packages for this to work. Now you can run this code inside that virtual environment. 