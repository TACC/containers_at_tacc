.. include:: ../substitutions.txt

Build from a Dockerfile
=======================

After going through the build process interactively, we can translate our build
steps into a Dockerfile using the directives described below.

.. note::

   Prerequisites: You should have access to a terminal with Docker installed
   You should also have a copy of |pipy|_


The FROM Instruction
--------------------

We can use the FROM instruction to start our new image from a known base image.
This should be the first line of our Dockerfile. In our hypothetical scenario,
we said our development platform / lab computer is a Linux workstation with
Ubuntu 18.04. We know our code works on that workstation, so that is how we will
containerize it. We will start our image from an official Ubuntu 18.04 image:

.. code-block:: dockerfile

   FROM ubuntu:18.04

Base images typically take the form ``os:version``. Avoid using the '``latest``'
version; it is hard to track where it came from and the identity of '``latest``'
can change.

.. tip::

   Browse `Docker Hub <https://hub.docker.com/>`_ to discover other potentially
   useful base images. Keep an eye out for the 'Official Image' badge.


The RUN Instruction
-------------------

We can install updates, install new software, or download code to our image by
running commands with the RUN instruction. In our case, our only dependency was
Python3. So, we will use a RUN instruction and the Ubuntu package manager
(``apt``) to install it. Keep in mind that the the ``docker build`` process cannot
handle interactive prompts, so we use the ``-y`` flag with ``apt``. We also need
to be sure to update our apt packages. A typical RUN instruction for an Ubuntu base
image may look like:

.. code-block:: dockerfile

   RUN apt-get update
   RUN apt-get upgrade -y
   RUN apt-get install -y python3

Each RUN instruction creates an intermediate image (called a 'layer'). Too many
layers makes the Docker image less performant, and makes building less
efficient. We can minimize the number of layers by combining the RUN
instructions:

.. code-block:: dockerfile

   RUN apt-get update && apt-get upgrade -y && apt-get install -y python3

A similar RUN instruction for a RedHat / CentOS base image may look like:

.. code-block:: dockerfile

   RUN yum update -y && yum install -y python3


The COPY Instruction
--------------------

There are a couple different ways to get your source code inside the image. One
way is to use a RUN instruction with ``wget`` to pull your code from the web. When
you are developing, however, it is usually more practical to copy code in from
the Docker build context using the COPY instruction. For example, we can add our
``pi.py`` python script to a root-level ``/code`` directory with the following
instruction:

.. code-block:: dockerfile

   COPY pi.py /code/pi.py

And, don't forget to perform one more RUN instruction to make the script
executable:

.. code-block:: dockerfile

   RUN chmod +rx /code/pi.py


The ENV Instruction
-------------------

Another useful instruction is the ENV instruction. This allows the image
developer to set environment variables inside the container runtime. In our
interactive build, we added the ``/code`` folder to the ``PATH``. We can do this
with an ENV instruction as follows:

.. code-block:: dockerfile

   ENV PATH "/code:$PATH"


Putting It All Together
-----------------------

The contents of the final Dockerfile should look like:

.. code-block:: dockerfile
   :linenos:

   FROM ubuntu:18.04

   RUN apt-get update && apt-get upgrade -y && apt-get install -y python3

   COPY pi.py /code/pi.py

   RUN chmod +rx /code/pi.py

   ENV PATH "/code:$PATH"


Build the Image
---------------

Once the Dockerfile is written and we are satisfied that we have minimized the
number of layers, the next step is to build an image. Building a Docker image
generally takes the form:

.. code-block:: console

   $ docker build -t username/code:version .

The ``-t`` flag is used to name or 'tag' the image with a descriptive name and
version. Optionally, you can preface the tag with your Docker Hub username or
other namespace where you have permissions to publish.
Adding that namespace allows you to push your image to a public container
registry and share it with others. The trailing dot '``.``' in the line above simply
indicates the location of the Dockerfile (a single '``.``' means 'the current
directory').

To build our image, use:

.. code-block:: console

   $ docker build -t username/pi-estimator:0.1 .

.. note::

   Don't forget to replace 'username' with your Docker Hub username.


Find the Image
--------------

Use ``docker images`` to ensure you see a copy of your image has been built. You can
also use ``docker inspect`` to find out more information about the image.

.. code-block:: console

   $ docker images
   REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
   username/pi-estimator     0.1                 482bd4f0bc9b        14 minutes ago      200MB
   ubuntu                    18.04               72300a873c2c        11 days ago         64.2MB

.. code-block:: console

   $ docker inspect username/pi-estimator:0.1


If you need to rename your image, you can either re-tag it with ``docker tag``, or
you can remove it with ``docker rmi`` and build it again. Issue each of the
commands on an empty command line to find out usage information.


Test the Image
--------------

We can test a newly-built image two ways: interactively and non-interactively.
In interactive testing, we will use ``docker run`` to start a shell inside the
image, just like we did when we were building it interactively. The difference
this time is that we are NOT mounting the code inside with the ``-v`` flag,
because the code is already in the container:

.. code-block:: console

   $ docker run --rm -it username/pi-estimator:0.1 /bin/bash
   ...
   root@e01e374d7749:/# ls /code
   pi.py
   root@e01e374d7749:/# pi.py 1000000
   Final pi estimate from 1000000 attempts = 3.137868

Here is an explanation of the options:

.. code-block:: console

  docker run      # run a container
  --rm            # remove the container when we exit
  -it             # interactively attach terminal to inside of container
  username/...    # image and tag on local machine
  /bin/bash       # shell to start inside container

Next, exit the container and test the code non-interactively. Notice we are calling
the container again with ``docker run``, but instead of specifying an interactive
(``-it``) run, we just issue the command as we want to call it ('``pi.py 1000000``')
on the command line:

.. code-block:: console

   $ docker run --rm username/pi-estimator:0.1 pi.py 1000000
   Final pi estimate from 1000000 attempts = 3.141208

If there are no errors, the container is built and ready to share!

Hands On Exercise
-----------------

Use ``docker inspect`` to look at the metadata for your ``pi-estimator`` image. Is
the ``/code`` folder in the ``$PATH``? Determine the contents of ``$PATH`` inside the
container to confirm.
