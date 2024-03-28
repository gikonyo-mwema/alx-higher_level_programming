#!/bin/bash
# sends an OPTION requet to a URL display all methods the server accept
curl -sI -X OPTIONS "$1" | grep Allow | cut -d ' ' -f 2-
