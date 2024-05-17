.. include:: ../substitutions.txt

.. _install_code_interactively:

Install Code Interactively
==========================

In this section, we will explore the first half of a typical development
workflow: installing an application interactively within a running Docker
container.

.. note::

   Prerequisites: You should have access to a terminal with Docker installed.


Set Up
------

Before we begin, make a new directory somewhere on your local computer, and
create an empty Dockerfile inside of it. It is important to carefully consider
what files and folders are in the same ``PATH`` as a Dockerfile (known as the
'build context'). The ``docker build`` process will index and send all files and
folders in the same directory as the Dockerfile to the Docker daemon, so take
care not to ``docker build`` at a root level. For example:

.. code-block:: console

  $ cd ~/
  $ mkdir python-container/
  $ cd python-container/
  $ touch Dockerfile
  $ pwd
  /Users/username/python-container/
  $ ls
  Dockerfile


Next, grab a copy of the source code we want to containerize:

.. code-block:: python
   :linenos:

   #!/usr/bin/env python3
   from random import random as r
   from math import pow as p
   from sys import argv

   # Make sure number of attempts is given on command line
   assert len(argv) == 2
   attempts = int(argv[1])
   inside = 0
   tries = 0

   # Try the specified number of random points
   while (tries < attempts):
       tries += 1
       if (p(r(),2) + p(r(),2) < 1):
           inside += 1

   # Compute and print a final ratio
   print( f'Final pi estimate from {attempts} attempts = {4.*(inside/tries)}' )


You can cut and paste the code block above into a new file called, e.g.,
``pi.py``, or download it from the following link:

|pipyurl|_


Now, you should have two files and nothing else in this folder:

.. code-block:: console

   $ pwd
   /Users/username/python-container/
   $ ls
   Dockerfile     pi.py


Important Considerations
------------------------

The most reproducible way to build a container is via a Dockerfile. We looked at
pre-formed Dockerfiles in the first section of this workshop. But, now we want
to build a Dockerfile from scratch. The questions you must ask yourself when
starting a new Dockerfile include:

1. What is an appropriate base image?
2. What dependencies are required for my program?
3. What is the install process for my program?
4. What environment variables may be important?


Start an Interactive Session
----------------------------

Let's work through these questions by performing an **interactive installation**
of our python script. In our hypothetical scenario, let's say our development
platform / lab computer is a Linux workstation with Ubuntu 18.04. We know our
code works on that workstation, so that is how we will containerize it. Use
``docker run`` to interactively attach to a fresh Ubuntu 18.04 container:

.. code-block:: console

  $ docker run -it -v $PWD:/code ubuntu:18.04 /bin/bash

Here is an explanation of the options:

.. code-block:: text

  docker run      # run a container
  -it             # interactively attach terminal to inside of container
  -v $PWD:/code   # mount the current directory to /code
  unbuntu:18.04   # image and tag from Docker Hub
  /bin/bash       # shell to start inside container

If this is your first time calling an Ubuntu 18.04 container on your laptop,
then Docker will first download the image. The command prompt will change,
signaling you are now 'inside' the container.

Update and Upgrade
------------------

The first thing we will typically do is use the Ubuntu package manager ``apt`` to
update the list of available packages and install newer versions of the packages
we have. We can do this with:

.. code-block:: console

  root@56c60cac8833:/# apt-get update
  ...
  root@56c60cac8833:/# apt-get upgrade
  ...

.. note::

  On the second command, you may need to choose 'Y' to install the upgrades.


Install Required Packages
-------------------------

For our python script to work, we need to install python3:

.. code-block:: console

  root@56c60cac8833:/# apt-get install python3
  ...
  root@56c60cac8833:/# python3 --version
  Python 3.6.9

An important question to ask is: Does this version match the version you are
developing with on your local workstation? If not, make sure to install the
correct version of python.


Install and Test Your Code
--------------------------

Since we are using a simple python script, there is not a difficult install
process. However, we can make it executable, make sure it is in the user's PATH,
and make sure it works as expected:

.. code-block:: console

  root@56c60cac8833:/# cd /code
  root@56c60cac8833:/# chmod +rx pi.py
  root@56c60cac8833:/# export PATH=/code:$PATH

Now test with the following:

.. code-block:: console

  root@56c60cac8833:/# cd /home
  root@56c60cac8833:/# which pi.py
  /code/pi.py
  root@56c60cac8833:/# pi.py 1000000
  Final pi estimate from 1000000 attempts = 3.142804


Wrapping Up
-----------

We have a functional installation of ``pi.py``! Now might be a good time to type
``history`` to see a record of the build process. When you are ready to start
working on a Dockerfile, type ``exit`` to exit the container.


Hands On Exercise
-----------------

What (if any) Docker images do you currently have on your machine? What (if any)
Docker processes are currently running? If you have an Ubuntu base image, try
removing it.
