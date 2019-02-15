package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

var (
	serverMode bool = true
	serverPort int  = 12345
	other      string
)

func init() {
	flag.BoolVar(&serverMode, "server", true, "run as server")
	flag.IntVar(&serverPort, "port", 12345, "port to listen")
	flag.StringVar(&other, "other", "", "a string flag")

	log.SetFlags(log.LstdFlags | log.Lshortfile)
	log.SetPrefix(fmt.Sprintf("[%s]", filepath.Base(os.Args[0])))
}

func main() {
	flag.Parse()

	if other != "" {
		fmt.Println("The other flag is ", other)
	}

	if serverMode {
		log.Printf("Will run as server to listen at port %d", serverPort)
	} else {
		log.Printf("Will run as client to connect with port %d", serverPort)
	}
}
