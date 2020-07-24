# Development

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/squeue$ make
gcc -c -o queue.o queue.c -I. -Wall -std=c99
gcc -c -o example.o example.c -I. -Wall -std=c99
gcc -o example queue.o example.o -I. -Wall -std=c99
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/squeue$ ./example 
This prints "gamma beta alpha delta" across four lines with a tab before each element, and preceded by "stack is:" on its own line:
queue is:
gamma	beta	alpha	delta
This prints "delta alpha beta gamma" across four lines with a tab before each element, and preceded by "stack is:" on its own line:
reversed queue is:
delta	alpha	beta	gamma
This prints "gammabeta alpha delta" across three lines with a tab before each element, and preceded by "stack is:" on its own line:
queue is:
gammabeta	alpha	delta
This prints "gammabeta deltaalpha" across two lines with a tab before each element, and preceded by "stack is:" on its own line:
queue is:
gammabeta	deltaalpha
This prints "alphadelta" in one line with a tab before each element, and preceded by "stack is:" on its own line:e
queue is:
deltaalpha
This prints "eta zeta" across two lines with a tab before each element, and preceded by "stack is:" on its own line:
queue is:
eta	zeta
This prints "eta zeta" in one line 
eta zeta
This nuke has no output, but is good form to call when done
This assertion should succeed
Illegal direction should cause error message
Error, illegal direction k
This prints "gamma beta alpha" across two lines with a tab before each element, and preceded by "stack is:" on its own line:
queue is:
gamma	beta	alpha
```