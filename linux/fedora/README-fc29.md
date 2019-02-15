
### Fedora-29-cloud-base

up
```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'fedora-29-cloud-base' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: >= 0
==> default: Box file was not detected as metadata. Adding it directly...
==> default: Adding box 'fedora-29-cloud-base' (v0) for provider: virtualbox
    default: Downloading: https://dl.fedoraproject.org/pub/fedora/linux/releases/29/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-29-1.2.x86_64.vagrant-virtualbox.box
==> default: Successfully added box 'fedora-29-cloud-base' (v0) for 'virtualbox'!
==> default: Importing base box 'fedora-29-cloud-base'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: lang-learn_default_1550165286258_208
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
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default: 
    default: Guest Additions Version: 5.2.0 r68940
    default: VirtualBox Version: 5.1
==> default: Configuring and enabling network interfaces...
    default: SSH address: 127.0.0.1:2200
    default: SSH username: vagrant
    default: SSH auth method: private key
==> default: Mounting shared folders...
    default: /Users/fanhongling/go => /Users/fanhongling/go
Vagrant was unable to mount VirtualBox shared folders. This is usually
because the filesystem "vboxsf" is not available. This filesystem is
made available via the VirtualBox Guest Additions and kernel module.
Please verify that these guest additions are properly installed in the
guest. This is not a bug in Vagrant and is usually caused by a faulty
Vagrant box. For context, the command attempted was:

mount -t vboxsf -o uid=1000,gid=1000 Users_fanhongling_go /Users/fanhongling/go

The error output from the command was:

```

```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant ssh
```

```
[vagrant@localhost ~]$ hostname -I
10.0.2.15 172.28.128.4 
```

```
[vagrant@localhost ~]$ exit
logout
Connection to 127.0.0.1 closed.
```

```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ ls /Applications/VirtualBox.app/Contents/MacOS/VBoxGuestAdditions.iso 
/Applications/VirtualBox.app/Contents/MacOS/VBoxGuestAdditions.iso
```

```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ scp -i ~/.ssh/vagrant /Applications/VirtualBox.app/Contents/MacOS/VBoxGuestAdditions.iso vagrant@172.28.128.4:/home/vagrant
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
8e:b8:ff:72:0d:0f:e2:07:d2:79:48:34:d9:94:55:d4.
Please contact your system administrator.
Add correct host key in /Users/fanhongling/.ssh/known_hosts to get rid of this message.
Offending RSA key in /Users/fanhongling/.ssh/known_hosts:76
RSA host key for 172.28.128.4 has changed and you have requested strict checking.
Host key verification failed.
lost connection
```

```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ cat ~/.ssh/known_hosts | grep 172.28.128.4
172.28.128.4 ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCh42nO+psbdVivwN95oLwQxhY2szn+yNJOqDidcMrBviE5eiY5Mzlt9pW83cydc89jhcjUzmYRaRjLY11toS4v3x+EhLuEiGZoffs5KhKzgNQOkGLbOXqcs0l9DfYDh0vCruHejUXxiOBg1oPb5cbPphYBTlTHq9oCN1fwvXvczaysWXvcWadL7lvzltUBxf8A+5t6dOt4lHsDRDpb+9FbBLB1MdwbvrMQHksvlpyfqr5K7s+pDPr6EcIlNg4r7vTDD7r9APHz5MwfmJSCnCfiBUDi9KT+sYaBZOkVXRXnBB/AClFc3jOX1QNDjEIKyEGh54S+7SMIPvCOS8EMGW51
```

```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ sed -i '' '/172.28.128.4/d' ~/.ssh/known_hosts 
```

```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ cat ~/.ssh/known_hosts | grep 172.28.128.4
```

```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ scp -i ~/.ssh/vagrant.pub /Applications/VirtualBox.app/Contents/MacOS/VBoxGuestAdditions.iso vagrant@172.28.128.4:/home/vagrant
The authenticity of host '172.28.128.4 (172.28.128.4)' can't be established.
RSA key fingerprint is 8e:b8:ff:72:0d:0f:e2:07:d2:79:48:34:d9:94:55:d4.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '172.28.128.4' (RSA) to the list of known hosts.
VBoxGuestAdditions.iso                                                                                               100%   57MB  56.7MB/s   00:01    
```

```
fanhonglingdeMacBook-Pro:lang-learn fanhongling$ ssh -i ~/.ssh/vagrant vagrant@172.28.128.4
Last login: Thu Feb 14 18:05:02 2019 from 10.0.2.2
```

```
[vagrant@localhost ~]$ mkdir dvd
```

```
[vagrant@localhost ~]$ sudo mount -t iso9660 -o loop VBoxGuestAdditions.iso dvd/
mount: /home/vagrant/dvd: WARNING: device write-protected, mounted read-only.
```

```
[vagrant@localhost ~]$ ls dvd/
32Bit  AUTORUN.INF  VBoxLinuxAdditions.run    VBoxWindowsAdditions-amd64.exe  VBoxWindowsAdditions.exe  cert
64Bit  OS2          VBoxSolarisAdditions.pkg  VBoxWindowsAdditions-x86.exe    autorun.sh                runasroot.sh
```

```
[vagrant@localhost ~]$ sudo dnf group info "C Development Tools and Libraries"
Failed to set locale, defaulting to C
Last metadata expiration check: 0:22:40 ago on Thu Feb 14 17:51:03 2019.

Group: C Development Tools and Libraries
 Description: These tools include core development tools such as automake, gcc and debuggers.
 Mandatory Packages:
   autoconf
   automake
   binutils
   bison
   flex
   gcc
   gcc-c++
   gdb
   glibc-devel
   libtool
   make
   pkgconf
   strace
 Default Packages:
   byacc
   ccache
   cscope
   ctags
   elfutils
   indent
   ltrace
   oprofile
   valgrind
 Optional Packages:
   ElectricFence
   astyle
   cbmc
   check
   cmake
   coan
   cproto
   insight
   nasm
   pscan
   python2-scons
   remake
   scorep
   splint
   trinity
   yasm
   zzuf
```

