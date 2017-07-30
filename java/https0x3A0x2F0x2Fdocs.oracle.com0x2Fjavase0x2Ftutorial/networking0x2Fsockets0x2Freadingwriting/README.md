# Instruction

## Command line

After `mvn clean package` to make jar:

For EchoServer
```
[vagrant@localhost networking0x2Fsockets0x2Freadingwriting]$ java -jar ./target/https0x3A0x2F0x2Fdocs0x2Eoracle0x2Ecom0x2Fjavase0x2Fnetworking0x2Fsockets0x2Freadingwriting-0.0.1-SNAPSHOT.jar
```

For EchoClient
```
[vagrant@localhost networking0x2Fsockets0x2Freadingwriting]$ java -classpath ./target/https0x3A0x2F0x2Fdocs0x2Eoracle0x2Ecom0x2Fjavase0x2Fnetworking0x2Fsockets0x2Freadingwriting-0.0.1-SNAPSHOT.jar examples.EchoClient 127.0.0.1 12345
```

## Maven

Run by `exec-maven-plugin`

### exec:java

For EchoServer
```
[vagrant@localhost networking0x2Fsockets0x2Freadingwriting]$ mvn clean package exec:java@runclass
```

### exec:exec

For EchoServer
```
[vagrant@localhost networking0x2Fsockets0x2Freadingwriting]$ mvn clean install exec:exec@runjar --port=12346
```

For EchoClient
```
[vagrant@localhost networking0x2Fsockets0x2Freadingwriting]$ mvn clean install exec:exec@runjar -Dexec.mainClass="examples.EchoClient" -Dexec.args="127.0.0.1 12346"
```

