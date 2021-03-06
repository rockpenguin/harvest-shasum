# Harvest SHA1 generators

This repo contains a couple of methods to download the file http://nginx.org/download/nginx-1.13.1.tar.gz and then generate a SHA1 hash of said file. It's certainly *somewhat* easier to use the CLI (curl, shasum, etc.) but I thought these would be fun.

## shasum_nginx.py

The Python way.  Just a simple Python script that downloads the file and calculates the SHA1 checksum of the file. Just note that this Python script uses Python 3 modules, so you must use Python v3. Did I mention you need to use Python 3? The #! should force it to use Python 3, but if you ain't got Python 3 I'm thinking it won't run :-)

## shasum_nginx.yml

The Ansible way. Same thing as the Python script, it just downloads the ol' file and figures out ye olde SHA1 checksum. The only hitch seemed to be that the Ansible 'stat' module didn't produce a checksum on the Mac, so I reverted to using the 'command' module instead. Not ideal since this really isn't portable across OSes.

To run it, use `ansible-playbook`: `ansible-playbook -i localhost, -c local shasum_nginx.yml`

## shasum_nginx.sh

Probably the easiest way to do it if you're not going to automate the process: just a simple, down-home bash script that curls the file and calculates the checksum using `shasum` on the command line. Well, I suppose you could use it for automation. Just sprinkle in some variables, wrestle with `getopts` to give it some CLI *de rigueur* and off to the races!