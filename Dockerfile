FROM python:3

RUN mkdir /code
WORKDIR /code

# Just adding basics
ADD requirements.txt /code/

# Add everything
ADD . /code/


# Nginx moved out
#COPY ./build/semesterly-nginx.conf /etc/nginx/sites-available/
#RUN rm /etc/nginx/sites-enabled/*
#RUN ln -s /etc/nginx/sites-available/semesterly-nginx.conf /etc/nginx/sites-enabled
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN pip install django
RUN pip install -r requirements.txt
# This is needed on newer ubuntu
RUN pip install psycopg2-binary

# RUN npm install
# RUN npm run build
# RUN python mysite/manage.py runserver
