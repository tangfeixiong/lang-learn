
**VirtualBox**

> fanhonglingdeMacBook-Pro:lang-learn fanhongling$ VBoxManage --version
> 6.0.24r139119


24/1/24
> fanhonglingdeMacBook-Pro:lang-learn fanhongling$ VBoxManage --version
> 6.1.50r161033

+ issue - https://www.virtualbox.org/manual/ch06.html#network_hostonly>
> On Linux, macOS and Solaris Oracle VM VirtualBox will only allow IP addresses in 192.168.56.0/21 range to be assigned to host-only adapters 

+ issue - <https://stackoverflow.com/questions/70704093/the-ip-address-configured-for-the-host-only-network-is-not-within-the-allowed-ra>

**Vagrant**

> fanhonglingdeMacBook-Pro:~ fanhongling$ vagrant --version | awk -F' ' '{print $2}'
> 2.2.6

24/1/24
> fanhonglingdeMacBook-Pro:lang-learn fanhongling$ vagrant --version
> Vagrant 2.2.19

plugins:
- <https://github.com/sprotheroe/vagrant-disksize>
- <https://github.com/dotless-de/vagrant-vbguest>

Upgrade >= 3.0.0: <https://stackoverflow.com/questions/39544703/getting-error-dyld-symbol-not-found-clock-gettime>
> dyld: Symbol not found: _clock_gettime

**others**

Package manager for macOS and Darwin - <https://www.macports.org/install.php#installing>

Safe read/write NTFS driver for FUSE - <https://ports.macports.org/port/ntfs-3g/>

macFUSE allows you to extend macOS's native file handling capabilities via third-party file systems - <https://osxfuse.github.io>

macFUSE for version > Mac Sierra (10.12) - <https://ports.macports.org/port/macfuse/details/>

Bypass VPN
- <https://superuser.com/questions/4904/how-to-selectively-route-network-traffic-through-vpn-on-mac-os-x-leopard>
- <https://www.cactusvpn.com/tutorials/how-to-bypass-vpn-for-specific-websites-and-ips-on-mac-os/>

Bash upgrade - <https://apple.stackexchange.com/questions/193411/update-bash-to-version-4-0-on-osx>