```
[vagrant@localhost ~]$ sudo dnf group install -y "C Development Tools and Libraries"
Failed to set locale, defaulting to C
Last metadata expiration check: 0:24:38 ago on Thu Feb 14 17:51:03 2019.
Dependencies resolved.
=======================================================================================================================================================
 Package                                Arch                   Version                                                   Repository               Size
=======================================================================================================================================================
Upgrading:
 elfutils-libelf                        x86_64                 0.174-5.fc29                                              updates                 177 k
 elfutils-libs                          x86_64                 0.174-5.fc29                                              updates                 259 k
 glibc                                  x86_64                 2.28-26.fc29                                              updates                 3.8 M
 glibc-common                           x86_64                 2.28-26.fc29                                              updates                 799 k
 glibc-langpack-en                      x86_64                 2.28-26.fc29                                              updates                 815 k
 libgcc                                 x86_64                 8.2.1-6.fc29                                              updates                  96 k
 libgomp                                x86_64                 8.2.1-6.fc29                                              updates                 206 k
 libstdc++                              x86_64                 8.2.1-6.fc29                                              updates                 456 k
Installing group/module packages:
 binutils                               x86_64                 2.31.1-17.fc29                                            updates                 6.0 M
 ccache                                 x86_64                 3.4.2-4.fc29                                              updates                 216 k
 cscope                                 x86_64                 15.9-2.fc29                                               updates                 206 k
 elfutils                               x86_64                 0.174-5.fc29                                              updates                 291 k
 gcc-c++                                x86_64                 8.2.1-6.fc29                                              updates                  12 M
 gdb                                    x86_64                 8.2-6.fc29                                                updates                 129 k
 glibc-devel                            x86_64                 2.28-26.fc29                                              updates                 1.0 M
 indent                                 x86_64                 2.2.11-27.fc29                                            updates                 150 k
 oprofile                               x86_64                 1.3.0-1.fc29                                              updates                 2.2 M
 strace                                 x86_64                 4.26-1.fc29                                               updates                 956 k
 valgrind                               x86_64                 1:3.14.0-10.fc29                                          updates                  11 M
 autoconf                               noarch                 2.69-28.fc29                                              fedora                  698 k
 automake                               noarch                 1.16.1-5.fc29                                             fedora                  696 k
 bison                                  x86_64                 3.0.5-1.fc29                                              fedora                  686 k
 byacc                                  x86_64                 1.9.20170709-6.fc29                                       fedora                   82 k
 ctags                                  x86_64                 5.8-24.fc29                                               fedora                  164 k
 flex                                   x86_64                 2.6.1-10.fc29                                             fedora                  308 k
 libtool                                x86_64                 2.4.6-27.fc29                                             fedora                  687 k
 ltrace                                 x86_64                 0.7.91-28.fc29                                            fedora                  143 k
 make                                   x86_64                 1:4.2.1-10.fc29                                           fedora                  487 k
 pkgconf                                x86_64                 1.5.3-2.fc29                                              fedora                   39 k
Installing dependencies:
 cpp                                    x86_64                 8.2.1-6.fc29                                              updates                  10 M
 gcc                                    x86_64                 8.2.1-6.fc29                                              updates                  23 M
 gdb-headless                           x86_64                 8.2-6.fc29                                                updates                 3.3 M
 glibc-headers                          x86_64                 2.28-26.fc29                                              updates                 464 k
 kernel-headers                         x86_64                 4.20.7-200.fc29                                           updates                 1.2 M
 libstdc++-devel                        x86_64                 8.2.1-6.fc29                                              updates                 2.1 M
 perl-Data-Dumper                       x86_64                 2.173-1.fc29                                              updates                  54 k
 perl-Errno                             x86_64                 1.29-427.fc29                                             updates                  24 k
 perl-File-Temp                         noarch                 1:0.230.900-1.fc29                                        updates                  61 k
 perl-IO                                x86_64                 1.39-427.fc29                                             updates                  89 k
 perl-Net-SSLeay                        x86_64                 1.85-9.fc29                                               updates                 324 k
 perl-interpreter                       x86_64                 4:5.28.1-427.fc29                                         updates                 6.4 M
 perl-libs                              x86_64                 4:5.28.1-427.fc29                                         updates                 1.6 M
 perl-macros                            x86_64                 4:5.28.1-427.fc29                                         updates                  20 k
 perl-threads-shared                    x86_64                 1.59-1.fc29                                               updates                  42 k
 emacs-filesystem                       noarch                 1:26.1-6.fc29                                             fedora                   10 k
 gc                                     x86_64                 7.6.4-4.fc29                                              fedora                  101 k
 guile                                  x86_64                 5:2.0.14-12.fc29                                          fedora                  3.5 M
 isl                                    x86_64                 0.16.1-7.fc29                                             fedora                  841 k
 libatomic_ops                          x86_64                 7.6.6-1.fc29                                              fedora                   34 k
 libbabeltrace                          x86_64                 1.5.6-1.fc29                                              fedora                  197 k
 libipt                                 x86_64                 2.0-1.fc29                                                fedora                   50 k
 libmpc                                 x86_64                 1.1.0-2.fc29                                              fedora                   58 k
 libpkgconf                             x86_64                 1.5.3-2.fc29                                              fedora                   35 k
 libtool-ltdl                           x86_64                 2.4.6-27.fc29                                             fedora                   34 k
 libxcrypt-devel                        x86_64                 4.2.1-3.fc29                                              fedora                   25 k
 m4                                     x86_64                 1.4.18-9.fc29                                             fedora                  214 k
 perl-Carp                              noarch                 1.50-417.fc29                                             fedora                   29 k
 perl-Digest                            noarch                 1.17-417.fc29                                             fedora                   24 k
 perl-Digest-MD5                        x86_64                 2.55-417.fc29                                             fedora                   35 k
 perl-Encode                            x86_64                 4:2.98-6.fc29                                             fedora                  1.5 M
 perl-Exporter                          noarch                 5.73-418.fc29                                             fedora                   31 k
 perl-File-Path                         noarch                 2.16-1.fc29                                               fedora                   36 k
 perl-Getopt-Long                       noarch                 1:2.50-417.fc29                                           fedora                   61 k
 perl-HTTP-Tiny                         noarch                 0.076-1.fc29                                              fedora                   55 k
 perl-MIME-Base64                       x86_64                 3.15-417.fc29                                             fedora                   30 k
 perl-PathTools                         x86_64                 3.75-1.fc29                                               fedora                   85 k
 perl-Pod-Escapes                       noarch                 1:1.07-417.fc29                                           fedora                   19 k
 perl-Pod-Perldoc                       noarch                 3.28.01-418.fc29                                          fedora                   83 k
 perl-Pod-Simple                        noarch                 1:3.35-417.fc29                                           fedora                  211 k
 perl-Pod-Usage                         noarch                 4:1.69-417.fc29                                           fedora                   32 k
 perl-Scalar-List-Utils                 x86_64                 3:1.50-417.fc29                                           fedora                   64 k
 perl-Socket                            x86_64                 4:2.027-417.fc29                                          fedora                   54 k
 perl-Storable                          x86_64                 1:3.11-5.fc29                                             fedora                   94 k
 perl-Term-ANSIColor                    noarch                 4.06-418.fc29                                             fedora                   44 k
 perl-Term-Cap                          noarch                 1.17-417.fc29                                             fedora                   22 k
 perl-Text-ParseWords                   noarch                 3.30-417.fc29                                             fedora                   16 k
 perl-Text-Tabs+Wrap                    noarch                 2013.0523-417.fc29                                        fedora                   23 k
 perl-Thread-Queue                      noarch                 3.13-1.fc29                                               fedora                   21 k
 perl-Time-Local                        noarch                 2:1.280-3.fc29                                            fedora                   31 k
 perl-URI                               noarch                 1.74-4.fc29                                               fedora                  109 k
 perl-Unicode-Normalize                 x86_64                 1.26-417.fc29                                             fedora                   81 k
 perl-constant                          noarch                 1.33-418.fc29                                             fedora                   23 k
 perl-libnet                            noarch                 3.11-418.fc29                                             fedora                  120 k
 perl-parent                            noarch                 1:0.237-2.fc29                                            fedora                   14 k
 perl-podlators                         noarch                 1:4.11-3.fc29                                             fedora                  115 k
 perl-threads                           x86_64                 1:2.22-417.fc29                                           fedora                   57 k
 pkgconf-m4                             noarch                 1.5.3-2.fc29                                              fedora                   17 k
 pkgconf-pkg-config                     x86_64                 1.5.3-2.fc29                                              fedora                   15 k
 xemacs-filesystem                      noarch                 21.5.34-30.20171230hg92757c2b8239.fc29                    fedora                   10 k
Installing weak dependencies:
 gcc-gdb-plugin                         x86_64                 8.2.1-6.fc29                                              updates                 135 k
 perl-IO-Socket-SSL                     noarch                 2.060-3.fc29                                              updates                 236 k
 perl-IO-Socket-IP                      noarch                 0.39-418.fc29                                             fedora                   42 k
 perl-Mozilla-CA                        noarch                 20180117-3.fc29                                           fedora                   12 k

Transaction Summary
=======================================================================================================================================================
Install  85 Packages
Upgrade   8 Packages

Total download size: 101 M
Downloading Packages:
(1/93): ccache-3.4.2-4.fc29.x86_64.rpm                                                                                 128 kB/s | 216 kB     00:01    

### snipp >>>

(93/93): glibc-2.28-26.fc29.x86_64.rpm                                                                                 1.5 MB/s | 3.8 MB     00:02    
-------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                  2.9 MB/s | 101 MB     00:35     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                               1/1 
Upgrade: glibc-common-2.28-26.fc29.x86_64
  Upgrading        : glibc-common-2.28-26.fc29.x86_64                                                                                            1/101 
Upgrade: glibc-common-2.28-26.fc29.x86_64

### snipp >>>

Upgraded: libgcc-8.2.1-2.fc29.x86_64
  Cleanup          : libgcc-8.2.1-2.fc29.x86_64                                                                                                101/101 
Upgraded: libgcc-8.2.1-2.fc29.x86_64
  Running scriptlet: libgcc-8.2.1-2.fc29.x86_64                                                                                                101/101 
  Running scriptlet: glibc-common-2.28-26.fc29.x86_64                                                                                          101/101 
  Verifying        : binutils-2.31.1-17.fc29.x86_64                                                                                              1/101 

### snipp >>>

  Verifying        : libstdc++-8.2.1-2.fc29.x86_64                                                                                             101/101 

Upgraded:
  elfutils-libelf-0.174-5.fc29.x86_64       elfutils-libs-0.174-5.fc29.x86_64     glibc-2.28-26.fc29.x86_64       glibc-common-2.28-26.fc29.x86_64    
  glibc-langpack-en-2.28-26.fc29.x86_64     libgcc-8.2.1-6.fc29.x86_64            libgomp-8.2.1-6.fc29.x86_64     libstdc++-8.2.1-6.fc29.x86_64       

Installed:
  binutils-2.31.1-17.fc29.x86_64                                                        ccache-3.4.2-4.fc29.x86_64                                     
  cscope-15.9-2.fc29.x86_64                                                             elfutils-0.174-5.fc29.x86_64                                   
  gcc-c++-8.2.1-6.fc29.x86_64                                                           gdb-8.2-6.fc29.x86_64                                          
  glibc-devel-2.28-26.fc29.x86_64                                                       indent-2.2.11-27.fc29.x86_64                                   
  oprofile-1.3.0-1.fc29.x86_64                                                          strace-4.26-1.fc29.x86_64                                      
  valgrind-1:3.14.0-10.fc29.x86_64                                                      autoconf-2.69-28.fc29.noarch                                   
  automake-1.16.1-5.fc29.noarch                                                         bison-3.0.5-1.fc29.x86_64                                      
  byacc-1.9.20170709-6.fc29.x86_64                                                      ctags-5.8-24.fc29.x86_64                                       
  flex-2.6.1-10.fc29.x86_64                                                             libtool-2.4.6-27.fc29.x86_64                                   
  ltrace-0.7.91-28.fc29.x86_64                                                          make-1:4.2.1-10.fc29.x86_64                                    
  pkgconf-1.5.3-2.fc29.x86_64                                                           gcc-gdb-plugin-8.2.1-6.fc29.x86_64                             
  perl-IO-Socket-SSL-2.060-3.fc29.noarch                                                perl-IO-Socket-IP-0.39-418.fc29.noarch                         
  perl-Mozilla-CA-20180117-3.fc29.noarch                                                cpp-8.2.1-6.fc29.x86_64                                        
  gcc-8.2.1-6.fc29.x86_64                                                               gdb-headless-8.2-6.fc29.x86_64                                 
  glibc-headers-2.28-26.fc29.x86_64                                                     kernel-headers-4.20.7-200.fc29.x86_64                          
  libstdc++-devel-8.2.1-6.fc29.x86_64                                                   perl-Data-Dumper-2.173-1.fc29.x86_64                           
  perl-Errno-1.29-427.fc29.x86_64                                                       perl-File-Temp-1:0.230.900-1.fc29.noarch                       
  perl-IO-1.39-427.fc29.x86_64                                                          perl-Net-SSLeay-1.85-9.fc29.x86_64                             
  perl-interpreter-4:5.28.1-427.fc29.x86_64                                             perl-libs-4:5.28.1-427.fc29.x86_64                             
  perl-macros-4:5.28.1-427.fc29.x86_64                                                  perl-threads-shared-1.59-1.fc29.x86_64                         
  emacs-filesystem-1:26.1-6.fc29.noarch                                                 gc-7.6.4-4.fc29.x86_64                                         
  guile-5:2.0.14-12.fc29.x86_64                                                         isl-0.16.1-7.fc29.x86_64                                       
  libatomic_ops-7.6.6-1.fc29.x86_64                                                     libbabeltrace-1.5.6-1.fc29.x86_64                              
  libipt-2.0-1.fc29.x86_64                                                              libmpc-1.1.0-2.fc29.x86_64                                     
  libpkgconf-1.5.3-2.fc29.x86_64                                                        libtool-ltdl-2.4.6-27.fc29.x86_64                              
  libxcrypt-devel-4.2.1-3.fc29.x86_64                                                   m4-1.4.18-9.fc29.x86_64                                        
  perl-Carp-1.50-417.fc29.noarch                                                        perl-Digest-1.17-417.fc29.noarch                               
  perl-Digest-MD5-2.55-417.fc29.x86_64                                                  perl-Encode-4:2.98-6.fc29.x86_64                               
  perl-Exporter-5.73-418.fc29.noarch                                                    perl-File-Path-2.16-1.fc29.noarch                              
  perl-Getopt-Long-1:2.50-417.fc29.noarch                                               perl-HTTP-Tiny-0.076-1.fc29.noarch                             
  perl-MIME-Base64-3.15-417.fc29.x86_64                                                 perl-PathTools-3.75-1.fc29.x86_64                              
  perl-Pod-Escapes-1:1.07-417.fc29.noarch                                               perl-Pod-Perldoc-3.28.01-418.fc29.noarch                       
  perl-Pod-Simple-1:3.35-417.fc29.noarch                                                perl-Pod-Usage-4:1.69-417.fc29.noarch                          
  perl-Scalar-List-Utils-3:1.50-417.fc29.x86_64                                         perl-Socket-4:2.027-417.fc29.x86_64                            
  perl-Storable-1:3.11-5.fc29.x86_64                                                    perl-Term-ANSIColor-4.06-418.fc29.noarch                       
  perl-Term-Cap-1.17-417.fc29.noarch                                                    perl-Text-ParseWords-3.30-417.fc29.noarch                      
  perl-Text-Tabs+Wrap-2013.0523-417.fc29.noarch                                         perl-Thread-Queue-3.13-1.fc29.noarch                           
  perl-Time-Local-2:1.280-3.fc29.noarch                                                 perl-URI-1.74-4.fc29.noarch                                    
  perl-Unicode-Normalize-1.26-417.fc29.x86_64                                           perl-constant-1.33-418.fc29.noarch                             
  perl-libnet-3.11-418.fc29.noarch                                                      perl-parent-1:0.237-2.fc29.noarch                              
  perl-podlators-1:4.11-3.fc29.noarch                                                   perl-threads-1:2.22-417.fc29.x86_64                            
  pkgconf-m4-1.5.3-2.fc29.noarch                                                        pkgconf-pkg-config-1.5.3-2.fc29.x86_64                         
  xemacs-filesystem-21.5.34-30.20171230hg92757c2b8239.fc29.noarch                      

Complete!
```

