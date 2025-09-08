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
