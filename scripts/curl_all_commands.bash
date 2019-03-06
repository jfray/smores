#!/bin/bash

for c in join help mute list who stop update private start test resend invite; do
  curl -X POST http://localhost:5000/async -d 'from=5107340278' -d "body=#${c} jfray"
done
