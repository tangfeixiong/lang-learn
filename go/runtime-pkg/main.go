package main

import (
	"log"
	"os"
	"runtime"
)

func main() {
	log.SetFlags(log.LstdFlags | log.Lshortfile)
	log.SetPrefix("[my log]")

	cores := runtime.NumCPU()
	log.Printf("CPU numbers %d", cores)

	log.Println("Enable process to use all CPU cores")
	if len(os.Getenv("GOMAXPROCS")) == 0 {
		runtime.GOMAXPROCS(runtime.NumCPU())
	}

	log.Println("Sum sequence from 1 to 100, and statistic memory usage")
	s := 0
	for i := 1; i <= 100; i++ {
		s += i
	}
	var mem runtime.MemStats
	runtime.ReadMemStats(&mem)

	log.Printf("memory currently used: %d", mem.Alloc)
}
