# IPAM-Tutorial
A small code that explains the docker installation, running, and visualization of the PRISMS-PF microgalvanic corrosion application.

## Getting started
For this demo, we're going to use Docker to grab an image of PRISMS-PF v2.4.0 and run one of our pre-built applications, allenCahn and microgalvanic corrosion.

If you want a brief explanation about what Docker is and why we use it, go [here](https://prisms-center.github.io/phaseField/doxygen/3.0.0-pre/docker.html). **_NOTE:_** The documentation for PRISMS-PF 3.0 is being redone.

To begin, please install Docker to your machine. You can find instructions for installing Docker on the official [Docker website](https://docs.docker.com/get-started/get-docker/). In addition, you will need VisIt for visualization, which can be obtained from the [VisIt website](https://visit-dav.github.io/visit-website/releases-as-tables/#latest).

## Create a directory to hold the PRISMS-PF applications folder
For example type 
```
mkdir ~/DockerWorkspace
```
and go to that directory by  
```
cd ~/DockerWorkspace
```

## Pulling the docker image
Download the docker image with
```
docker pull prismspf/prismspf:2.4
```
This shouldn't take too long since the compressed size in only ~1.8GB.

## Clone the repo

Now, clone the PRISMS-PF v2.4.0 repo and its submodules.
```
git clone --recurse-submodules https://github.com/UMThorntonGroup/ipam-hackathon.git
```
**_NOTE:_** If you have a git version prior to 2.13, use `--recursive` instead of `--recurse-submodules`.


## Launching the docker image
For this next part, we're going to run an interactive container.

First, go to the `ipam-hackathon` directory:

```
cd ipam-hackathon
```

Then launch the container with one of the following commands:

**Linux & macOS (bash and z-shell)**
```
docker run -ti -v $(pwd)/prisms-pf-2.4/applications:/home/dealii/phaseField/applications prismspf/prismspf:2.4
```
**macOS (c-shell)**
```
docker run -ti -v `pwd`/prisms-pf-2.4/applications:/home/dealii/phaseField/applications prismspf/prismspf:2.4
```
**Windows PowerShell**
```
docker run -ti -v ${PWD}/prisms-pf-2.4/applications:/home/dealii/phaseField/applications prismspf/prismspf:2.4
```
**Windows Command Prompt**
```
docker run -ti -v %cd%/prisms-pf-2.4/applications:/home/dealii/phaseField/applications prismspf/prismspf:2.4
```

This will link your local applications directory (the one in `prisms-pf-2.4`) to the one in the Docker image. If you plan to modify the core library, you should link one directory higher to preserve your changes.

## Running the Allen-Cahn application
Allen-Cahn equation simulates the evolution of nonconserved an order parameter (or multiple order parameters). We use this as a simple test to make sure everything is working and get you started.

Click on the copy icon on the right of each line, and paste into the terminal window (and hit return). You can ignore the warnings.
```
cd applications/allenCahn
```
```
cmake .
```
```
make release
```
```
mpirun -n 1 ./main
```
After the run is complete, check to see the output files have been created.  
```
ls
```
You should see files named "solution-xxxx.vtu" (xxxx is a number) if all worked. These files have the snapshots of data (inlcuding the order parameter) from the simulation. We will visualize the results later.

## Running the microgalvanic corrosion application

Two of the many applications set up in PRISMS-PF release simulate corrosion. One of these simulates microgalvanic corrosion, in which two phases of an alloy are in contact. The details can be found in the pdf document in the corrosion_microgalvanic folder (see below) and in the following publication.

Goel, V., Lyu, Y., DeWitt, S. et al. Simulating microgalvanic corrosion in alloys using the PRISMS phase-field framework. MRS Communications 12, 1050–1059 (2022). https://doi.org/10.1557/s43579-022-00266-6

To run the `corrosion_microgalvanic` application, you can use the following commands:
```
cd applications/corrosion_microgalvanic
```
```
cmake .
```
```
make release
```
```
mpirun -n 1 ./main
```
This simulation will likely take a while, so we will move onto visualization while this is running.
Once your simulation is done you can exit the interactive docker container with
```
exit
```

## Visualizing the result from `allenCahn` application
Open a new terminal window (leaving the one with the simulation running).

Open VisIt.
Select "Open" under the Sources section.

<img width="221" height="128" alt="image" src="https://github.com/user-attachments/assets/890ac9c9-9e6a-4ebb-abbd-251bcb380cdb" />

Navigate to the folder with your simulation results (which should be ~/DockerWorkspace/ipam-hackathon/prisms-pf-2.4/applications/allenCahn) and click on the solution files and press OK.

<img width="1185" height="960" alt="image" src="https://github.com/user-attachments/assets/e71a0f6e-671c-4c1b-9e86-af75fcf7cdab" />

Under Plots, select Add, pseudocolor, n to plot the order parameter.  

Click draw. This will show the two phase "microstructure". You can use the right arrow to see the evolution of the system, and the left arrow to go backwards in simulation time.

<img width="1059" height="961" alt="image" src="https://github.com/user-attachments/assets/d089d5ab-2184-4b17-befa-b8feff5f54c7" />

## Visualizing the result from `corrosion_microgalvanic` application

Select "Open" under the Sources section.

<img width="221" height="128" alt="image" src="https://github.com/user-attachments/assets/890ac9c9-9e6a-4ebb-abbd-251bcb380cdb" />

Navigate the folder with your simulation results (which should be ~/DockerWorkspace/ipam-hackathon/prisms-pf-2.4/applications/corrosion_microgalvanic) and click on the solution files and press OK.

<img width="848" height="745" alt="image" src="https://github.com/user-attachments/assets/b6a052cc-6ed5-4f77-bed9-ff17398776c4" />

Here, the plot is a little more complicated, so we prepared a script for you. To use the script, launch the CLI:

<img width="529" height="284" alt="image" src="https://github.com/user-attachments/assets/6bb81560-c342-4a8b-89a7-2af94207f66e" />

Sourcing the load_plots.py file. This will be different depending on whether you're on Linux/macOS and Windows due to the way VisIt installs.

**Linux/macOS**
```
Source("../../../load_plots.py")
```
**Windows**
```
Source("../../path/to/ipam-hackathon/load_plots.py")
```

Alternatively, if you want to specify an absolute path, you need to write a little python.
```
import os
path = "~/path/to/ipam-hackathon/load_plots.py"
Source(os.path.expanduser(path))
```

You should get something like this:

<img width="1434" height="1328" alt="image" src="https://github.com/user-attachments/assets/6c37811c-0739-4160-b783-34963c7e2e7c" />

## Further learning

You can learn more about PRISMS-PF at [the PRISMS-PF website](https://prisms-center.github.io/phaseField/).

There are also other tools develoed within the PRISMS Center; see [the PRISMS Center Software website](https://www.prisms-center.org/#/ctools/software).

