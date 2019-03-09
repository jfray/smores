api: python app.py
queue: rq worker
web: ngrok http -subdomain $NGROK_HOSTNAME 5000
neo4j: scripts/honcho_service_check.bash neo4j
redis: scripts/honcho_service_check.bash redis
