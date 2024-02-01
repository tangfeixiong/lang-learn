# Contents

_Vagrant provided VM_

Ubuntu Bionic (18.04) - vagrant log - networking issue: [vagrant.txt](./vagrant.txt)

**NumPy**

Jupyter notebook
- numpy_userguide_gettingstarted_quickstart.ipynb <https://numpy.org/devdocs/user/quickstart.html>
- numpy_userguide_gettingstarted_2_basicforbeginners.ipynb <https://numpy.org/doc/stable/user/absolute_beginners.html>

Python3.12 - Matplotlib
+ install >= 3.5.0: clang error
+ install >=1.5.0 < 3.5.0: AttributeError: module 'configparser' has no attribute 'SafeConfigParser'. Did you mean: 'RawConfigParser'?

https://bugs.python.org/issue45173
```
fanhonglingdeMacBook-Pro:python fanhongling$ python3.12 -c "import configparser; dir(configparser.SafeConfigParser)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
AttributeError: module 'configparser' has no attribute 'SafeConfigParser'. Did you mean: 'RawConfigParser'?
fanhonglingdeMacBook-Pro:python fanhongling$ python3.11 -c "import configparser; print(type(configparser.SafeConfigParser))"
<class 'abc.ABCMeta'>
```

python3.11
+ Matplotlib==3.2.0: <https://github.com/matplotlib/matplotlib/blob/v3.2.0/INSTALL.rst#installing-from-source>
+ rpds-py==0.13.0: notebook dependency. Higher version should build error
+ notebook==6.0.0: [matplotlib-python31x-MacOSX.txt](matplotlib-python31x-MacOSX.txt)
+ pandas==2.2.0
    
**Scikit-Learn**

Nov 22 2018 - Scikit-Learn 0.20 - Install, build and run examples: [scikit-learn.txt](./scikit-learn.txt)
+ Installation
    - https://github.com/scikit-learn/scikit-learn#user-installation
    - https://github.com/numpy/numpy/blob/master/INSTALL.rst.txt
    - https://github.com/scipy/scipy/blob/master/INSTALL.rst.txt
+ Build scikit-learn
    - https://scikit-learn.org/stable/developers/advanced_installation.html#linux
    - https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/appveyor/requirements.txt
    - https://github.com/scikit-learn/scikit-learn/blob/master/Makefile 

Mac OS X - Install Scikit-Learn 0.20 and run examples: [scikit-learn-mac.txt](./scikit-learn-mac.txt)

_Plot isotonic regression_
![屏幕快照 2018-11-22 上午9.49.21.png](屏幕快照%202018-11-22%20上午9.49.21.png)

_Plot multioutput face completion_
![屏幕快照 2018-11-22 上午9.57.29.png](屏幕快照%202018-11-22%20上午9.57.29.png)

_Plot multilabel_
![屏幕快照 2018-11-22 上午10.01.23.png](屏幕快照%202018-11-22%20上午10.01.23.png)

## exercise2401

[MacPorts](https://www.macports.org/) and pip - issue in installing package: [issue2401-MacOS.txt](./issue2401-MacOS.txt)

**Python3.8:**

Matplotlib
- Python3.8: matplotlib==3.2.0: <https://github.com/microsoft/pylance-release/issues/2374#issuecomment-1049658946>
- Python3.11: matplotlib==3.2.0

Pandas
- AttributeError: 'DataFrame' object has no attribute 'append': <https://appdividend.com/2023/07/26/attributeerror-dataframe-object-has-no-attribute-append/>
- Python3.8: Pandas==1.5.2, PyArrow==1.0.1, FastParquet==0.4.0: <https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/install.html#other-data-sources>

FastParquet and PyArrow
- PyArrow (>9) unenable to build
- PyArrow [6, 9] can be installed with Pandas 2.0.3, but leading segment fault
- If PyArrow not installed, FastParquet could not be found by Pandas 2.0.3: via pandas.show_versions()
- PyArrow==1.0.1, FastParquet==0.4.0

Seaborn
- The get_dataset_names() failed with SSLCertVerificationError <https://github.com/mwaskom/seaborn/issues/2418#issuecomment-755469511>
- Lower version of get_dataset_names() return empty
    The code to request dataset_names.txt use bad github raw url. Just update get_dateset_names() code in <installed python's site-package dir>/seaborn/utils.py with Github master version

```
>>> sns.get_dataset_names()
[]
>>> sns.__version__
'0.12.2'
```

```
def get_dataset_names():
    """Report available example datasets, useful for reporting issues.

    Requires an internet connection.

    """
    DATASET_SOURCE = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master"
    DATASET_NAMES_URL = f"{DATASET_SOURCE}/dataset_names.txt"
    with urlopen(DATASET_NAMES_URL) as resp:
        txt = resp.read()

    dataset_names = [name.strip() for name in txt.decode().split("\n")]
    return list(filter(None, dataset_names))
    '''
    url = "https://github.com/mwaskom/seaborn-data"
    with urlopen(url) as resp:
        html = resp.read()

    pat = r"/mwaskom/seaborn-data/blob/master/(\w*).csv"
    datasets = re.findall(pat, html.decode())
    return datasets
    '''
```

Torch
- Higher version work failed in old Mac, installed 1.6.0

Torchvision package
- Torchvision 0.7.0 requires pillow>=4.1.1
- Install Pillow requires compiling with jpeg library files