```
[vagrant@localhost ~]$ sudo dvd/VBoxLinuxAdditions.run 
Verifying archive integrity... All good.
Uncompressing VirtualBox 5.1.30 Guest Additions for Linux...........
VirtualBox Guest Additions installer
Copying additional installer modules ...
Installing additional modules ...
vboxadd.sh: Starting the VirtualBox Guest Additions.

Could not find the X.Org or XFree86 Window System, skipping.
```

```
[vagrant@localhost ~]$ sudo dnf search xorg | head
Failed to set locale, defaulting to C
Last metadata expiration check: 0:36:26 ago on Thu Feb 14 17:51:03 2019.
========================= Summary & Name Matched: xorg =========================
abrt-addon-xorg.x86_64 : abrt's Xorg addon
xorg-x11-server-Xorg.x86_64 : Xorg X server
xorg-x11-drv-ati.x86_64 : Xorg X11 ati video driver
xorg-x11-drv-qxl.x86_64 : Xorg X11 qxl video driver
xorg-x11-drv-v4l.x86_64 : Xorg X11 v4l video driver
xorg-x11-drv-fbturbo.x86_64 : Xorg X11 fbturbo driver
xorg-x11-drv-ivtv.x86_64 : Xorg X11 ivtv video driver
xorg-x11-drv-vesa.x86_64 : Xorg X11 vesa video driver
xorg-x11-drv-dummy.x86_64 : Xorg X11 dummy video driver
```

