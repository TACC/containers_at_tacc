Other Considerations
====================

- Tips for keeping images small
- Don't use entrypoint or cmd
- More

Save your Dockerfiles – GitHub is a good place for this
You may not need ENTRYPOINT or CMD
Usually better to use COPY instead of ADD
Order of operations in the Dockerfile is important; combine steps where possible
Avoid latest tag; use explicit tag callouts
The command docker system prune is your friend
Use docker-compose for multi-container pipelines and microservices
Considerations for one tool per container vs. multiple tools per container
