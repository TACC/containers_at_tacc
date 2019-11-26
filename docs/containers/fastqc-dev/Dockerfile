# Choose a base operating system
FROM ubuntu:18.04

# Update and install necessary packages
RUN apt-get update && apt-get upgrade -y |
  && apt-get install -y default-jre perl wget zip

# Install the application
RUN wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.7.zip \
    && unzip fastqc_v0.11.7.zip \
    && rm fastqc_v0.11.7.zip \
    && chmod +x /FastQC/fastqc

# Use environment variable to add executable to PATH
ENV PATH "/FastQC:$PATH"
