FROM python:3.8.8-slim AS build

COPY requirements.txt .

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ && \
    pip install --upgrade pip &&\
    pip install --timeout 30 --no-cache-dir --no-warn-script-location -r requirements.txt

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' >/etc/timezone && \
    mkdir /data

WORKDIR /data
COPY . /data

CMD ["python", "run.py"]