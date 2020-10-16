package veins_myproject.src.car;

import org.car2x.veins.base.modules.*;
import org.car2x.veins.modules.nic.Nic80211p;

module MyCar
{
    parameters:
        string applType; //type of the application layer
        string nicType = default("Nic80211p"); // type of network interface card
        string veinsmobilityType = default("org.car2x.veins.modules.mobility.traci.TraCIMobility"); //type of the mobility module
    gates:
        input veinsradioIn; // gate for sendDirect
    submodules:
        appl: <applType> like org.car2x.veins.base.modules.IBaseApplLayer {
            parameters:
                @display("p=60,50;i=veins/node/car");
        }

        nic: <nicType> like org.car2x.veins.modules.nic.INic80211p {
            parameters:
                @display("p=60,166");
        }

        veinsmobility: <veinsmobilityType> like org.car2x.veins.base.modules.IMobility {
            parameters:
                @display("p=130,172;i=block/cogwheel");
        }

    connections:
        nic.upperLayerOut --> appl.lowerLayerIn;
        nic.upperLayerIn <-- appl.lowerLayerOut;
        nic.upperControlOut --> appl.lowerControlIn;
        nic.upperControlIn <-- appl.lowerControlOut;

        veinsradioIn --> nic.radioIn;


}