```
[vagrant@localhost ~]$ sudo dnf install -y xorg-x11-server-Xorg
Failed to set locale, defaulting to C
Last metadata expiration check: 0:38:33 ago on Thu Feb 14 17:51:03 2019.
Dependencies resolved.
=======================================================================================================================================================
 Package                                      Arch                         Version                                 Repository                     Size
=======================================================================================================================================================
Installing:
 xorg-x11-server-Xorg                         x86_64                       1.20.3-3.fc29                           updates                       1.4 M
Installing dependencies:
 hwdata                                       noarch                       0.320-1.fc29                            updates                       1.5 M
 libX11                                       x86_64                       1.6.7-1.fc29                            updates                       593 k
 libX11-common                                noarch                       1.6.7-1.fc29                            updates                       155 k
 libX11-xcb                                   x86_64                       1.6.7-1.fc29                            updates                        11 k
 libdrm                                       x86_64                       2.4.97-1.fc29                           updates                       145 k
 libinput                                     x86_64                       1.12.6-1.fc29                           updates                       166 k
 libwacom                                     x86_64                       0.32-2.fc29                             updates                        31 k
 libwacom-data                                noarch                       0.32-2.fc29                             updates                        74 k
 mesa-libEGL                                  x86_64                       18.2.8-1.fc29                           updates                       104 k
 mesa-libGL                                   x86_64                       18.2.8-1.fc29                           updates                       148 k
 mesa-libgbm                                  x86_64                       18.2.8-1.fc29                           updates                        36 k
 mesa-libglapi                                x86_64                       18.2.8-1.fc29                           updates                        36 k
 xorg-x11-drv-libinput                        x86_64                       0.28.2-1.fc29                           updates                        43 k
 xorg-x11-server-common                       x86_64                       1.20.3-3.fc29                           updates                        36 k
 libXau                                       x86_64                       1.0.8-14.fc29                           fedora                         29 k
 libXdamage                                   x86_64                       1.1.4-15.fc29                           fedora                         21 k
 libXdmcp                                     x86_64                       1.1.2-12.fc29                           fedora                         34 k
 libXext                                      x86_64                       1.3.3-10.fc29                           fedora                         38 k
 libXfixes                                    x86_64                       5.0.3-8.fc29                            fedora                         18 k
 libXfont2                                    x86_64                       2.0.3-3.fc29                            fedora                        148 k
 libXxf86vm                                   x86_64                       1.1.4-10.fc29                           fedora                         17 k
 libepoxy                                     x86_64                       1.5.3-1.fc29                            fedora                        197 k
 libevdev                                     x86_64                       1.5.9-5.fc29                            fedora                         38 k
 libfontenc                                   x86_64                       1.1.3-9.fc29                            fedora                         30 k
 libglvnd                                     x86_64                       1:1.1.0-2.fc29                          fedora                         65 k
 libglvnd-egl                                 x86_64                       1:1.1.0-2.fc29                          fedora                         43 k
 libglvnd-glx                                 x86_64                       1:1.1.0-2.fc29                          fedora                        114 k
 libgudev                                     x86_64                       232-4.fc29                              fedora                         32 k
 libpciaccess                                 x86_64                       0.14-2.fc29                             fedora                         26 k
 libunwind                                    x86_64                       1.2.1-6.fc29                            fedora                         61 k
 libwayland-client                            x86_64                       1.16.0-1.fc29                           fedora                         31 k
 libwayland-server                            x86_64                       1.16.0-1.fc29                           fedora                         37 k
 libxcb                                       x86_64                       1.13.1-1.fc29                           fedora                        201 k
 libxkbfile                                   x86_64                       1.0.9-11.fc29                           fedora                         85 k
 libxshmfence                                 x86_64                       1.3-3.fc29                              fedora                         12 k
 mtdev                                        x86_64                       1.1.5-13.fc29                           fedora                         20 k
 pixman                                       x86_64                       0.34.0-10.fc29                          fedora                        253 k
 xorg-x11-xkb-utils                           x86_64                       7.7-27.fc29                             fedora                        110 k

Transaction Summary
=======================================================================================================================================================
Install  39 Packages

Total download size: 6.0 M
Installed size: 23 M
Downloading Packages:
(1/39): libX11-common-1.6.7-1.fc29.noarch.rpm                                                                           70 kB/s | 155 kB     00:02    

### snipp >>>

(39/39): xorg-x11-server-Xorg-1.20.3-3.fc29.x86_64.rpm                                                                 143 kB/s | 1.4 MB     00:10    
-------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                  292 kB/s | 6.0 MB     00:21     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                               1/1 
Installed: libxshmfence-1.3-3.fc29.x86_64
  Installing       : libxshmfence-1.3-3.fc29.x86_64                                                                                               1/39 
Installed: libxshmfence-1.3-3.fc29.x86_64

### snipp >>>

Installed: xorg-x11-server-Xorg-1.20.3-3.fc29.x86_64
  Installing       : xorg-x11-server-Xorg-1.20.3-3.fc29.x86_64                                                                                   39/39 
Installed: xorg-x11-server-Xorg-1.20.3-3.fc29.x86_64
  Running scriptlet: xorg-x11-server-Xorg-1.20.3-3.fc29.x86_64                                                                                   39/39 
  Verifying        : hwdata-0.320-1.fc29.noarch                                                                                                   1/39 
  Verifying        : libX11-1.6.7-1.fc29.x86_64                                                                                                   2/39 
  Verifying        : libX11-common-1.6.7-1.fc29.noarch                                                                                            3/39 
  Verifying        : libX11-xcb-1.6.7-1.fc29.x86_64                                                                                               4/39 
  Verifying        : libdrm-2.4.97-1.fc29.x86_64                                                                                                  5/39 
  Verifying        : libinput-1.12.6-1.fc29.x86_64                                                                                                6/39 
  Verifying        : libwacom-0.32-2.fc29.x86_64                                                                                                  7/39 
  Verifying        : libwacom-data-0.32-2.fc29.noarch                                                                                             8/39 
  Verifying        : mesa-libEGL-18.2.8-1.fc29.x86_64                                                                                             9/39 
  Verifying        : mesa-libGL-18.2.8-1.fc29.x86_64                                                                                             10/39 
  Verifying        : mesa-libgbm-18.2.8-1.fc29.x86_64                                                                                            11/39 
  Verifying        : mesa-libglapi-18.2.8-1.fc29.x86_64                                                                                          12/39 
  Verifying        : xorg-x11-drv-libinput-0.28.2-1.fc29.x86_64                                                                                  13/39 
  Verifying        : xorg-x11-server-Xorg-1.20.3-3.fc29.x86_64                                                                                   14/39 
  Verifying        : xorg-x11-server-common-1.20.3-3.fc29.x86_64                                                                                 15/39 
  Verifying        : libXau-1.0.8-14.fc29.x86_64                                                                                                 16/39 
  Verifying        : libXdamage-1.1.4-15.fc29.x86_64                                                                                             17/39 
  Verifying        : libXdmcp-1.1.2-12.fc29.x86_64                                                                                               18/39 
  Verifying        : libXext-1.3.3-10.fc29.x86_64                                                                                                19/39 
  Verifying        : libXfixes-5.0.3-8.fc29.x86_64                                                                                               20/39 
  Verifying        : libXfont2-2.0.3-3.fc29.x86_64                                                                                               21/39 
  Verifying        : libXxf86vm-1.1.4-10.fc29.x86_64                                                                                             22/39 
  Verifying        : libepoxy-1.5.3-1.fc29.x86_64                                                                                                23/39 
  Verifying        : libevdev-1.5.9-5.fc29.x86_64                                                                                                24/39 
  Verifying        : libfontenc-1.1.3-9.fc29.x86_64                                                                                              25/39 
  Verifying        : libglvnd-1:1.1.0-2.fc29.x86_64                                                                                              26/39 
  Verifying        : libglvnd-egl-1:1.1.0-2.fc29.x86_64                                                                                          27/39 
  Verifying        : libglvnd-glx-1:1.1.0-2.fc29.x86_64                                                                                          28/39 
  Verifying        : libgudev-232-4.fc29.x86_64                                                                                                  29/39 
  Verifying        : libpciaccess-0.14-2.fc29.x86_64                                                                                             30/39 
  Verifying        : libunwind-1.2.1-6.fc29.x86_64                                                                                               31/39 
  Verifying        : libwayland-client-1.16.0-1.fc29.x86_64                                                                                      32/39 
  Verifying        : libwayland-server-1.16.0-1.fc29.x86_64                                                                                      33/39 
  Verifying        : libxcb-1.13.1-1.fc29.x86_64                                                                                                 34/39 
  Verifying        : libxkbfile-1.0.9-11.fc29.x86_64                                                                                             35/39 
  Verifying        : libxshmfence-1.3-3.fc29.x86_64                                                                                              36/39 
  Verifying        : mtdev-1.1.5-13.fc29.x86_64                                                                                                  37/39 
  Verifying        : pixman-0.34.0-10.fc29.x86_64                                                                                                38/39 
  Verifying        : xorg-x11-xkb-utils-7.7-27.fc29.x86_64                                                                                       39/39 

Installed:
  xorg-x11-server-Xorg-1.20.3-3.fc29.x86_64        hwdata-0.320-1.fc29.noarch                        libX11-1.6.7-1.fc29.x86_64                        
  libX11-common-1.6.7-1.fc29.noarch                libX11-xcb-1.6.7-1.fc29.x86_64                    libdrm-2.4.97-1.fc29.x86_64                       
  libinput-1.12.6-1.fc29.x86_64                    libwacom-0.32-2.fc29.x86_64                       libwacom-data-0.32-2.fc29.noarch                  
  mesa-libEGL-18.2.8-1.fc29.x86_64                 mesa-libGL-18.2.8-1.fc29.x86_64                   mesa-libgbm-18.2.8-1.fc29.x86_64                  
  mesa-libglapi-18.2.8-1.fc29.x86_64               xorg-x11-drv-libinput-0.28.2-1.fc29.x86_64        xorg-x11-server-common-1.20.3-3.fc29.x86_64       
  libXau-1.0.8-14.fc29.x86_64                      libXdamage-1.1.4-15.fc29.x86_64                   libXdmcp-1.1.2-12.fc29.x86_64                     
  libXext-1.3.3-10.fc29.x86_64                     libXfixes-5.0.3-8.fc29.x86_64                     libXfont2-2.0.3-3.fc29.x86_64                     
  libXxf86vm-1.1.4-10.fc29.x86_64                  libepoxy-1.5.3-1.fc29.x86_64                      libevdev-1.5.9-5.fc29.x86_64                      
  libfontenc-1.1.3-9.fc29.x86_64                   libglvnd-1:1.1.0-2.fc29.x86_64                    libglvnd-egl-1:1.1.0-2.fc29.x86_64                
  libglvnd-glx-1:1.1.0-2.fc29.x86_64               libgudev-232-4.fc29.x86_64                        libpciaccess-0.14-2.fc29.x86_64                   
  libunwind-1.2.1-6.fc29.x86_64                    libwayland-client-1.16.0-1.fc29.x86_64            libwayland-server-1.16.0-1.fc29.x86_64            
  libxcb-1.13.1-1.fc29.x86_64                      libxkbfile-1.0.9-11.fc29.x86_64                   libxshmfence-1.3-3.fc29.x86_64                    
  mtdev-1.1.5-13.fc29.x86_64                       pixman-0.34.0-10.fc29.x86_64                      xorg-x11-xkb-utils-7.7-27.fc29.x86_64             

Complete!
```

