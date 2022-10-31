#!/bin/bash

curl 127.0.0.1:5000
res=$?
if test "$res" != "0"; then
	echo "curl command failed : $res"
fi
