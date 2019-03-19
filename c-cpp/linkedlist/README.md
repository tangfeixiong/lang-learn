# About

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/linkedlist$ make
gcc -Wall -std=c99 -c -o linked_list.o linked_list.c
gcc -Wall -std=c99 -c -o find_last_node.o find_last_node.c
gcc -Wall -std=c99 -o find_last_node find_last_node.o linked_list.o
```

```
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/c-cpp/linkedlist$ ./find_last_node 
Enter number you want to search for:5
Node found: value = 5 and marker = a
```