"""
Common utils
"""
import os
import re
import json
import urllib
import traceback
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

# import psutil
import requests
from decimal import Decimal
from sqlalchemy.ext.declarative import DeclarativeMeta

from app.main import app, redis_store


def get_current_datetime():
    tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00

    return datetime.now(tz=tz_utc_8)


def get_utc_8_timestamp(obj):
    if isinstance(obj, str):
        obj = datetime.fromisoformat(obj)

    tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
    return obj.replace(tzinfo=tz_utc_8).timestamp()


def get_timestamp(time):
    time_array = time.strptime(time, "%Y-%m-%d %H:%M:%S")
    time_ = int(time.mktime(time_array))
    return time_


def http_get_request(url, params, add_to_headers=None):
    headers = {
        "Content-type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.71 Safari/537.36',
    }
    if add_to_headers:
        headers.update(add_to_headers)
    post_data = urllib.parse.urlencode(params)
    response = requests.get(url, post_data, headers=headers, timeout=10)
    app.logger.debug("http_get_request=====>response: {}, params:{}".format(response, params))
    try:

        if response.status_code == 200:
            app.logger.debug("resp=====>url: {}, params: {}, add_to_header: {}, response: {}".format(url, params,
                                                                                                     add_to_headers,
                                                                                                     response.json()))
            return response.json()
        else:
            return
    except BaseException as e:
        # traceback.print_exc()
        # app.logger.error("httpGet failed, detail is:%s,%s" % (response.text, e))
        return


def http_post_request(url, params, add_to_headers=None):
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    post_data = json.dumps(params)
    response = requests.post(url, post_data, headers=headers, timeout=60)
    app.logger.debug("===>httpPost response, response is:{}".format(response))
    try:

        if response.status_code == 200:
            return response.json()
        else:
            return
    except BaseException as e:
        traceback.print_exc()
        app.logger.error("httpPost failed, detail is:%s,%s" % (response.text, e))
        return


# def memory_usage():
#     mem_available = psutil.virtual_memory().available
#     mem_process = psutil.Process(os.getpid()).memory_info().rss
#     return round(mem_process / 1024 / 1024, 2), round(mem_available / 1024 / 1024, 2)


def is_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?].*)$', re.IGNORECASE)

    if re.match(regex, url):
        return True
    else:
        return False


def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, Decimal):
                        fields[field] = str(data)
                    elif isinstance(data, datetime):
                        fields[field] = data.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        json.dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields


def redis_balance(balance_key: str) -> str:
    balance = redis_store.lpop(balance_key)
    if balance:
        return app.config.get('REDIS_PREFIX') + balance % len(app.config.get('REDIS_QUEUE'))
    else:
        redis_store.lpush(balance_key, [i for i in range(pow(2, 27))])

        return redis_balance(balance_key)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        import datetime as dt
        if isinstance(obj, dt.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, dt.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)
