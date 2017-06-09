# Harvest SHA1 generators

This repo contains a couple of methods to download the file http://nginx.org/download/nginx-1.13.1.tar.gz and then generate a SHA1 hash of said file.

## shasum_nginx.py

The Python way.  Just a simple Python script that downloads the file and calculates the SHA1 checksum of the file.

## shasum_nginx.yml

The Ansible way. Same thing as the Python script, just download the ol' file and figure out ye olde SHA1 checksum. The only hitch seemed to be that the Ansible 'stat' module didn't produce a checksum on the Mac, so I reverted to using the 'command' module instead.