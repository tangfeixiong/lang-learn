# Development

build
```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/encryption$ make
gcc -c -o crypt.o crypt.c -I. -Wall -std=c99
gcc -c -o demo.o demo.c -I. -Wall -std=c99
gcc -o demo crypt.o demo.o -I. -Wall -std=c99
```

encrypt
```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/encryption$ ./demo -i encrypt.txt -m 1 -t mapping.csv 
hpyhpofi
sf
opy
```

decrypt
```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/encryption$ ./demo -i decrypt.txt -m 2 -t mapping.csv 
edmonton
```