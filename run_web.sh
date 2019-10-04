sh install_netdata.sh
sudo apt-get install -y nodejs npm
sudo npm install -g localtunnel

sudo cp summary.html /usr/share/netdata/web/
sudo chown netdata:netdata /usr/share/netdata/web/summary.html

nohup lt --port 19999 --subdomain robolabws1 &
