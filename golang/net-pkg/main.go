package main

import (
	"io"
	"log"
	"net"
	"strconv"
	"strings"
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

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Println("Networking has trouble")
			return
		}
		go func(conn net.Conn) {
			log.Printf("Guest %s is calling\n", conn.RemoteAddr().String())
			conn.Write([]byte("hi\n"))
			for {
				b := make([]byte, 1024)
				n, err := conn.Read(b)
				if err != nil {
					log.Println("Get connection error:", err.Error())
					if err == io.EOF {
						conn.Close()
						break
					}
				}
				if n > 0 {
					log.Println("Listened:", string(b))

					msg := string(b)
					switch {
					case strings.HasPrefix(msg, "add"):
						params := strings.Split(msg[4:n-2], ",")
						args := make([]int, 0)
						for _, v := range params {
							i, err := strconv.Atoi(strings.Trim(v, " "))
							if err != nil {
								log.Println(err)
								conn.Write([]byte("invalide args for procedure call\n"))
								break
							}
							args = append(args, i)
						}
						result := add(args...)
						conn.Write([]byte(strconv.Itoa(result)))
						conn.Write([]byte{'\n'})
					default:
						conn.Write([]byte("invalid procedure call\n"))
					}
				}
				log.Println("keep connection")
			}
		}(conn)

		time.Sleep(time.Second)
		log.Println("enable more acception")
	}
}

func add(args ...int) int {
	s := 0
	for _, v := range args {
		s += v
	}
	return s
}
