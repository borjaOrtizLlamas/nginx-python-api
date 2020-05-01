FROM ubuntu:latest
LABEL MANTEINER="ortizllamasborja@gmail.com" 
EXPOSE 80
EXPOSE 443
RUN DEBIAN_FRONTEND=nointeractive apt-get update -y --no-install-recommends && \
apt-get install -y --no-install-recommends locales && locale-gen en_US.UTF-8 && \
apt-get install -y --no-install-recommends nginx
CMD ["nginx","-g","daemon off;"]