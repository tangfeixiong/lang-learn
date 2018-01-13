package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	basename := filepath.Base(os.Args[0])
	fmt.Println("this bin name is", basename)

	wd, err := os.Getwd()
	if err != nil {
		fmt.Printf("get working directory failed: %v\n", err)
	}
	fmt.Println("golang-versionized PWD, result:", wd)

	hostname, _ := os.Hostname()
	if hostname != "" {
		fmt.Printf("golang-versionized command %s\n %s", "hostname", hostname)
	}

}
