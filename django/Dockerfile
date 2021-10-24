FROM python:3-alpine

RUN addgroup -S app && adduser -S app -G app
WORKDIR /home/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

# this would be nice, but does not work because changing "static_volume" would not be permissable
#USER app
