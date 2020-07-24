# Development

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/bstack$ make
gcc -c -o stack.o stack.c -I. -Wall -std=c99
gcc -c -o example.o example.c -I. -Wall -std=c99
gcc -o example stack.o example.o -I. -Wall -std=c99
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/bstack$ ./example 
This prints "alpha":
alpha
This prints "beta":
beta
This prints "gamma":
gamma
This prints "delta":
delta
This will print the whole stack with a tab before each element:"delta gamma beta alpha" across 4 lines, preceded by "stack is:" on a line on its own
stack is:
	delta
	gamma
	beta
	alpha
This will print an empty stack so just "stack is:"
stack is:
This will print a stack that only contains "alice"
stack is:
	alice
This will print an empty stack so just "stack is:"
stack is:
This will print the whole stack with a tab before each element:"bob bob" across 2 lines, preceded by "stack is:" on a line on its own
stack is:
	bob
	bob
This will print the whole stack with a tab before each element:"mike bob bob" across 3 lines, preceded by "stack is:" on a line on its own
stack is:
	mike
	bob
	bob
This will print the whole stack after swapping first two with a tab before each element:"bob mike bob" across 3 lines, preceded by "stack is:" on a line on its own
stack is:
	bob
	mike
	bob
This will print an empty stack so just "stack is:"
stack is:
```