
```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/sklearn0.20-python2.7-venv$ git clone -b 0.20.X https://github.com/scikit-learn/scikit-learn github.com/scikit-learn/scikit-learn
Cloning into 'github.com/scikit-learn/scikit-learn'...
remote: Enumerating objects: 28, done.
remote: Counting objects: 100% (28/28), done.
remote: Compressing objects: 100% (24/24), done.
remote: Total 161560 (delta 7), reused 8 (delta 4), pack-reused 161532
Receiving objects: 100% (161560/161560), 93.60 MiB | 124.00 KiB/s, done.
Resolving deltas: 100% (120690/120690), done.
Checking out files: 100% (1207/1207), done.
```

### Linux

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/scikit-learn-0.21-python2.7-venv$ virtualenv venv-linux
New python executable in /Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/scikit-learn-0.21-python2.7-venv/venv-linux/bin/python
Installing setuptools, pip, wheel...
done.
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab$ scikit-learn-0.21-python2.7-venv/venv-linux/bin/python --version
Python 2.7.15rc1
```

### Mac

Default Python2
```
fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ python --version
Python 2.7.6
```

Find Python2.7
```
fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ which python2.7
/usr/bin/python2.7
```

Repository
```
fanhonglingdeMacBook-Pro:github.com fanhongling$ git clone https://github.com/pypa/virtualenv pypa/virtualenv
Cloning into 'pypa/virtualenv'...
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (15/15), done.
remote: Total 6484 (delta 5), reused 5 (delta 1), pack-reused 6468
Receiving objects: 100% (6484/6484), 61.67 MiB ø 158.00 KiB/s, done.
Resolving deltas: 100% (4165/4165), done.
Checking connectivity... done.
```

Install from SRC
```
fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ python github.com/pypa/virtualenv/src/virtualenv.py venv-mac
New python executable in /Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/scikit-learn-0.21-python2.7-venv/venv-mac/bin/python
Installing setuptools, pip, wheel...
done.
```


Activate venv
```
fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ . venv-mac/bin/activate
```

```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ which python
/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/scikit-learn-0.21-python2.7-venv/venv-mac/bin/python
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ python --version
Python 2.7.6
```

Auto-installed pip
```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ which pip
/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/scikit-learn-0.21-python2.7-venv/venv-mac/bin/pip
```

```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ pip --version
pip 18.1 from /Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/scikit-learn-0.21-python2.7-venv/venv-mac/lib/python2.7/site-packages/pip (python 2.7)
```

```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ ls venv-mac/lib/python2.7/site-packages/pip
__init__.py	__init__.pyc	__main__.py	__main__.pyc	_internal	_vendor
```



Pip repository
```
fanhonglingdeMacBook-Pro:github.com fanhongling$ git clone https://github.com/pypa/pip pypa/pip
Cloning into 'pypa/pip'...
remote: Enumerating objects: 29, done.
remote: Counting objects: 100% (29/29), done.
remote: Compressing objects: 100% (22/22), done.
remote: Total 36904 (delta 9), reused 17 (delta 6), pack-reused 36875
Receiving objects: 100% (36904/36904), 48.14 MiB ø 419.00 KiB/s, done.
Resolving deltas: 100% (25317/25317), done.
Checking connectivity... done.
```

### Reference

https://virtualenv.pypa.io/en/latest/installation/

https://github.com/pypa/virtualenv

https://pip.pypa.io/en/stable/installing/

https://github.com/pypa/pip
