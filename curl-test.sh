#!/bin/bash

NOMBRE=$1
EMAIL=$2
CONTENIDO=$3
curl --request POST http://localhost:5000/api/timeline_post -d 'name=Daniel&email=dan@hotmail.com&content=This is a message'

curl http://localhost:5000/api/timeline_post
