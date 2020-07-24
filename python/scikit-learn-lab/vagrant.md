__Provide VM__

Ubuntu 18.04 Vagrant image failed to configure private network interface
```
fanhonglingdeMacBook-Pro:scikit-learn-lab fanhongling$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'u1804_at_cloud-images_dot_ubuntu_dot_com' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: >= 0
==> default: Box file was not detected as metadata. Adding it directly...
==> default: Adding box 'u1804_at_cloud-images_dot_ubuntu_dot_com' (v0) for provider: virtualbox
    default: Downloading: https://cloud-images.ubuntu.com/releases/18.04/release-20181101/ubuntu-18.04-server-cloudimg-amd64-vagrant.box
==> default: Successfully added box 'u1804_at_cloud-images_dot_ubuntu_dot_com' (v0) for 'virtualbox'!
==> default: Importing base box 'u1804_at_cloud-images_dot_ubuntu_dot_com'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: scikit-learn-lab_default_1542195237244_50777
==> default: Fixed port collision for 22 => 2222. Now on port 2200.
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 2375 (guest) => 2375 (host) (adapter 1)
    default: 22 (guest) => 2200 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2200
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
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
    default: Guest Additions Version: 5.2.10
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


VirtualBox command
```
fanhonglingdeMacBook-Pro:scikit-learn-lab fanhongling$ VBoxManage list runningvms
"scikit-learn-lab_default_1542195237244_50777" {cdb2fbc6-b584-4381-8dd4-ae996b928283}
```

Vagrant command _ssh_
```
fanhonglingdeMacBook-Pro:scikit-learn-lab fanhongling$ vagrant ssh
Welcome to Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-38-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Nov 14 11:37:00 UTC 2018

  System load:  0.16             Processes:             87
  Usage of /:   9.8% of 9.63GB   Users logged in:       0
  Memory usage: 6%               IP address for enp0s3: 10.0.2.15
  Swap usage:   0%


  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.
```

Private network interface
```
vagrant@ubuntu-bionic:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 02:84:d8:33:f5:88 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic enp0s3
       valid_lft 86193sec preferred_lft 86193sec
    inet6 fe80::84:d8ff:fe33:f588/64 scope link 
       valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 08:00:27:e5:e2:33 brd ff:ff:ff:ff:ff:ff
```

Private network configuration
```
vagrant@ubuntu-bionic:~$ cat /etc/network/interfaces
# ifupdown has been replaced by netplan(5) on this system.  See
# /etc/netplan for current configuration.
# To re-enable ifupdown on this system, you can run:
#    sudo apt install ifupdown
#VAGRANT-BEGIN
# The contents below are automatically generated by Vagrant. Do not modify.
auto enp0s8
iface enp0s8 inet dhcp
    post-up route del default dev $IFACE || true
#VAGRANT-END
```

APT install network tool
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
Fetched 55.9 kB in 6s (9075 B/s)                                                                                                                       
Selecting previously unselected package ifupdown.
(Reading database ... 59663 files and directories currently installed.)
Preparing to unpack .../ifupdown_0.8.17ubuntu1.1_amd64.deb ...
Unpacking ifupdown (0.8.17ubuntu1.1) ...
Setting up ifupdown (0.8.17ubuntu1.1) ...
Created symlink /etc/systemd/system/multi-user.target.wants/networking.service → /lib/systemd/system/networking.service.
Created symlink /etc/systemd/system/network-online.target.wants/networking.service → /lib/systemd/system/networking.service.
Processing triggers for ureadahead (0.100.0-20) ...
Processing triggers for systemd (237-3ubuntu10.3) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
```

Quit guest machine
```
vagrant@ubuntu-bionic:~$ exit
logout
Connection to 127.0.0.1 closed.
```

Vagrant command _reload_
```
fanhonglingdeMacBook-Pro:scikit-learn-lab fanhongling$ vagrant reload
==> default: Attempting graceful shutdown of VM...
==> default: Clearing any previously set forwarded ports...
==> default: Fixed port collision for 22 => 2222. Now on port 2200.
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 2375 (guest) => 2375 (host) (adapter 1)
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
    default: Guest Additions Version: 5.2.10
    default: VirtualBox Version: 5.1
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /Users/fanhongling/go => /Users/fanhongling/go
    default: /Users/fanhongling/Downloads => /Users/fanhongling/Downloads
```

The guest is OK
```
fanhonglingdeMacBook-Pro:scikit-learn-lab fanhongling$ vagrant ssh
Welcome to Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-38-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Nov 14 12:11:22 UTC 2018

  System load:  0.0              Processes:             84
  Usage of /:   9.8% of 9.63GB   Users logged in:       0
  Memory usage: 6%               IP address for enp0s3: 10.0.2.15
  Swap usage:   0%               IP address for enp0s8: 172.28.128.4


  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.
```

The private network is OK
```
vagrant@ubuntu-bionic:~$ ip a show enp0s8
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:e5:e2:33 brd ff:ff:ff:ff:ff:ff
    inet 172.28.128.4/24 brd 172.28.128.255 scope global enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fee5:e233/64 scope link 
       valid_lft forever preferred_lft forever
```

__Default ssh key pair__

Already has vagrant default public key
```
vagrant@ubuntu-bionic:~$ cat .ssh/authorized_keys 
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key
```

Quit
```
vagrant@ubuntu-bionic:~$ exit
logout
Connection to 127.0.0.1 closed.
```

Require vagrant default private key
```
fanhonglingdeMacBook-Pro:scikit-learn-lab fanhongling$ ssh vagrant@172.28.128.4
The authenticity of host '172.28.128.4 (172.28.128.4)' can't be established.
RSA key fingerprint is 45:d9:36:e5:7e:1c:a8:9e:66:2d:98:7c:81:9c:87:3f.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '172.28.128.4' (RSA) to the list of known hosts.
Permission denied (publickey).

```

Directory of vagrant default private key
```
fanhonglingdeMacBook-Pro:scikit-learn-lab fanhongling$ ls ~/.vagrant.d/insecure_private_key 
/Users/fanhongling/.vagrant.d/insecure_private_key
```

So ssh with private network addr
```
fanhonglingdeMacBook-Pro:scikit-learn-lab fanhongling$ ssh -i ~/.vagrant.d/insecure_private_key vagrant@172.28.128.4
Welcome to Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-38-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Nov 14 12:29:09 UTC 2018

  System load:  0.0              Processes:             85
  Usage of /:   9.8% of 9.63GB   Users logged in:       0
  Memory usage: 5%               IP address for enp0s3: 10.0.2.15
  Swap usage:   0%               IP address for enp0s8: 172.28.128.4


  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.


Last login: Wed Nov 14 12:27:54 2018 from 172.28.128.1
vagrant@ubuntu-bionic:~$ 
```

__Others__

Vagrant footprint of guest machine
```
fanhonglingdeMacBook-Pro:scikit-learn-lab fanhongling$ ls .vagrant/machines/default/virtualbox/
action_set_name	creator_uid	id		index_uuid	vagrant_cwd
```

Vagrant plugins
```
fanhonglingdeMacBook-Pro:scikit-learn-lab fanhongling$ vagrant plugin list
vagrant-share (1.1.9, system)
vagrant-vbguest (0.17.2)
```