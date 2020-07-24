# Development

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/realloc$ make
gcc -c -o student.o student.c -I. -Wall -std=c99
gcc -o main student.o -I. -Wall -std=c99
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/realloc$ ./main 
Enter operation: 1
Enter ID to add (5 spots available): 1234
Enter student name: Alice
Enter operation: 
1
Enter ID to add (4 spots available): 345
Enter student name: Bob
Enter operation: 0
You have 2 students in the class:
1234, Alice
345, Bob
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/realloc$ ./main 
Enter operation: 1
Enter ID to add (5 spots available): 1234
Enter student name: Alice
Enter operation: 1
Enter ID to add (4 spots available): 345
Enter student name: Bob
Enter operation: 1
Enter ID to add (3 spots available): 98
Enter student name: John
Enter operation: 2
Enter ID to drop: 345
Enter operation: 1
Enter ID to add (3 spots available): 100
Enter student name: Mary
Enter operation: 0
You have 2 students in the class:
1234, Alice
100, Mary
98, John
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/realloc$ ./main 
Enter operation: 1
Enter ID to add (5 spots available): 1234
Enter student name: Alice
Enter operation: 1
Enter ID to add (4 spots available): 345
Enter student name: Bob
Enter operation: 1
Enter ID to add (3 spots available): 98
Enter student name: John
Enter operation: 1
Enter ID to add (2 spots available): 100
Enter student name: Mary
Enter operation: 1
Enter ID to add (1 spots available): 200
Enter student name: Rob
You have reached the maximum capacity of the class. You have 5 students in the class:
1234, Alice
345, Bob
98, John
100, Mary
200, Rob
Enter operation: 0
You have 5 students in the class:
1234, Alice
345, Bob
98, John
100, Mary
200, Rob
```