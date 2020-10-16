/*
 * SocketConnection.cpp
 *
 *  Created on: 24 de fev de 2020
 *      Author: edsonmottac
 */

#include "SocketConnection.h"

    int port = 4447;
    //create a message buffer
    char msg[256];
    int bytesRead, bytesWritten = 0;
    int clientSd;

    void SocketConnection::Connect() {

            //setup a socket and connection tools
            struct hostent* host = gethostbyname("127.0.0.1");
            sockaddr_in sendSockAddr;
            bzero((char*)&sendSockAddr, sizeof(sendSockAddr));
            sendSockAddr.sin_family = AF_INET;
            sendSockAddr.sin_addr.s_addr =
                inet_addr(inet_ntoa(*(struct in_addr*)*host->h_addr_list));
            sendSockAddr.sin_port = htons(port);
            clientSd = socket(AF_INET, SOCK_STREAM, 0);
            //try to connect...
            int status = connect(clientSd,
                                 (sockaddr*) &sendSockAddr, sizeof(sendSockAddr));
            if(status < 0)
            {
                cout<<"Error connecting to socket!"; //break;
            } else {
                cout << "Connected to the server!";
            }
    }


    void SocketConnection::SendMessage(string c) {

       //Connect();

       struct timeval start1, end1;
       gettimeofday(&start1, NULL);
       string data;
       data=c;
       memset(&msg, 0, sizeof(msg));//clear the buffer
       strcpy(msg, data.c_str());
       bytesWritten += send(clientSd, (char*)&msg, strlen(msg), 0);
       std::cerr << "mensagem: " << msg;

       //close(clientSd);


       /*
       int wbytes,wbytes2,wbytes3;
       string str = c ; // PASSANDO
       const char *p = "\n";
       string s = c + p;
       const char *wbuff = s.c_str(); // convert from string to c string, has to have \0 terminal
       wbytes = write(clientSd, wbuff, strlen(wbuff));
       */

    }
