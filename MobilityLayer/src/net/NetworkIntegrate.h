/*
 * NetworkIntegrate.h
 *
 *  Created on: Jul 23, 2019
 *      Author: Edson Mota
 */

#ifndef SRC_NET_NETWORKINTEGRATE_H_
#define SRC_NET_NETWORKINTEGRATE_H_

#include <string.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <cstdlib>
#include <unistd.h>
#include <iostream>

using namespace std;
using std::string;

//namespace net {

    class NetworkIntegrate {

        public:


           int sockfd; // socket file descriptor
           int portno = 4447; // port number
           struct sockaddr_in serv_addr;
           struct hostent *server;

               void Connect();
               void Start(string c);
               void SendMessage(string c);

    };

//} /* namespace net */

#endif /* SRC_NET_NETWORKINTEGRATE_H_ */
