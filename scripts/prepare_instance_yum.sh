#!/bin/sh

# Change this to where you want to install. $HOME
# is probably a bad choice if it needs to be maintained
# by a group of people

# This was developed on Ubuntu 18.04 LTS on Google Cloud

INSTALL_ROOT=/opt

# Prepare instance (or machine) with Docker, docker-compose, python

sudo yum install -y git \
                        build-essential \
                        nginx \
                        python-dev

# Needed module for system python
wget https://bootstrap.pypa.io/get-pip.py
sudo /usr/bin/python get-pip.py
sudo pip install ipaddress
sudo pip install oauth2client


# Install Docker dependencies
sudo yum install -y yum-utils device-mapper-persistent-data lvm2

#Add a stable repo
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

#Install Docker!
sudo yum install docker-ce -y

#Start docker service
sudo systemctl start docker
sudo systemctl enable docker

#make sure to add all users that will maintain / use the registry
sudo usermod -aG docker $USER
sudo usermod -aG docker bradlma

# test, you will still need sudo
sudo docker run hello-world

# Docker group should already exist
# sudo groupadd docker

# Docker-compose
sudo yum -y install docker-compose



# Note that you will need to log in and out for changes to take effect

if [ ! -d $INSTALL_ROOT/sregistry ]; then
    cd $INSTALL_ROOT

    # if you need to install a specific branch
    # git clone -b <branch> https://www.github.com/singularityhub/sregistry.git

    # otherwise production
    git clone https://www.github.com/singularityhub/sregistry.git

    cd sregistry
    docker build -t quay.io/vanessa/sregistry .
    docker-compose up -d
fi
