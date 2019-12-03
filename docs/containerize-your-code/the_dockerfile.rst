The Dockerfile
==============

After going through the build process interactively, we can translate our build
steps into a Dockerfile using the following directives:


**The FROM Instruction**

We can use the FROM instruction to start our new image from a known base image.
This should be the first line of our Dockerfile. In our hypothetical scenario,
we said our development platform / lab computer is a Linux workstation with
Ubuntu 16.04. We know our code works on that workstation, so that is how we will
containerize it. We will start our image from an official Ubuntu 16.04 image:

.. code-block:: bash

   FROM ubuntu:16.04


.. tip::

   Browse `Docker Hub <https://hub.docker.com/>`_ to discover other potentially
   useful base images.


**The RUN Instruction**

We can install updates, install new software, or download code to our image by
running commands with the RUN instruction. In our case, our only dependency was
Python3. So, we will use a RUN instruction and the Ubuntu package manager
(`apt`) to install it. Keep in mind that the the `docker build` process cannot
handle interactive prompts, so we use the `-y` flag in `apt`. We also need to be
sure to update our apt packages. A typical RUN instruction for an Ubuntu base
image may look like:

.. code-block:: bash

   RUN apt-get update
   RUN apt-get upgrade -y
   RUN apt-get install -y python3

Each RUN instruction creates an intermediate image (called a 'layer'). Too many
layers makes the Docker image less performant, and makes building less
efficient. We can minimize the number of layers by combining the RUN
instructions:

.. code-block:: bash

   RUN apt-get update && apt-get upgrade -y && apt-get install -y python3

A similar RUN instruction for a RedHat / CentOS base image may look like:

.. code-block:: bash

   RUN yum update -y && yum install -y python3



**The COPY Instruction**

There are a couple different ways to get your source code inside the image. One
way is to use a RUN instruction with `wget` to pull your code from the web. When
you are developing, however, it is usually more practical to copy code in from
the Docker build context using the COPY instruction. For example, we can add our
`pi.py` python script to a root-level `/code` directory with the following
instruction:

.. code-block:: bash

   COPY pi.py /code/pi.py

And, don't forget to perform one more RUN instruction to make the script
executable:

.. code-block:: bash

   RUN chmod +x /code/pi.py



**The ENV Instruction**

Another useful instruction is the ENV instruction. This allows the image
developer to set environment variables inside the container runtime. In our
interactive build, we added the `/code` folder to the `PATH`. We can do this
with an ENV instruction as follows:

.. code-block:: bash

   ENV PATH "/code:$PATH"


**Putting It All Together**

The contents of the final Dockerfile should look like:

.. code-block:: bash

   FROM ubuntu:16.04

   RUN apt-get update && apt-get upgrade -y && apt-get install -y python3

   COPY pi.py /code/pi.py

   RUN chmod +x /code/pi.py

   ENV PATH "/code:$PATH"

Next, we are ready to `docker build`.
