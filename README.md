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