```
[vagrant@localhost ~]$ uname -r
4.18.16-300.fc29.x86_64
```

```
[vagrant@localhost ~]$ sudo dnf install -y kernel-headers-`uname -r`
Failed to set locale, defaulting to C
Last metadata expiration check: 1:16:01 ago on Thu Feb 14 17:51:03 2019.
Dependencies resolved.
=======================================================================================================================================================
 Package                                Arch                           Version                                    Repository                      Size
=======================================================================================================================================================
Downgrading:
 kernel-headers                         x86_64                         4.18.16-300.fc29                           fedora                         1.2 M

Transaction Summary
=======================================================================================================================================================
Downgrade  1 Package

Total download size: 1.2 M
Downloading Packages:
kernel-headers-4.18.16-300.fc29.x86_64.rpm                                                                              22 kB/s | 1.2 MB     00:54    
-------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                   21 kB/s | 1.2 MB     00:56     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                               1/1 
Downgrade: kernel-headers-4.18.16-300.fc29.x86_64
  Downgrading      : kernel-headers-4.18.16-300.fc29.x86_64                                                                                        1/2 
Downgrade: kernel-headers-4.18.16-300.fc29.x86_64
Downgraded: kernel-headers-4.20.7-200.fc29.x86_64
  Cleanup          : kernel-headers-4.20.7-200.fc29.x86_64                                                                                         2/2 
Downgraded: kernel-headers-4.20.7-200.fc29.x86_64
  Verifying        : kernel-headers-4.18.16-300.fc29.x86_64                                                                                        1/2 
  Verifying        : kernel-headers-4.20.7-200.fc29.x86_64                                                                                         2/2 

Downgraded:
  kernel-headers-4.18.16-300.fc29.x86_64                                                                                                               

Complete!
```

