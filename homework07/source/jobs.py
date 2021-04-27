import uuid
import time
import os
from redis import StrictRedis
from hotqueue import HotQueue

redis_ip = os.environ.get('REDIS_IP')
q = HotQueue("queue", host=redis_ip, port=6379, db=1)
rd = StrictRedis(host=redis_ip, port=6379, db=0)


def _generate_jid():
    return str(uuid.uuid4())


def _generate_job_key(jid):
    return 'job.{}'.format(jid)


def _instantiate_job(jid, worker, status, start, end):
    if type(jid) == str:
        return {'id': jid,
                'status': status,
                'start': start,
                'end': end, 
                'worker': worker}
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'start': start.decode('utf-8'),
            'end': end.decode('utf-8'), 
            'worker': worker.decode('utf-8') }


def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.hmset(job_key, job_dict)


def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)
    

def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, 'None', status, start, end)
    _save_job(_generate_job_key(jid), job_dict)
    _queue_job(jid)
    return job_dict


def update_job_status(jid, new_status):
    """Update the status of job with job id `jid` to status `status`."""
    worker, jid, status, start, end = rd.hmget(_generate_job_key(jid), 'worker', 'id', 'status', 'start', 'end')
    job = _instantiate_job(jid, worker, status, start, end)
    if job:
        job['status'] = new_status
        job['worker'] = os.environ.get("WORKER_IP")
        _save_job(_generate_job_key(job["id"]), job)
    else:
        raise Exception()
