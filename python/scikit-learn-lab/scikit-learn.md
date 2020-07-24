# Lab

## SKLearn 0.20.0 Release (Nov 22 2018)

### Reference

https://github.com/scikit-learn/scikit-learn#user-installation

https://github.com/numpy/numpy/blob/master/INSTALL.rst.txt

https://github.com/scipy/scipy/blob/master/INSTALL.rst.txt

### Install

numpy
```
vagrant@ubuntu-bionic:~$ sudo pip3 install numpy
The directory '/home/vagrant/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/vagrant/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/ff/7f/9d804d2348471c67a7d8b5f84f9bc59fd1cefa148986f2b74552f8573555/numpy-1.15.4-cp36-cp36m-manylinux1_x86_64.whl (13.9MB)
    100% |████████████████████████████████| 13.9MB 11kB/s 
Installing collected packages: numpy
Successfully installed numpy-1.15.4
```

scipy
```
vagrant@ubuntu-bionic:~$ sudo pip3 install scipy
The directory '/home/vagrant/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/vagrant/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting scipy
  Downloading https://files.pythonhosted.org/packages/a8/0b/f163da98d3a01b3e0ef1cab8dd2123c34aee2bafbb1c5bffa354cc8a1730/scipy-1.1.0-cp36-cp36m-manylinux1_x86_64.whl (31.2MB)
    100% |████████████████████████████████| 31.2MB 15kB/s 
Requirement already satisfied: numpy>=1.8.2 in /usr/local/lib/python3.6/dist-packages (from scipy)
Installing collected packages: scipy
Successfully installed scipy-1.1.0
```

sklearn release
```
vagrant@ubuntu-bionic:~$ sudo pip3 install scikit-learn
The directory '/home/vagrant/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/vagrant/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting scikit-learn
  Downloading https://files.pythonhosted.org/packages/0c/b2/05be9b6da9ae4a4c54f537be22e95833f722742a02b1e355fdc09363877c/scikit_learn-0.20.0-cp36-cp36m-manylinux1_x86_64.whl (5.3MB)
    100% |████████████████████████████████| 5.3MB 33kB/s 
Requirement already satisfied: numpy>=1.8.2 in /usr/local/lib/python3.6/dist-packages (from scikit-learn)
Requirement already satisfied: scipy>=0.13.3 in /usr/local/lib/python3.6/dist-packages (from scikit-learn)
Installing collected packages: scikit-learn
Successfully installed scikit-learn-0.20.0
```

## Build SKLearn 0.20.X
 
Nov 22 2018

### Reference

https://scikit-learn.org/stable/developers/advanced_installation.html#linux

https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/appveyor/requirements.txt

https://github.com/scikit-learn/scikit-learn/blob/master/Makefile


### Build

git
```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace$ git clone https://github.com/scikit-learn/scikit-learn src/github.com/scikit-learn/scikit-learn
Cloning into 'src/github.com/scikit-learn/scikit-learn'...
remote: Enumerating objects: 28, done.
remote: Counting objects: 100% (28/28), done.
remote: Compressing objects: 100% (24/24), done.
remote: Total 161560 (delta 7), reused 8 (delta 4), pack-reused 161532
Receiving objects: 100% (161560/161560), 93.60 MiB | 80.00 KiB/s, done.
Resolving deltas: 100% (120690/120690), done.
Checking out files: 100% (1220/1220), done.
```