```
[vagrant@localhost ~]$ sudo dnf install -y kernel-devel-`uname -r`
Failed to set locale, defaulting to C
Last metadata expiration check: 1:17:37 ago on Thu Feb 14 17:51:03 2019.
Dependencies resolved.
=======================================================================================================================================================
 Package                               Arch                            Version                                   Repository                       Size
=======================================================================================================================================================
Installing:
 kernel-devel                          x86_64                          4.18.16-300.fc29                          fedora                           13 M

Transaction Summary
=======================================================================================================================================================
Install  1 Package

Total download size: 13 M
Installed size: 50 M
Downloading Packages:
kernel-devel-4.18.16-300.fc29.x86_64.rpm                                                                               1.5 MB/s |  13 MB     00:08    
-------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                  1.3 MB/s |  13 MB     00:09     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                               1/1 
Installed: kernel-devel-4.18.16-300.fc29.x86_64
  Installing       : kernel-devel-4.18.16-300.fc29.x86_64                                                                                          1/1 
  Running scriptlet: kernel-devel-4.18.16-300.fc29.x86_64                                                                                          1/1 
Installed: kernel-devel-4.18.16-300.fc29.x86_64
  Verifying        : kernel-devel-4.18.16-300.fc29.x86_64                                                                                          1/1 

Installed:
  kernel-devel-4.18.16-300.fc29.x86_64                                                                                                                 

Complete!
```

