# What it does
This is a dashboard for [Kimai](www.kimai.org).
It shows all active timeschedule records (i.e. the tasks that have startet but not yet been ended) of a user.

# How to use it
A running docker instance of Kimai is required (see [here](www.kimai.org/documentation/docker.html)
for a `docker-compose.yml`).
Add a `.env.prod` file with the following content:

```
DEBUG=0
SECRET_KEY=???
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

KIMAI_HOST=kimai2_nginx_1
KIMAI_X-AUTH-USER=test user
KIMAI_X-AUTH-TOKEN=testapitoken
```

Replace `???` with a secret string
(this is [django's secret key](https://docs.djangoproject.com/en/3.2/topics/signing/)).
Replace `test user` and `testapitoken`
(you can set an API password kimai profile settings).
Adjust the other settings according to your setup.
You may have to change `kimai2_default` to the actual name of kimai's docker network
(run `docker network ls` while running kimai to find out the name).
