

https://scikit-learn.org/stable/developers/advanced_installation.html#linux

https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/appveyor/requirements.txt

https://github.com/scikit-learn/scikit-learn/blob/master/Makefile

https://github.com/numpy/numpy/blob/master/INSTALL.rst.txt

https://github.com/scipy/scipy/blob/master/INSTALL.rst.txt


vagrant@ubuntu-bionic:~$ sudo pip3 install numpy
The directory '/home/vagrant/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/vagrant/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/ff/7f/9d804d2348471c67a7d8b5f84f9bc59fd1cefa148986f2b74552f8573555/numpy-1.15.4-cp36-cp36m-manylinux1_x86_64.whl (13.9MB)
    100% |████████████████████████████████| 13.9MB 11kB/s 
Installing collected packages: numpy
Successfully installed numpy-1.15.4


vagrant@ubuntu-bionic:~$ sudo pip3 install scipy
The directory '/home/vagrant/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/vagrant/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting scipy
  Downloading https://files.pythonhosted.org/packages/a8/0b/f163da98d3a01b3e0ef1cab8dd2123c34aee2bafbb1c5bffa354cc8a1730/scipy-1.1.0-cp36-cp36m-manylinux1_x86_64.whl (31.2MB)
    100% |████████████████████████████████| 31.2MB 15kB/s 
Requirement already satisfied: numpy>=1.8.2 in /usr/local/lib/python3.6/dist-packages (from scipy)
Installing collected packages: scipy
Successfully installed scipy-1.1.0


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



### Development


vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace$ git clone https://github.com/scikit-learn/scikit-learn src/github.com/scikit-learn/scikit-learn
Cloning into 'src/github.com/scikit-learn/scikit-learn'...
remote: Enumerating objects: 28, done.
remote: Counting objects: 100% (28/28), done.
remote: Compressing objects: 100% (24/24), done.
remote: Total 161560 (delta 7), reused 8 (delta 4), pack-reused 161532
Receiving objects: 100% (161560/161560), 93.60 MiB | 80.00 KiB/s, done.
Resolving deltas: 100% (120690/120690), done.
Checking out files: 100% (1220/1220), done.


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



vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace$ cd src/github.com/scikit-learn/scikit-learn/

vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ source ~/scikit-learn-python3.7-venv/bin/activate(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ 


(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ pip3 install -r build_tools/appveyor/requirements.txt 
Collecting numpy (from -r build_tools/appveyor/requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/38/39/f73e104d44f19a6203e786d5204532e214443ea2954917b27f3229e7639b/numpy-1.15.4-cp37-cp37m-manylinux1_x86_64.whl (13.8MB)
    100% |████████████████████████████████| 13.9MB 62kB/s 
Collecting scipy (from -r build_tools/appveyor/requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/40/de/0c22c6754370ba6b1fa8e53bd6e514d4a41a181125d405a501c215cbdbd6/scipy-1.1.0-cp37-cp37m-manylinux1_x86_64.whl (31.2MB)
    100% |████████████████████████████████| 31.2MB 40kB/s 
Collecting cython==0.27.3 (from -r build_tools/appveyor/requirements.txt (line 4))
  Downloading https://files.pythonhosted.org/packages/ee/2a/c4d2cdd19c84c32d978d18e9355d1ba9982a383de87d0fcb5928553d37f4/Cython-0.27.3.tar.gz (1.8MB)
    100% |████████████████████████████████| 1.8MB 147kB/s 
Collecting pytest (from -r build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/bb/d5/7601c468ded9a59478dcb39d21e24d58bb375681c64a06fbb629d2bc2ac3/pytest-4.0.0-py2.py3-none-any.whl (217kB)
    100% |████████████████████████████████| 225kB 23kB/s 
Collecting wheel (from -r build_tools/appveyor/requirements.txt (line 6))
  Cache entry deserialization failed, entry ignored
  Downloading https://files.pythonhosted.org/packages/5a/9b/6aebe9e2636d35d1a93772fa644c828303e1d5d124e8a88f156f42ac4b87/wheel-0.32.2-py2.py3-none-any.whl
Collecting wheelhouse_uploader (from -r build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/1a/38/ec316138d9e94aebb04e41cc3fc36841a11d6c749def6fddd7c83071566d/wheelhouse_uploader-0.10.1-py2.py3-none-any.whl
Collecting pillow (from -r build_tools/appveyor/requirements.txt (line 8))
  Downloading https://files.pythonhosted.org/packages/62/8c/230204b8e968f6db00c765624f51cfd1ecb6aea57b25ba00b240ee3fb0bd/Pillow-5.3.0-cp37-cp37m-manylinux1_x86_64.whl (2.0MB)
    100% |████████████████████████████████| 2.0MB 217kB/s 
Collecting six>=1.10.0 (from pytest->-r build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
Collecting attrs>=17.4.0 (from pytest->-r build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/3a/e1/5f9023cc983f1a628a8c2fd051ad19e76ff7b142a0faf329336f9a62a514/attrs-18.2.0-py2.py3-none-any.whl
Collecting atomicwrites>=1.0 (from pytest->-r build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/3a/9a/9d878f8d885706e2530402de6417141129a943802c084238914fa6798d97/atomicwrites-1.2.1-py2.py3-none-any.whl
Requirement already satisfied: setuptools in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from pytest->-r build_tools/appveyor/requirements.txt (line 5))
Collecting pluggy>=0.7 (from pytest->-r build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/1c/e7/017c262070af41fe251401cb0d0e1b7c38f656da634cd0c15604f1f30864/pluggy-0.8.0-py2.py3-none-any.whl
Collecting py>=1.5.0 (from pytest->-r build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/3e/c7/3da685ef117d42ac8d71af525208759742dd235f8094221fdaafcd3dba8f/py-1.7.0-py2.py3-none-any.whl (83kB)
    100% |████████████████████████████████| 92kB 433kB/s 
Collecting more-itertools>=4.0.0 (from pytest->-r build_tools/appveyor/requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/79/b1/eace304ef66bd7d3d8b2f78cc374b73ca03bc53664d78151e9df3b3996cc/more_itertools-4.3.0-py3-none-any.whl (48kB)
    100% |████████████████████████████████| 51kB 240kB/s 
Collecting packaging (from wheelhouse_uploader->-r build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/89/d1/92e6df2e503a69df9faab187c684585f0136662c12bb1f36901d426f3fab/packaging-18.0-py2.py3-none-any.whl
Collecting apache-libcloud==2.2.1 (from wheelhouse_uploader->-r build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/23/b5/b57733c2b0f5d810835a60f3a6e7fd679489879444603524efe5a6ac08c0/apache_libcloud-2.2.1-py2.py3-none-any.whl (2.9MB)
    100% |████████████████████████████████| 2.9MB 279kB/s 
Collecting certifi (from wheelhouse_uploader->-r build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/56/9d/1d02dd80bc4cd955f98980f28c5ee2200e1209292d5f9e9cc8d030d18655/certifi-2018.10.15-py2.py3-none-any.whl (146kB)
    100% |████████████████████████████████| 153kB 494kB/s 
Collecting pyparsing>=2.0.2 (from packaging->wheelhouse_uploader->-r build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/71/e8/6777f6624681c8b9701a8a0a5654f3eb56919a01a78e12bf3c73f5a3c714/pyparsing-2.3.0-py2.py3-none-any.whl (59kB)
    100% |████████████████████████████████| 61kB 312kB/s 
Collecting requests (from apache-libcloud==2.2.1->wheelhouse_uploader->-r build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/ff/17/5cbb026005115301a8fb2f9b0e3e8d32313142fe8b617070e7baad20554f/requests-2.20.1-py2.py3-none-any.whl (57kB)
    100% |████████████████████████████████| 61kB 617kB/s 
Collecting urllib3<1.25,>=1.21.1 (from requests->apache-libcloud==2.2.1->wheelhouse_uploader->-r build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl (118kB)
    100% |████████████████████████████████| 122kB 128kB/s 
Collecting chardet<3.1.0,>=3.0.2 (from requests->apache-libcloud==2.2.1->wheelhouse_uploader->-r build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
    100% |████████████████████████████████| 143kB 155kB/s 
Collecting idna<2.8,>=2.5 (from requests->apache-libcloud==2.2.1->wheelhouse_uploader->-r build_tools/appveyor/requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna-2.7-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 27kB/s 
Building wheels for collected packages: cython
  Running setup.py bdist_wheel for cython ... error
  Complete output from command /home/vagrant/scikit-learn-python3.7-venv/bin/python3.7 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-j9i7o0v3/cython/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpqu_f1bswpip-wheel- --python-tag cp37:
  Unable to find pgen, not compiling formal grammar.
  usage: -c [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or: -c --help [cmd1 cmd2 ...]
     or: -c --help-commands
     or: -c cmd --help
  
  error: invalid command 'bdist_wheel'
  
  ----------------------------------------
  Failed building wheel for cython
  Running setup.py clean for cython
Failed to build cython
Installing collected packages: numpy, scipy, cython, six, attrs, atomicwrites, pluggy, py, more-itertools, pytest, wheel, pyparsing, packaging, urllib3, chardet, idna, certifi, requests, apache-libcloud, wheelhouse-uploader, pillow
  Running setup.py install for cython ... done
Successfully installed apache-libcloud-2.2.1 atomicwrites-1.2.1 attrs-18.2.0 certifi-2018.10.15 chardet-3.0.4 cython-0.27.3 idna-2.7 more-itertools-4.3.0 numpy-1.15.4 packaging-18.0 pillow-5.3.0 pluggy-0.8.0 py-1.7.0 pyparsing-2.3.0 pytest-4.0.0 requests-2.20.1 scipy-1.1.0 six-1.11.0 urllib3-1.24.1 wheel-0.32.2 wheelhouse-uploader-0.10.1









vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/scikit-learn-lab$ git clone -b 0.20.X https://github.com/scikit-learn/scikit-learn github.com/scikit-learn/scikit-learn
Cloning into 'github.com/scikit-learn/scikit-learn'...
remote: Enumerating objects: 28, done.
remote: Counting objects: 100% (28/28), done.
remote: Compressing objects: 100% (24/24), done.
remote: Total 161560 (delta 7), reused 8 (delta 4), pack-reused 161532
Receiving objects: 100% (161560/161560), 93.60 MiB | 124.00 KiB/s, done.
Resolving deltas: 100% (120690/120690), done.
Checking out files: 100% (1207/1207), done.






(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ make all
rm -f tags
python setup.py clean
Partial import of sklearn during the build process.
running clean
Will remove generated .c files
rm -rf dist
python setup.py build_ext -i
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
Compiling sklearn/__check_build/_check_build.pyx because it changed.
Compiling sklearn/preprocessing/_csr_polynomial_expansion.pyx because it changed.
Compiling sklearn/cluster/_dbscan_inner.pyx because it changed.
Compiling sklearn/cluster/_hierarchical.pyx because it changed.
Compiling sklearn/cluster/_k_means_elkan.pyx because it changed.
Compiling sklearn/cluster/_k_means.pyx because it changed.
Compiling sklearn/datasets/_svmlight_format.pyx because it changed.
Compiling sklearn/decomposition/_online_lda.pyx because it changed.
Compiling sklearn/decomposition/cdnmf_fast.pyx because it changed.
Compiling sklearn/ensemble/_gradient_boosting.pyx because it changed.
Compiling sklearn/feature_extraction/_hashing.pyx because it changed.
Compiling sklearn/manifold/_utils.pyx because it changed.
Compiling sklearn/manifold/_barnes_hut_tsne.pyx because it changed.
Compiling sklearn/metrics/cluster/expected_mutual_info_fast.pyx because it changed.
Compiling sklearn/metrics/pairwise_fast.pyx because it changed.
Compiling sklearn/neighbors/ball_tree.pyx because it changed.
Compiling sklearn/neighbors/kd_tree.pyx because it changed.
Compiling sklearn/neighbors/dist_metrics.pyx because it changed.
Compiling sklearn/neighbors/typedefs.pyx because it changed.
Compiling sklearn/neighbors/quad_tree.pyx because it changed.
Compiling sklearn/tree/_tree.pyx because it changed.
Compiling sklearn/tree/_splitter.pyx because it changed.
Compiling sklearn/tree/_criterion.pyx because it changed.
Compiling sklearn/tree/_utils.pyx because it changed.
Compiling sklearn/svm/libsvm.pyx because it changed.
Compiling sklearn/svm/liblinear.pyx because it changed.
Compiling sklearn/svm/libsvm_sparse.pyx because it changed.
Compiling sklearn/_isotonic.pyx because it changed.
Compiling sklearn/linear_model/cd_fast.pyx because it changed.
Compiling sklearn/linear_model/sgd_fast.pyx because it changed.
Compiling sklearn/linear_model/sag_fast.pyx because it changed.
Compiling sklearn/utils/sparsefuncs_fast.pyx because it changed.
Compiling sklearn/utils/arrayfuncs.pyx because it changed.
Compiling sklearn/utils/murmurhash.pyx because it changed.
Compiling sklearn/utils/lgamma.pyx because it changed.
Compiling sklearn/utils/graph_shortest_path.pyx because it changed.
Compiling sklearn/utils/fast_dict.pyx because it changed.
Compiling sklearn/utils/seq_dataset.pyx because it changed.
Compiling sklearn/utils/weight_vector.pyx because it changed.
Compiling sklearn/utils/_random.pyx because it changed.
Compiling sklearn/utils/_logistic_sigmoid.pyx because it changed.
[ 1/41] Cythonizing sklearn/__check_build/_check_build.pyx
[ 2/41] Cythonizing sklearn/_isotonic.pyx
[ 3/41] Cythonizing sklearn/cluster/_dbscan_inner.pyx
[ 4/41] Cythonizing sklearn/cluster/_hierarchical.pyx
[ 5/41] Cythonizing sklearn/cluster/_k_means.pyx
[ 6/41] Cythonizing sklearn/cluster/_k_means_elkan.pyx
[ 7/41] Cythonizing sklearn/datasets/_svmlight_format.pyx
[ 8/41] Cythonizing sklearn/decomposition/_online_lda.pyx
[ 9/41] Cythonizing sklearn/decomposition/cdnmf_fast.pyx
[10/41] Cythonizing sklearn/ensemble/_gradient_boosting.pyx
[11/41] Cythonizing sklearn/feature_extraction/_hashing.pyx
[12/41] Cythonizing sklearn/linear_model/cd_fast.pyx
[13/41] Cythonizing sklearn/linear_model/sag_fast.pyx
[14/41] Cythonizing sklearn/linear_model/sgd_fast.pyx
[15/41] Cythonizing sklearn/manifold/_barnes_hut_tsne.pyx
[16/41] Cythonizing sklearn/manifold/_utils.pyx
[17/41] Cythonizing sklearn/metrics/cluster/expected_mutual_info_fast.pyx
[18/41] Cythonizing sklearn/metrics/pairwise_fast.pyx
[19/41] Cythonizing sklearn/neighbors/ball_tree.pyx
[20/41] Cythonizing sklearn/neighbors/dist_metrics.pyx
[21/41] Cythonizing sklearn/neighbors/kd_tree.pyx
[22/41] Cythonizing sklearn/neighbors/quad_tree.pyx
[23/41] Cythonizing sklearn/neighbors/typedefs.pyx
[24/41] Cythonizing sklearn/preprocessing/_csr_polynomial_expansion.pyx
[25/41] Cythonizing sklearn/svm/liblinear.pyx
[26/41] Cythonizing sklearn/svm/libsvm.pyx
[27/41] Cythonizing sklearn/svm/libsvm_sparse.pyx
[28/41] Cythonizing sklearn/tree/_criterion.pyx
[29/41] Cythonizing sklearn/tree/_splitter.pyx
[30/41] Cythonizing sklearn/tree/_tree.pyx
[31/41] Cythonizing sklearn/tree/_utils.pyx
[32/41] Cythonizing sklearn/utils/_logistic_sigmoid.pyx
[33/41] Cythonizing sklearn/utils/_random.pyx
[34/41] Cythonizing sklearn/utils/arrayfuncs.pyx
[35/41] Cythonizing sklearn/utils/fast_dict.pyx
[36/41] Cythonizing sklearn/utils/graph_shortest_path.pyx
[37/41] Cythonizing sklearn/utils/lgamma.pyx
[38/41] Cythonizing sklearn/utils/murmurhash.pyx
[39/41] Cythonizing sklearn/utils/seq_dataset.pyx
[40/41] Cythonizing sklearn/utils/sparsefuncs_fast.pyx
[41/41] Cythonizing sklearn/utils/weight_vector.pyx
running build_ext
running build_src
build_src
building library "libsvm-skl" sources
building library "cblas" sources
building extension "sklearn.__check_build._check_build" sources
building extension "sklearn.preprocessing._csr_polynomial_expansion" sources
building extension "sklearn.cluster._dbscan_inner" sources
building extension "sklearn.cluster._hierarchical" sources
building extension "sklearn.cluster._k_means_elkan" sources
building extension "sklearn.cluster._k_means" sources
building extension "sklearn.datasets._svmlight_format" sources
building extension "sklearn.decomposition._online_lda" sources
building extension "sklearn.decomposition.cdnmf_fast" sources
building extension "sklearn.ensemble._gradient_boosting" sources
building extension "sklearn.feature_extraction._hashing" sources
building extension "sklearn.manifold._utils" sources
building extension "sklearn.manifold._barnes_hut_tsne" sources
building extension "sklearn.metrics.cluster.expected_mutual_info_fast" sources
building extension "sklearn.metrics.pairwise_fast" sources
building extension "sklearn.neighbors.ball_tree" sources
building extension "sklearn.neighbors.kd_tree" sources
building extension "sklearn.neighbors.dist_metrics" sources
building extension "sklearn.neighbors.typedefs" sources
building extension "sklearn.neighbors.quad_tree" sources
building extension "sklearn.tree._tree" sources
building extension "sklearn.tree._splitter" sources
building extension "sklearn.tree._criterion" sources
building extension "sklearn.tree._utils" sources
building extension "sklearn.svm.libsvm" sources
building extension "sklearn.svm.liblinear" sources
building extension "sklearn.svm.libsvm_sparse" sources
building extension "sklearn._isotonic" sources
building extension "sklearn.linear_model.cd_fast" sources
building extension "sklearn.linear_model.sgd_fast" sources
building extension "sklearn.linear_model.sag_fast" sources
building extension "sklearn.utils.sparsefuncs_fast" sources
building extension "sklearn.utils.arrayfuncs" sources
building extension "sklearn.utils.murmurhash" sources
building extension "sklearn.utils.lgamma" sources
building extension "sklearn.utils.graph_shortest_path" sources
building extension "sklearn.utils.fast_dict" sources
building extension "sklearn.utils.seq_dataset" sources
building extension "sklearn.utils.weight_vector" sources
building extension "sklearn.utils._random" sources
building extension "sklearn.utils._logistic_sigmoid" sources
building data_files sources
build_src: building npy-pkg config files
customize UnixCCompiler
customize UnixCCompiler using build_clib
building 'libsvm-skl' library
compiling C++ sources
C compiler: x86_64-linux-gnu-g++ -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build
creating build/temp.linux-x86_64-3.7
creating build/temp.linux-x86_64-3.7/sklearn
creating build/temp.linux-x86_64-3.7/sklearn/svm
creating build/temp.linux-x86_64-3.7/sklearn/svm/src
creating build/temp.linux-x86_64-3.7/sklearn/svm/src/libsvm
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-g++: sklearn/svm/src/libsvm/libsvm_template.cpp
x86_64-linux-gnu-gcc-ar: adding 1 object files to build/temp.linux-x86_64-3.7/liblibsvm-skl.a
building 'cblas' library
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/src
creating build/temp.linux-x86_64-3.7/sklearn/src/cblas
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_drefasum.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_drefcopy.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_drefgemv.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_drefgemvN.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_drefgemvT.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_drefger.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_drefrot.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_drefrotg.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_dsrefdot.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_srefasum.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_srefcopy.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_srefgemv.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_srefgemvN.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_srefgemvT.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_srefger.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_srefnrm2.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_srefrot.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/ATL_srefrotg.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_dasum.c
In file included from sklearn/src/cblas/cblas_dasum.c:32:0:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_daxpy.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_dcopy.c
In file included from sklearn/src/cblas/atlas_level1.h:37:0,
                 from sklearn/src/cblas/cblas_dcopy.c:36:
sklearn/src/cblas/cblas_dcopy.c: In function ‘cblas_dcopy’:
sklearn/src/cblas/atlas_refalias1.h:25:24: warning: implicit declaration of function ‘ATL_drefcopy’; did you mean ‘ATL_dgecopy’? [-Wimplicit-function-declaration]
    #define ATL_dcopy   ATL_drefcopy
                        ^
sklearn/src/cblas/cblas_dcopy.c:46:24: note: in expansion of macro ‘ATL_dcopy’
          if (incY < 0) ATL_dcopy(N, X, -incX, Y, -incY);
                        ^~~~~~~~~
In file included from sklearn/src/cblas/cblas_dcopy.c:32:0:
At top level:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_ddot.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_dgemv.c
sklearn/src/cblas/cblas_dgemv.c: In function ‘cblas_dgemv’:
sklearn/src/cblas/cblas_dgemv.c:79:7: warning: implicit declaration of function ‘cblas_xerbla’; did you mean ‘cblas_zher2k’? [-Wimplicit-function-declaration]
       cblas_xerbla(info, "cblas_dgemv", "");
       ^~~~~~~~~~~~
       cblas_zher2k
In file included from sklearn/src/cblas/cblas_dgemv.c:32:0:
At top level:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_dger.c
sklearn/src/cblas/cblas_dger.c: In function ‘cblas_dger’:
sklearn/src/cblas/cblas_dger.c:73:7: warning: implicit declaration of function ‘cblas_xerbla’; did you mean ‘cblas_zher2k’? [-Wimplicit-function-declaration]
       cblas_xerbla(info, "cblas_dger", "");
       ^~~~~~~~~~~~
       cblas_zher2k
In file included from sklearn/src/cblas/cblas_dger.c:32:0:
At top level:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_dnrm2.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_drot.c
In file included from sklearn/src/cblas/cblas_drot.c:32:0:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_drotg.c
In file included from sklearn/src/cblas/cblas_drotg.c:32:0:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_dscal.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_errprn.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_sasum.c
In file included from sklearn/src/cblas/cblas_sasum.c:32:0:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_saxpy.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_scopy.c
In file included from sklearn/src/cblas/atlas_level1.h:37:0,
                 from sklearn/src/cblas/cblas_scopy.c:36:
sklearn/src/cblas/cblas_scopy.c: In function ‘cblas_scopy’:
sklearn/src/cblas/atlas_refalias1.h:12:24: warning: implicit declaration of function ‘ATL_srefcopy’; did you mean ‘ATL_sgecopy’? [-Wimplicit-function-declaration]
    #define ATL_scopy   ATL_srefcopy
                        ^
sklearn/src/cblas/cblas_scopy.c:46:24: note: in expansion of macro ‘ATL_scopy’
          if (incY < 0) ATL_scopy(N, X, -incX, Y, -incY);
                        ^~~~~~~~~
In file included from sklearn/src/cblas/cblas_scopy.c:32:0:
At top level:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_sdot.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_sgemv.c
sklearn/src/cblas/cblas_sgemv.c: In function ‘cblas_sgemv’:
sklearn/src/cblas/cblas_sgemv.c:79:7: warning: implicit declaration of function ‘cblas_xerbla’; did you mean ‘cblas_zher2k’? [-Wimplicit-function-declaration]
       cblas_xerbla(info, "cblas_sgemv", "");
       ^~~~~~~~~~~~
       cblas_zher2k
In file included from sklearn/src/cblas/cblas_sgemv.c:32:0:
At top level:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_sger.c
sklearn/src/cblas/cblas_sger.c: In function ‘cblas_sger’:
sklearn/src/cblas/cblas_sger.c:73:7: warning: implicit declaration of function ‘cblas_xerbla’; did you mean ‘cblas_zher2k’? [-Wimplicit-function-declaration]
       cblas_xerbla(info, "cblas_sger", "");
       ^~~~~~~~~~~~
       cblas_zher2k
In file included from sklearn/src/cblas/cblas_sger.c:32:0:
At top level:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_snrm2.c
In file included from sklearn/src/cblas/cblas_snrm2.c:32:0:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_srot.c
In file included from sklearn/src/cblas/cblas_srot.c:32:0:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_srotg.c
In file included from sklearn/src/cblas/cblas_srotg.c:32:0:
sklearn/src/cblas/atlas_misc.h:409:14: warning: ‘ATL_Align2Ptr’ defined but not used [-Wunused-function]
 static void *ATL_Align2Ptr(const void *pu, const void *pA)
              ^~~~~~~~~~~~~
sklearn/src/cblas/atlas_misc.h:393:12: warning: ‘ATL_AlignOffset’ defined but not used [-Wunused-function]
 static int ATL_AlignOffset
            ^~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_sscal.c
x86_64-linux-gnu-gcc: sklearn/src/cblas/cblas_xerbla.c
sklearn/src/cblas/cblas_xerbla.c: In function ‘cblas_xerbla’:
sklearn/src/cblas/cblas_xerbla.c:52:4: warning: implicit declaration of function ‘exit’ [-Wimplicit-function-declaration]
    exit(-1);
    ^~~~
sklearn/src/cblas/cblas_xerbla.c:52:4: warning: incompatible implicit declaration of built-in function ‘exit’
sklearn/src/cblas/cblas_xerbla.c:52:4: note: include ‘<stdlib.h>’ or provide a declaration of ‘exit’
x86_64-linux-gnu-gcc-ar: adding 40 object files to build/temp.linux-x86_64-3.7/libcblas.a
customize UnixCCompiler
customize UnixCCompiler using build_ext
customize UnixCCompiler
customize UnixCCompiler using build_ext
building 'sklearn.__check_build._check_build' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/__check_build
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/__check_build/_check_build.c
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/__check_build/_check_build.o -Lbuild/temp.linux-x86_64-3.7 -o sklearn/__check_build/_check_build.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.preprocessing._csr_polynomial_expansion' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/preprocessing
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/preprocessing/_csr_polynomial_expansion.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/preprocessing/_csr_polynomial_expansion.c:547:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/preprocessing/_csr_polynomial_expansion.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/preprocessing/_csr_polynomial_expansion.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.cluster._dbscan_inner' extension
compiling C++ sources
C compiler: x86_64-linux-gnu-g++ -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/cluster
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-g++: sklearn/cluster/_dbscan_inner.cpp
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/cluster/_dbscan_inner.cpp:564:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/cluster/_dbscan_inner.o -Lbuild/temp.linux-x86_64-3.7 -o sklearn/cluster/_dbscan_inner.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.cluster._hierarchical' extension
compiling C++ sources
C compiler: x86_64-linux-gnu-g++ -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-g++: sklearn/cluster/_hierarchical.cpp
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/cluster/_hierarchical.cpp:562:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/cluster/_hierarchical.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/cluster/_hierarchical.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.cluster._k_means_elkan' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/cluster/_k_means_elkan.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/cluster/_k_means_elkan.c:547:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/cluster/_k_means_elkan.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/cluster/_k_means_elkan.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.cluster._k_means' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-Isklearn/src/cblas -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/cluster/_k_means.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/cluster/_k_means.c:551:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
sklearn/cluster/_k_means.c: In function ‘__pyx_fuse_0__pyx_f_7sklearn_7cluster_8_k_means__assign_labels_array’:
sklearn/cluster/_k_means.c:3951:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_sdot;
               ^
sklearn/cluster/_k_means.c: In function ‘__pyx_fuse_1__pyx_f_7sklearn_7cluster_8_k_means__assign_labels_array’:
sklearn/cluster/_k_means.c:4749:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_ddot;
               ^
sklearn/cluster/_k_means.c: In function ‘__pyx_fuse_0__pyx_f_7sklearn_7cluster_8_k_means__assign_labels_csr’:
sklearn/cluster/_k_means.c:6348:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_sdot;
               ^
sklearn/cluster/_k_means.c: In function ‘__pyx_fuse_1__pyx_f_7sklearn_7cluster_8_k_means__assign_labels_csr’:
sklearn/cluster/_k_means.c:7211:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_ddot;
               ^
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/cluster/_k_means.o -Lbuild/temp.linux-x86_64-3.7 -lcblas -lm -o sklearn/cluster/_k_means.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.datasets._svmlight_format' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/datasets
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/datasets/_svmlight_format.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/datasets/_svmlight_format.c:545:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/datasets/_svmlight_format.o -Lbuild/temp.linux-x86_64-3.7 -o sklearn/datasets/_svmlight_format.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.decomposition._online_lda' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/decomposition
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/decomposition/_online_lda.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/decomposition/_online_lda.c:548:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/decomposition/_online_lda.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/decomposition/_online_lda.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.decomposition.cdnmf_fast' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/decomposition/cdnmf_fast.c
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/decomposition/cdnmf_fast.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/decomposition/cdnmf_fast.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.ensemble._gradient_boosting' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/ensemble
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/ensemble/_gradient_boosting.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/ensemble/_gradient_boosting.c:545:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/ensemble/_gradient_boosting.o -Lbuild/temp.linux-x86_64-3.7 -o sklearn/ensemble/_gradient_boosting.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.feature_extraction._hashing' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/feature_extraction
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/feature_extraction/_hashing.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/feature_extraction/_hashing.c:549:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/feature_extraction/_hashing.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/feature_extraction/_hashing.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.manifold._utils' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/manifold
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
extra options: '-O3'
x86_64-linux-gnu-gcc: sklearn/manifold/_utils.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/manifold/_utils.c:552:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/manifold/_utils.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/manifold/_utils.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.manifold._barnes_hut_tsne' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-Isklearn/src/cblas -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
extra options: '-O4'
x86_64-linux-gnu-gcc: sklearn/manifold/_barnes_hut_tsne.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/manifold/_barnes_hut_tsne.c:553:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
sklearn/manifold/_barnes_hut_tsne.c: In function ‘__pyx_f_7sklearn_8manifold_16_barnes_hut_tsne_compute_gradient_negative’:
sklearn/manifold/_barnes_hut_tsne.c:3439:9: warning: variable ‘__pyx_v_force’ set but not used [-Wunused-but-set-variable]
   float __pyx_v_force[3];
         ^~~~~~~~~~~~~
sklearn/manifold/_barnes_hut_tsne.c:3438:9: warning: variable ‘__pyx_v_iQ’ set but not used [-Wunused-but-set-variable]
   float __pyx_v_iQ[1];
         ^~~~~~~~~~
sklearn/manifold/_barnes_hut_tsne.c: In function ‘__pyx_pf_7sklearn_8manifold_16_barnes_hut_tsne_gradient.isra.33’:
sklearn/manifold/_barnes_hut_tsne.c:3822:76: warning: ‘__pyx_v_neg_force[2]’ may be used uninitialized in this function [-Wmaybe-uninitialized]
         (__pyx_v_neg_force[__pyx_t_12]) = ((__pyx_v_neg_force[__pyx_t_12]) + (__pyx_v_mult * (__pyx_v_summary[((__pyx_v_j * __pyx_v_offset) + __pyx_v_ax)])));
                                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sklearn/manifold/_barnes_hut_tsne.c:3440:9: note: ‘__pyx_v_neg_force[2]’ was declared here
   float __pyx_v_neg_force[3];
         ^~~~~~~~~~~~~~~~~
sklearn/manifold/_barnes_hut_tsne.c:3822:76: warning: ‘__pyx_v_neg_force[1]’ may be used uninitialized in this function [-Wmaybe-uninitialized]
         (__pyx_v_neg_force[__pyx_t_12]) = ((__pyx_v_neg_force[__pyx_t_12]) + (__pyx_v_mult * (__pyx_v_summary[((__pyx_v_j * __pyx_v_offset) + __pyx_v_ax)])));
                                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sklearn/manifold/_barnes_hut_tsne.c:3440:9: note: ‘__pyx_v_neg_force[1]’ was declared here
   float __pyx_v_neg_force[3];
         ^~~~~~~~~~~~~~~~~
sklearn/manifold/_barnes_hut_tsne.c:3822:76: warning: ‘__pyx_v_neg_force[0]’ may be used uninitialized in this function [-Wmaybe-uninitialized]
         (__pyx_v_neg_force[__pyx_t_12]) = ((__pyx_v_neg_force[__pyx_t_12]) + (__pyx_v_mult * (__pyx_v_summary[((__pyx_v_j * __pyx_v_offset) + __pyx_v_ax)])));
                                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sklearn/manifold/_barnes_hut_tsne.c:3440:9: note: ‘__pyx_v_neg_force[0]’ was declared here
   float __pyx_v_neg_force[3];
         ^~~~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/manifold/_barnes_hut_tsne.o -Lbuild/temp.linux-x86_64-3.7 -lcblas -o sklearn/manifold/_barnes_hut_tsne.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.metrics.cluster.expected_mutual_info_fast' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/metrics
creating build/temp.linux-x86_64-3.7/sklearn/metrics/cluster
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/metrics/cluster/expected_mutual_info_fast.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/metrics/cluster/expected_mutual_info_fast.c:548:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/metrics/cluster/expected_mutual_info_fast.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/metrics/cluster/expected_mutual_info_fast.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.metrics.pairwise_fast' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-Isklearn/src/cblas -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/metrics/pairwise_fast.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/metrics/pairwise_fast.c:550:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/metrics/pairwise_fast.o -Lbuild/temp.linux-x86_64-3.7 -lcblas -lm -o sklearn/metrics/pairwise_fast.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.neighbors.ball_tree' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/neighbors
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/neighbors/ball_tree.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/neighbors/ball_tree.c:547:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
sklearn/neighbors/ball_tree.c: In function ‘__pyx_f_7sklearn_9neighbors_9ball_tree_10BinaryTree__recursive_build’:
sklearn/neighbors/ball_tree.c:24057:82: warning: ‘__pyx_v_sample_weight’ may be used uninitialized in this function [-Wmaybe-uninitialized]
       __pyx_v_sum_weight_node = (__pyx_v_sum_weight_node + (__pyx_v_sample_weight[(__pyx_v_idx_array[__pyx_v_i])]));
                                                                                  ^
sklearn/neighbors/ball_tree.c:23882:50: note: ‘__pyx_v_sample_weight’ was declared here
   __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t *__pyx_v_sample_weight;
                                                  ^~~~~~~~~~~~~~~~~~~~~
sklearn/neighbors/ball_tree.c: In function ‘__pyx_f_7sklearn_9neighbors_9ball_tree_10BinaryTree__kde_single_breadthfirst’:
sklearn/neighbors/ball_tree.c:20350:65: warning: ‘__pyx_v_sample_weight’ may be used uninitialized in this function [-Wmaybe-uninitialized]
           __pyx_t_12 = PyFloat_FromDouble((__pyx_v_sample_weight[(__pyx_v_idx_array[__pyx_v_i])])); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 2228, __pyx_L1_error)
                                                                 ^
sklearn/neighbors/ball_tree.c: In function ‘__pyx_f_7sklearn_9neighbors_9ball_tree_10BinaryTree__kde_single_depthfirst’:
sklearn/neighbors/ball_tree.c:21069:63: warning: ‘__pyx_v_sample_weight’ may be used uninitialized in this function [-Wmaybe-uninitialized]
         __pyx_t_12 = PyFloat_FromDouble((__pyx_v_sample_weight[(__pyx_v_idx_array[__pyx_v_i])])); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 2363, __pyx_L1_error)
                                                               ^
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/neighbors/ball_tree.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/neighbors/ball_tree.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.neighbors.kd_tree' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/neighbors/kd_tree.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/neighbors/kd_tree.c:547:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
sklearn/neighbors/kd_tree.c: In function ‘__pyx_f_7sklearn_9neighbors_7kd_tree_10BinaryTree__kde_single_depthfirst’:
sklearn/neighbors/kd_tree.c:21040:63: warning: ‘__pyx_v_sample_weight’ may be used uninitialized in this function [-Wmaybe-uninitialized]
         __pyx_t_12 = PyFloat_FromDouble((__pyx_v_sample_weight[(__pyx_v_idx_array[__pyx_v_i])])); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 2363, __pyx_L1_error)
                                                               ^
sklearn/neighbors/kd_tree.c: In function ‘__pyx_f_7sklearn_9neighbors_7kd_tree_10BinaryTree__kde_single_breadthfirst’:
sklearn/neighbors/kd_tree.c:20321:65: warning: ‘__pyx_v_sample_weight’ may be used uninitialized in this function [-Wmaybe-uninitialized]
           __pyx_t_12 = PyFloat_FromDouble((__pyx_v_sample_weight[(__pyx_v_idx_array[__pyx_v_i])])); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 2228, __pyx_L1_error)
                                                                 ^
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/neighbors/kd_tree.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/neighbors/kd_tree.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.neighbors.dist_metrics' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/neighbors/dist_metrics.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/neighbors/dist_metrics.c:548:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
sklearn/neighbors/dist_metrics.c: In function ‘__pyx_f_7sklearn_9neighbors_12dist_metrics_18SEuclideanDistance_dist’:
sklearn/neighbors/dist_metrics.c:6955:85: warning: passing argument 1 of ‘__pyx_f_7sklearn_9neighbors_12dist_metrics_18SEuclideanDistance_rdist’ from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_t_1 = __pyx_f_7sklearn_9neighbors_12dist_metrics_18SEuclideanDistance_rdist(((struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_DistanceMetric *)__pyx_v_self), __pyx_v_x1, __pyx_v_x2, __pyx_v_size); if (unlikely(__pyx_t_1 == ((__pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t)-1.0))) __PYX_ERR(1, 463, __pyx_L1_error)
                                                                                     ^
sklearn/neighbors/dist_metrics.c:6760:54: note: expected ‘struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_SEuclideanDistance *’ but argument is of type ‘struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_DistanceMetric *’
 static __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t __pyx_f_7sklearn_9neighbors_12dist_metrics_18SEuclideanDistance_rdist(struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_SEuclideanDistance *__pyx_v_self, __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t *__pyx_v_x1, __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t *__pyx_v_x2, __pyx_t_7sklearn_9neighbors_8typedefs_ITYPE_t __pyx_v_size) {
                                                      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sklearn/neighbors/dist_metrics.c: In function ‘__pyx_f_7sklearn_9neighbors_12dist_metrics_17MinkowskiDistance_dist’:
sklearn/neighbors/dist_metrics.c:7767:84: warning: passing argument 1 of ‘__pyx_f_7sklearn_9neighbors_12dist_metrics_17MinkowskiDistance_rdist’ from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_t_1 = __pyx_f_7sklearn_9neighbors_12dist_metrics_17MinkowskiDistance_rdist(((struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_DistanceMetric *)__pyx_v_self), __pyx_v_x1, __pyx_v_x2, __pyx_v_size); if (unlikely(__pyx_t_1 == ((__pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t)-1.0))) __PYX_ERR(1, 552, __pyx_L1_error)
                                                                                    ^
sklearn/neighbors/dist_metrics.c:7688:54: note: expected ‘struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_MinkowskiDistance *’ but argument is of type ‘struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_DistanceMetric *’
 static __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t __pyx_f_7sklearn_9neighbors_12dist_metrics_17MinkowskiDistance_rdist(struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_MinkowskiDistance *__pyx_v_self, __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t *__pyx_v_x1, __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t *__pyx_v_x2, __pyx_t_7sklearn_9neighbors_8typedefs_ITYPE_t __pyx_v_size) {
                                                      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sklearn/neighbors/dist_metrics.c: In function ‘__pyx_f_7sklearn_9neighbors_12dist_metrics_18WMinkowskiDistance_dist’:
sklearn/neighbors/dist_metrics.c:8470:85: warning: passing argument 1 of ‘__pyx_f_7sklearn_9neighbors_12dist_metrics_18WMinkowskiDistance_rdist’ from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_t_1 = __pyx_f_7sklearn_9neighbors_12dist_metrics_18WMinkowskiDistance_rdist(((struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_DistanceMetric *)__pyx_v_self), __pyx_v_x1, __pyx_v_x2, __pyx_v_size); if (unlikely(__pyx_t_1 == ((__pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t)-1.0))) __PYX_ERR(1, 611, __pyx_L1_error)
                                                                                     ^
sklearn/neighbors/dist_metrics.c:8285:54: note: expected ‘struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_WMinkowskiDistance *’ but argument is of type ‘struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_DistanceMetric *’
 static __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t __pyx_f_7sklearn_9neighbors_12dist_metrics_18WMinkowskiDistance_rdist(struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_WMinkowskiDistance *__pyx_v_self, __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t *__pyx_v_x1, __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t *__pyx_v_x2, __pyx_t_7sklearn_9neighbors_8typedefs_ITYPE_t __pyx_v_size) {
                                                      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sklearn/neighbors/dist_metrics.c: In function ‘__pyx_f_7sklearn_9neighbors_12dist_metrics_19MahalanobisDistance_dist’:
sklearn/neighbors/dist_metrics.c:9333:86: warning: passing argument 1 of ‘__pyx_f_7sklearn_9neighbors_12dist_metrics_19MahalanobisDistance_rdist’ from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_t_1 = __pyx_f_7sklearn_9neighbors_12dist_metrics_19MahalanobisDistance_rdist(((struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_DistanceMetric *)__pyx_v_self), __pyx_v_x1, __pyx_v_x2, __pyx_v_size); if (unlikely(__pyx_t_1 == ((__pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t)-1.0))) __PYX_ERR(1, 684, __pyx_L1_error)
                                                                                      ^
sklearn/neighbors/dist_metrics.c:9093:54: note: expected ‘struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_MahalanobisDistance *’ but argument is of type ‘struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_DistanceMetric *’
 static __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t __pyx_f_7sklearn_9neighbors_12dist_metrics_19MahalanobisDistance_rdist(struct __pyx_obj_7sklearn_9neighbors_12dist_metrics_MahalanobisDistance *__pyx_v_self, __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t *__pyx_v_x1, __pyx_t_7sklearn_9neighbors_8typedefs_DTYPE_t *__pyx_v_x2, __pyx_t_7sklearn_9neighbors_8typedefs_ITYPE_t __pyx_v_size) {
                                                      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/neighbors/dist_metrics.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/neighbors/dist_metrics.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.neighbors.typedefs' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/neighbors/typedefs.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/neighbors/typedefs.c:547:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/neighbors/typedefs.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/neighbors/typedefs.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.neighbors.quad_tree' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/neighbors/quad_tree.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/neighbors/quad_tree.c:547:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
sklearn/neighbors/quad_tree.c: In function ‘__pyx_f_7sklearn_9neighbors_9quad_tree_9_QuadTree__get_cell_ndarray’:
sklearn/neighbors/quad_tree.c:7141:36: warning: passing argument 1 of ‘(PyObject * (*)(PyTypeObject *, PyArray_Descr *, int,  npy_intp *, npy_intp *, void *, int,  PyObject *))*(PyArray_API + 752)’ from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_t_2 = PyArray_NewFromDescr(((PyObject *)__pyx_ptype_5numpy_ndarray), ((PyArray_Descr *)__pyx_t_1), 1, __pyx_v_shape, __pyx_v_strides, ((void *)__pyx_v_self->cells), NPY_DEFAULT, Py_None); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 574, __pyx_L1_error)
                                    ^
sklearn/neighbors/quad_tree.c:7141:36: note: expected ‘PyTypeObject * {aka struct _typeobject *}’ but argument is of type ‘PyObject * {aka struct _object *}’
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/neighbors/quad_tree.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/neighbors/quad_tree.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.tree._tree' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/tree
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
extra options: '-O3'
x86_64-linux-gnu-gcc: sklearn/tree/_tree.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/tree/_tree.c:550:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
sklearn/tree/_tree.c: In function ‘__pyx_f_7sklearn_4tree_5_tree_4Tree__get_node_ndarray’:
sklearn/tree/_tree.c:15202:36: warning: passing argument 1 of ‘(PyObject * (*)(PyTypeObject *, PyArray_Descr *, int,  npy_intp *, npy_intp *, void *, int,  PyObject *))*(PyArray_API + 752)’ from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_t_2 = PyArray_NewFromDescr(((PyObject *)__pyx_ptype_5numpy_ndarray), ((PyArray_Descr *)__pyx_t_1), 1, __pyx_v_shape, __pyx_v_strides, ((void *)__pyx_v_self->nodes), NPY_DEFAULT, Py_None); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1129, __pyx_L1_error)
                                    ^
sklearn/tree/_tree.c:15202:36: note: expected ‘PyTypeObject * {aka struct _typeobject *}’ but argument is of type ‘PyObject * {aka struct _object *}’
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/tree/_tree.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/tree/_tree.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.tree._splitter' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
extra options: '-O3'
x86_64-linux-gnu-gcc: sklearn/tree/_splitter.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/tree/_splitter.c:550:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/tree/_splitter.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/tree/_splitter.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.tree._criterion' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
extra options: '-O3'
x86_64-linux-gnu-gcc: sklearn/tree/_criterion.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/tree/_criterion.c:550:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/tree/_criterion.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/tree/_criterion.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.tree._utils' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
extra options: '-O3'
x86_64-linux-gnu-gcc: sklearn/tree/_utils.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/tree/_utils.c:550:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
sklearn/tree/_utils.c: In function ‘__pyx_f_7sklearn_4tree_6_utils_24WeightedMedianCalculator_remove’:
sklearn/tree/_utils.c:9265:4: warning: ‘__pyx_v_original_median’ may be used uninitialized in this function [-Wmaybe-uninitialized]
   ((struct __pyx_vtabstruct_7sklearn_4tree_6_utils_WeightedMedianCalculator *)__pyx_v_self->__pyx_vtab)->update_median_parameters_post_remove(__pyx_v_self, __pyx_v_data, __pyx_v_weight, __pyx_v_original_median);
   ~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sklearn/tree/_utils.c: In function ‘__pyx_f_7sklearn_4tree_6_utils_24WeightedMedianCalculator_pop’:
sklearn/tree/_utils.c:9377:4: warning: ‘__pyx_v_original_median’ may be used uninitialized in this function [-Wmaybe-uninitialized]
   ((struct __pyx_vtabstruct_7sklearn_4tree_6_utils_WeightedMedianCalculator *)__pyx_v_self->__pyx_vtab)->update_median_parameters_post_remove(__pyx_v_self, (__pyx_v_data[0]), (__pyx_v_weight[0]), __pyx_v_original_median);
   ~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sklearn/tree/_utils.c: In function ‘__pyx_f_7sklearn_4tree_6_utils_24WeightedMedianCalculator_push’:
sklearn/tree/_utils.c:8909:4: warning: ‘__pyx_v_original_median’ may be used uninitialized in this function [-Wmaybe-uninitialized]
   ((struct __pyx_vtabstruct_7sklearn_4tree_6_utils_WeightedMedianCalculator *)__pyx_v_self->__pyx_vtab)->update_median_parameters_post_push(__pyx_v_self, __pyx_v_data, __pyx_v_weight, __pyx_v_original_median);
   ~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/tree/_utils.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/tree/_utils.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.svm.libsvm' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -Isklearn/svm/src/libsvm -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/svm/libsvm.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/svm/libsvm.c:552:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/svm/libsvm.o -Lbuild/temp.linux-x86_64-3.7 -llibsvm-skl -o sklearn/svm/libsvm.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.svm.liblinear' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-Isklearn/svm -I./sklearn/svm -Isklearn/src/cblas -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/svm/liblinear.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/svm/liblinear.c:556:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
In file included from sklearn/svm/liblinear.c:559:0:
sklearn/svm/src/liblinear/liblinear_helper.c: In function ‘set_problem’:
sklearn/svm/src/liblinear/liblinear_helper.c:145:28: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
     problem->sample_weight = sample_weight;
                            ^
sklearn/svm/src/liblinear/liblinear_helper.c: In function ‘csr_set_problem’:
sklearn/svm/src/liblinear/liblinear_helper.c:174:28: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
     problem->sample_weight = sample_weight;
                            ^
compiling C++ sources
C compiler: x86_64-linux-gnu-g++ -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/svm/src/liblinear
compile options: '-Isklearn/svm -I./sklearn/svm -Isklearn/src/cblas -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-g++: sklearn/svm/src/liblinear/linear.cpp
sklearn/svm/src/liblinear/linear.cpp: In function ‘model* train(const problem*, const parameter*)’:
sklearn/svm/src/liblinear/linear.cpp:2370:6: warning: unused variable ‘n_iter’ [-Wunused-variable]
  int n_iter;
      ^~~~~~
x86_64-linux-gnu-g++: sklearn/svm/src/liblinear/tron.cpp
x86_64-linux-gnu-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/svm/liblinear.o build/temp.linux-x86_64-3.7/sklearn/svm/src/liblinear/linear.o build/temp.linux-x86_64-3.7/sklearn/svm/src/liblinear/tron.o -Lbuild/temp.linux-x86_64-3.7 -lcblas -lm -o sklearn/svm/liblinear.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.svm.libsvm_sparse' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -Isklearn/svm/src/libsvm -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/svm/libsvm_sparse.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/svm/libsvm_sparse.c:550:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/svm/libsvm_sparse.o -Lbuild/temp.linux-x86_64-3.7 -llibsvm-skl -o sklearn/svm/libsvm_sparse.cpython-37m-x86_64-linux-gnu.so
building 'sklearn._isotonic' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/_isotonic.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/_isotonic.c:547:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/_isotonic.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/_isotonic.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.linear_model.cd_fast' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/linear_model
compile options: '-Isklearn/src/cblas -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/linear_model/cd_fast.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/linear_model/cd_fast.c:551:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
sklearn/linear_model/cd_fast.c: In function ‘__pyx_pf_7sklearn_12linear_model_7cd_fast_8enet_coordinate_descent’:
sklearn/linear_model/cd_fast.c:5081:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_gemv = cblas_sgemv;
                ^
sklearn/linear_model/cd_fast.c:5090:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_sdot;
               ^
sklearn/linear_model/cd_fast.c:5099:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_axpy = cblas_saxpy;
                ^
sklearn/linear_model/cd_fast.c:5108:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_asum = cblas_sasum;
                ^
sklearn/linear_model/cd_fast.c:5117:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_copy = cblas_scopy;
                ^
sklearn/linear_model/cd_fast.c: In function ‘__pyx_pf_7sklearn_12linear_model_7cd_fast_10enet_coordinate_descent’:
sklearn/linear_model/cd_fast.c:6487:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_gemv = cblas_dgemv;
                ^
sklearn/linear_model/cd_fast.c:6496:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_ddot;
               ^
sklearn/linear_model/cd_fast.c:6505:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_axpy = cblas_daxpy;
                ^
sklearn/linear_model/cd_fast.c:6514:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_asum = cblas_dasum;
                ^
sklearn/linear_model/cd_fast.c:6523:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_copy = cblas_dcopy;
                ^
sklearn/linear_model/cd_fast.c: In function ‘__pyx_pf_7sklearn_12linear_model_7cd_fast_14sparse_enet_coordinate_descent’:
sklearn/linear_model/cd_fast.c:8792:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_sdot;
               ^
sklearn/linear_model/cd_fast.c:8801:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_asum = cblas_sasum;
                ^
sklearn/linear_model/cd_fast.c: In function ‘__pyx_pf_7sklearn_12linear_model_7cd_fast_16sparse_enet_coordinate_descent’:
sklearn/linear_model/cd_fast.c:10761:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_ddot;
               ^
sklearn/linear_model/cd_fast.c:10770:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_asum = cblas_dasum;
                ^
sklearn/linear_model/cd_fast.c: In function ‘__pyx_pf_7sklearn_12linear_model_7cd_fast_20enet_coordinate_descent_gram’:
sklearn/linear_model/cd_fast.c:13321:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_sdot;
               ^
sklearn/linear_model/cd_fast.c:13330:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_axpy = cblas_saxpy;
                ^
sklearn/linear_model/cd_fast.c:13339:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_asum = cblas_sasum;
                ^
sklearn/linear_model/cd_fast.c: In function ‘__pyx_pf_7sklearn_12linear_model_7cd_fast_22enet_coordinate_descent_gram’:
sklearn/linear_model/cd_fast.c:14849:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_ddot;
               ^
sklearn/linear_model/cd_fast.c:14858:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_axpy = cblas_daxpy;
                ^
sklearn/linear_model/cd_fast.c:14867:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_asum = cblas_dasum;
                ^
sklearn/linear_model/cd_fast.c: In function ‘__pyx_pf_7sklearn_12linear_model_7cd_fast_26enet_coordinate_descent_multi_task’:
sklearn/linear_model/cd_fast.c:17078:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_sdot;
               ^
sklearn/linear_model/cd_fast.c:17087:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_nrm2 = cblas_snrm2;
                ^
sklearn/linear_model/cd_fast.c:17096:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_asum = cblas_sasum;
                ^
sklearn/linear_model/cd_fast.c:17105:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_copy = cblas_scopy;
                ^
sklearn/linear_model/cd_fast.c:17123:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_ger = cblas_sger;
               ^
sklearn/linear_model/cd_fast.c:17132:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_gemv = cblas_sgemv;
                ^
sklearn/linear_model/cd_fast.c: In function ‘__pyx_pf_7sklearn_12linear_model_7cd_fast_28enet_coordinate_descent_multi_task’:
sklearn/linear_model/cd_fast.c:18805:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_dot = cblas_ddot;
               ^
sklearn/linear_model/cd_fast.c:18814:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_nrm2 = cblas_dnrm2;
                ^
sklearn/linear_model/cd_fast.c:18823:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_asum = cblas_dasum;
                ^
sklearn/linear_model/cd_fast.c:18832:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_copy = cblas_dcopy;
                ^
sklearn/linear_model/cd_fast.c:18850:15: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_ger = cblas_dger;
               ^
sklearn/linear_model/cd_fast.c:18859:16: warning: assignment from incompatible pointer type [-Wincompatible-pointer-types]
   __pyx_v_gemv = cblas_dgemv;
                ^
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/linear_model/cd_fast.o -Lbuild/temp.linux-x86_64-3.7 -lcblas -lm -o sklearn/linear_model/cd_fast.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.linear_model.sgd_fast' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-Isklearn/linear_model -Isklearn/src/cblas -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/linear_model/sgd_fast.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/linear_model/sgd_fast.c:553:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/linear_model/sgd_fast.o -Lbuild/temp.linux-x86_64-3.7 -lcblas -lm -o sklearn/linear_model/sgd_fast.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.linear_model.sag_fast' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-Isklearn/linear_model -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/linear_model/sag_fast.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/linear_model/sag_fast.c:546:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/linear_model/sag_fast.o -Lbuild/temp.linux-x86_64-3.7 -o sklearn/linear_model/sag_fast.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.utils.sparsefuncs_fast' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/utils
compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/utils/sparsefuncs_fast.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/utils/sparsefuncs_fast.c:542:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/utils/sparsefuncs_fast.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/utils/sparsefuncs_fast.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.utils.arrayfuncs' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-Isklearn/utils -Isklearn/src/cblas -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/utils/arrayfuncs.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/utils/arrayfuncs.c:551:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/utils/arrayfuncs.o -Lbuild/temp.linux-x86_64-3.7 -lcblas -lm -o sklearn/utils/arrayfuncs.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.utils.murmurhash' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-Isklearn/utils -Isklearn/utils/src -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/utils/murmurhash.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/utils/murmurhash.c:545:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
compiling C++ sources
C compiler: x86_64-linux-gnu-g++ -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

creating build/temp.linux-x86_64-3.7/sklearn/utils/src
compile options: '-Isklearn/utils -Isklearn/utils/src -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-g++: sklearn/utils/src/MurmurHash3.cpp
x86_64-linux-gnu-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/utils/murmurhash.o build/temp.linux-x86_64-3.7/sklearn/utils/src/MurmurHash3.o -Lbuild/temp.linux-x86_64-3.7 -o sklearn/utils/murmurhash.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.utils.lgamma' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-Isklearn/utils -Isklearn/utils/src -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/utils/lgamma.c
x86_64-linux-gnu-gcc: sklearn/utils/src/gamma.c
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/utils/lgamma.o build/temp.linux-x86_64-3.7/sklearn/utils/src/gamma.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/utils/lgamma.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.utils.graph_shortest_path' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/utils/graph_shortest_path.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/utils/graph_shortest_path.c:544:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/utils/graph_shortest_path.o -Lbuild/temp.linux-x86_64-3.7 -o sklearn/utils/graph_shortest_path.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.utils.fast_dict' extension
compiling C++ sources
C compiler: x86_64-linux-gnu-g++ -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-g++: sklearn/utils/fast_dict.cpp
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/utils/fast_dict.cpp:568:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
sklearn/utils/fast_dict.cpp: In function ‘PyObject* __pyx_pw_7sklearn_5utils_9fast_dict_1argmin(PyObject*, PyObject*)’:
sklearn/utils/fast_dict.cpp:25389:47: warning: ‘__pyx_v_min_key’ may be used uninitialized in this function [-Wmaybe-uninitialized]
             return PyInt_FromLong((long) value);
                                               ^
sklearn/utils/fast_dict.cpp:4445:46: note: ‘__pyx_v_min_key’ was declared here
   __pyx_t_7sklearn_5utils_9fast_dict_ITYPE_t __pyx_v_min_key;
                                              ^~~~~~~~~~~~~~~
x86_64-linux-gnu-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/utils/fast_dict.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/utils/fast_dict.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.utils.seq_dataset' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/utils/seq_dataset.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/utils/seq_dataset.c:544:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/utils/seq_dataset.o -Lbuild/temp.linux-x86_64-3.7 -o sklearn/utils/seq_dataset.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.utils.weight_vector' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-Isklearn/src/cblas -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/utils/weight_vector.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/utils/weight_vector.c:550:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/utils/weight_vector.o -Lbuild/temp.linux-x86_64-3.7 -lcblas -lm -o sklearn/utils/weight_vector.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.utils._random' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/utils/_random.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/utils/_random.c:547:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/utils/_random.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/utils/_random.cpython-37m-x86_64-linux-gnu.so
building 'sklearn.utils._logistic_sigmoid' extension
compiling C sources
C compiler: x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC

compile options: '-I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include -I/home/vagrant/scikit-learn-python3.7-venv/include -I/usr/include/python3.7m -c'
x86_64-linux-gnu-gcc: sklearn/utils/_logistic_sigmoid.c
In file included from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1821:0,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18,
                 from /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sklearn/utils/_logistic_sigmoid.c:548:
/home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: #warning "Using deprecated NumPy API, disable it by " "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
 #warning "Using deprecated NumPy API, disable it by " \
  ^~~~~~~
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/sklearn/utils/_logistic_sigmoid.o -Lbuild/temp.linux-x86_64-3.7 -lm -o sklearn/utils/_logistic_sigmoid.cpython-37m-x86_64-linux-gnu.so
pytest --showlocals -v sklearn --durations=20
================================================================= test session starts ==================================================================
platform linux -- Python 3.7.0, pytest-4.0.0, py-1.7.0, pluggy-0.8.0 -- /home/vagrant/scikit-learn-python3.7-venv/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn, inifile: setup.cfg
collected 10547 items                                                                                                                                  

sklearn/_config.py::sklearn._config.config_context PASSED                                                                                        [  0%]
sklearn/discriminant_analysis.py::sklearn.discriminant_analysis.LinearDiscriminantAnalysis PASSED                                                [  0%]
sklearn/discriminant_analysis.py::sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis PASSED                                             [  0%]

### >>>> snippets >>>>

sklearn/utils/tests/test_validation.py::test_check_array_memmap[False] PASSED                                                                    [ 99%]
sklearn/utils/tests/test_validation.py::test_check_non_negative[asarray] PASSED                                                                  [ 99%]
sklearn/utils/tests/test_validation.py::test_check_non_negative[csr_matrix] PASSED                                                               [ 99%]
sklearn/utils/tests/test_validation.py::test_check_non_negative[csc_matrix] PASSED                                                               [ 99%]
sklearn/utils/tests/test_validation.py::test_check_non_negative[coo_matrix] PASSED                                                               [ 99%]
sklearn/utils/tests/test_validation.py::test_check_non_negative[lil_matrix] PASSED                                                               [ 99%]
sklearn/utils/tests/test_validation.py::test_check_non_negative[bsr_matrix] PASSED                                                               [ 99%]
sklearn/utils/tests/test_validation.py::test_check_non_negative[dok_matrix] PASSED                                                               [ 99%]
sklearn/utils/tests/test_validation.py::test_check_non_negative[dia_matrix] PASSED                                                               [ 99%]
sklearn/utils/tests/test_validation.py::test_check_X_y_informative_error PASSED                                                                  [ 99%]
sklearn/utils/tests/test_validation.py::test_retrieve_samples_from_non_standard_shape PASSED                                                     [100%]
=============================================================== short test summary info ================================================================
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: This test is failing on the buildbot, but cannot reproduce. Temporarily disabling it until it can be reproduced and  fixed.
SKIP [1] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/compose/tests/test_column_transformer.py:133: could not import 'pandas'
SKIP [2] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/compose/tests/test_column_transformer.py:264: could not import 'pandas'
SKIP [1] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/compose/tests/test_column_transformer.py:471: could not import 'pandas'
SKIP [9] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/compose/tests/test_column_transformer.py:788: could not import 'pandas'
SKIP [1] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/compose/tests/test_column_transformer.py:978: could not import 'pandas'
SKIP [3] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: Download 20 newsgroups to run this test
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: California housing dataset can not be loaded.
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: Covertype dataset can not be loaded.
SKIP [2] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: kddcup99 dataset can not be loaded.
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: Download RCV1 dataset to run this test.
SKIP [2] sklearn/decomposition/tests/test_sparse_pca.py:160: skipping mini_batch_fit_transform.
SKIP [3] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: Matplotlib not available.
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: test_bayesian_on_diabetes is broken
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: pyamg not available.
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/doctest.py:347: all tests skipped by +SKIP option
SKIP [4] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/preprocessing/tests/test_data.py:870: 'with_mean=True' cannot be used with sparse matrix.
SKIP [2] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/preprocessing/tests/test_data.py:1077: RobustScaler cannot center sparse matrix
SKIP [3] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/preprocessing/tests/test_encoders.py:294: could not import 'pandas'
SKIP [1] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/preprocessing/tests/test_encoders.py:475: could not import 'pandas'
SKIP [1] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/preprocessing/tests/test_encoders.py:643: could not import 'pandas'
SKIP [1] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/preprocessing/tests/test_function_transformer.py:203: could not import 'pandas'
SKIP [46] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: pandas is not installed: not testing for input of type pandas.Series to class weight.
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: score_samples of BernoulliRBM is not invariant when applied to a subset.
SKIP [3] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: Skipping check_estimators_data_not_an_array for cross decomposition module as estimators are not deterministic.
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: transform of MiniBatchSparsePCA is not invariant when applied to a subset.
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: Not testing NuSVC class weight as it is ignored.
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: decision_function of SVC is not invariant when applied to a subset.
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: transform of SparsePCA is not invariant when applied to a subset.
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: numpydoc is required to test the docstrings, as well as python version >= 3.5
SKIP [2] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/tests/test_impute.py:301: could not import 'pandas'
SKIP [2] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/tests/test_impute.py:414: could not import 'pandas'
SKIP [1] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/tree/tests/test_export.py:317: could not import 'matplotlib.pyplot'
SKIP [3] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: Pandas not found
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: numpydoc is required to test the docstrings
SKIP [1] /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn/sklearn/utils/tests/test_validation.py:701: could not import 'pandas'

============================================================== slowest 20 test durations ===============================================================
12.28s call     sklearn/ensemble/tests/test_gradient_boosting.py::test_feature_importance_regression
7.45s call     sklearn/utils/tests/test_estimator_checks.py::test_check_estimator
6.40s call     sklearn/metrics/tests/test_classification.py::test_matthews_corrcoef_overflow[1000000]
5.03s call     sklearn/utils/tests/test_estimator_checks.py::test_check_estimator_clones
3.77s call     sklearn/tree/tests/test_tree.py::test_min_impurity_decrease
3.22s call     sklearn/tests/test_common.py::test_non_meta_estimators[LogisticRegressionCV-LogisticRegressionCV-check_estimator_sparse_data]
3.07s call     sklearn/cluster/tests/test_mean_shift.py::test_parallel
2.80s call     sklearn/decomposition/tests/test_dict_learning.py::test_sparse_coder_parallel_mmap
2.56s call     sklearn/neural_network/tests/test_mlp.py::test_n_iter_no_change_inf
2.54s call     sklearn/tests/test_multioutput.py::test_base_chain_fit_and_predict_with_sparse_data_and_cv
2.45s call     sklearn/ensemble/tests/test_bagging.py::test_oob_score_removed_on_warm_start
2.41s call     sklearn/random_projection.py::sklearn.random_projection.GaussianRandomProjection
2.40s call     sklearn/mixture/tests/test_bayesian_mixture.py::test_monotonic_likelihood
2.38s call     sklearn/ensemble/tests/test_bagging.py::test_parallel_classification
2.38s call     sklearn/manifold/tests/test_t_sne.py::test_uniform_grid[exact]
2.26s call     sklearn/feature_extraction/tests/test_image.py::test_connect_regions
2.00s call     sklearn/linear_model/tests/test_logistic.py::test_ovr_multinomial_iris
1.96s call     sklearn/model_selection/tests/test_search.py::test_random_search_cv_results_multimetric
1.90s call     sklearn/model_selection/tests/test_validation.py::test_cross_validate_many_jobs
1.74s call     sklearn/feature_extraction/tests/test_image.py::test_connect_regions_with_grid
======================================== 10438 passed, 108 skipped, 1 xfailed, 14238 warnings in 558.07 seconds ========================================
 This problem is unconstrained.
RUNNING THE L-BFGS-B CODE

           * * *

Machine precision = 2.220D-16
 N =            3     M =           10

At X0         0 variables are exactly at the bounds

At iterate    0    f=  1.38629D+02    |proj g|=  6.27865D+01

           * * *

Tit   = total number of iterations
Tnf   = total number of function evaluations
Tnint = total number of segments explored during Cauchy searches
Skip  = number of BFGS updates skipped
Nact  = number of active bounds at final generalized Cauchy point
Projg = norm of the final projected gradient
F     = final function value

           * * *

   N    Tit     Tnf  Tnint  Skip  Nact     Projg        F
    3      1      2      1     0     0   2.422D+01   9.713D+01
  F =   97.133816163368223     

STOP: TOTAL NO. of ITERATIONS REACHED LIMIT                 

 Cauchy                time 0.000E+00 seconds.
 Subspace minimization time 0.000E+00 seconds.
 Line search           time 0.000E+00 seconds.

 Total User time 0.000E+00 seconds.

pytest --showlocals -v doc/sphinxext/
================================================================= test session starts ==================================================================
platform linux -- Python 3.7.0, pytest-4.0.0, py-1.7.0, pluggy-0.8.0 -- /home/vagrant/scikit-learn-python3.7-venv/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn, inifile: setup.cfg
collected 1 item / 1 errors                                                                                                                            

======================================================================== ERRORS ========================================================================
___________________________________________________ ERROR collecting doc/sphinxext/sphinx_issues.py ____________________________________________________
doc/sphinxext/sphinx_issues.py:25: in <module>
    from docutils import nodes, utils
E   ModuleNotFoundError: No module named 'docutils'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
=============================================================== 1 error in 0.52 seconds ================================================================
Makefile:29: recipe for target 'test-sphinxext' failed
make: *** [test-sphinxext] Error 2



(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ pip install docutils
Collecting docutils
  Downloading https://files.pythonhosted.org/packages/36/fa/08e9e6e0e3cbd1d362c3bbee8d01d0aedb2155c4ac112b19ef3cae8eed8d/docutils-0.14-py3-none-any.whl (543kB)
    100% |████████████████████████████████| 552kB 195kB/s 
Installing collected packages: docutils
Successfully installed docutils-0.14


(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ make test-sphinxext test-doc
pytest --showlocals -v doc/sphinxext/
================================================================= test session starts ==================================================================
platform linux -- Python 3.7.0, pytest-4.0.0, py-1.7.0, pluggy-0.8.0 -- /home/vagrant/scikit-learn-python3.7-venv/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn, inifile: setup.cfg
collected 1 item / 1 errors                                                                                                                            

======================================================================== ERRORS ========================================================================
___________________________________________________ ERROR collecting doc/sphinxext/sphinx_issues.py ____________________________________________________
doc/sphinxext/sphinx_issues.py:26: in <module>
    from sphinx.util.nodes import split_explicit_title
E   ModuleNotFoundError: No module named 'sphinx'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
=============================================================== 1 error in 0.76 seconds ================================================================
Makefile:29: recipe for target 'test-sphinxext' failed
make: *** [test-sphinxext] Error 2
(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ pip install sphinx
Collecting sphinx
  Downloading https://files.pythonhosted.org/packages/ff/d5/3a8727d6f890b1ae45da72a55bf8449e9f2c535a444923b338c3f509f203/Sphinx-1.8.2-py2.py3-none-any.whl (3.1MB)
    100% |████████████████████████████████| 3.1MB 112kB/s 
Collecting Pygments>=2.0 (from sphinx)
  Downloading https://files.pythonhosted.org/packages/02/ee/b6e02dc6529e82b75bb06823ff7d005b141037cb1416b10c6f00fc419dca/Pygments-2.2.0-py2.py3-none-any.whl (841kB)
    100% |████████████████████████████████| 849kB 496kB/s 
Collecting sphinxcontrib-websupport (from sphinx)
  Downloading https://files.pythonhosted.org/packages/52/69/3c2fbdc3702358c5b34ee25e387b24838597ef099761fc9a42c166796e8f/sphinxcontrib_websupport-1.1.0-py2.py3-none-any.whl
Requirement already satisfied: six>=1.5 in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from sphinx)
Requirement already satisfied: setuptools in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from sphinx)
Collecting Jinja2>=2.3 (from sphinx)
  Downloading https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl (126kB)
    100% |████████████████████████████████| 133kB 132kB/s 
Collecting babel!=2.0,>=1.3 (from sphinx)
  Downloading https://files.pythonhosted.org/packages/b8/ad/c6f60602d3ee3d92fbed87675b6fb6a6f9a38c223343ababdb44ba201f10/Babel-2.6.0-py2.py3-none-any.whl (8.1MB)
    100% |████████████████████████████████| 8.1MB 76kB/s 
Requirement already satisfied: requests>=2.0.0 in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from sphinx)
Requirement already satisfied: packaging in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from sphinx)
Collecting imagesize (from sphinx)
  Downloading https://files.pythonhosted.org/packages/fc/b6/aef66b4c52a6ad6ac18cf6ebc5731ed06d8c9ae4d3b2d9951f261150be67/imagesize-1.1.0-py2.py3-none-any.whl
Collecting alabaster<0.8,>=0.7 (from sphinx)
  Downloading https://files.pythonhosted.org/packages/10/ad/00b090d23a222943eb0eda509720a404f531a439e803f6538f35136cae9e/alabaster-0.7.12-py2.py3-none-any.whl
Collecting snowballstemmer>=1.1 (from sphinx)
  Downloading https://files.pythonhosted.org/packages/d4/6c/8a935e2c7b54a37714656d753e4187ee0631988184ed50c0cf6476858566/snowballstemmer-1.2.1-py2.py3-none-any.whl (64kB)
    100% |████████████████████████████████| 71kB 309kB/s 
Requirement already satisfied: docutils>=0.11 in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from sphinx)
Collecting MarkupSafe>=0.23 (from Jinja2>=2.3->sphinx)
  Downloading https://files.pythonhosted.org/packages/e4/c4/adcc2d6f2ac2146cc04e076f14f1006c1de8e1e747fa067668b6573000b8/MarkupSafe-1.1.0-cp37-cp37m-manylinux1_x86_64.whl
Collecting pytz>=0a (from babel!=2.0,>=1.3->sphinx)
  Downloading https://files.pythonhosted.org/packages/f8/0e/2365ddc010afb3d79147f1dd544e5ee24bf4ece58ab99b16fbb465ce6dc0/pytz-2018.7-py2.py3-none-any.whl (506kB)
    100% |████████████████████████████████| 512kB 508kB/s 
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from requests>=2.0.0->sphinx)
Requirement already satisfied: certifi>=2017.4.17 in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from requests>=2.0.0->sphinx)
Requirement already satisfied: idna<2.8,>=2.5 in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from requests>=2.0.0->sphinx)
Requirement already satisfied: urllib3<1.25,>=1.21.1 in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from requests>=2.0.0->sphinx)
Requirement already satisfied: pyparsing>=2.0.2 in /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages (from packaging->sphinx)
Installing collected packages: Pygments, sphinxcontrib-websupport, MarkupSafe, Jinja2, pytz, babel, imagesize, alabaster, snowballstemmer, sphinx
Successfully installed Jinja2-2.10 MarkupSafe-1.1.0 Pygments-2.2.0 alabaster-0.7.12 babel-2.6.0 imagesize-1.1.0 pytz-2018.7 snowballstemmer-1.2.1 sphinx-1.8.2 sphinxcontrib-websupport-1.1.0



(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ make test-sphinxext test-doc
pytest --showlocals -v doc/sphinxext/
================================================================= test session starts ==================================================================
platform linux -- Python 3.7.0, pytest-4.0.0, py-1.7.0, pluggy-0.8.0 -- /home/vagrant/scikit-learn-python3.7-venv/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn, inifile: setup.cfg
collected 1 item                                                                                                                                       

doc/sphinxext/github_link.py::github_link._linkcode_resolve PASSED                                                                               [100%]

=============================================================== 1 passed in 0.18 seconds ===============================================================
pytest doc/about.rst doc/authors.rst doc/data_transforms.rst doc/datasets/index.rst doc/developers/advanced_installation.rst doc/developers/contributing.rst doc/developers/index.rst doc/developers/maintainer.rst doc/developers/performance.rst doc/developers/tips.rst doc/developers/utilities.rst doc/documentation.rst doc/faq.rst doc/glossary.rst doc/includes/big_toc_css.rst doc/includes/bigger_toc_css.rst doc/index.rst doc/install.rst doc/model_selection.rst doc/modules/biclustering.rst doc/modules/calibration.rst doc/modules/classes.rst doc/modules/clustering.rst doc/modules/compose.rst doc/modules/computing.rst doc/modules/covariance.rst doc/modules/cross_decomposition.rst doc/modules/cross_validation.rst doc/modules/decomposition.rst doc/modules/density.rst doc/modules/ensemble.rst doc/modules/feature_extraction.rst doc/modules/feature_selection.rst doc/modules/gaussian_process.rst doc/modules/grid_search.rst doc/modules/impute.rst doc/modules/isotonic.rst doc/modules/kernel_approximation.rst doc/modules/kernel_ridge.rst doc/modules/label_propagation.rst doc/modules/lda_qda.rst doc/modules/learning_curve.rst doc/modules/linear_model.rst doc/modules/manifold.rst doc/modules/metrics.rst doc/modules/mixture.rst doc/modules/model_evaluation.rst doc/modules/model_persistence.rst doc/modules/multiclass.rst doc/modules/naive_bayes.rst doc/modules/neighbors.rst doc/modules/neural_networks_supervised.rst doc/modules/neural_networks_unsupervised.rst doc/modules/outlier_detection.rst doc/modules/pipeline.rst doc/modules/preprocessing.rst doc/modules/preprocessing_targets.rst doc/modules/random_projection.rst doc/modules/sgd.rst doc/modules/svm.rst doc/modules/tree.rst doc/modules/unsupervised_reduction.rst doc/other_distributions.rst doc/preface.rst doc/presentations.rst doc/related_projects.rst doc/supervised_learning.rst doc/support.rst doc/templates/class.rst doc/templates/class_with_call.rst doc/templates/class_without_init.rst doc/templates/deprecated_class.rst doc/templates/deprecated_class_with_call.rst doc/templates/deprecated_class_without_init.rst doc/templates/deprecated_function.rst doc/templates/function.rst doc/templates/numpydoc_docstring.rst doc/testimonials/testimonials.rst doc/themes/scikit-learn/static/ML_MAPS_README.rst doc/tune_toc.rst doc/tutorial/basic/tutorial.rst doc/tutorial/index.rst doc/tutorial/machine_learning_map/index.rst doc/tutorial/statistical_inference/finding_help.rst doc/tutorial/statistical_inference/index.rst doc/tutorial/statistical_inference/model_selection.rst doc/tutorial/statistical_inference/putting_together.rst doc/tutorial/statistical_inference/settings.rst doc/tutorial/statistical_inference/supervised_learning.rst doc/tutorial/statistical_inference/unsupervised_learning.rst doc/tutorial/text_analytics/working_with_text_data.rst doc/unsupervised_learning.rst doc/user_guide.rst doc/whats_new.rst doc/whats_new/_contributors.rst doc/whats_new/older_versions.rst doc/whats_new/v0.13.rst doc/whats_new/v0.14.rst doc/whats_new/v0.15.rst doc/whats_new/v0.16.rst doc/whats_new/v0.17.rst doc/whats_new/v0.18.rst doc/whats_new/v0.19.rst doc/whats_new/v0.20.rst doc/whats_new/v0.21.rst
================================================================= test session starts ==================================================================
platform linux -- Python 3.7.0, pytest-4.0.0, py-1.7.0, pluggy-0.8.0
rootdir: /Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn, inifile: setup.cfg
collected 40 items                                                                                                                                     

doc/datasets/index.rst s                                                                                                                         [  2%]
doc/developers/contributing.rst .                                                                                                                [  5%]
doc/developers/utilities.rst .                                                                                                                   [  7%]
doc/faq.rst .                                                                                                                                    [ 10%]
doc/glossary.rst .                                                                                                                               [ 12%]
doc/modules/biclustering.rst .                                                                                                                   [ 15%]
doc/modules/clustering.rst .                                                                                                                     [ 17%]
doc/modules/compose.rst s                                                                                                                        [ 20%]
doc/modules/computing.rst .                                                                                                                      [ 22%]
doc/modules/cross_validation.rst .                                                                                                               [ 25%]
doc/modules/decomposition.rst .                                                                                                                  [ 27%]
doc/modules/density.rst .                                                                                                                        [ 30%]
doc/modules/ensemble.rst .                                                                                                                       [ 32%]
doc/modules/feature_extraction.rst .                                                                                                             [ 35%]
doc/modules/feature_selection.rst .                                                                                                              [ 37%]
doc/modules/gaussian_process.rst .                                                                                                               [ 40%]
doc/modules/impute.rst s                                                                                                                         [ 42%]
doc/modules/kernel_approximation.rst .                                                                                                           [ 45%]
doc/modules/learning_curve.rst .                                                                                                                 [ 47%]
doc/modules/linear_model.rst .                                                                                                                   [ 50%]
doc/modules/metrics.rst .                                                                                                                        [ 52%]
doc/modules/model_evaluation.rst .                                                                                                               [ 55%]
doc/modules/model_persistence.rst .                                                                                                              [ 57%]
doc/modules/multiclass.rst .                                                                                                                     [ 60%]
doc/modules/naive_bayes.rst .                                                                                                                    [ 62%]
doc/modules/neighbors.rst .                                                                                                                      [ 65%]
doc/modules/neural_networks_supervised.rst .                                                                                                     [ 67%]
doc/modules/preprocessing.rst .                                                                                                                  [ 70%]
doc/modules/preprocessing_targets.rst .                                                                                                          [ 72%]
doc/modules/random_projection.rst .                                                                                                              [ 75%]
doc/modules/sgd.rst .                                                                                                                            [ 77%]
doc/modules/svm.rst .                                                                                                                            [ 80%]
doc/modules/tree.rst .                                                                                                                           [ 82%]
doc/tutorial/basic/tutorial.rst .                                                                                                                [ 85%]
doc/tutorial/statistical_inference/model_selection.rst .                                                                                         [ 87%]
doc/tutorial/statistical_inference/putting_together.rst .                                                                                        [ 90%]
doc/tutorial/statistical_inference/settings.rst .                                                                                                [ 92%]
doc/tutorial/statistical_inference/supervised_learning.rst .                                                                                     [ 95%]
doc/tutorial/statistical_inference/unsupervised_learning.rst .                                                                                   [ 97%]
doc/tutorial/text_analytics/working_with_text_data.rst s                                                                                         [100%]
=============================================================== short test summary info ================================================================
SKIP [2] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: Skipping dataset loading doctests
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: Skipping compose.rst, pandas not installed
SKIP [1] /home/vagrant/scikit-learn-python3.7-venv/lib/python3.7/site-packages/_pytest/nose.py:27: Skipping impute.rst, pandas not installed

================================================== 36 passed, 4 skipped, 99 warnings in 17.58 seconds ==================================================
(scikit-learn-python3.7-venv) vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/scikit-learn/scikit-learn$ 



