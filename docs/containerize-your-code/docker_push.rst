Docker Push
===========

Now that the container is built, tested, and tagged. It is time to push it to
Docker hub so others can use it. Remember, the image must be name-spaced with
either your Docker hub username or a Docker hub organization that you have write
privileges in order to push it:

.. code-block:: bash

   $ docker login
   ...
   $ docker push username/pi-estimator:0.1


Others will be able to pull a copy of your container with:

.. code-block:: bash

   $ docker pull username/pi-estimator:0.1


It is also a good idea to save your Dockerfile and accompanying code somewhere
safe and somewhere others may find it. Github is a good place for that. Github
also has integrations to automatically update your Dockerfile every time you
commit new code.

For example, see: `Set up automated builds <https://docs.docker.com/docker-hub/builds/>`_
