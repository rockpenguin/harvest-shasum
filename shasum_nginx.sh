#! /usr/bin/env bash

# OK, let's grab the file
curl --connect-timeout 10 -O http://nginx.org/download/nginx-1.13.1.tar.gz

# Better sleep for a little bit to make sure the file is downloaded and flushed to disk
sleep 10

shasum -a 1 nginx-1.13.1.tar.gz