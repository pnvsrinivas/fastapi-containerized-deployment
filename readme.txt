
docker-compose down


docker-compose up --build -d

--below not workikng
docker-compose up -d

curl http://localhost/

docker exec -it <container_id> date

docker-compose logs -f nginx

locust -f locustfile.py

docker exec -it <container_id> cat /etc/nginx/nginx.conf

docker logs 653169467a62

docker network ls

docker network inspect <network_name>

docker-compose restart nginx

curl -v http://localhost

docker exec -it d64331698070 curl http://localhost

---------------------

netstat -ano | findstr LISTEN
tasklist /FI "PID eq 12560"
netstat -ano | findstr :80

taskkill /PID 0 /F