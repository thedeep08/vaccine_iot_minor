#!/bin/bash

docker run  -it --name mqtt -p 1883:1883 -p 9001:9001 --rm -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto

# docker run --name mqtt --rm --net=host -tid -v $(pwd)/mosquitto.conf:/mosquitto/config/mosquitto.conf -v $(pwd)/mosquitto/data/:/mosquitto/data -v $(pwd)/mosquitto/log/:/mosquitto/log  toke/mosquitto

# /volume1/docker/mqtt/config:/mqtt/config:ro -v /volume1/docker/mqtt/log:/mqtt/log -v /volume1/docker/mqtt/data/:/mqtt/data/
