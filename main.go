package main

import (
	"log"
	"net"
)

func main() {
	s := newServer()
	go s.run()

	listener, err := net.Listen("tcp", ":8888")
	if err != nil {
		log.Fatalf("Не получается запустить сервер: \n%s", err.Error())
	}

	defer listener.Close()
	log.Printf("Сервер запущен \nПорт :8888")

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Printf("Не получается установить соединение с сервером: \n%s", err.Error())
			continue
		}

		c := s.newClient(conn)
		go c.readInput()
	}
}