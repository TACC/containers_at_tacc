Build the Container
===================

Once the Dockerfile is written and we are satisfied that we have minimized the
number of layers, the next step is to build an image. Building a Docker image
generally takes the form:

.. code-block:: bash

   $ docker build -t username/code:version .

The `-t` flag is used to name or 'tag' the image with a descriptive name and
version. Optionally, you can preface the tag with your Docker Hub username.
Adding that namespace allows you to push your image to a public container
registry and share it with others. The trailing dot `.` in the line above simply
indicates the location of the Dockerfile (a single `.` means the current
directory).

**Build the Image**

To build our image, use:

.. code-block:: bash

   $ docker build -t username/pi-estimator:0.1 .

.. note::

   Don't forget to replace 'username' with your Docker Hub username.


**Find the Image**

Use `docker images` to ensure you see a copy of your image has been built. You can
also use `docker inspect` to find out more information about the image.

.. code-block:: bash

   $ docker images
   REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
   username/pi-estimator     0.1                 482bd4f0bc9b        14 minutes ago      200MB
   ubuntu                    16.04               5e13f8dd4c1a        4 months ago        120MB

.. code-block:: bash

   $ docker inspect username/pi-estimator:0.1
   ...

If you need to rename your image, you can either re-tag it with `docker tag`, or
you can remove and rebuild it with `docker rmi`. Issue each of the commands on
an empty command line to find out usage information.


**Test the Image**

We can test a newly-built image two ways: interactively and non-interactively.
In interactive testing, we will use Docker run to start a shell inside the
image, just like we did when we were building it. The difference this time is
that we are NOT mounting the code inside with the `-v` flag, because the code is
already in the container:

.. code-block:: bash

   [local]$ docker run --rm -it username/pi-estimator:0.1 /bin/bash
   ...
   root@e01e374d7749:/# ls /code
   pi.py
   root@e01e374d7749:/# pi.py 1000000
   Final pi estimate from 1000000 attempts = 3.137868

Next, exit the container and test the code non-interactively. Notice we are calling
the container again with `docker run`, but instead of specifying an interactive
(`-it`) run, we just issue the command as we want to call it `pi.py 1000000` on
the command line:

.. code-block:: bash

   $ docker run --rm username/pi-estimator:0.1 pi.py 1000000
   Final pi estimate from 1000000 attempts = 3.141208

If there are no errors, the container is built and ready to share!
