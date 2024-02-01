# The study of Python

__MacOS__

Mac OS X Yosemite (2015)
> fanhonglingdeMacBook-Pro:~ fanhongling$ sw_vers -productVersion
> 10.10.4

Python3: <https://www.macports.org/install.php#installing>
> fanhonglingdeMacBook-Pro:~ fanhongling$ python3 -VV | head -1
> Python 3.8.18 (default, Aug 25 2023, 02:55:01) 

VirtualBox (virtulization) - <https://www.virtualbox.org/wiki/Download_Old_Builds>
> fanhonglingdeMacBook-Pro:lang-learn fanhongling$ VBoxManage --version
> 6.0.24r139119

Vagrant: (command line to provide VM) - <https://www.vagrantup.com/>
> fanhonglingdeMacBook-Pro:~ fanhongling$ vagrant --version | awk -F' ' '{print $2}'
> 2.2.6

__Exercise Resurces__

Python documentation - <https://docs.python.org/3/index.html>

Popular website, for example:
+ <https://www.geeksforgeeks.org/python-programming-language/?ref=shm>
+ <https://datagy.io/sklearn-random-forests/>

Machine Learning and Neural Network
+ NumPy - <https://numpy.org/doc/stable/user/index.html>
+ Scikit-Learn - <https://scikit-learn.org/stable/user_guide.html>
+ PyTorch - <https://pytorch.org/tutorials/>

__Jupter Notebook__

notebook 4.0.0 + Python3.8: <./jupyter-notebook-MacOSX.txt>
+ incompleted: may be installed but jupyter kernel not connected)

notebook 6.0.0 + Python3.1x: <./jupyter-notebook-MacOSX-py31x.txt>

__Anaconda__

Ubuntu 18.04 - Anaconda3: <./conda.md>
+ https://conda.io/docs/user-guide/install/linux.html
+ https://www.anaconda.com/download/#linux

__Pip and VirtualEnv__

pip and setuptools: <./ensurepip-MacOSX.txt>, <./get-pip.txt>
+ https://stackoverflow.com/questions/77364550/attributeerror-module-pkgutil-has-no-attribute-impimporter-did-you-mean
+ https://docs.python.org/3/library/ensurepip.html
+ https://docs.python.org/3.12/whatsnew/3.12.html#distutils
+ https://docs.python.org/3.12/whatsnew/3.12.html#ensurepip
+ https://pip.pypa.io/en/stable/installation/
    
Mac OS X - Python2.7 virtual env: <./py2-venv-mac.txt>
+ https://virtualenv.pypa.io/en/latest/installation/
+ https://github.com/pypa/virtualenv
+ https://pip.pypa.io/en/stable/installing/
+ https://github.com/pypa/pip

Ubuntu 18.04 - Python and pip, venv: <./py-venv.txt>
+ https://docs.python.org/3/using/unix.html#on-linux
+ https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/


