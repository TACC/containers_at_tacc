Solution
========

.. code-block:: bash
   :linenos:

   # 1: edit pi.py to include new code
   # 2: edit Dockerfile to include CMD instruction
   # 3: follow the steps below

   $ docker build -t username/pi-estimator:0.2 .
   $ docker run --rm username/pi-estimator:0.2
   usage: pi.py [-h] number

   positional arguments:
     number      number of random points (int)

   optional arguments:
     -h, --help  show this help message and exit

   $ docker run --rm username/pi-estimator:0.2 pi.py 1000000
   Final pi estimate from 1000000 attempts = 3.143672

   $ docker run --rm -it username/pi-estimator:0.2 /bin/bash
   root@c5aa145e5546:/# which pi.py
   /code/pi.py
   root@c5aa145e5546:/# pi.py 1000000
   Final pi estimate from 1000000 attempts = 3.141168
   root@c5aa145e5546:/# exit

   $ docker push username/pi-estimator:0.2
