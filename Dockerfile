#FROM alpine/git as git_repo

#ARG SSH_PRIVATE_KEY
#RUN mkdir /root/.ssh/ && chmod 755 /root/.ssh/
#RUN echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa && chmod 600 /root/.ssh/id_rsa
#RUN touch /root/.ssh/known_hosts
#RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

#WORKDIR /code
#RUN git clone git@github.com:unsw-cse-comp3900-9900-22T2/capstone-project-9900-t16p-fazeclan.git
#WORKDIR /code/capstone-project-9900-t16p-fazeclan
#RUN git checkout docker_setup

FROM node:latest

#COPY --from=git_repo /code/capstone-project-9900-t16p-fazeclan /movie-search
COPY . /

RUN apt-get update || : && apt-get install python3 -y
RUN apt-get install python3-pip -y

RUN pip install -r backend/env_vlab.txt
RUN yarn --cwd frontend/ install --ignore-engines

EXPOSE 3000 5000

RUN chmod 777 run.sh

CMD ./run.sh
