# Quicksort

__reference__

https://en.wikipedia.org/wiki/Quicksort

__Development__

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/qsort$ make
gcc -c -o qsort.o qsort.c -I. -Wall -std=c99
gcc -c -o quicksort.o quicksort.c -I. -Wall -std=c99
gcc -o quicksort qsort.o quicksort.o -I. -Wall -std=c99
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/qsort$ ./quicksort 
Enter 9 numbers to be sorted: 3 7 8 5 9 1 2 5 4
0x7ffed57085d0 0x7ffed57085d4 0x7ffed57085d8 0x7ffed57085dc 0x7ffed57085e0 0x7ffed57085e4 0x7ffed57085e8 0x7ffed57085ec 0x7ffed57085f0 ---- lo: 0x7ffed57085d0 hi: 0x7ffed57085f0 pivot: 4
--> lo: 0x7ffed57085d4 (7) hi: 0x7ffed57085f0 (4)
<-- lo: 0x7ffed57085d4 (7) hi: 0x7ffed57085e8 (2)
--> lo: 0x7ffed57085d8 (8) hi: 0x7ffed57085e8 (2)
<-- lo: 0x7ffed57085d8 (8) hi: 0x7ffed57085e4 (1)
--> lo: 0x7ffed57085dc (5) hi: 0x7ffed57085e4 (1)
<-- lo: 0x7ffed57085dc (5) hi: 0x7ffed57085dc (5)
3 2 1 4 9 5 8 5 7  lo=hi= 0x7ffed57085dc (4)

0x7ffed57085d0 0x7ffed57085d4 0x7ffed57085d8 0x7ffed57085dc 0x7ffed57085e0 0x7ffed57085e4 0x7ffed57085e8 0x7ffed57085ec 0x7ffed57085f0 ---- lo: 0x7ffed57085d0 hi: 0x7ffed57085d8 pivot: 1
--> lo: 0x7ffed57085d0 (3) hi: 0x7ffed57085d8 (1)
<-- lo: 0x7ffed57085d0 (3) hi: 0x7ffed57085d0 (3)
1 2 3 4 9 5 8 5 7  lo=hi= 0x7ffed57085d0 (1)

0x7ffed57085d0 0x7ffed57085d4 0x7ffed57085d8 0x7ffed57085dc 0x7ffed57085e0 0x7ffed57085e4 0x7ffed57085e8 0x7ffed57085ec 0x7ffed57085f0 ---- lo: 0x7ffed57085d4 hi: 0x7ffed57085d8 pivot: 3
--> lo: 0x7ffed57085d8 (3) hi: 0x7ffed57085d8 (3)
1 2 3 4 9 5 8 5 7  lo=hi= 0x7ffed57085d8 (3)

0x7ffed57085d0 0x7ffed57085d4 0x7ffed57085d8 0x7ffed57085dc 0x7ffed57085e0 0x7ffed57085e4 0x7ffed57085e8 0x7ffed57085ec 0x7ffed57085f0 ---- lo: 0x7ffed57085e0 hi: 0x7ffed57085f0 pivot: 7
--> lo: 0x7ffed57085e0 (9) hi: 0x7ffed57085f0 (7)
<-- lo: 0x7ffed57085e0 (9) hi: 0x7ffed57085ec (5)
--> lo: 0x7ffed57085e8 (8) hi: 0x7ffed57085ec (5)
<-- lo: 0x7ffed57085e8 (8) hi: 0x7ffed57085e8 (8)
1 2 3 4 5 5 7 8 9  lo=hi= 0x7ffed57085e8 (7)

0x7ffed57085d0 0x7ffed57085d4 0x7ffed57085d8 0x7ffed57085dc 0x7ffed57085e0 0x7ffed57085e4 0x7ffed57085e8 0x7ffed57085ec 0x7ffed57085f0 ---- lo: 0x7ffed57085e0 hi: 0x7ffed57085e4 pivot: 5
--> lo: 0x7ffed57085e4 (5) hi: 0x7ffed57085e4 (5)
1 2 3 4 5 5 7 8 9  lo=hi= 0x7ffed57085e4 (5)

0x7ffed57085d0 0x7ffed57085d4 0x7ffed57085d8 0x7ffed57085dc 0x7ffed57085e0 0x7ffed57085e4 0x7ffed57085e8 0x7ffed57085ec 0x7ffed57085f0 ---- lo: 0x7ffed57085ec hi: 0x7ffed57085f0 pivot: 9
--> lo: 0x7ffed57085f0 (9) hi: 0x7ffed57085f0 (9)
1 2 3 4 5 5 7 8 9  lo=hi= 0x7ffed57085f0 (9)

In sorted order: 1 2 3 4 5 5 7 8 9 
```