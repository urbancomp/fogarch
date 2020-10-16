#include <stdlib.h>
#include "MyApplicaton.h"

using Veins::TraCIMobilityAccess;
using Veins::AnnotationManagerAccess;
using Veins::TraCIConnection;


using namespace veins_myproject;

Define_Module(MyApplicaton);
int w = 0;
std::string idCar;

void MyApplicaton::initialize(int stage) {

    BaseWaveApplLayer::initialize(stage);
        if (stage == 0) {

            //setup veins pointers
            mobility = TraCIMobilityAccess().get(getParentModule());
            traci = mobility->getCommandInterface();
            traciVehicle = mobility->getVehicleCommandInterface();
            lastDroveAt = simTime();
            //traciVehicle->setLaneChangeMode(0);

            sentMessage = false;
            lastDroveAt = simTime();
            currentSubscribedServiceId = -1;



        }
}

void MyApplicaton::receiveSignal(cComponent* source, simsignal_t signalID, cObject* obj, cObject* details) {

    Enter_Method_Silent();
    if (signalID == mobilityStateChangedSignal) {
        handlePositionUpdate(obj);
    }
}

void MyApplicaton::handlePositionUpdate(cObject* obj) {

    BaseWaveApplLayer::handlePositionUpdate(obj);

        // stopped for for at least 10s?
        if (mobility->getSpeed() < 1) {
            if (simTime() - lastDroveAt >= 10 && sentMessage == false) {
                findHost()->getDisplayString().updateWith("r=16,red");
                sentMessage = true;

                WaveShortMessage* wsm = new WaveShortMessage();
                populateWSM(wsm);
                wsm->setWsmData(mobility->getRoadId().c_str());

                //host is standing still due to crash
                if (dataOnSch) {
                    startService(Channels::SCH2, 42, "Traffic Information Service");
                    //started service and server advertising, schedule message to self to send later
                    scheduleAt(computeAsynchronousSendingTime(1,type_SCH),wsm);
                }
                else {
                    //send right away on CCH, because channel switching is disabled
                    sendDown(wsm);
                }
            }
        }
}

