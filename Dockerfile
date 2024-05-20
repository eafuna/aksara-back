
FROM python:3.10.13-slim-bullseye AS builder

WORKDIR /app 

RUN apt-get update && apt-get install -y \
	gcc \
	libpq-dev

COPY ./aksara /app/aksara
COPY manage.py /app 
COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV DJANGO_SECRET_KEY='qf2!esmy+t-vz_sgva7ud#1ktv5%_ev*keox6z59%%xxex)ydw'
ENV DEBUG=True
ENV DJANGO_ALLOWED_HOST='*'

# POSTGRES CONFIG
# ENV POSTGRES_USER=postgres
# #ENV POSTGRES_HOST=dev-postgres-cluster-instance-1-ap-southeast-1a.cj88ymqqu01f.ap-southeast-1.rds.amazonaws.com
# ENV POSTGRES_PORT=5432
# ENV POSTGRES_PASSWORD=Aksara123
# ENV POSTGRES_DB=postgres

EXPOSE 8000
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]


