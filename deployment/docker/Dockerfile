# Note this base image is based on debian
# Pulling from kartoza django base image that we maintain
FROM kartoza/django-base

MAINTAINER Alison Mukoma<mukomalison@gmail.com>

#RUN  ln -s /bin/true /sbin/initctl

# Pandoc needed to generate rst dumps, uic compressor needed for django-pipeline
RUN apt-get update -y; apt-get -y --force-yes install yui-compressor
RUN wget https://github.com/jgm/pandoc/releases/download/1.17.1/pandoc-1.17.1-2-amd64.deb
RUN dpkg -i pandoc-1.17.1-2-amd64.deb && rm pandoc-1.17.1-2-amd64.deb

ADD REQUIREMENTS.txt /REQUIREMENTS.txt
RUN pip install -r /REQUIREMENTS.txt
RUN pip install uwsgi


# Open port 8080 as we will be running our uwsgi socket on that
EXPOSE 8080

#USER www-data

WORKDIR /home/web/django_project
CMD ["uwsgi", "--ini", "/uwsgi.conf"]
