Interactive Build
=================

The most reproducible way to build a container is via a Dockerfile. We looked at
pre-formed Dockerfiles in the first section of this workshop. But, now we want
to build a Dockerfile from scratch. The questions you must ask yourself when
starting a new Dockerfile include:

1. What is an appropriate base image?
2. What dependencies are required for my program?
3. What is the install process for my program?
4. What environment variables may be important?

**Start an Interactive Session**

Let's work through these questions by performing an **interactive installation**
of our python script. In our hypothetical scenario, let's say our development
platform / lab computer is a Linux workstation with Ubuntu 16.04. We know our
code works on that workstation, so that is how we will containerize it. Use
`docker run` to interactively attach to a fresh Ubuntu 16.04 container:

.. code-block:: shell

   [local]$ docker run --rm -it -v $PWD:/code ubuntu:16.04 /bin/bash


If this is your first time calling an Ubuntu 16.04 container on your laptop,
then docker will first download the image. The command prompt will change,
signaling you are now 'inside' the container.

**Update and Upgrade**

The first thing we will typically do is use the Ubuntu package manager `apt` to
update the list of available packages and install newer versions of the packages
we have. We can do this with:

.. code-block:: bash

   root@56c60cac8833:/# apt-get update
   ...
   root@56c60cac8833:/# apt-get upgrade
   ...

Note: on the second command, you need to choose `Y` to install the upgrades.

**Install New Packages**

For our python script to work, we need to install python3:

.. code-block:: bash

   root@56c60cac8833:/# apt-get install python3
   ...
   root@56c60cac8833:/# python3 --version
   Python 3.5.2

An important question to ask is: Does this version match the version you are
developing with on your local workstation?




.. code-block:: bash

   root@56c60cac8833:/# apt-get install -y wget
   root@56c60cac8833:/# wget https://raw.githubusercontent.com/TACC/containers_at_tacc/master/docs/scripts/pi.py

After choosing a base OS, it might be easiest to interactively install your program.

.. code-block:: bash

   $ docker build -t ubuntu:16.04 .

.. code-block:: bash

   $ docker run --rm -it ubuntu:16.04 /bin/bash

....Record build steps
