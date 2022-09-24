FROM python:3.8.8-alpine3.13 
COPY requirements.txt .
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk update && \
    apk add --no-cache gcc libffi-dev musl-dev mysql-dev tzdata && \
    pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ && \
    pip install -U pip && \
    pip install --timeout 30 --no-cache-dir -r requirements.txt && \
    apk del gcc libffi-dev musl-dev

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' >/etc/timezone && \
    adduser -u 1001 -g 1001 -s /sbin/nologin -D http && \
    mkdir /var/log/uwsgi && \
    chown 1001:1001 /var/log/uwsgi && \
    mkdir -p /data/scrape_web && \
    chown 1001:1001 /data/scrape_web

WORKDIR /data
COPY --chown=1001:1001 . /data/scrape_web
CMD ["uwsgi", "--ini", "/data/scrape_web/uwsgi.ini"]
