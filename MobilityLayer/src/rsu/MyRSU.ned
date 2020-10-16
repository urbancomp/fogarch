
package veins_myproject.src.rsu;


import org.car2x.veins.modules.application.ieee80211p.BaseWaveApplLayer;
import org.car2x.veins.base.modules.*;
import org.car2x.veins.modules.nic.Nic80211p;

module MyRSU
{
    parameters:
        string applType; //type oackage veins_teste.src;f the application layer
        string nicType = default("Nic80211p"); // type of network interface card
    gates:
        input veinsradioIn; // gate for sendDirect
    submodules:
        appl: <applType> like org.car2x.veins.base.modules.IBaseApplLayer {
            parameters:
                @display("p=60,50;i=block/network");
        }

        nic: <nicType> like org.car2x.veins.modules.nic.INic80211p {
            parameters:
                @display("p=60,166");
        }

        mobility: BaseMobility {
            parameters:
                @display("p=140,159;i=block/cogwheel");
        }

    connections:
        nic.upperLayerOut --> appl.lowerLayerIn;
        nic.upperLayerIn <-- appl.lowerLayerOut;
        nic.upperControlOut --> appl.lowerControlIn;
        nic.upperControlIn <-- appl.lowerControlOut;

        veinsradioIn --> nic.radioIn;

}
