## How to start Project - Docker
1. Install docker
2. Build the docker image
    `sudo docker build --no-cache -t movie-search .`
3. [Optional] Find your latest docker image id with the tag `movie-search`
    `sudo docker images`
4. Run the docker image
    `sudo docker -p 3000:3000 -p 5000:5000 [image-id]`
5. Access the webserver through 127.0.0.1:3000 on your web browser