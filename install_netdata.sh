#/bin/bash
bash <(curl -Ss https://my-netdata.io/kickstart.sh)

cd /tmp/
git clone https://github.com/Splo0sh/netdata_nv_plugin --depth 1
sudo cp netdata_nv_plugin/nv.chart.py /usr/libexec/netdata/python.d/
sudo cp netdata_nv_plugin/python_modules/pynvml.py /usr/libexec/netdata/python.d/python_modules/
sudo cp netdata_nv_plugin/nv.conf /etc/netdata/python.d/
