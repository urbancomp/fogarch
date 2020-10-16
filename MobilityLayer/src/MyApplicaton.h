

#ifndef SRC_MYAPPLICATON_H_
#define SRC_MYAPPLICATON_H_

#include "veins/modules/application/ieee80211p/BaseWaveApplLayer.h"
#include "veins/modules/mobility/traci/TraCIMobility.h"
#include "veins/modules/mobility/traci/TraCICommandInterface.h"
#include "message/BeaconMessage_m.h"

using Veins::TraCIMobility;
using Veins::TraCICommandInterface;

namespace veins_myproject {

    class MyApplicaton : public BaseWaveApplLayer {

        public:
            virtual void initialize(int stage);
            virtual void receiveSignal(cComponent* source, simsignal_t signalID, cObject* obj, cObject* details);
        protected:
            TraCIMobility* mobility;
            TraCICommandInterface* traci;
            TraCICommandInterface::Vehicle* traciVehicle;

            simtime_t lastDroveAt; // the last time this sent a message
            bool sentMessage;
            int currentSubscribedServiceId;

            virtual void onWSM(WaveShortMessage* wsm);
            virtual void onBSM(BasicSafetyMessage* bsm);
            virtual void handlePositionUpdate(cObject* obj);
            virtual void handleSelfMsg(cMessage* msg);


    };
}
#endif /* SRC_MYNODES_H_ */



