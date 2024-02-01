# Computer Language Learning

**macOS**

Package manager tool: MacPorts

Safe read/write NTFS driver in Mac OS X: Fuse + ntfs3g

Virtual machine provider and command tool: Virtual Box + Vagrant

**Linux**

Ubuntu VM

+ provide from __Vagrangfile__ and logged into _vagrant.txt_
+ earlier version script backups are in __linux/ubuntu-vagrant__

CentOS7 VM

+ __linux/centos7-vagrant__

**Python**

- NumPy
- Scikit-Learn
- Torch
- Jupyter Notebook
- Anaconda
- LLM (huggingface etc)

**Golang**

install: <https://golang.org/doc/install>

**Notes**

Mac Cache

> fanhonglingdeMacBook-Pro:~ fanhongling$ du -scm Library/Caches/* | sort -n
> ...
> 2325	Library/Caches/pip
> 2398	Library/Caches/com.apple.Safari
> 4646	Library/Caches/IdeaIC2017.3
> 10874	total

home cache

> fanhonglingdeMacBook-Pro:~ fanhongling$ ls -lAgo ~/.cache/ | tail -n+2
> drwxr-xr-x  3   102  1 29 15:11 huggingface
> drwxr-xr-x  4   136  1 29 15:21 lepton
> drwxr-xr-x  5   170  1 22 10:56 matplotlib

pip cached

> vagrant@ubuntu-jammy:~$ pip3 cache dir
> /home/vagrant/.cache/pip

> vagrant@ubuntu-jammy:~$ ln -s /Users/fanhongling/Downloads/all-shared-local-repo/home_.cache/pip .cache/

> vagrant@ubuntu-jammy:~$ pip3 cache dir
> /Users/fanhongling/Downloads/all-shared-local-repo/home_.cache/pip


golang cached

> fanhonglingdeMacBook-Pro:~ fanhongling$ go env | grep CACHE
> GOCACHE="/Users/fanhongling/Library/Caches/go-build"
> GOMODCACHE="/Users/fanhongling/go/pkg/mod"

> fanhonglingdeMacBook-Pro:~ fanhongling$ du -sh sdk/
> 502M	sdk/

vagrant cached

> fanhonglingdeMacBook-Pro:~ fanhongling$ du -sh .vagrant.d/*
> 1.5G	.vagrant.d/boxes
> ...
>  86M	.vagrant.d/gems
> 4.0K	.vagrant.d/insecure_private_key
> ...
>  10M	.vagrant.d/tmp

maven cached

>fanhonglingdeMacBook-Pro:~ fanhongling$ ls -lAgo .m2/ | tail -n+2
> lrwxr-xr-x  1   72  1 23 14:30 repository -> /Users/fanhongling/Downloads/all-shared-local-repo/maven_.m2/repository/
> lrwxr-xr-x  1   69  1 23 14:31 wrapper -> /Users/fanhongling/Downloads/all-shared-local-repo/maven_.m2/wrapper/

gradle cached

>fanhonglingdeMacBook-Pro:~ fanhongling$ ls -lAgo .gradle/ | tail -n+2
> lrwxr-xr-x   1    71  1 25 16:47 caches -> /Users/fanhongling/Downloads/all-shared-local-repo/home_.gradle/caches/
> ... 
> lrwxr-xr-x   1    72  1 25 16:34 wrapper -> /Users/fanhongling/Downloads/all-shared-local-repo/home_.gradle/wrapper/

rust-lang cached

> fanhonglingdeMacBook-Pro:~ fanhongling$ du -sh .rustup/ .cargo/
> 243M	.rustup/
> 8.3M	.cargo/

npm cached

> fanhonglingdeMacBook-Pro:~ fanhongling$ du -sh .npm
> 29M	.npm

virtualbox usage

>fanhonglingdeMacBook-Pro:~ fanhongling$ du -sg VirtualBox\ VMs/* | sort -n
> ...
> 4	VirtualBox VMs/lang-learn_default_1706138105123_98643
> 25	VirtualBox VMs/machine-learning_default_1542195237244_50777
> 32	VirtualBox VMs/vagrant-centos7_default_1616526292700_44948


disk usage of hidden files

> fanhonglingdeMacBook-Pro:~ fanhongling$ du -scm .[^.]* | sort -n
> 0	.Trash
> ...
> 2372	total
