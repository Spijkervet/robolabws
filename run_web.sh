./install_netdata.sh

sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -

sudo apt-get install -y nodejs
sudo npm install -g localtunnel

nohup lt --port 19999 --subdomain robolabws2 &
