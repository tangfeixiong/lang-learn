# About

## Project

### Compile

Using [maven_wrapper](https://github.com/takari/maven-wrapper)

    fanhonglingdeMacBook-Pro:learnjavafx1 fanhongling$ ./mvnw clean compile exec:java@runclass -Dexec.args="--abc=123"

### Execute 

Package and exec

    fanhonglingdeMacBook-Pro:learnjavafx1 fanhongling$ ./mvnw package exec:exec@runjar

Or 
    
    fanhonglingdeMacBook-Pro:learnjavafx1 fanhongling$ ./mvnw clean package exec:exec@runjar -Dmain.class=apple.Main

Execute _jar_

    fanhonglingdeMacBook-Pro:learnjavafx1 fanhongling$ java -jar target/learnjavafx1-0.0.1-SNAPSHOT.jar 

Or 

    fanhonglingdeMacBook-Pro:learnjavafx1 fanhongling$ java -cp target/learnjavafx1-0.0.1-SNAPSHOT.jar apple.Main

### Builder wrapper

For example

    fanhonglingdeMacBook-Pro:learnjavafx1 fanhongling$ mvn -N io.takari:maven:wrapper
    [INFO] Scanning for projects...

...

    [INFO] 
    [INFO] The Maven Wrapper version 0.2.1 has been successfully setup for your project.
    [INFO] Using Apache Maven 3.5.0
    [INFO] 
    [INFO] ------------------------------------------------------------------------
    [INFO] BUILD SUCCESS
    [INFO] ------------------------------------------------------------------------
    [INFO] Total time: 49.402 s
    [INFO] Finished at: 2017-05-29T08:38:00-07:00
    [INFO] Final Memory: 10M/245M
    [INFO] ------------------------------------------------------------------------
