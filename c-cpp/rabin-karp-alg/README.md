
# About Lab

## Test

__example 1__

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/rabin-karp-alg$ gcc -o topleft topleft.c
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/rabin-karp-alg$ ./topleft
(0, 0); (1, 1); (2, 2); 
(0, 1); (1, 2); 
(0, 2); 
(1, 0); (2, 1); 
(2, 0); 
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/rabin-karp-alg$ ./topleft 5
(0, 0); (1, 1); (2, 2); (3, 3); (4, 4); 
(0, 1); (1, 2); (2, 3); (3, 4); 
(0, 2); (1, 3); (2, 4); 
(0, 3); (1, 4); 
(0, 4); 
(1, 0); (2, 1); (3, 2); (4, 3); 
(2, 0); (3, 1); (4, 2); 
(3, 0); (4, 1); 
(4, 0); 
```

__example 2__

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/rabin-karp-alg$ gcc calculategrid.c -lm -o calculategrid
```

otherwise
```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/rabin-karp-alg$ gcc calculategrid.c -o calculategrid
/tmp/ccWhG0at.o: In function `main':
calculategrid.c:(.text+0x262): undefined reference to `pow'
calculategrid.c:(.text+0x2e4): undefined reference to `pow'
collect2: error: ld returned 1 exit status
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/rabin-karp-alg$ ./calculategrid 1
calculate from left to right:
(0, 0, 1000102); (0, 1, 1071213); (0, 2, 1041328); (0, 3, 0); (0, 4, 0); 
(1, 0, 1071213); (1, 1, 1041317); (1, 2, 1112727); (1, 3, 0); (1, 4, 0); 
(2, 0, 1060709); (2, 1, 1010708); (2, 2, 1112117); (2, 3, 0); (2, 4, 0); 
(3, 0, 1020611); (3, 1, 1082021); (3, 2, 1102624); (3, 3, 0); (3, 4, 0); 
(4, 0, 1091509); (4, 1, 1030614); (4, 2, 1062014); (4, 3, 0); (4, 4, 0); 
--- x variable
(0, 0, 1000102); (0, 1, 1071213); (0, 2, 1041328); (0, 3, 0); (0, 4, 0); 
(1, 0, 1071213); (1, 1, 1041317); (1, 2, 1112727); (1, 3, 0); (1, 4, 0); 
(2, 0, 1060709); (2, 1, 1010708); (2, 2, 1112117); (2, 3, 0); (2, 4, 0); 
(3, 0, 1020611); (3, 1, 1082021); (3, 2, 1102624); (3, 3, 0); (3, 4, 0); 
(4, 0, 1091509); (4, 1, 1030614); (4, 2, 1062014); (4, 3, 0); (4, 4, 0); 
```