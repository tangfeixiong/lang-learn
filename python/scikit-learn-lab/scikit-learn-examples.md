

## Linux Ubuntu 18.04

vagrant@ubuntu-bionic:~$ . ./scikit-learn-python3.7-venv/bin/activate

(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:~$ cd /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/examples/


(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ python3.7 examples/plot_isotonic_regression.py 

===================
Isotonic Regression
===================

An illustration of the isotonic regression on generated data. The
isotonic regression finds a non-decreasing approximation of a function
while minimizing the mean squared error on the training data. The benefit
of such a model is that it does not assume any form for the target
function such as linearity. For comparison a linear regression is also
presented.


Traceback (most recent call last):
  File "examples/plot_isotonic_regression.py", line 21, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'


(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ pip install matplotlib
Collecting matplotlib
  Downloading https://files.pythonhosted.org/packages/e7/f9/5377596cb1c035c102396f5934237a046f80da69974026f90bee5db8b7ba/matplotlib-3.0.2-cp37-cp37m-manylinux1_x86_64.whl (12.9MB)
    100% |████████████████████████████████| 12.9MB 37kB/s 
Collecting cycler>=0.10 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from matplotlib)
Collecting kiwisolver>=1.0.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/5c/7e/d6cae2f241ba474a2665f24b480bf4e247036d63939dda2bbc4d2ee5069d/kiwisolver-1.0.1-cp37-cp37m-manylinux1_x86_64.whl (89kB)
    100% |████████████████████████████████| 92kB 70kB/s 
Collecting python-dateutil>=2.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/74/68/d87d9b36af36f44254a8d512cbfc48369103a3b9e474be9bdfe536abfc45/python_dateutil-2.7.5-py2.py3-none-any.whl (225kB)
    100% |████████████████████████████████| 235kB 122kB/s 
Requirement already satisfied: numpy>=1.10.0 in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from matplotlib)
Requirement already satisfied: six in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from cycler>=0.10->matplotlib)
Requirement already satisfied: setuptools in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from kiwisolver>=1.0.1->matplotlib)
Installing collected packages: cycler, kiwisolver, python-dateutil, matplotlib
Successfully installed cycler-0.10.0 kiwisolver-1.0.1 matplotlib-3.0.2 python-dateutil-2.7.5



