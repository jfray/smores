#!/bin/bash

./app.py &
rq worker &
ngrok http -subdomain smack 5000
