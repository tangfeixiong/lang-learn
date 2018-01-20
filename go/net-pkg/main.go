package main

import (
	"log"
	"net"
	"time"
)

func main() {
	log.SetFlags(log.Lshortfile)

	listener, e := net.Listen("tcp", "0.0.0.0:12345") // any available address
	if e != nil {
		log.Fatalf("net.Listen tcp :0: %v", e)
	}

	log.Println("TCP server is created at", listener.Addr().String())

	defer listener.Close()

	conn, err := listener.Accept()
	if err != nil {
		log.Println("Networking has trouble")
		return
	}
	log.Printf("Guest %s is calling\n", conn.RemoteAddr().String())
	conn.Write([]byte("hi"))
	for {
		b := make([]byte, 1024)
		n, err := conn.Read(b)
		if err != nil {
			log.Println("Get connection error:", err.Error())
			conn.Close()
			break
		}
		if n > 0 {
			log.Println("Listened:", string(b))
			log.Println("keep connection")
		}
		time.Sleep(time.Second)
	}

}
