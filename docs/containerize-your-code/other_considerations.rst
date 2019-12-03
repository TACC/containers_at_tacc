Other Considerations
====================

The best way to learn to build docker images is to practice building images for
tools you use. The online `Docker documentation <https://docs.docker.com/>`_
contains a lot of good advice on building images.

Some miscellaneous tips for building images include:

* Save your Dockerfiles – GitHub is a good place for this
* You may not need ENTRYPOINT or CMD
* Usually better to use COPY instead of ADD
* Order of operations in the Dockerfile is important; combine steps where possible
* Remove temporary and unnecessary files to keep images small
* Avoid using `latest` tag; use explicit tag callouts
* The command `docker system prune` is your friend
* Use docker-compose for multi-container pipelines and microservices
* Considerations for one tool per container vs. multiple tools per container
