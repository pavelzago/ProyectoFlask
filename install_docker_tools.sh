#!/bin/bash
#
# Script para instalar 'docker' y 'docker-compose'
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2021-08-10
#
# ---
#
# Las siguientes lineas muestran commo instalar Docker del repositorio oficial
#
# ---> COMIENZO
# curl -fsSL https://get.docker.com -o get-docker.sh
# sh get-docker.sh 
# rm -f get-docker.sh
# ---> FIN
#
# Y estas son las lineas para descargar 'docker' desde el repositorio de Ubuntu
#
#sudo apt install -y docker.io
sudo apt update && apt upgrade 
sudo snap install docker -y
sudo systemctl start docker
sudo systemctl enable docker
#
# Adicionando el grupo 'docker' al perfil del usuario 'vagrant'
#
usermod -aG docker vagrant
#
# Descargando e instalando 'docker-compose'
#
curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
