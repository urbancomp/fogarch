/*
 * NetworkIntegrate.h
 *
 *  Created on: Jul 23, 2019
 *      Author: Edson Mota
 */


#include "../net/NetworkIntegrate.h"

//namespace net {


    void NetworkIntegrate::Connect() {


        sockfd = socket(AF_INET, SOCK_STREAM, 0); // Gera file descriptor

        int enable = 1;
        if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &enable, sizeof(int)) < 0)
            std::cout  << "ERROR, setsockopt\n";


        if (sockfd < 0)
            std::cout << "ERROR opening socket";

        //server = gethostbyname("10.129.145.50"); //  Ip do Servidor (ou nome) do servidor que esta escutando.
        server = gethostbyname("127.0.0.1");

        if (server == NULL) {
            std::cout  << "ERROR, no such host\n";
            exit(0);
        }

        bzero((char *) &serv_addr, sizeof(serv_addr));
        serv_addr.sin_family = AF_INET;

        bcopy((char *)server->h_addr,
                 (char *)&serv_addr.sin_addr.s_addr,
                 server->h_length);

        serv_addr.sin_port = htons(portno); // Porta

        // Conectando o Socket
        if (connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr)) < 0)
            std::cout  << "ERROR connecting";


    }

    void NetworkIntegrate::Start(string c){

        //int sockfd; // socket file descriptor
        //int portno = 4447; // port number
        //struct sockaddr_in serv_addr;
        //struct hostent *server;


        Connect();


       char rbuff[256];
       int rbytes;

       //rbytes = read(sockfd, rbuff, sizeof(rbuff)); // read from socket and store the msg into buffer
       rbytes = recv(sockfd, rbuff, sizeof(rbuff), 0); // similar to read(), but return -1 if socket closed
       rbuff[rbytes] = '\0'; // set null terminal
       std::cout      << " \n MENSAGEM:  " << rbuff;


       int wbytes;
        //char wbuff[256]; // passando dados do prompt
        //char * retorno;

        //printf("Entre com uma mensagem para o servidor: ");
        //bzero(wbuff,256); // pega dados digitados no prompt
        //fgets(wbuff,255,stdin);

       string str = c ; // PASSANDO
       const char *p = "\n";
       string s = c + p;
       const char *wbuff = s.c_str(); // convert from string to c string, has to have \0 terminal
       wbytes = write(sockfd, wbuff, strlen(wbuff));
       //if(wbytes < 0) perror("Cannot write to socket");

       //return 0;


    }

    void NetworkIntegrate::SendMessage(string c) {

        Connect();

        /* recebe retorno do socket */
        //char rbuff[256];
        //int rbytes;
        //rbytes = recv(sockfd, rbuff, sizeof(rbuff), 0); // similar to read(), but return -1 if socket closed
        //rbuff[rbytes] = '\0'; // set null terminal
        //std::cout      << " \n MENSAGEM:  " << rbuff;

        try {

            //ESCREVE
            int wbytes,wbytes2,wbytes3;
            string str = c ; // PASSANDO
            const char *p = "\n";
            string s = c + p;
            const char *wbuff = s.c_str(); // convert from string to c string, has to have \0 terminal

            wbytes = write(sockfd, wbuff, strlen(wbuff));
            //wbytes2 = write(sockfd, wbuff, strlen(wbuff));
            //wbytes3 = write(sockfd, wbuff, strlen(wbuff));

            std::cerr << "\n\n\n CONEXAO: "<< sockfd << "\n\n\n";


        } catch (int e) {
            cout << "An exception occurred. Exception Nr. " << e << '\n';
        }


        close(sockfd);
        //if(wbytes < 0) perror("Cannot write to socket");



    }


    //}