```
[vagrant@localhost ~]$ sudo dnf install -y dkms
Failed to set locale, defaulting to C
Last metadata expiration check: 0:06:48 ago on Thu Feb 14 19:14:45 2019.
Dependencies resolved.
=======================================================================================================================================================
 Package                          Arch                               Version                                  Repository                          Size
=======================================================================================================================================================
Installing:
 dkms                             noarch                             2.6.1-2.fc29                             fedora                              78 k

Transaction Summary
=======================================================================================================================================================
Install  1 Package

Total download size: 78 k
Installed size: 219 k
Downloading Packages:
dkms-2.6.1-2.fc29.noarch.rpm                                                                                            57 kB/s |  78 kB     00:01    
-------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                   27 kB/s |  78 kB     00:02     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                               1/1 
Installed: dkms-2.6.1-2.fc29.noarch
  Installing       : dkms-2.6.1-2.fc29.noarch                                                                                                      1/1 
  Running scriptlet: dkms-2.6.1-2.fc29.noarch                                                                                                      1/1 
Installed: dkms-2.6.1-2.fc29.noarch
  Verifying        : dkms-2.6.1-2.fc29.noarch                                                                                                      1/1 

Installed:
  dkms-2.6.1-2.fc29.noarch                                                                                                                             

Complete!
```

```
[vagrant@localhost ~]$ sudo dvd/VBoxLinuxAdditions.run 
Verifying archive integrity... All good.
Uncompressing VirtualBox 5.1.30 Guest Additions for Linux...........
VirtualBox Guest Additions installer
Removing installed version 5.1.30 of VirtualBox Guest Additions...
Copying additional installer modules ...
Installing additional modules ...
vboxadd.sh: Starting the VirtualBox Guest Additions.

```

```
[vagrant@localhost ~]$ cat /var/log/vboxadd-install.log 
grep: /lib/modules/4.18.16-300.fc29.x86_64/build/include/linux/version.h: No such file or directory
make KBUILD_VERBOSE=1 CONFIG_MODULE_SIG= -C /lib/modules/4.18.16-300.fc29.x86_64/build SUBDIRS=/tmp/vbox.0 SRCROOT=/tmp/vbox.0 -j2 modules
make[1]: warning: -jN forced in submake: disabling jobserver mode.
Makefile:946: *** "Cannot generate ORC metadata for CONFIG_UNWINDER_ORC=y, please install libelf-dev, libelf-devel or elfutils-libelf-devel".  Stop.
make: *** [/tmp/vbox.0/Makefile.include.footer:85: vboxguest] Error 2
Creating user for the Guest Additions.
Creating udev rule for the Guest Additions kernel module.
```

```
[vagrant@localhost ~]$ sudo dnf search libelf
Failed to set locale, defaulting to C
=========================================================== Name & Summary Matched: libelf ============================================================
elfutils-libelf-devel.i686 : Development support for libelf
elfutils-libelf-devel.x86_64 : Development support for libelf
elfutils-libelf-devel-static.i686 : Static archive of libelf
elfutils-libelf-devel-static.x86_64 : Static archive of libelf
================================================================ Name Matched: libelf =================================================================
elfutils-libelf.x86_64 : Library to read and write ELF files
elfutils-libelf.i686 : Library to read and write ELF files
elfutils-libelf.x86_64 : Library to read and write ELF files
```

```
[vagrant@localhost ~]$ sudo dnf install -y elfutils-libelf-devel
Failed to set locale, defaulting to C
Fedora Modular 29 - x86_64                                                                                              12 kB/s |  16 kB     00:01    
Fedora Modular 29 - x86_64 - Updates                                                                                    10 kB/s |  15 kB     00:01    
Fedora 29 - x86_64 - Updates                                                                                            11 kB/s |  15 kB     00:01    
Fedora 29 - x86_64                                                                                                      11 kB/s |  16 kB     00:01    
Dependencies resolved.
=======================================================================================================================================================
 Package                                      Arch                          Version                               Repository                      Size
=======================================================================================================================================================
Installing:
 elfutils-libelf-devel                        x86_64                        0.174-5.fc29                          updates                         23 k
Installing dependencies:
 zlib-devel                                   x86_64                        1.2.11-14.fc29                        fedora                          46 k

Transaction Summary
=======================================================================================================================================================
Install  2 Packages

Total download size: 69 k
Installed size: 170 k
Downloading Packages:
(1/2): elfutils-libelf-devel-0.174-5.fc29.x86_64.rpm                                                                   5.4 kB/s |  23 kB     00:04    
(2/2): zlib-devel-1.2.11-14.fc29.x86_64.rpm                                                                             11 kB/s |  46 kB     00:04    
-------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                  9.4 kB/s |  69 kB     00:07     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                               1/1 
Installed: zlib-devel-1.2.11-14.fc29.x86_64
  Installing       : zlib-devel-1.2.11-14.fc29.x86_64                                                                                              1/2 
Installed: zlib-devel-1.2.11-14.fc29.x86_64
Installed: elfutils-libelf-devel-0.174-5.fc29.x86_64
  Installing       : elfutils-libelf-devel-0.174-5.fc29.x86_64                                                                                     2/2 
Installed: elfutils-libelf-devel-0.174-5.fc29.x86_64
  Running scriptlet: elfutils-libelf-devel-0.174-5.fc29.x86_64                                                                                     2/2 
  Verifying        : elfutils-libelf-devel-0.174-5.fc29.x86_64                                                                                     1/2 
  Verifying        : zlib-devel-1.2.11-14.fc29.x86_64                                                                                              2/2 

Installed:
  elfutils-libelf-devel-0.174-5.fc29.x86_64                                      zlib-devel-1.2.11-14.fc29.x86_64                                     

Complete!
```

