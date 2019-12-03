Build the Container
===================

Once the Dockerfile is complete, try to do a `docker build`

.. code-block:: bash

   $ docker build -t username/code:version .

List it

.. code-block:: bash

   $ docker images

Test it

.. code-block:: bash

   $ docker run --rm -it username/code:version /bin/bash
   [container] $ /path/to/code.py

.. code-block:: bash

   $ docker run --rm -it username/code:version /path/to/code.py




   Building the Image
   To build an image from a Dockerfile we use the docker build command. We use the -t flag to tag the image: that is, give our image a name. We also need to specify the working directory for the buid. We specify the current working directory using a dot (.) character:

   docker build -t classify_image .
   Note that this command requires all the files in the classifier directory in the Tutorial github repo (https://github.com/TACC/taccster18_Cloud_Tutorial/tree/master/classifier)
