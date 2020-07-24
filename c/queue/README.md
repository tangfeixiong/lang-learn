Development

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/queue$ make
gcc -c -o main.o main.c -I. -Wall -std=c99
gcc -o main queue.o main.o -I. -Wall -std=c99
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/queue$ ./main 
Enter operation: 1
Enter item to enter: 4
Enter operation: 1
Enter item to enter: 10
Enter operation: 5
queue is:
	4
	10
Enter operation: 1
Enter item to enter: 20
Enter operation: 2
Enter operation: 5
queue is:
	10
	20
Enter operation: 3
The head value of queue is: 10
Enter operation: 4
The tail value of queue is: 20
Enter operation: 5
queue is:
	10
	20
Enter operation: 6
Queue is not empty
Enter operation: 7
Enter operation: 0
Bye!
```