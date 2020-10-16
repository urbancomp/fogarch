

#ifndef SRC_MYRSUAPP_H_
#define SRC_MYRSUAPP_H_

#include <omnetpp.h>
#include "veins/modules/application/ieee80211p/BaseWaveApplLayer.h"
#include "message/BeaconMessage_m.h"
#include "net/NetworkIntegrate.h"
#include "net/SocketConnection.h"

#include "veins/modules/mobility/traci/TraCIMobility.h"
#include "veins/modules/mobility/traci/TraCICommandInterface.h"


namespace veins_myproject {

    class MyRSUApp : public BaseWaveApplLayer {

        public:
            virtual void initialize(int stage);
            //virtual void receiveSignal(cComponent* source, simsignal_t signalID, cObject* obj, cObject* details);


        protected:

            NetworkIntegrate in;
            SocketConnection in2;

            virtual void onWSA(WaveServiceAdvertisment* wsa);
            virtual void onWSM(WaveShortMessage* wsm);

            /*Envio e recebimento de Mensagens*/
            virtual void handleLowerMsg(cMessage* msg);
            virtual void handleSelfMsg(cMessage* msg);

        };

};
#endif
