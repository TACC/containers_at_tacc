Other Considerations
====================

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
