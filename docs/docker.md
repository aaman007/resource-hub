docker build --tag resource_hub .             
docker images ls                 
docker run --rm -p 5000:5000 resource_hub      

docker-compose up       
docker-compose up -d          
docker-compose up --build         
docker-compose down           