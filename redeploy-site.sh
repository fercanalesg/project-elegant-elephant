#!/bin/bash

# WE USED THIS WHEN WE WERE USING TMUX SESSIONS TO KEEP OUR WEBSITE RUNNING
#tmux kill-server

# WE USED THIS WHEN WE CREATED A SERVICE TO KEEP OUR WEBSITE RUNNING
#systemctl daemon-reload
#systemctl restart-myportfolio


cd /root/project-elegant-elephant-mio
git fetch 
git reset origin/main --hard
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build

#source python3-virtualenv/bin/activate
#pip3 install -r requirements.txt



#tmux new-session -d -s "Portfolio" 'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'
 

