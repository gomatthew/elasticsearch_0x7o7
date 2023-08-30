import time
import redis
from rq import Queue
from rq.job import JobStatus
from app.main import app


def rq_retry_handler(job, *exc_info):
    # Returning True moves the job to the failed queue (or continue to
    # the next handler)

    job.meta.setdefault('failures', 1)
    app.logger.info("Retrying Job {} {} times".format(job.id, job.meta['failures']))
    job.meta['failures'] += 1

    if job.meta['failures'] > app.config.get("RQ_MAX_RETRIES"):
        job.save()
        return True

    time.sleep(job.meta['failures'])
    job.status = JobStatus.QUEUED
    for queue_ in app.config['QUEUES']:
        if queue_ == job.origin:
            redis_url = app.config['RQ_REDIS_URL']
            redis_connection = redis.from_url(redis_url)
            q = Queue(queue_, connection=redis_connection)
            q.enqueue_job(job, at_front=True)
            break
    else:
        return True  # Queue has disappeared, fail job

    return False  # Job is handled. Stop the handler chain.
