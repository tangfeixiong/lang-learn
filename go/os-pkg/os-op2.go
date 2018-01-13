package main

import (
	"fmt"
	"log"
	"os/exec"
)

func main() {
	out, err := exec.Command("date").Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("The date is %s\n", out)

	cmd := exec.Command("ls")
	cmd.Args = []string{"-l", "/"}
	out, err = cmd.Output()
	if err != nil {
		fmt.Println("Error:", err.Error())
	} else {
		fmt.Println(string(out))
	}

	cmd = exec.Command("python", "--version")
	out, _ = cmd.CombinedOutput()
	fmt.Println(string(out))

	cmd = exec.Command("java", "-version")
	out, err = cmd.CombinedOutput()
	if err != nil {
		fmt.Println(err.Error())
	}
	fmt.Println(string(out))
}
