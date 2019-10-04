./install_netdata.sh

sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -

sudo apt-get install -y nodejs
sudo npm install -g localtunnel

sudo cp summary.html /usr/share/netdata/web/
sudo chown netdata:netdata /usr/share/netdata/web/summary.html

nohup lt --port 19999 --subdomain robolabws1 &
nohup lt --port 19999 --subdomain robolabws2 &
