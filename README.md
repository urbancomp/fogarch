
<!-- ABOUT THE PROJECT -->
## Multi-Layered Fog Computing Architecture for DataReduction in a Traffic Congestion Detection System


The Multi-Layered Fog Computing Architecture uses Cloud as a macro-control of the geographic position of all vehicles, acquiring traffic flow data to perform traffic congestion detection. In the network edge, the Multi-Layered Fog Computing Architecture uses traditional and cluster-based algorithms to reduce the amount of traffic data (as position and speed information) transmitted by all vehicles.

The cluster-based algorithms use the spatial density of the road map for clustering the traffic data, reducing the amount of data that is sent from the vehicular network to the Cloud. The results have shown that cluster-based algorithms in our Multi-Layered Fog Computing Architecture can achieve high accuracy on traffic congestion detection at a lower cost, even in an overloaded scenario.
About the implementation

The project was structured in two steps. First, we have the simulation files which are responsible to handle with the mobility layer. Second, the fog computing project. Here we have an infrastructure and algorithms that make possible the data reduction process plays its role.

<!-- GETTING STARTED -->
## Getting Started

Here, we have some simple steps to create this data Reduction Environment in your infrastructure.

### Prerequisites

First of all, we have to make the simulation environment operational.  In this project, we used three simulation tools that work in an integrated way.

For the mobility scenario, we are used:
* SUMO Simulator
* OMNET ++
* VEINS

Within this context, the sumo simulator is responsible for modeling the traffic environment, here we are able to define road and junctions. Next, the OMNET++ is responsible to offer the connectivity aspects, and at last, we have the Veins simulator. Veins is responsible to integrate the SUMO simulator and OMNET++ under the connectivity protocol IEEE 802.11p.

These simulators are available in:

* https://omnetpp.org/download/
* https://veins.car2x.org/download/
* https://www.eclipse.org/sumo/

### Installation of the simulation scenario

1. Clone the repo```sh git clone https://github.com/your_username_/Project-Name.git```
3. Install NPM packages
```sh
npm install
```
4. Enter your API in `config.js`
```JS
const API_KEY = 'ENTER YOUR API';
```

### Installation of the fog archtecture
1. Clone the repo```sh git clone https://github.com/your_username_/Project-Name.git```
3. Install NPM packages
```sh
npm install
```
4. Enter your API in `config.js`
```JS
const API_KEY = 'ENTER YOUR API';
```

## Usage

The Multi-Layered Fog Computing Architecture for DataReduction in a Traffic Congestion Detection System is a framework able to host different approaches to traffic detect congestion and data reduction process simultaneously. Thus, our implementation is able to apply some of the technics available in the literature and compare each one. Some results are introduced in the following image in experiment with 50 vehicles.

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <table>
    <tr>
      <td>
          <img src="images/logo.png" alt="Logo" width="80" height="80">
      </td>
      <td>
          <img src="images/logo.png" alt="Logo" width="80" height="80">
      </td>
      <td>
          <img src="images/logo.png" alt="Logo" width="80" height="80">
      </td>
    </tr>
    <tr>
      <td>
          <img src="images/logo.png" alt="Logo" width="80" height="80">
      </td>
      <td>
          <img src="images/logo.png" alt="Logo" width="80" height="80">
      </td>
      <td>
          <img src="images/logo.png" alt="Logo" width="80" height="80">
      </td>
    </tr>
  </table>
</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. 

<!-- CONTACT -->
## Contact

Prof. Dr. Maycon Leone - email@example.com


Project Link: [https://github.com/urbancomp/fogarch](https://github.com/urbancomp/fogarch)
