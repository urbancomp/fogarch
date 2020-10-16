#include "MyRSUApp.h"
#include <string>
#include <iomanip>
#include <iostream>
#include <fstream>

using Veins::TraCIMobilityAccess;
using Veins::AnnotationManagerAccess;

using namespace veins_myproject;

Define_Module(MyRSUApp);

double somaVelocidades = 0;
double mediaVelocidades = 0;


#define NLIN 20
//#define NCOL 10
//double controlePista[NLIN][2];
int temID = 0;
int contaCarros = 0;
std::string situacao;
int cabecalhovetor = 0;

std::ofstream myfile;
int cabecalho = 0;
int contaBeacons = 0;

//estrutura do veículo para manipulação no vetor
struct veiculo
  {
    std::string pista;
    double id;
    double velocidade;
    double posicaox;
    double posicaoy;
    double posroad;
  };

//vetor do tipo veículo estruturado
struct veiculo veiculosMapa[NLIN];

void MyRSUApp::initialize(int stage) {

    BaseWaveApplLayer::initialize(stage);
    if (stage == 0) {
        //in.SendMessage("testando");
        in2.Connect();
    }

    std::cout << "\n\n\n\n *********** PASSOU NA INICIALIZAÇÃO ******** \n\n\n\n";

}

//void MyRSUApp::receiveSignal(cComponent* source, simsignal_t signalID, cObject* obj, cObject* details) {
//}

void MyRSUApp::onWSA(WaveServiceAdvertisment* wsa) {
    std::cout << "\n PASSOU AQUI: onWSA "<<myId;
}

void MyRSUApp::onWSM(WaveShortMessage* wsm) {
    std::cout << "\n PASSOU AQUI: onWSM "<<myId;
}

void MyRSUApp::handleLowerMsg(cMessage* msg) {

      std::string c = msg->getClassName();
    //std::cerr << "\n\n\n TIPO: " << msg->getClassName() << "\n\n\n";

    if (c == "BasicSafetyMessage"){

        BasicSafetyMessage* bsm = check_and_cast<BasicSafetyMessage*>(msg);

        BeaconMessage* BC = dynamic_cast<BeaconMessage*>(bsm->decapsulate());
        contaBeacons++;

        std::ostringstream px;
        px << BC->getPosicaoX();

        std::ostringstream py;
        py << BC->getPosicaoY();

        std::ostringstream pp;
        pp << BC->getPosRoad();

        std::ostringstream lr;
        lr << BC->getLenRoad();

        std::ostringstream speed;
        speed << BC->getSpeed();

       //Passando querystring para o socket
       string    QS  =       "data-car;";
                 QS  = QS  + "id:"        +  BC->getIdSender()             + ";";
                 QS  = QS  + "veloact:"   +  speed.str()                   + ";";
                 QS  = QS  + "pista:"     +  BC->getRoadSender()           + ";";
                 QS  = QS  + "posx:"      +  px.str()                      + ";";
                 QS  = QS  + "posy:"      +  py.str()                      + ";";
                 QS  = QS  + "posroad:"   +  pp.str()                      + ";";
                 QS  = QS  + "lenroad:"   +  lr.str()                      + ";";
                 QS  = QS  + "simtime:"   +  simTime().str()               + ";\n";

       in2.SendMessage(QS);


        //Mensagem de dados recebida - apresenta na console
        //Escrevi apenas para validação do esquema

        std::cerr        << "\n -------------------------------------------------- "
                         << "\n [" <<  BC->getTypeDevice() << "] X [RSU] : MENSAGEM RECEBIDA -------"
                         << "\n -- Recebida na RSU : "<< myId
                         << "\n -- Desencapsulando a Mensagem ----------- "
                         << "\n    -- Envida pelo veiculo: " << BC->getIdSender()
                         << "\n    -- Estrada : " << BC->getRoadSender()
                         << "\n    -- Velocidade : " << BC->getSpeed()
                         << "\n    -- POS X: " << BC->getPosicaoX()
                         << "\n    -- POS Y: " << BC->getPosicaoY()
                         << "\n    -- POS LR: " << BC->getLenRoad()
                         << "\n    -- POS PP: " << BC->getPosRoad()
                         << "\n -------------------------------------------------- ";

    }


}

void MyRSUApp::handleSelfMsg(cMessage* msg) {
  /*
    switch (msg->getKind()) {
        case SEND_BEACON_EVT: {

            //Cria um objeto  BasicSafetyMessage
            BasicSafetyMessage* bsm = new BasicSafetyMessage();
            BeaconMessage* beaconMessage = new BeaconMessage("beacon");

            //Encapsula oObjetos em uma mensagem
            //beaconMessage->setRoadSender(mobility->getRoadId().c_str());
            beaconMessage->setIdSender(myId);
            beaconMessage->setTypeDevice("RSU");

            bsm->encapsulate(beaconMessage);

            populateWSM(bsm);
            sendDown(bsm);

            std::cerr       << "\n ------------------------------------- "
                            << "\n [My RSU] :: ENVIANDO MENSAGEM -------"
                            << "\n -- Mensagem enviada pela RSU: "<<myId
                            << "\n ------------------------------------- ";

            scheduleAt(simTime() + beaconInterval, sendBeaconEvt);
            break;
        }
        case SEND_WSA_EVT:   {
            WaveServiceAdvertisment* wsa = new WaveServiceAdvertisment();
            populateWSM(wsa);
            sendDown(wsa);
            scheduleAt(simTime() + wsaInterval, sendWSAEvt);
            break;
        }
        default: {
            if (msg)
                DBG_APP << "APP: Error: Got Self Message of unknown kind! Name: " << msg->getName() << endl;
            break;
        }
    }
    */
}

