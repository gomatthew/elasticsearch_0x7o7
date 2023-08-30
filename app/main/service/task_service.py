import json
import uuid

from app.main import app, redis_store


# def add_task_tracking(index_name, callback_url, items):
#     """
#     Set a list to track the indexing progress
#
#     key_name: [REDIS_PREFIX][index_name]:[uuid]
#     """
#     task_id = str(uuid.uuid4())
#     ids = []
#     for item in items:
#         if isinstance(item, dict):
#             ids.append(item.get("id"))
#         else:
#             ids.append(item)
#
#     # first set the tracking list
#     key_name = app.config.get("REDIS_PREFIX") + index_name + ":" + task_id
#     redis_store.set(key_name, json.dumps({
#         "task_id": task_id,
#         "callback_url": callback_url,
#         "ids": ids,
#         "indexed": []
#     }), ex=app.config.get("REDIS_DEFAULT_TTL"))
#
#     return task_id


def get_task_tracking(index_name, task_id):
    key_name = app.config.get("REDIS_PREFIX") + index_name + ":" + task_id
    task = redis_store.get(key_name)

    if task:
        return json.loads(task)
    else:
        return None


def remove_task_tracking(index_name, task_id):
    key_name = app.config.get("REDIS_PREFIX") + index_name + ":" + task_id
    if redis_store.exists(key_name):
        redis_store.delete(key_name)


def update_task_tracking(index_name, task_id, task):
    key_name = app.config.get("REDIS_PREFIX") + index_name + ":" + task_id
    if redis_store.exists(key_name):
        redis_store.set(key_name, json.dumps(task), ex=app.config.get("REDIS_DEFAULT_TTL"))
    else:
        app.logger.error("can not find key {} to update".format(key_name))