appveyor requirements
```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace$ sudo pip3 install -r src/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt 
The directory '/home/vagrant/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/vagrant/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from -r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 1))
Requirement already satisfied: scipy in /usr/local/lib/python3.6/dist-packages (from -r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 2))
Collecting cython==0.27.3 (from -r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 4))
  Downloading https://files.pythonhosted.org/packages/e9/91/46cb3f4c73f1e96faa517f96e9d12de5b8c97d404c7ab71553da0e58c980/Cython-0.27.3-cp36-cp36m-manylinux1_x86_64.whl (3.1MB)
    100% |████████████████████████████████| 3.1MB 19kB/s 
Collecting pytest (from -r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/57/94/305477fb977546970a3464c21b63c6800df6705384af2978b89acccfb151/pytest-3.10.1-py2.py3-none-any.whl (216kB)
    100% |████████████████████████████████| 225kB 38kB/s 
Requirement already satisfied: wheel in /usr/lib/python3/dist-packages (from -r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 6))
Collecting wheelhouse_uploader (from -r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/1a/38/ec316138d9e94aebb04e41cc3fc36841a11d6c749def6fddd7c83071566d/wheelhouse_uploader-0.10.1-py2.py3-none-any.whl
Collecting pillow (from -r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 8))
  Downloading https://files.pythonhosted.org/packages/62/94/5430ebaa83f91cc7a9f687ff5238e26164a779cca2ef9903232268b0a318/Pillow-5.3.0-cp36-cp36m-manylinux1_x86_64.whl (2.0MB)
    100% |████████████████████████████████| 2.0MB 34kB/s 
Requirement already satisfied: six>=1.10.0 in /usr/lib/python3/dist-packages (from pytest->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 5))
Collecting more-itertools>=4.0.0 (from pytest->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/79/b1/eace304ef66bd7d3d8b2f78cc374b73ca03bc53664d78151e9df3b3996cc/more_itertools-4.3.0-py3-none-any.whl (48kB)
    100% |████████████████████████████████| 51kB 28kB/s 
Requirement already satisfied: attrs>=17.4.0 in /usr/lib/python3/dist-packages (from pytest->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 5))
Collecting pluggy>=0.7 (from pytest->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/1c/e7/017c262070af41fe251401cb0d0e1b7c38f656da634cd0c15604f1f30864/pluggy-0.8.0-py2.py3-none-any.whl
Requirement already satisfied: setuptools in /usr/lib/python3/dist-packages (from pytest->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 5))
Collecting py>=1.5.0 (from pytest->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/3e/c7/3da685ef117d42ac8d71af525208759742dd235f8094221fdaafcd3dba8f/py-1.7.0-py2.py3-none-any.whl (83kB)
    100% |████████████████████████████████| 92kB 16kB/s 
Collecting atomicwrites>=1.0 (from pytest->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/3a/9a/9d878f8d885706e2530402de6417141129a943802c084238914fa6798d97/atomicwrites-1.2.1-py2.py3-none-any.whl
Requirement already satisfied: certifi in /usr/lib/python3/dist-packages (from wheelhouse_uploader->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 7))
Collecting packaging (from wheelhouse_uploader->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/89/d1/92e6df2e503a69df9faab187c684585f0136662c12bb1f36901d426f3fab/packaging-18.0-py2.py3-none-any.whl
Collecting apache-libcloud==2.2.1 (from wheelhouse_uploader->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/23/b5/b57733c2b0f5d810835a60f3a6e7fd679489879444603524efe5a6ac08c0/apache_libcloud-2.2.1-py2.py3-none-any.whl (2.9MB)
    100% |████████████████████████████████| 2.9MB 45kB/s 
Collecting pyparsing>=2.0.2 (from packaging->wheelhouse_uploader->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 7))
  Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))': /simple/pyparsing/
  Downloading https://files.pythonhosted.org/packages/71/e8/6777f6624681c8b9701a8a0a5654f3eb56919a01a78e12bf3c73f5a3c714/pyparsing-2.3.0-py2.py3-none-any.whl (59kB)
    100% |████████████████████████████████| 61kB 14kB/s 
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (from apache-libcloud==2.2.1->wheelhouse_uploader->-r /Users/fanhongling/Downloads/99-mirror/scikit-learn-lab/github.com/scikit-learn/scikit-learn/build_tools/appveyor/requirements.txt (line 7))
Installing collected packages: cython, more-itertools, pluggy, py, atomicwrites, pytest, pyparsing, packaging, apache-libcloud, wheelhouse-uploader, pillow
Successfully installed apache-libcloud-2.2.1 atomicwrites-1.2.1 cython-0.27.3 more-itertools-4.3.0 packaging-18.0 pillow-5.3.0 pluggy-0.8.0 py-1.7.0 pyparsing-2.3.0 pytest-3.10.1 wheelhouse-uploader-0.10.1
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace$ cd src/github.com/scikit-learn/scikit-learn/
```

Execute `make` in python3.7 venv

* [sklearn-0.20-build.txt](./sklearn-0.20-build.txt)











