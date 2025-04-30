package main

import (
	"bytes"
	"flag"
	"fmt"
	"golang.org/x/crypto/ssh"
	"log"
	"os"
	"strings"
)

func main() {
	var (
		username = flag.String("u", "root", "SSH USER")
		password = flag.String("p", "root", "SSH PASS")
		addr     = flag.String("i", "192.168.1.1:22", "SSH ADDR")
		command  = flag.String("c", "whoami", "SSH COMMAND")
		filename string
	)
	flag.Parse()
	config := &ssh.ClientConfig{
		User: *username,
		Auth: []ssh.AuthMethod{
			ssh.Password(*password),
		},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
	}

	client, err := ssh.Dial("tcp", *addr, config)
	if err != nil {
		log.Fatal("Failed to dial: ", err)
	}
	defer client.Close()

	// 开启一个session，用于执行一个命令
	session, err := client.NewSession()
	if err != nil {
		log.Fatal("Failed to create session: ", err)
	}
	defer session.Close()

	// 执行命令，并将执行的结果写到 b 中
	var b bytes.Buffer
	session.Stdout = &b

	// 也可以使用 session.CombinedOutput() 整合输出
	if err := session.Run(*command); err != nil {
		log.Fatal("Failed to run: " + err.Error())
	}
	fmt.Println("[ " + *command + " ]")
	fmt.Println(b.String())

	replacements := map[string]string{
		".": "_",
		":": "_",
	}

	// 遍历替换所有的字符串
	for old, new := range replacements {
		filename = "command-" + strings.Replace(*addr, old, new, -1)
	}
	filename = filename + ".txt"
	f, err := os.OpenFile(filename, os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		fmt.Println("无法打开文件:", err)
	} else {
		defer f.Close()
		_, err := f.WriteString("[ " + *command + " ]\n" + b.String() + "\n")
		if err != nil {
			fmt.Println("无法追加文件内容:", err)
		} else {
			fmt.Println("============结果保存 【" + filename + "】 =============")
		}
	}

}