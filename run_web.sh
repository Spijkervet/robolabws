sh install_netdata.sh
sudo apt-get install -y nodejs npm
sudo npm install -g localtunnel

nohup lt --port 19999 --subdomain robolabws1 &
