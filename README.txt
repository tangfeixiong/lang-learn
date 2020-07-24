

## Golang

以下示例环境为Ubuntu 18.04虚拟机，参见Vagrantfile里的 _Share an additional disk folder to the guest VM_
```
  config.vm.synced_folder "/Users/fanhongling/Downloads", "/Users/fanhongling/Downloads"
```
要求被创建的虚拟机挂载主机（mac）的Downloads目录（第一个路径名）， 因为：
* 可以节省该虚拟机的虚拟磁盘
* 当需要用多个虚拟机时，主机往往没有足够的硬盘空间用作虚拟硬盘
* 有时课避免一些开发工具的重复安装，而是把工具放在该目录下
* 在虚拟机里采用同名的目录（第2个路径）是为了方便记忆



fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 443 (guest) => 5443 (host) (adapter 1)
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
==> default: Machine booted and ready!
Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.8
VBoxService inside the vm claims: 5.2.18
Going on, assuming VBoxService is correct...
[default] GuestAdditions versions on your host (5.1.30) and guest (5.2.18) do not match.
Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.8
VBoxService inside the vm claims: 5.2.18
Going on, assuming VBoxService is correct...
Reading package lists...
Building dependency tree...
Reading state information...
Package 'virtualbox-guest-dkms' is not installed, so not removed
Package 'virtualbox-guest-x11' is not installed, so not removed
The following packages will be REMOVED:
  virtualbox-guest-utils*
0 upgraded, 0 newly installed, 1 to remove and 36 not upgraded.
After this operation, 2796 kB disk space will be freed.
(Reading database ... 95922 files and directories currently installed.)
Removing virtualbox-guest-utils (5.2.18-dfsg-2~ubuntu18.04.3) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
(Reading database ... 95909 files and directories currently installed.)
Purging configuration files for virtualbox-guest-utils (5.2.18-dfsg-2~ubuntu18.04.3) ...
Processing triggers for ureadahead (0.100.0-20) ...
Processing triggers for systemd (237-3ubuntu10.13) ...
Reading package lists...
Building dependency tree...
Reading state information...
linux-headers-4.15.0-46-generic is already the newest version (4.15.0-46.49).
linux-headers-4.15.0-46-generic set to manually installed.
Suggested packages:
  menu
The following NEW packages will be installed:
  dkms
0 upgraded, 1 newly installed, 0 to remove and 36 not upgraded.
Need to get 68.0 kB of archives.
After this operation, 290 kB of additional disk space will be used.
Err:1 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 dkms all 2.3-3ubuntu9.2
  404  Not Found [IP: 91.189.88.149 80]
E: Failed to fetch http://archive.ubuntu.com/ubuntu/pool/main/d/dkms/dkms_2.3-3ubuntu9.2_all.deb  404  Not Found [IP: 91.189.88.149 80]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
Reading package lists...
W: --force-yes is deprecated, use one of the options starting with --allow instead.
E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)
E: Unable to lock directory /var/lib/apt/lists/
Reading package lists...
Building dependency tree...
Reading state information...
linux-headers-4.15.0-46-generic is already the newest version (4.15.0-46.49).
linux-headers-4.15.0-46-generic set to manually installed.
Suggested packages:
  menu
The following NEW packages will be installed:
  dkms
0 upgraded, 1 newly installed, 0 to remove and 36 not upgraded.
Need to get 68.0 kB of archives.
After this operation, 290 kB of additional disk space will be used.
Err:1 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 dkms all 2.3-3ubuntu9.2
  404  Not Found [IP: 91.189.88.162 80]
E: Failed to fetch http://archive.ubuntu.com/ubuntu/pool/main/d/dkms/dkms_2.3-3ubuntu9.2_all.deb  404  Not Found [IP: 91.189.88.162 80]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
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
The following SSH command responded with a non-zero exit status.
Vagrant assumes that this means the command failed!

apt-get install -y linux-headers-`uname -r` dkms

Stdout from the command:

