
package veins_myproject.src;

import org.car2x.veins.base.connectionManager.ConnectionManager;
import org.car2x.veins.base.modules.BaseWorldUtility;
import org.car2x.veins.modules.mobility.traci.TraCIScenarioManager*;
import org.car2x.veins.modules.obstacle.ObstacleControl;
import org.car2x.veins.modules.world.annotations.AnnotationManager;
//import org.car2x.veins.nodes.Car;
//import org.car2x.veins.nodes.RSU;

network Scenario {
    
   parameters:
        double playgroundSizeX @unit(m); // x size of the area the nodes are in (in meters)
        double playgroundSizeY @unit(m); // y size of the area the nodes are in (in meters)
        double playgroundSizeZ @unit(m); // z size of the area the nodes are in (in meters)
        @display("bgb=431,239");
    submodules:
        //obstacles: ObstacleControl {
        //    @display("p=239,128");
        //}
        annotations: AnnotationManager {
            @display("p=259,151");
        }
        connectionManager: ConnectionManager {
            parameters:
                @display("p=147,151;i=abstract/multicast");
        }
        world: BaseWorldUtility {
            parameters:
                playgroundSizeX = playgroundSizeX;
                playgroundSizeY = playgroundSizeY;
                playgroundSizeZ = playgroundSizeZ;
                @display("p=32,151;i=misc/globe");
        }
        manager: TraCIScenarioManagerLaunchd {
            parameters:
                @display("p=512,128");
        }

       //rsu[1]: RSU {
       rsu[1]: veins_myproject.src.rsu.MyRSU {
        	parameters:
                @display("p=342,151;i=veins/sign/yellowdiamond");
                

        }
    connections allowunconnected:
    
    
}


    
