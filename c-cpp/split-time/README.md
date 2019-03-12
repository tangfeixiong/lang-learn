# Development

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/split-time$ make
gcc -c -o seconds.o seconds.c -I. -Wall
gcc -c -o splitseconds.o splitseconds.c -I. -Wall
gcc -o splitseconds seconds.o splitseconds.o -I. -Wall
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/split-time$ ./splitseconds 12345
aflag = 0, bflag = 0, cvalue = (null)
Non-option argument 12345
times=3:25:45
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/split-time$ ./splitseconds -a 123456
aflag = 1, bflag = 0, cvalue = (null)
Non-option argument 123456
days = 1
times=10:17:36
times=34:17:36
```