Share Your Docker Image
=======================

.. note::

   Prerequisites: You should have access to a terminal with Docker installed
   and a Docker Hub account. You should also have a copy of `pi.py <https://raw.githubusercontent.com/TACC/containers_at_tacc/master/docs/scripts/pi.py>`_

Now that you have containerized, tested, and tagged your code in a Docker image,
the next step is to disseminate it so others can use it.

Interface with Docker Hub
-------------------------


Docker Hub is the de facto place to share an image you built. Remember, the
image must be name-spaced with either your Docker Hub username or a Docker Hub
organization where you have write privileges in order to push it:

.. code-block:: bash

   $ docker login
   ...
   $ docker push username/pi-estimator:0.1


You and others will now be able to pull a copy of your container with:

.. code-block:: bash

   $ docker pull username/pi-estimator:0.1


It is also a good idea to save your Dockerfile and accompanying code somewhere
safe and somewhere others may find it. Github is a good place for that. Github
also has integrations to automatically update your image in the public container
registry every time you commit new code.

For example, see: `Set up automated builds <https://docs.docker.com/docker-hub/builds/>`_


Hands On Exercise
-----------------

*Scenario:* You have the great idea to update your python code to use `argparse`
to better handle the command line arguments. Outside of the container, modify
`pi.py` to look like:

.. code-block:: python
   :linenos:
   :emphasize-lines: 6-10,13

   #!/usr/bin/env python3
   from random import random as r
   from math import pow as p
   from sys import argv

   # Use argparse to take command line options and generate help text
   import argparse
   parser = argparse.ArgumentParser()
   parser.add_argument("number", help="number of random points (int)", type=int)
   args = parser.parse_args()

   # Grab number of attempts from command line
   attempts = args.number
   inside=0
   tries=0
   ratio=0.

   # Try the specified number of random points
   while (tries < attempts):
       tries += 1
       if (p(r(),2) + p(r(),2) < 1):
           inside += 1

   # Compute and print a final ratio
   ratio=4.*(inside/(tries))
   print("Final pi estimate from", attempts, "attempts =", ratio)

(New and modified lines are highlighted). With this change, the user can execute
'`pi.py -h`' to get usage information. You can also download this code from
here:

`https://raw.githubusercontent.com/TACC/containers_at_tacc/master/docs/scripts/pi-updated.py <https://raw.githubusercontent.com/TACC/containers_at_tacc/master/docs/scripts/pi-updated.py>`_


Next, update the Dockerfile to include a new kind of instruction at the very end
of the file - CMD:

.. code-block:: bash
   :linenos:
   :emphasize-lines: 11

   FROM ubuntu:18.04

   RUN apt-get update && apt-get upgrade -y && apt-get install -y python3

   COPY pi.py /code/pi.py

   RUN chmod +x /code/pi.py

   ENV PATH "/code:$PATH"

   CMD ["pi.py", "-h"]

This command will be executed in the container if the user calls the container
without any arguments.

Finally, rebuild the container and update the version tag to '0.2'. Test that
the code in the new container has been updated, and that it is working as
expected. If you are happy that it is working, push the updated container with
the new tag to Docker Hub.

.. toctree::
   :maxdepth: 1

   solution


Other Considerations
--------------------

The best way to learn to build docker images is to practice building lots of
images for tools you use. The online
`Docker documentation <https://docs.docker.com/>`_ contains a lot of good
advice on building images.

Some miscellaneous tips for building images include:

* Save your Dockerfiles – GitHub is a good place for this
* You probably don't want to use ENTRYPOINT - turns an container into a black box
* If you use CMD, make it print the help text for the containerized code
* Usually better to use COPY instead of ADD
* Order of operations in the Dockerfile is important; combine steps where possible
* Remove temporary and unnecessary files to keep images small
* Avoid using `latest` tag; use explicit tag callouts
* The command `docker system prune` will help free up space in your local environment
* Use `docker-compose` for multi-container pipelines and microservices
* A good rule of thumb is one tool or process per container
