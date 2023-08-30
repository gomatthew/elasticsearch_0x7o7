FROM python:3.10
LABEL author="0x7o7"
LABEL purpose = 'ElasricSearch Service'

ENV TZ=Asia/Shanghai
RUN echo $RUNTIME_ENV
ENV PYTHONUNBUFFERED 0
ENV RUNTIME_ENV testing


COPY . /app
COPY ./docker/sources.list /etc/apt/sources.list
RUN mkdir -p /app/logs

RUN apt-get update && apt-get install -y libtinfo5 --allow-remove-essential # supervisor 依赖
RUN apt-get install -y supervisor
RUN apt-get install -y vim
# 光标修正
RUN apt-get install ncurses-base

COPY ./docker/services/* /etc/supervisor/conf.d/
COPY ./docker/supervisord.conf /etc/supervisor/

# 设定时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app
RUN pip3 install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple
RUN pip3 install -r /app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple
EXPOSE 8000
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]