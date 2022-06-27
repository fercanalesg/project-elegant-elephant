#!/bin/bash


#tmux kill-server

systemctl daemon-reload
systemctl restart-myportfolio
cd /root/project-elegant-elephant-mio
git fetch 
git reset origin/main --hard
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt



#tmux new-session -d -s "Portfolio" 'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'
 

