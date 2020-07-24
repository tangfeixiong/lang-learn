
### Test

Interfaces
```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/google/gopacket/examples$ go test -v -run NetIface /Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/golang/net-pkg/iface_test.go 
=== RUN   TestNetIface
	name: lo
	name: enp0s3
	name: enp0s8
	name: docker0
	name: vethefc9000
	name: veth027e7f9
--- PASS: TestNetIface (0.00s)
    iface_test.go:15: Reading network interfaces...
        
    iface_test.go:19: Done!
PASS
ok  	command-line-arguments	0.004s
```

### knowledge

https://github.com/firstrow/tcp_server