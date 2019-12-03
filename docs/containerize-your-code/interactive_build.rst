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

.. code-block:: bash

   [local]$ docker run --rm -it -v $PWD:/code ubuntu:16.04 /bin/bash

Here is an explanation of the options:

.. code-block:: bash

   docker run      # run a container
   --rm            # remove the container when we exit
   -it             # interactively attach terminal to inside of container
   -v $PWD:/code   # mount the current directory to /code
   unbuntu:16.04   # image and tag from Docker Hub
   /bin/bash       # shell to start inside container

If this is your first time calling an Ubuntu 16.04 container on your laptop,
then Docker will first download the image. The command prompt will change,
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

Note: on the second command, you need to choose 'Y' to install the upgrades.

**Install New Packages**

For our python script to work, we need to install python3:

.. code-block:: bash

   root@56c60cac8833:/# apt-get install python3
   ...
   root@56c60cac8833:/# python3 --version
   Python 3.5.2

An important question to ask is: Does this version match the version you are
developing with on your local workstation? If not, make sure to install the
correct version of python.


**Install and Test Your Code**

Since we are using a simple python script, there is no burdensome install
process. However, we can make it executable, make sure it is in the user's PATH,
and make sure it works as expected:

.. code-block:: bash

   root@56c60cac8833:/# cd /code
   root@56c60cac8833:/# chmod +x pi.py
   root@56c60cac8833:/# export PATH=/code:$PATH

Now test with the following:

.. code-block:: bash

   root@56c60cac8833:/# cd /home
   root@56c60cac8833:/# which pi.py
   /code/pi.py
   root@56c60cac8833:/# pi.py 1000000
   Final pi estimate from 1000000 attempts = 3.142804

.. note::

   The command `which` probably did not work the first time you tried it. But,
   it is installed on your local computer. Why didn't it work? Use `apt-get` to
   install `which` if desired.


**Wrapping Up**

We have a functional installation of `pi.py`! Now might be a good time to type
`history` to see a record of the build process. When you are ready to start
working on a Dockerfile, type `exit` to exit the container.
