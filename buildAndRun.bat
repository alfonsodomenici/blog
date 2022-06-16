#/bin/sh
docker build -t blog .
docker rm -f   blog
docker run -d --name blog -p5000:5000 blog