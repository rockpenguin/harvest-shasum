#! /usr/bin/env python3

import hashlib
import os
import urllib.request

# OK, let's download the file to the working dir - this should create a tuple of the filename, etc.
nginx_tar_file = urllib.request.urlretrieve("http://nginx.org/download/nginx-1.13.1.tar.gz", "nginx-1.13.1.tar.gz")

buffer = 131072  #we're going to read the file in 128kb size chunks so as not to chew up mem
sha1sum_obj = hashlib.sha1() # create a sha1 object using hashlib function sha1

#OK, now we grab the filename from the tuple and open it up as RO/binary
with open(nginx_tar_file[0], 'rb') as fd:
    while True:
        data_in = fd.read(buffer)
        if not data_in: # this will cause the while loop to end when the buffer is done
            break 
        sha1sum_obj.update(data_in)

sha1sum = sha1sum_obj.hexdigest() 

print("NGINX SHA1: {0}".format(sha1sum))