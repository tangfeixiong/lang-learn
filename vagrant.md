# Vagrant provided Linux

1. [Vagrant](https://www.vagrantup.com/)
1. [gcc](#gcc)

## Ubuntu 18.04

up
```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'ubuntu-18.04-server-cloud' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: >= 0
==> default: Box file was not detected as metadata. Adding it directly...
==> default: Adding box 'ubuntu-18.04-server-cloud' (v0) for provider: virtualbox
    default: Downloading: https://cloud-images.ubuntu.com/releases/18.04/release/ubuntu-18.04-server-cloudimg-amd64-vagrant.box
==> default: Successfully added box 'ubuntu-18.04-server-cloud' (v0) for 'virtualbox'!
==> default: Importing base box 'ubuntu-18.04-server-cloud'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: lang-learn_default_1550177000903_27272
==> default: Fixed port collision for 22 => 2222. Now on port 2200.
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 443 (guest) => 5443 (host) (adapter 1)
    default: 22 (guest) => 2200 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2200
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default: 
    default: Guest Additions Version: 5.2.18
    default: VirtualBox Version: 5.1
==> default: Configuring and enabling network interfaces...
The following SSH command responded with a non-zero exit status.
Vagrant assumes that this means the command failed!

/sbin/ifdown 'enp0s8' || true
/sbin/ip addr flush dev 'enp0s8'
# Remove any previous network modifications from the interfaces file
sed -e '/^#VAGRANT-BEGIN/,$ d' /etc/network/interfaces > /tmp/vagrant-network-interfaces.pre
sed -ne '/^#VAGRANT-END/,$ p' /etc/network/interfaces | tac | sed -e '/^#VAGRANT-END/,$ d' | tac > /tmp/vagrant-network-interfaces.post

cat \
  /tmp/vagrant-network-interfaces.pre \
  /tmp/vagrant-network-entry \
  /tmp/vagrant-network-interfaces.post \
  > /etc/network/interfaces

rm -f /tmp/vagrant-network-interfaces.pre
rm -f /tmp/vagrant-network-entry
rm -f /tmp/vagrant-network-interfaces.post

/sbin/ifup 'enp0s8'

Stdout from the command:



Stderr from the command:

bash: line 4: /sbin/ifdown: No such file or directory
bash: line 20: /sbin/ifup: No such file or directory

```

ssh
```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant ssh
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-45-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Feb 14 20:45:09 UTC 2019

  System load:  0.16             Processes:             97
  Usage of /:   9.9% of 9.63GB   Users logged in:       0
  Memory usage: 3%               IP address for enp0s3: 10.0.2.15
  Swap usage:   0%


  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.

```

network iface
```
vagrant@ubuntu-bionic:~$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 02:88:80:28:66:3a brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic enp0s3
       valid_lft 86313sec preferred_lft 86313sec
    inet6 fe80::88:80ff:fe28:663a/64 scope link 
       valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 08:00:27:cb:ca:d4 brd ff:ff:ff:ff:ff:ff
```

apt-get
```
vagrant@ubuntu-bionic:~$ sudo apt-get update
Hit:1 http://archive.ubuntu.com/ubuntu bionic InRelease
Get:2 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
Get:3 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]           
Get:4 http://archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]
Get:5 http://security.ubuntu.com/ubuntu bionic-security/multiverse Sources [2308 B]
Get:6 http://security.ubuntu.com/ubuntu bionic-security/universe Sources [34.6 kB]
Get:7 http://archive.ubuntu.com/ubuntu bionic/restricted Sources [5324 B]         
Get:8 http://security.ubuntu.com/ubuntu bionic-security/main Sources [76.0 kB]
Get:9 http://archive.ubuntu.com/ubuntu bionic/main Sources [829 kB]
Get:10 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages [268 kB]
Get:11 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 Packages [126 kB]
Get:12 http://archive.ubuntu.com/ubuntu bionic/multiverse Sources [181 kB]      
Get:13 http://security.ubuntu.com/ubuntu bionic-security/universe Translation-en [70.6 kB]
Get:14 http://archive.ubuntu.com/ubuntu bionic/universe Sources [9051 kB]
Get:15 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 Packages [3324 B]
Get:16 http://security.ubuntu.com/ubuntu bionic-security/multiverse Translation-en [1848 B]
Get:17 http://archive.ubuntu.com/ubuntu bionic/universe amd64 Packages [8570 kB]                                                                      
Get:18 http://archive.ubuntu.com/ubuntu bionic/universe Translation-en [4941 kB]                                                                      
Get:19 http://archive.ubuntu.com/ubuntu bionic/multiverse amd64 Packages [151 kB]                                                                     
Get:20 http://archive.ubuntu.com/ubuntu bionic/multiverse Translation-en [108 kB]                                                                     
Get:21 http://archive.ubuntu.com/ubuntu bionic-updates/universe Sources [129 kB]                                                                      
Get:22 http://archive.ubuntu.com/ubuntu bionic-updates/main Sources [246 kB]                                                                          
Get:23 http://archive.ubuntu.com/ubuntu bionic-updates/restricted Sources [2064 B]                                                                    
Get:24 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse Sources [4192 B]                                                                    
Get:25 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [523 kB]                                                                   
Get:26 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [730 kB]                                                               
Get:27 http://archive.ubuntu.com/ubuntu bionic-updates/universe Translation-en [185 kB]                                                               
Get:28 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 Packages [6384 B]                                                             
Get:29 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse Translation-en [3452 B]                                                             
Get:30 http://archive.ubuntu.com/ubuntu bionic-backports/universe Sources [2068 B]                                                                    
Get:31 http://archive.ubuntu.com/ubuntu bionic-backports/universe amd64 Packages [3472 B]                                                             
Get:32 http://archive.ubuntu.com/ubuntu bionic-backports/universe Translation-en [1604 B]                                                             
Fetched 26.5 MB in 24s (1094 kB/s)                                                                                                                    
Reading package lists... Done
```

iface tools
```
vagrant@ubuntu-bionic:~$ sudo apt-cache search ifupdown
ifupdown - high level tools to configure network interfaces
guessnet - Guess which LAN a network device is connected to
ifupdown-extra - Network scripts for ifupdown
ifupdown-multi - multiple default gateway support for ifupdown
ifupdown2 - Network Interface Management tool similar to ifupdown
netscript-2.4 - Linux 2.4/2.6/3.x router/firewall/VM host network config system.
netscript-ipfilter - Linux 2.6/3.x iptables management system.
```

```
vagrant@ubuntu-bionic:~$ sudo apt install ifupdown
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Suggested packages:
  ppp rdnssd
The following NEW packages will be installed:
  ifupdown
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 55.9 kB of archives.
After this operation, 227 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 ifupdown amd64 0.8.17ubuntu1.1 [55.9 kB]
Fetched 55.9 kB in 1s (81.7 kB/s) 
Selecting previously unselected package ifupdown.
(Reading database ... 59746 files and directories currently installed.)
Preparing to unpack .../ifupdown_0.8.17ubuntu1.1_amd64.deb ...
Unpacking ifupdown (0.8.17ubuntu1.1) ...
Setting up ifupdown (0.8.17ubuntu1.1) ...
Created symlink /etc/systemd/system/multi-user.target.wants/networking.service → /lib/systemd/system/networking.service.
Created symlink /etc/systemd/system/network-online.target.wants/networking.service → /lib/systemd/system/networking.service.
Processing triggers for ureadahead (0.100.0-20) ...
Processing triggers for systemd (237-3ubuntu10.12) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
```

exit
```
vagrant@ubuntu-bionic:~$ exit
logout
Connection to 127.0.0.1 closed.
```

reload
```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant reload
==> default: Attempting graceful shutdown of VM...
==> default: Clearing any previously set forwarded ports...
==> default: Fixed port collision for 22 => 2222. Now on port 2200.
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 443 (guest) => 5443 (host) (adapter 1)
    default: 22 (guest) => 2200 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2200
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection reset. Retrying...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default: 
    default: Guest Additions Version: 5.2.18
    default: VirtualBox Version: 5.1
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /Users/fanhongling/go => /Users/fanhongling/go
    default: /Users/fanhongling/Downloads => /Users/fanhongling/Downloads
```

login
```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant ssh
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-45-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Feb 14 20:51:20 UTC 2019

  System load:  0.08              Processes:             99
  Usage of /:   11.8% of 9.63GB   Users logged in:       0
  Memory usage: 3%                IP address for enp0s3: 10.0.2.15
  Swap usage:   0%                IP address for enp0s8: 172.28.128.5


  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.


Last login: Thu Feb 14 20:45:10 2019 from 10.0.2.2
```

### gcc

apt-get
```
vagrant@ubuntu-bionic:~$ sudo apt-get install -y build-essential 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu cpp cpp-7 dpkg-dev fakeroot g++ g++-7 gcc gcc-7 gcc-7-base libalgorithm-diff-perl
  libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan4 libatomic1 libbinutils libc-dev-bin libc6-dev libcc1-0 libcilkrts5 libdpkg-perl
  libfakeroot libfile-fcntllock-perl libgcc-7-dev libgomp1 libisl19 libitm1 liblsan0 libmpc3 libmpx2 libquadmath0 libstdc++-7-dev libtsan0 libubsan0
  linux-libc-dev make manpages-dev
Suggested packages:
  binutils-doc cpp-doc gcc-7-locales debian-keyring g++-multilib g++-7-multilib gcc-7-doc libstdc++6-7-dbg gcc-multilib autoconf automake libtool
  flex bison gdb gcc-doc gcc-7-multilib libgcc1-dbg libgomp1-dbg libitm1-dbg libatomic1-dbg libasan4-dbg liblsan0-dbg libtsan0-dbg libubsan0-dbg
  libcilkrts5-dbg libmpx2-dbg libquadmath0-dbg glibc-doc bzr libstdc++-7-doc make-doc
The following NEW packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-7 dpkg-dev fakeroot g++ g++-7 gcc gcc-7 gcc-7-base
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan4 libatomic1 libbinutils libc-dev-bin libc6-dev libcc1-0
  libcilkrts5 libdpkg-perl libfakeroot libfile-fcntllock-perl libgcc-7-dev libgomp1 libisl19 libitm1 liblsan0 libmpc3 libmpx2 libquadmath0
  libstdc++-7-dev libtsan0 libubsan0 linux-libc-dev make manpages-dev
0 upgraded, 40 newly installed, 0 to remove and 0 not upgraded.
Need to get 37.1 MB of archives.
After this operation, 161 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 binutils-common amd64 2.30-21ubuntu1~18.04 [193 kB]

### snipp >>>

Get:40 http://archive.ubuntu.com/ubuntu bionic/main amd64 manpages-dev all 4.15-1 [2217 kB]                                                           
Fetched 37.1 MB in 19s (1907 kB/s)                                                                                                                    
Extracting templates from packages: 100%
Selecting previously unselected package binutils-common:amd64.
(Reading database ... 59783 files and directories currently installed.)
Preparing to unpack .../00-binutils-common_2.30-21ubuntu1~18.04_amd64.deb ...
Unpacking binutils-common:amd64 (2.30-21ubuntu1~18.04) ...

### snipp >>>

Selecting previously unselected package manpages-dev.
Preparing to unpack .../39-manpages-dev_4.15-1_all.deb ...
Unpacking manpages-dev (4.15-1) ...
Setting up libquadmath0:amd64 (8.2.0-1ubuntu2~18.04) ...
Setting up libgomp1:amd64 (8.2.0-1ubuntu2~18.04) ...
Setting up libatomic1:amd64 (8.2.0-1ubuntu2~18.04) ...
Setting up libcc1-0:amd64 (8.2.0-1ubuntu2~18.04) ...
Setting up make (4.1-9.1ubuntu1) ...
Setting up libtsan0:amd64 (8.2.0-1ubuntu2~18.04) ...
Setting up linux-libc-dev:amd64 (4.15.0-45.48) ...
Setting up libdpkg-perl (1.19.0.5ubuntu2.1) ...
Setting up liblsan0:amd64 (8.2.0-1ubuntu2~18.04) ...
Setting up gcc-7-base:amd64 (7.3.0-27ubuntu1~18.04) ...
Setting up binutils-common:amd64 (2.30-21ubuntu1~18.04) ...
Setting up libfile-fcntllock-perl (0.22-3build2) ...
Setting up libmpx2:amd64 (8.2.0-1ubuntu2~18.04) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
Setting up libfakeroot:amd64 (1.22-2ubuntu1) ...
Setting up libalgorithm-diff-perl (1.19.03-1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Setting up libmpc3:amd64 (1.1.0-1) ...
Setting up libc-dev-bin (2.27-3ubuntu1) ...
Setting up manpages-dev (4.15-1) ...
Setting up libc6-dev:amd64 (2.27-3ubuntu1) ...
Setting up libitm1:amd64 (8.2.0-1ubuntu2~18.04) ...
Setting up libisl19:amd64 (0.19-1) ...
Setting up libasan4:amd64 (7.3.0-27ubuntu1~18.04) ...
Setting up libbinutils:amd64 (2.30-21ubuntu1~18.04) ...
Setting up libcilkrts5:amd64 (7.3.0-27ubuntu1~18.04) ...
Setting up libubsan0:amd64 (7.3.0-27ubuntu1~18.04) ...
Setting up fakeroot (1.22-2ubuntu1) ...
update-alternatives: using /usr/bin/fakeroot-sysv to provide /usr/bin/fakeroot (fakeroot) in auto mode
Setting up libgcc-7-dev:amd64 (7.3.0-27ubuntu1~18.04) ...
Setting up cpp-7 (7.3.0-27ubuntu1~18.04) ...
Setting up libstdc++-7-dev:amd64 (7.3.0-27ubuntu1~18.04) ...
Setting up libalgorithm-merge-perl (0.08-3) ...
Setting up libalgorithm-diff-xs-perl (0.04-5) ...
Setting up binutils-x86-64-linux-gnu (2.30-21ubuntu1~18.04) ...
Setting up cpp (4:7.3.0-3ubuntu2.1) ...
Setting up binutils (2.30-21ubuntu1~18.04) ...
Setting up gcc-7 (7.3.0-27ubuntu1~18.04) ...
Setting up g++-7 (7.3.0-27ubuntu1~18.04) ...
Setting up gcc (4:7.3.0-3ubuntu2.1) ...
Setting up dpkg-dev (1.19.0.5ubuntu2.1) ...
Setting up g++ (4:7.3.0-3ubuntu2.1) ...
update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
Setting up build-essential (12.4ubuntu1) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
```