Reading package lists...
Building dependency tree...
Reading state information...
linux-headers-4.15.0-46-generic is already the newest version (4.15.0-46.49).
linux-headers-4.15.0-46-generic set to manually installed.
Suggested packages:
  menu
The following NEW packages will be installed:
  dkms
0 upgraded, 1 newly installed, 0 to remove and 36 not upgraded.
Need to get 68.0 kB of archives.
After this operation, 290 kB of additional disk space will be used.
Err:1 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 dkms all 2.3-3ubuntu9.2
  404  Not Found [IP: 91.189.88.162 80]


Stderr from the command:

E: Failed to fetch http://archive.ubuntu.com/ubuntu/pool/main/d/dkms/dkms_2.3-3ubuntu9.2_all.deb  404  Not Found [IP: 91.189.88.162 80]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?






fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant ssh
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Nov  5 17:33:23 UTC 2019

  System load:  0.04              Processes:             108
  Usage of /:   24.2% of 9.63GB   Users logged in:       0
  Memory usage: 4%                IP address for enp0s3: 10.0.2.15
  Swap usage:   0%                IP address for enp0s8: 172.28.128.5

 * Ubuntu's Kubernetes 1.14 distributions can bypass Docker and use containerd
   directly, see https://bit.ly/ubuntu-containerd or try it now with

     snap install microk8s --channel=1.14/beta --classic

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

36 packages can be updated.
0 updates are security updates.


Last login: Tue Mar 26 05:41:10 2019 from 172.28.128.1




vagrant@ubuntu-bionic:~$ sudo apt-get update --fix-missing
Hit:1 http://security.ubuntu.com/ubuntu bionic-security InRelease                                        
Hit:2 http://archive.ubuntu.com/ubuntu bionic InRelease                                                  
Hit:3 http://archive.ubuntu.com/ubuntu bionic-updates InRelease                 
Hit:4 http://archive.ubuntu.com/ubuntu bionic-backports InRelease               
Reading package lists... Done                        
vagrant@ubuntu-bionic:~$ sudo apt-get install -y linux-headers-`uname -r` dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
linux-headers-4.15.0-46-generic is already the newest version (4.15.0-46.49).
linux-headers-4.15.0-46-generic set to manually installed.
The following packages were automatically installed and are no longer required:
  linux-headers-4.15.0-45 linux-headers-4.15.0-45-generic linux-image-4.15.0-45-generic linux-modules-4.15.0-45-generic
Use 'sudo apt autoremove' to remove them.
Suggested packages:
  menu
The following NEW packages will be installed:
  dkms
0 upgraded, 1 newly installed, 0 to remove and 117 not upgraded.
Need to get 68.1 kB of archives.
After this operation, 291 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 dkms all 2.3-3ubuntu9.7 [68.1 kB]
Fetched 68.1 kB in 1s (48.9 kB/s)
Selecting previously unselected package dkms.
(Reading database ... 126505 files and directories currently installed.)
Preparing to unpack .../dkms_2.3-3ubuntu9.7_all.deb ...
Unpacking dkms (2.3-3ubuntu9.7) ...
Setting up dkms (2.3-3ubuntu9.7) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
vagrant@ubuntu-bionic:~$ exit
logout
Connection to 127.0.0.1 closed.




fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant reload
==> default: Attempting graceful shutdown of VM...
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 443 (guest) => 5443 (host) (adapter 1)
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
==> default: Machine booted and ready!
[default] GuestAdditions versions on your host (5.1.30) and guest (5.2.8) do not match.
Reading package lists...
Building dependency tree...
Reading state information...
dkms is already the newest version (2.3-3ubuntu9.7).
linux-headers-4.15.0-66-generic is already the newest version (4.15.0-66.75).
linux-headers-4.15.0-66-generic set to manually installed.
The following packages were automatically installed and are no longer required:
  linux-headers-4.15.0-45 linux-headers-4.15.0-45-generic
  linux-image-4.15.0-45-generic linux-modules-4.15.0-45-generic
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 117 not upgraded.
Copy iso file /Applications/VirtualBox.app/Contents/MacOS/VBoxGuestAdditions.iso into the box /tmp/VBoxGuestAdditions.iso
Mounting Virtualbox Guest Additions ISO to: /mnt
mount: /mnt: WARNING: device write-protected, mounted read-only.
Installing Virtualbox Guest Additions 5.1.30 - guest version is 5.2.8
Verifying archive integrity... All good.
Uncompressing VirtualBox 5.1.30 Guest Additions for Linux...........
VirtualBox Guest Additions installer
Copying additional installer modules ...
Installing additional modules ...
vboxadd.sh: Starting the VirtualBox Guest Additions.

Could not find the X.Org or XFree86 Window System, skipping.
An error occurred during installation of VirtualBox Guest Additions 5.1.30. Some functionality may not work as intended.
In most cases it is OK that the "Window System drivers" installation failed.
Job for vboxadd-service.service failed because the control process exited with error code.
See "systemctl status vboxadd-service.service" and "journalctl -xe" for details.
Unmounting Virtualbox Guest Additions ISO from: /mnt
Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.8
VBoxService inside the vm claims: 5.1.30
Going on, assuming VBoxService is correct...
Got different reports about installed GuestAdditions version:
Virtualbox on your host claims:   5.2.8
VBoxService inside the vm claims: 5.1.30
Going on, assuming VBoxService is correct...
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default: 
    default: Guest Additions Version: 5.2.8_KernelUbuntu r120774
    default: VirtualBox Version: 5.1
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /Users/fanhongling/go => /Users/fanhongling/go
    default: /Users/fanhongling/Downloads => /Users/fanhongling/Downloads
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: flag to force provisioning. Provisioners marked to run always will still run.

fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant ssh
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-66-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Nov  5 17:53:06 UTC 2019

  System load:  0.09              Processes:             109
  Usage of /:   26.1% of 9.63GB   Users logged in:       0
  Memory usage: 3%                IP address for enp0s3: 10.0.2.15
  Swap usage:   0%                IP address for enp0s8: 172.28.128.5

 * Ubuntu's Kubernetes 1.14 distributions can bypass Docker and use containerd
   directly, see https://bit.ly/ubuntu-containerd or try it now with

     snap install microk8s --channel=1.14/beta --classic

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

117 packages can be updated.
0 updates are security updates.


Last login: Tue Nov  5 17:33:23 2019 from 10.0.2.2

vagrant@ubuntu-bionic:~$ ls /Users/fanhongling/Downloads/99-mirror/linux-bin/
apache-cassandra-3.0.8  etcd            go                     govendor      jre1.8.0_91       protoc-gen-gofast      protoc-gen-gostring
apache-maven-3.5.2      etcd-v2_3_0     go-bindata             hadoop-3.0.0  k8s-v1.7.4        protoc-gen-gogo        protoc-gen-grpc-gateway
apache-tomcat-7.0.73    etcdctl         godep                  helm          packer            protoc-gen-gogofast    protoc-gen-swagger
dep                     flanneld-amd64  gofabric8-linux-amd64  jdk1.7.0_80   protoc-gen-combo  protoc-gen-gogofaster  protoc-min-version
docker-compose          glide           gofileserver           jdk1.8.0_112  protoc-gen-go     protoc-gen-gogoslick   sdk


### 安装go

用Ubuntu系统的默认安装工具，如下为运行go来查看提示

vagrant@ubuntu-bionic:~$ go version

Command 'go' not found, but can be installed with:

snap install go         # version 1.13.4, or
apt  install golang-go
apt  install gccgo-go 

See 'snap info go' for additional versions.


安装到共享目录，使用go文档的推荐方法

For installing golang tools binaries, refer to _./golang/installing-golang.md_

vagrant@ubuntu-bionic:~$ ls
go1.13.4.linux-amd64.tar.gz
