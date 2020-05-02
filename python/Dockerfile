FROM borjaortizllamas/nginx:1.0.0 as python
MAINTAINER ortizllamasborja@gmail.com
# installing python 
RUN DEBIAN_FRONTEND=nointeractive apt-get update -y --no-install-recommends && \
apt-get install -y --no-install-recommends \
python3-pip  \
python3-dev \
build-essential \
libssl-dev \
libffi-dev \ 
python3-setuptools \
python3-venv 

FROM python as configure

RUN DEBIAN_FRONTEND=nointeractive apt-get install -y supervisor

#proyect of python
COPY ./provision/proyectPython/ /home/proyectPython/
#config nginx
COPY ./provision/nginx_conf/ /etc/nginx/
#config services
COPY ./provision/supervisord.conf /etc/supervisor/conf.d/
#script to run python script
COPY ./provision/pythonExecute.sh /home/pythonExecute.sh
VOLUME ["/home"]
CMD ["/usr/bin/supervisord"]