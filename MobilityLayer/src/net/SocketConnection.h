/*
 * SocketConnection.h
 *
 *  Created on: 24 de fev de 2020
 *      Author: edsonmottac
 */


#include <iostream>
#include <string>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <netdb.h>
#include <sys/uio.h>
#include <sys/time.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

#ifndef SRC_NET_SOCKETCONNECTION_H_
#define SRC_NET_SOCKETCONNECTION_H_

class SocketConnection {

    public:

              void Connect();
              void SendMessage(string c);


};

#endif /* SRC_NET_SOCKETCONNECTION_H_ */
