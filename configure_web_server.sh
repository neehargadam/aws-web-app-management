#!/bin/bash
apt-get update
apt-get install -y nginx
systemctl start nginx
systemctl enable nginx
mkdir -p /var/www/html
cp /home/ubuntu/index.html /var/www/html/index.html
