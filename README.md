# ipam-hackathon
A small code that explains the docker installation, running, and visualization of the PRISMS-PF microgalvanic corrosion application.

## Getting started
For this demo, we're going to use Docker to grab an image of PRISMS-PF v2.4.0 and run one of our pre-built applications, microgalvanic corrosion.

If you want a brief explanation about what Docker is and why we use it, go [here](https://prisms-center.github.io/phaseField/doxygen/3.0.0-pre/docker.html). **_NOTE:_** The documentation for PRISMS-PF 3.0 is being redone.

To begin, please install Docker to your machine. You can find instructions for installing Docker on the official [Docker website](https://docs.docker.com/get-started/get-docker/).

Now, clone this repo and its submodules.
```
git clone --recurse-submodules https://github.com/UMThorntonGroup/ipam-hackathon.git
```
**_NOTE:_** If you have a git version prior to 2.13, use `--recursive` instead of `--recurse-submodules`.

## Pulling the docker image
Download the docker image with
```
docker pull prismspf/prismspf:2.4
```
This shouldn't take too long since the compressed size in only ~1.8GB.

## Launching the docker image
For this next part, we're going to run an interactive container.

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
This is just a simply test to make sure everything is working.
```
cd applications/allenCahn
cmake .
make release
mpirun -n 1 ./main
```

## Running the microgalvanic corrosion application
To run the `corrosion_microgalvanic` application, you can use the following commands:
```
cd applications/corrosion_microgalvanic
cmake .
make release
mpirun -n 1 ./main
```
Once your simulation is done you can exit the interactive docker container with
```
exit
```

## Visualizing the result
Open VisIt and hit the open button under the sources section.

<img width="221" height="128" alt="image" src="https://github.com/user-attachments/assets/890ac9c9-9e6a-4ebb-abbd-251bcb380cdb" />

Navigate the folder with your simulation results and click on the solution files and press OK.

<img width="848" height="745" alt="image" src="https://github.com/user-attachments/assets/b6a052cc-6ed5-4f77-bed9-ff17398776c4" />

Launch the CLI.

<img width="529" height="284" alt="image" src="https://github.com/user-attachments/assets/6bb81560-c342-4a8b-89a7-2af94207f66e" />

Sourcing the load_plots.py file. This will be different depending on whether you're on Linux/macOS and Windows due to the way VisIt installs.
**Linux/macOS**
Source("../../load_plots.py")
**Windows**
Source("../../path/to/ipam-hackathon/load_plots.py")

You should get something like this:

<img width="1434" height="1328" alt="image" src="https://github.com/user-attachments/assets/6c37811c-0739-4160-b783-34963c7e2e7c" />

