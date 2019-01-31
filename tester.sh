#!/usr/bin/env bash

curl -i http://127.0.0.1:9090/test?[1-10] &
curl -i http://127.0.0.1:9090/test?[1-10] &
curl -i http://127.0.0.1:9090/test?[1-10] &

wait