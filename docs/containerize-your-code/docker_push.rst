Docker Push
===========

Now that the container is built, tested, and tagged. It is time to push it to docker hub so others can use it:

.. code-block:: bash

   $ docker push username/code:tag

It is also a good idea to save your Dockerfile and accompanying code somewhere safe and somewhere others may find it. Github is a good place for that. Github also has integrations to automatically update your Dockerfile every time you commit new code.