```
[vagrant@localhost ~]$ sudo dnf upgrade -y kernel*
Failed to set locale, defaulting to C
Last metadata expiration check: 0:16:34 ago on Thu Feb 14 19:14:45 2019.
Dependencies resolved.
=======================================================================================================================================================
 Package                             Arch                        Version                                            Repository                    Size
=======================================================================================================================================================
Upgrading:
 kernel-headers                      x86_64                      4.20.7-200.fc29                                    updates                      1.2 M
Installing dependencies:
 kernel-core                         x86_64                      4.20.7-200.fc29                                    updates                       25 M
 kernel-devel                        x86_64                      4.20.7-200.fc29                                    updates                       13 M
 linux-firmware                      noarch                      20190118-91.gita8b75cac.fc29                       updates                       77 M

Transaction Summary
=======================================================================================================================================================
Install  3 Packages
Upgrade  1 Package

Total download size: 116 M
Downloading Packages:
(1/4): kernel-core-4.20.7-200.fc29.x86_64.rpm                                                                           65 kB/s |  25 MB     06:34    
(2/4): kernel-headers-4.20.7-200.fc29.x86_64.rpm                                                                       1.7 MB/s | 1.2 MB     00:00    
(3/4): kernel-devel-4.20.7-200.fc29.x86_64.rpm                                                                          22 kB/s |  13 MB     10:09    
(4/4): linux-firmware-20190118-91.gita8b75cac.fc29.noarch.rpm                                                           36 kB/s |  77 MB     36:27    
-------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                   54 kB/s | 116 MB     36:29     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                               1/1 
Installed: linux-firmware-20190118-91.gita8b75cac.fc29.noarch
  Installing       : linux-firmware-20190118-91.gita8b75cac.fc29.noarch                                                                            1/5 
Installed: linux-firmware-20190118-91.gita8b75cac.fc29.noarch
Installed: kernel-core-4.20.7-200.fc29.x86_64
  Installing       : kernel-core-4.20.7-200.fc29.x86_64                                                                                            2/5 
  Running scriptlet: kernel-core-4.20.7-200.fc29.x86_64                                                                                            2/5 
Installed: kernel-core-4.20.7-200.fc29.x86_64
Upgrade: kernel-headers-4.20.7-200.fc29.x86_64
  Upgrading        : kernel-headers-4.20.7-200.fc29.x86_64                                                                                         3/5 
Upgrade: kernel-headers-4.20.7-200.fc29.x86_64
Installed: kernel-devel-4.20.7-200.fc29.x86_64
  Installing       : kernel-devel-4.20.7-200.fc29.x86_64                                                                                           4/5 
  Running scriptlet: kernel-devel-4.20.7-200.fc29.x86_64                                                                                           4/5 
Installed: kernel-devel-4.20.7-200.fc29.x86_64
Upgraded: kernel-headers-4.18.16-300.fc29.x86_64
  Cleanup          : kernel-headers-4.18.16-300.fc29.x86_64                                                                                        5/5 
Upgraded: kernel-headers-4.18.16-300.fc29.x86_64
  Running scriptlet: kernel-core-4.20.7-200.fc29.x86_64                                                                                            5/5 
vboxadd.sh: failed: Look at /var/log/vboxadd-install.log to find out what went wrong.

  Running scriptlet: kernel-headers-4.18.16-300.fc29.x86_64                                                                                        5/5 
  Verifying        : kernel-core-4.20.7-200.fc29.x86_64                                                                                            1/5 
  Verifying        : kernel-devel-4.20.7-200.fc29.x86_64                                                                                           2/5 
  Verifying        : linux-firmware-20190118-91.gita8b75cac.fc29.noarch                                                                            3/5 
  Verifying        : kernel-headers-4.20.7-200.fc29.x86_64                                                                                         4/5 
  Verifying        : kernel-headers-4.18.16-300.fc29.x86_64                                                                                        5/5 

Upgraded:
  kernel-headers-4.20.7-200.fc29.x86_64                                                                                                                

Installed:
  kernel-core-4.20.7-200.fc29.x86_64          kernel-devel-4.20.7-200.fc29.x86_64          linux-firmware-20190118-91.gita8b75cac.fc29.noarch         

Complete!
```


```
[vagrant@localhost ~]$ exit
logout
Connection to 172.28.128.4 closed.
```



```
fanhonglingdeMacBook-Pro:fedora fanhongling$ vagrant reload
==> default: This machine used to live in /Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn but it's now at /Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/fedora.
==> default: Depending on your current provider you may need to change the name of
==> default: the machine to run it as a different machine.
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
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default: 
    default: Guest Additions Version: 5.2.0 r68940
    default: VirtualBox Version: 5.1
==> default: Configuring and enabling network interfaces...
    default: SSH address: 127.0.0.1:2200
    default: SSH username: vagrant
    default: SSH auth method: private key
==> default: Mounting shared folders...
    default: /Users/fanhongling/go => /Users/fanhongling/go
Vagrant was unable to mount VirtualBox shared folders. This is usually
because the filesystem "vboxsf" is not available. This filesystem is
made available via the VirtualBox Guest Additions and kernel module.
Please verify that these guest additions are properly installed in the
guest. This is not a bug in Vagrant and is usually caused by a faulty
Vagrant box. For context, the command attempted was:

mount -t vboxsf -o uid=1000,gid=1000 Users_fanhongling_go /Users/fanhongling/go

The error output from the command was:

/sbin/mount.vboxsf: mounting failed with the error: No such device

fanhonglingdeMacBook-Pro:fedora fanhongling$ ssh -i ~/.ssh/vagrant vagrant@172.28.128.4
Last login: Thu Feb 14 19:03:11 2019 from 172.28.128.1
[vagrant@localhost ~]$ uname -r
4.20.7-200.fc29.x86_64
```

```
[vagrant@localhost ~]$ export KERN_DIR=/lib/modules/4.20.7-200.fc29.x86_64/build/
[vagrant@localhost ~]$ echo $KERN_DIR
/lib/modules/4.20.7-200.fc29.x86_64/build/
```
