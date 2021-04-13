FROM python:3.8.5

WORKDIR /app

# не добаввляются файлы с расширением .рус
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#
RUN apt-get update \
	&& apt-get install netcat -y 
	# && --no-install-recommends apt-utils
RUN apt-get upgrade -y && apt-get install -y postgresql gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

COPY . .

# RUN ["chmod", "+x", "entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint.sh"] 













# FROM python:3.8.5

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /usr/src/four_rest

# COPY ./req.txt /usr/src/req.txt
# RUN pip install -r /usr/src/req.txt

# COPY . /usr/src/four_rest

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]