(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ python examples/plot_isotonic_regression.py 

===================
Isotonic Regression
===================

An illustration of the isotonic regression on generated data. The
isotonic regression finds a non-decreasing approximation of a function
while minimizing the mean squared error on the training data. The benefit
of such a model is that it does not assume any form for the target
function such as linearity. For comparison a linear regression is also
presented.


Traceback (most recent call last):
  File "examples/plot_isotonic_regression.py", line 24, in <module>
    from sklearn.linear_model import LinearRegression
ModuleNotFoundError: No module named 'sklearn'



(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ ls build/temp.linux-x86_64-3.7/
libcblas.a  liblibsvm-skl.a  sklearn


(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ python setup.py install
Partial import of sklearn during the build process.
/usr/lib/python3.7/distutils/dist.py:274: UserWarning: Unknown distribution option: 'install_requires'
  warnings.warn(msg)
blas_opt_info:
blas_mkl_info:
customize UnixCCompiler
  libraries mkl_rt not found in ['/home/vagrant/scikit-learn-python3.7-venv/lib', '/usr/local/lib', '/usr/lib', '/usr/lib/x86_64-linux-gnu']
  NOT AVAILABLE

blis_info:
customize UnixCCompiler
  libraries blis not found in ['/home/vagrant/scikit-learn-python3.7-venv/lib', '/usr/local/lib', '/usr/lib', '/usr/lib/x86_64-linux-gnu']
  NOT AVAILABLE

openblas_info:
customize UnixCCompiler
customize UnixCCompiler
  libraries openblas not found in ['/home/vagrant/scikit-learn-python3.7-venv/lib', '/usr/local/lib', '/usr/lib', '/usr/lib/x86_64-linux-gnu']
  NOT AVAILABLE

atlas_3_10_blas_threads_info:
Setting PTATLAS=ATLAS
customize UnixCCompiler
  libraries tatlas not found in ['/home/vagrant/scikit-learn-python3.7-venv/lib', '/usr/local/lib', '/usr/lib', '/usr/lib/x86_64-linux-gnu']
  NOT AVAILABLE

atlas_3_10_blas_info:
customize UnixCCompiler
  libraries satlas not found in ['/home/vagrant/scikit-learn-python3.7-venv/lib', '/usr/local/lib', '/usr/lib', '/usr/lib/x86_64-linux-gnu']
  NOT AVAILABLE

atlas_blas_threads_info:
Setting PTATLAS=ATLAS
customize UnixCCompiler
  libraries ptf77blas,ptcblas,atlas not found in ['/home/vagrant/scikit-learn-python3.7-venv/lib', '/usr/local/lib', '/usr/lib', '/usr/lib/x86_64-linux-gnu']
  NOT AVAILABLE

atlas_blas_info:
customize UnixCCompiler
  libraries f77blas,cblas,atlas not found in ['/home/vagrant/scikit-learn-python3.7-venv/lib', '/usr/local/lib', '/usr/lib', '/usr/lib/x86_64-linux-gnu']
  NOT AVAILABLE

accelerate_info:
  NOT AVAILABLE

/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/distutils/system_info.py:625: UserWarning: 
    Atlas (http://math-atlas.sourceforge.net/) libraries not found.
    Directories to search for the libraries can be specified in the
    numpy/distutils/site.cfg file (section [atlas]) or by setting
    the ATLAS environment variable.
  self.calc_info()
blas_info:
customize UnixCCompiler
  libraries blas not found in ['/home/vagrant/scikit-learn-python3.7-venv/lib', '/usr/local/lib', '/usr/lib', '/usr/lib/x86_64-linux-gnu']
  NOT AVAILABLE

/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/distutils/system_info.py:625: UserWarning: 
    Blas (http://www.netlib.org/blas/) libraries not found.
    Directories to search for the libraries can be specified in the
    numpy/distutils/site.cfg file (section [blas]) or by setting
    the BLAS environment variable.
  self.calc_info()
blas_src_info:
  NOT AVAILABLE

/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/distutils/system_info.py:625: UserWarning: 
    Blas (http://www.netlib.org/blas/) sources not found.
    Directories to search for the sources can be specified in the
    numpy/distutils/site.cfg file (section [blas_src]) or by setting
    the BLAS_SRC environment variable.
  self.calc_info()
  NOT AVAILABLE

sklearn/setup.py:73: UserWarning: 
    Blas (http://www.netlib.org/blas/) libraries not found.
    Directories to search for the libraries can be specified in the
    numpy/distutils/site.cfg file (section [blas]) or by setting
    the BLAS environment variable.
  warnings.warn(BlasNotFoundError.__doc__)
sklearn/manifold/_barnes_hut_tsne.pyx: cannot find cimported module 'sklearn.neighbors'
running install
running build
running config_cc
unifing config_cc, config, build_clib, build_ext, build commands --compiler options
running config_fc
unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
running build_src
build_src
building library "libsvm-skl" sources
building library "cblas" sources
building extension "sklearn.__check_build._check_build" sources
building extension "sklearn.preprocessing._csr_polynomial_expansion" sources
###
### >>> snippets >>>
###
copying sklearn/tree/_criterion.pxd -> /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/sklearn/tree/
copying sklearn/tree/_splitter.pxd -> /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/sklearn/tree/
copying sklearn/tree/_tree.pxd -> /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/sklearn/tree/
copying sklearn/tree/_utils.pxd -> /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/sklearn/tree/
running install_egg_info
Writing /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/scikit_learn-0.21.dev0.egg-info
running install_clib



(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ ls ~/scikit-learn-python3.7-venv/lib64/python3.7/site-packages/sklearn/
__check_build                              cluster                   ensemble            kernel_approximation.py  multioutput.py        setup.py
__init__.py                                compose                   exceptions.py       kernel_ridge.py          naive_bayes.py        svm
__pycache__                                covariance                externals           linear_model             neighbors             tests
_build_utils                               cross_decomposition       feature_extraction  manifold                 neural_network        tree
_config.py                                 datasets                  feature_selection   metrics                  pipeline.py           utils
_isotonic.cpython-37m-x86_64-linux-gnu.so  decomposition             gaussian_process    mixture                  preprocessing
base.py                                    discriminant_analysis.py  impute.py           model_selection          random_projection.py
calibration.py                             dummy.py                  isotonic.py         multiclass.py            semi_supervised


(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ python examples/plot_isotonic_regression.py 

===================
Isotonic Regression
===================

An illustration of the isotonic regression on generated data. The
isotonic regression finds a non-decreasing approximation of a function
while minimizing the mean squared error on the training data. The benefit
of such a model is that it does not assume any form for the target
function such as linearity. For comparison a linear regression is also
presented.


## MAC

### Prerequisites

[python2.7-venv.md](./python2.7-venv.md)

```
(venv-mac) fanhonglingdeMacBook-Pro:sklearn0.20-python2.7-venv fanhongling$ git clone -b 0.20.X https://github.com/scikit-learn/scikit-learn github.com/scikit-learn/scikit-learn
Cloning into 'github.com/scikit-learn/scikit-learn'...
remote: Enumerating objects: 72, done.
remote: Counting objects: 100% (72/72), done.
remote: Compressing objects: 100% (47/47), done.
remote: Total 162836 (delta 37), reused 40 (delta 25), pack-reused 162764
Receiving objects: 100% (162836/162836), 94.25 MiB ø 2.34 MiB/s, done.
Resolving deltas: 100% (121715/121715), done.
Checking connectivity... done.
```


```
(venv-mac) fanhonglingdeMacBook-Pro:sklearn0.20-python2.7-venv fanhongling$ git clone https://github.com/pypa/virtualenv github.com/pypa/virtualenv
Cloning into 'github.com/pypa/virtualenv'...
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (15/15), done.
remote: Total 6484 (delta 5), reused 5 (delta 1), pack-reused 6468
Receiving objects: 100% (6484/6484), 61.67 MiB ø 3.05 MiB/s, done.
Resolving deltas: 100% (4165/4165), done.
Checking connectivity... done.
```

```
fanhonglingdeMacBook-Pro:sklearn0.20-python2.7-venv fanhongling$ python github.com/pypa/virtualenv/src/virtualenv.py venv-mac
New python executable in /Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/sklearn0.20-python2.7-venv/venv-mac/bin/python
Installing setuptools, pip, wheel...
done.
```

```
(venv-mac) fanhonglingdeMacBook-Pro:sklearn0.20-python2.7-venv fanhongling$ pip install numpy scipy scikit-learn matplotlib
Collecting numpy
  Using cached https://files.pythonhosted.org/packages/c0/b9/2b485bb32d0b26631f433580d90daad5dea830e6dc5bd18c4f227b1829f7/numpy-1.15.4-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting scipy
  Using cached https://files.pythonhosted.org/packages/d1/d6/3eac96ffcf7cbeb37ed72982cf3fdd3138472cb04ab32cdce1f444d765f2/scipy-1.1.0-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting scikit-learn
  Using cached https://files.pythonhosted.org/packages/11/2a/ca1d592d30856cf0d72fa3fb581f4c7fef81511411283ca412e9c12af769/scikit_learn-0.20.0-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting matplotlib
  Using cached https://files.pythonhosted.org/packages/23/16/8f83901b3094199078acd965657b9ee22604f33795fcb32a704566dd4cdf/matplotlib-2.2.3-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/71/e8/6777f6624681c8b9701a8a0a5654f3eb56919a01a78e12bf3c73f5a3c714/pyparsing-2.3.0-py2.py3-none-any.whl
Collecting python-dateutil>=2.1 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/74/68/d87d9b36af36f44254a8d512cbfc48369103a3b9e474be9bdfe536abfc45/python_dateutil-2.7.5-py2.py3-none-any.whl
Collecting kiwisolver>=1.0.1 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/79/d8/94633718f3f77dcb638687a77ba199325a1cb158d2d4b00c9dc17f2b5c72/kiwisolver-1.0.1-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting cycler>=0.10 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Collecting subprocess32 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/1f/b5/dcb236f263f61cdaac6dad65df42bbff91f66ef90854ae1a96ad4c8dd654/subprocess32-3.5.3-cp27-cp27m-macosx_10_6_intel.whl
Collecting pytz (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/f8/0e/2365ddc010afb3d79147f1dd544e5ee24bf4ece58ab99b16fbb465ce6dc0/pytz-2018.7-py2.py3-none-any.whl
Collecting six>=1.10 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
Collecting backports.functools-lru-cache (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/03/8e/2424c0e65c4a066e28f539364deee49b6451f8fcd4f718fefa50cc3dcf48/backports.functools_lru_cache-1.5-py2.py3-none-any.whl
Requirement already satisfied: setuptools in ./venv-mac/lib/python2.7/site-packages (from kiwisolver>=1.0.1->matplotlib) (40.6.2)
Installing collected packages: numpy, scipy, scikit-learn, pyparsing, six, python-dateutil, kiwisolver, cycler, subprocess32, pytz, backports.functools-lru-cache, matplotlib
Successfully installed backports.functools-lru-cache-1.5 cycler-0.10.0 kiwisolver-1.0.1 matplotlib-2.2.3 numpy-1.15.4 pyparsing-2.3.0 python-dateutil-2.7.5 pytz-2018.7 scikit-learn-0.20.0 scipy-1.1.0 six-1.11.0 subprocess32-3.5.3
```

```
(venv-mac) fanhonglingdeMacBook-Pro:sklearn0.20-python2.7-venv fanhongling$ cp /usr/bin/pythonw venv-mac/bin/
```

### Examples

Plot isotonic regression
```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ python github.com/scikit-learn/scikit-learn/examples/plot_isotonic_regression.py 

===================
Isotonic Regression
===================

An illustration of the isotonic regression on generated data. The
isotonic regression finds a non-decreasing approximation of a function
while minimizing the mean squared error on the training data. The benefit
of such a model is that it does not assume any form for the target
function such as linearity. For comparison a linear regression is also
presented.


Traceback (most recent call last):
  File "github.com/scikit-learn/scikit-learn/examples/plot_isotonic_regression.py", line 21, in <module>
    import matplotlib.pyplot as plt
ImportError: No module named matplotlib.pyplot
```

```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ pip install matplotlib
Collecting matplotlib
  Downloading https://files.pythonhosted.org/packages/23/16/8f83901b3094199078acd965657b9ee22604f33795fcb32a704566dd4cdf/matplotlib-2.2.3-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (13.8MB)
    100% ø████████████████████████████████ø 13.8MB 1.1MB/s 
Requirement already satisfied: numpy>=1.7.1 in ./venv-mac/lib/python2.7/site-packages (from matplotlib) (1.15.4)
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/71/e8/6777f6624681c8b9701a8a0a5654f3eb56919a01a78e12bf3c73f5a3c714/pyparsing-2.3.0-py2.py3-none-any.whl (59kB)
    100% ø████████████████████████████████ø 61kB 13.2MB/s 
Collecting python-dateutil>=2.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/74/68/d87d9b36af36f44254a8d512cbfc48369103a3b9e474be9bdfe536abfc45/python_dateutil-2.7.5-py2.py3-none-any.whl (225kB)
    100% ø████████████████████████████████ø 235kB 146kB/s 
Collecting kiwisolver>=1.0.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/79/d8/94633718f3f77dcb638687a77ba199325a1cb158d2d4b00c9dc17f2b5c72/kiwisolver-1.0.1-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (110kB)
    100% ø████████████████████████████████ø 112kB 572kB/s 
Collecting cycler>=0.10 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Collecting subprocess32 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/1f/b5/dcb236f263f61cdaac6dad65df42bbff91f66ef90854ae1a96ad4c8dd654/subprocess32-3.5.3-cp27-cp27m-macosx_10_6_intel.whl
Collecting pytz (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/f8/0e/2365ddc010afb3d79147f1dd544e5ee24bf4ece58ab99b16fbb465ce6dc0/pytz-2018.7-py2.py3-none-any.whl (506kB)
    100% ø████████████████████████████████ø 512kB 1.4MB/s 
Collecting six>=1.10 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
Collecting backports.functools-lru-cache (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/03/8e/2424c0e65c4a066e28f539364deee49b6451f8fcd4f718fefa50cc3dcf48/backports.functools_lru_cache-1.5-py2.py3-none-any.whl
Requirement already satisfied: setuptools in ./venv-mac/lib/python2.7/site-packages (from kiwisolver>=1.0.1->matplotlib) (40.6.2)
Installing collected packages: pyparsing, six, python-dateutil, kiwisolver, cycler, subprocess32, pytz, backports.functools-lru-cache, matplotlib
Successfully installed backports.functools-lru-cache-1.5 cycler-0.10.0 kiwisolver-1.0.1 matplotlib-2.2.3 pyparsing-2.3.0 python-dateutil-2.7.5 pytz-2018.7 six-1.11.0 subprocess32-3.5.3
```

```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ python github.com/scikit-learn/scikit-learn/examples/plot_isotonic_regression.py 

===================
Isotonic Regression
===================

An illustration of the isotonic regression on generated data. The
isotonic regression finds a non-decreasing approximation of a function
while minimizing the mean squared error on the training data. The benefit
of such a model is that it does not assume any form for the target
function such as linearity. For comparison a linear regression is also
presented.


Traceback (most recent call last):
  File "github.com/scikit-learn/scikit-learn/examples/plot_isotonic_regression.py", line 21, in <module>
    import matplotlib.pyplot as plt
  File "/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/scikit-learn-0.21-python2.7-venv/venv-mac/lib/python2.7/site-packages/matplotlib/pyplot.py", line 115, in <module>
    _backend_mod, new_figure_manager, draw_if_interactive, _show = pylab_setup()
  File "/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/scikit-learn-0.21-python2.7-venv/venv-mac/lib/python2.7/site-packages/matplotlib/backends/__init__.py", line 62, in pylab_setup
    Æbackend_nameÅ, 0)
  File "/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/scikit-learn-0.21-python2.7-venv/venv-mac/lib/python2.7/site-packages/matplotlib/backends/backend_macosx.py", line 17, in <module>
    from matplotlib.backends import _macosx
RuntimeError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. See the Python documentation for more information on installing Python as a framework on Mac OS X. Please either reinstall Python as a framework, or try one of the other backends. If you are using (Ana)Conda please install python.app and replace the use of 'python' with 'pythonw'. See 'Working with Matplotlib on OSX' in the Matplotlib FAQ for more information.
```

```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ which pythonw
/usr/bin/pythonw
```

```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ cp /usr/bin/pythonw venv-mac/bin/
```

```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ pythonw github.com/scikit-learn/scikit-learn/examples/plot_isotonic_regression.py 

===================
Isotonic Regression
===================

An illustration of the isotonic regression on generated data. The
isotonic regression finds a non-decreasing approximation of a function
while minimizing the mean squared error on the training data. The benefit
of such a model is that it does not assume any form for the target
function such as linearity. For comparison a linear regression is also
presented.


/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/python/scikit-learn-lab/scikit-learn-0.21-python2.7-venv/venv-mac/lib/python2.7/site-packages/sklearn/linear_model/base.py:485: RuntimeWarning: internal gelsd driver lwork query error, required iwork dimension not returned. This is likely the result of LAPACK bug 0038, fixed in LAPACK 3.2.2 (released July 21, 2010). Falling back to 'gelss' driver.
  linalg.lstsq(X, y)
```

![屏幕快照 2018-11-22 上午9.49.21.png](屏幕快照%202018-11-22%20上午9.49.21.png)


Plot multioutput face
```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ pythonw github.com/scikit-learn/scikit-learn/examples/plot_multioutput_face_completion.py 

==============================================
Face completion with a multi-output estimators
==============================================

This example shows the use of multi-output estimator to complete images.
The goal is to predict the lower half of a face given its upper half.

The first column of images shows true faces. The next columns illustrate
how extremely randomized trees, k nearest neighbors, linear
regression and ridge regression complete the lower half of those faces.


downloading Olivetti faces from https://ndownloader.figshare.com/files/5976027 to /Users/fanhongling/scikit_learn_data

```

![屏幕快照 2018-11-22 上午9.57.29.png](屏幕快照%202018-11-22%20上午9.57.29.png)

Plot multilabel
```
(venv-mac) fanhonglingdeMacBook-Pro:scikit-learn-0.21-python2.7-venv fanhongling$ pythonw github.com/scikit-learn/scikit-learn/examples/plot_multilabel.py 

=========================
Multilabel classification
=========================

This example simulates a multi-label document classification problem. The
dataset is generated randomly based on the following process:

    - pick the number of labels: n ~ Poisson(n_labels)
    - n times, choose a class c: c ~ Multinomial(theta)
    - pick the document length: k ~ Poisson(length)
    - k times, choose a word: w ~ Multinomial(theta_c)

In the above process, rejection sampling is used to make sure that n is more
than 2, and that the document length is never zero. Likewise, we reject classes
which have already been chosen.  The documents that are assigned to both
classes are plotted surrounded by two colored circles.

The classification is performed by projecting to the first two principal
components found by PCA and CCA for visualisation purposes, followed by using
the :class:`sklearn.multiclass.OneVsRestClassifier` metaclassifier using two
SVCs with linear kernels to learn a discriminative model for each class.
Note that PCA is used to perform an unsupervised dimensionality reduction,
while CCA is used to perform a supervised one.

Note: in the plot, "unlabeled samples" does not mean that we don't know the
labels (as in semi-supervised learning) but that the samples simply do *not*
have a label.

```

![屏幕快照 2018-11-22 上午10.01.23.png](屏幕快照%202018-11-22%20上午10.01.23.png)
