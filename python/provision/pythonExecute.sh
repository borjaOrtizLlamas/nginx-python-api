#/bin/bash
cd /home/proyectPython
source pythonDev/bin/activate
pip3 install uwsgi flask
python3 wsgi.py