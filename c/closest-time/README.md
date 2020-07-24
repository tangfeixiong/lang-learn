# Development

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/closest-time$ make
gcc -I. -Wall -std=c99   -c -o closest.o closest.c
gcc -o main closest.o main.o -I. -Wall -std=c99
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/closest-time$ ./main 
Enter a 24-hour (hh:mm, where hh between 0 and 23) time: 9:00
8	00	am
9	43	am
11	19	am
12	47	pm
---
9	00
---
-60	43	139	227	
43 d->9:43am a<-11:52am
d->9:43am a<-11:52am
Closest departure time is 9:43am, arriving at 11:52am.
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/closest-time$ ./main 
Enter a 24-hour (hh:mm, where hh between 0 and 23) time: 13:15
8	00	am
9	43	am
11	19	am
12	47	pm
---
13	15
---
-315	-212	-116	-28	
No appropriate flight
```