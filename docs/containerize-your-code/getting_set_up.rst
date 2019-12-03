Getting Set Up
==============

Before we begin, make a new directory somewhere on your local computer, and
create an empty Dockerfile inside of it. It is important to carefully consider
what files and folders are in the same `PATH` as a Dockerfile (known as the
'build context'). The `docker build` process will index and send all files and
folders in the same directory as the Dockerfile to the Docker daemon (which you
don't want to do), so take care not to `docker build` at a root level. For
example:

.. code-block:: shell

  $ cd ~/
  $ mkdir python-container/
  $ cd python-container/
  $ touch Dockerfile
  $ pwd
  /Users/wallen/python-container/
  $ ls
  Dockerfile


Next, grab a copy of the source code we want to containerize:

.. code-block:: python
   :linenos:

   #!/usr/bin/env python
   from random import random as r
   from math import pow as p
   from sys import argv

   # Make sure number of attempts is given on command line
   assert len(argv) == 2
   attempts = int(argv[1])
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


You can either cut and paste that python code into a new file called, e.g.,
`pi.py`, or `wget` it from the command line:

.. code-block:: shell

   $ wget https://raw.githubusercontent.com/TACC/containers_at_tacc/master/docs/scripts/pi.py


Now, you should have two files and nothing else in this folder:

.. code-block:: shell

   $ pwd
   /Users/wallen/python-container/
   $ ls
   Dockerfile     pi.py