void MyApplicaton::handleSelfMsg(cMessage* msg) {
    switch (msg->getKind()) {
        case SEND_BEACON_EVT: {

            // Método criado na classe TraCICommandInterface "getTraCIXY"
            Coord coordOmnet = mobility->getCurrentPosition();
            std::pair<double,double> coordTraCI = traci->getTraCIXY(mobility->getCurrentPosition());

            //Cria um objeto  BasicSafetyMessage
            BasicSafetyMessage* bsm = new BasicSafetyMessage();

            BeaconMessage* beaconMessage = new BeaconMessage("beacon");

            // Ontem o ID do veículo. Mesmo ID utilizado no SUMO
            std::string carroid = std::to_string(getParentModule()->getIndex()+1);

            //Encapsula oObjetos em uma mensagem
            //beaconMessage->setRoadSender(mobility->getRoadId().c_str());
            beaconMessage->setRoadSender(traciVehicle->getLaneId().c_str());
            beaconMessage->setIdSender(carroid.c_str());
            beaconMessage->setTypeDevice("CAR");
            beaconMessage->setPosicaoX(coordTraCI.first);
            beaconMessage->setPosicaoY(coordTraCI.second);
            beaconMessage->setPosRoad(traciVehicle->getLanePosition()); // posição do veículo ao longo da via
            beaconMessage->setLenRoad(traci->lane(traciVehicle->getLaneId()).getLength()); // Tamanho da via completa
            beaconMessage->setSpeed(mobility->getSpeed());

            bsm->encapsulate(beaconMessage);

            //popula a memsagem com os dados encapsulados
            populateWSM(bsm);

            //Envia para a infraestrutura
            sendDown(bsm);


            /*
            //IDENTIFICANDO A PSOIÇÃO PARA A UMA RSU (TESTANDO VALORES )
            Coord cteste;
            cteste.x=884.239;
            cteste.y=991.592;
            std::pair<double,double> cconvert = traci->getTraCIXY(mobility->getCurrentPosition()); // Método criado na classe TraCICommandInterface "getTraCIXY"
            std::cout     << "\n\n   Posição X RSU: " << cconvert.first
                          << "\n\n   Posição Y RSU: " << cconvert.second;
            */

            // TESTANDO ID DO CARRO
            //std::to_string(myId);
            // getParentModule()->getIndex()+1

            std::cout     << "\n ---------------------------------------------------- "
                          << "\n [CAR] :: ENVIANDO MENSAGEM --------------------------"
                          << "\n -- ID DO VEÍCULO : "<< getParentModule()->getIndex()
                          << "\n -----------------------------------------------------"
                          << "\n ****************CONTEÚDO DA MENSAGEM*****************"
                          << "\n Velocidade Atual : " << mobility->getSpeed()
                          << "\n POSIÇÃO X: " << coordTraCI.first
                          << "\n POSIÇÃO Y: " << coordTraCI.second
                          << "\n ESTRADA: " << traciVehicle->getLaneId()
                          << "\n POSIÇÃO NA FAIXA: " << traciVehicle->getLanePosition()
                          << "\n TAMANHO TOTAL DA FAIXA: " << traci->lane(traciVehicle->getLaneId()).getLength()
                          << "\n ---------------------------------------------------- " << "\n";

                scheduleAt(simTime() + beaconInterval, sendBeaconEvt);

                break;
        }
        case SEND_WSA_EVT:   {
            //WaveServiceAdvertisment* wsa = new WaveServiceAdvertisment();
            //populateWSM(wsa);
            //sendDown(wsa);
            //scheduleAt(simTime() + wsaInterval, sendWSAEvt);
            break;
        }
        default: {
            if (msg)
                DBG_APP << "APP: Error: Got Self Message of unknown kind! Name: " << msg->getName() << endl;
            break;
        }
    }
}

void MyApplicaton::onWSM(WaveShortMessage* wsm) {
    std::cerr << "\n Chegou uma Wave Short Message em: onWSM";
   // BasicSafetyMessage* WC = dynamic_cast<BasicSafetyMessage*>(bsm->decapsulate());
}

void MyApplicaton::onBSM(BasicSafetyMessage* bsm) {

    //BeaconMessage* BC = dynamic_cast<BeaconMessage*>(bsm->decapsulate());

    //int velo_antiga = bsm->getSenderSpeed().x;

    /*
    if (BC != NULL) {
        // MENSAGEM ENCAPSULADA
      std::cout       << "\n ------------------------------------- "
                      << "\n [" <<  BC->getTypeDevice() << "] X [CAR] :: MENSAGEM RECEBIDA -------"
                      << "\n -- Veículo          : "<< myId
                      << "\n -- Velocidade atual : "<< velo_antiga
                      << "\n -- Desencapsulando a Mensagem ----------- "
                      << "\n    -- Dispositivo Emissor   : " << BC->getTypeDevice()
                      << "\n    -- Còdigo do Dispositivo : " << BC->getIdSender()
                      << "\n    -- Estrada : " << BC->getRoadSender()
                      << "\n    -- Velocidade : " << bsm->getSenderSpeed().x
                      << "\n    -- Posição X: " << bsm->getSenderPos().x << "Posição Y: " << bsm->getSenderPos().y
                      << "\n ------------------------------------- ";
    } else {

        std::cout     << " \n ------------------------------------- "
                        << "\n [My CAR] :: RECEBIDA :: MENSAGEM NORMAL ----"
                        << "\n -- Mensagem recebida pelo veículo: "<<myId
                        << "\n -- Velocidade atual : "<< velo_antiga
                        << "\n ------------------------------------- ";
    }
    */
}
