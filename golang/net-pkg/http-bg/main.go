package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"log"
	"net"
	"regexp"
	"strings"
)

func init() {
	log.SetFlags(log.Lshortfile | log.LstdFlags)
}

func main() {
	listener, e := net.Listen("tcp", "0.0.0.0:8080") // any available address
	if e != nil {
		log.Fatalf("net.Listen tcp :0: %v", e)
	}
	defer listener.Close()

	log.Println("TCP server is created at", listener.Addr().String())

LOOP_ACCEPTION:
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Println("Networking has trouble")
			continue
		}
		log.Printf("Guest %s is calling\n", conn.RemoteAddr().String())

		var b []byte = make([]byte, 1024)
		var n int
		for {
			n, err = conn.Read(b)
			if err != nil {
				log.Println("Get connection error:", err.Error())
				if err == io.EOF {
					conn.Close()
					break
				}
				break LOOP_ACCEPTION
			}
			if n > 0 {
				log.Println("Let's see what is HTTP spec")
				req := b[:n]
				fmt.Println(string(req))
				resp := processRequest(b)
				conn.Write([]byte(resp))
			}
		}
	}
}

func processRequest(rb []byte) string {
	var protocolRequestLine string
	var contentLengthLine string
	var contentTypeLine string

	var match bool
	var err error

	scanner := bufio.NewScanner(bytes.NewBuffer(rb))
	var line string
	for scanner.Scan() {
		line = scanner.Text()

		match, err = regexp.MatchString(`(GET|POST) \S+ HTTP/\S+`, line)
		if err != nil {
			log.Printf("regexp error: %s. line: %s\n", err.Error(), line)
			continue
		}
		if match {
			protocolRequestLine = line
			continue
		}

		match, err = regexp.MatchString(`User-Agent:.*`, line)
		if err != nil {
			log.Printf("regexp error: %s. line: %s\n", err.Error(), line)
			continue
		}
		if match {
			continue
		}

		match, err = regexp.MatchString(`Accept:.*`, line)
		if err != nil {
			log.Printf("regexp error: %s. line: %s\n", err.Error(), line)
			continue
		}
		if match {
			continue
		}

		match, err = regexp.MatchString(`Content-Length:.*`, line)
		if err != nil {
			log.Printf("regexp error: %s. line: %s\n", err.Error(), line)
			continue
		}
		if match {
			contentLengthLine = line
			continue
		}

		match, err = regexp.MatchString(`Content-Type:.*`, line)
		if err != nil {
			log.Printf("regexp error: %s. line: %s\n", err.Error(), line)
			continue
		}
		if match {
			contentTypeLine = line
			continue
		}

		match, err = regexp.MatchString(`\s*`, line)
		if err != nil {
			log.Printf("regexp error: %s. line: %s\n", err.Error(), line)
			continue
		}
		if match {
			break
		}
		log.Println("This code can no process this line")
		fmt.Println(line)
	}

	log.Println("The followings ware user data")
	for scanner.Scan() {
		fmt.Println(line)
	}

	protocols := strings.Split(protocolRequestLine, " ")
	log.Printf("method: %s\npath: %s\nhttp version: %s\n", protocols[0], protocols[1], protocols[2])

	path := protocols[1]
	var protocolResponseLine string
	switch path {
	case "/", "/index.html":
		protocolResponseLine = "HTTP/1.1 200 OK"
		contentTypeLine = "Content-Type: text/html"
		msg := strings.Replace(index_html, "\n", "", -1)
		contentLengthLine = fmt.Sprintf("Content-Length: %d", len(msg))
		return fmt.Sprintf("%s\r\n%s\r\n%s\r\n\r\n%s\r\n", protocolResponseLine, contentTypeLine, contentLengthLine, msg)
	default:
		protocolResponseLine = "HTTP/1.1 404 Not Found"
		return fmt.Sprintf("%s\r\n\r\n", protocolResponseLine)
	}
}

var index_html string = `<html>
  <body>
    <h1>welcome</h1>
  </body>
</html>
`
