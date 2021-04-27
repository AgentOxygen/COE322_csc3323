# Homework 7
Cameron Cummins (csc3323)

## Part A

To create all of my deployments, I used the following commands in sequeunce:
~~~
cd /deploy
kubectl apply -f development-python-debug.yml
kubectl apply -f api/oxygen-flask-hw7-deployment.yml
kubectl apply -f db/oxygen-hw7-redis-deployment.yml
kubectl apply -f worker/oxygen-hw7-worker-deployment.yml
~~~

Entering the debug pod and executing the following command...
~~~
curl -X POST -H "content-type: application/json" -d '{"start":"START", "end":"END"}' 10.99.66.186:5000/jobs
~~~
... returned the following output:
~~~
{"id": "9102c507-89c9-4556-ab1c-c638d1dd2d53", "status": "submitted", "start": "START", "end": "END"}
~~~
After submitting multiple jobs, I opened a `python` terminal to see if it worked.
~~~
Python 3.9.2 (default, Feb 19 2021, 17:11:58)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> rd = redis.StrictRedis(host="10.109.252.67", port=6379, db=0)
>>>
>>>
>>> for key in rd.keys():
...     print(rd.hgetall(key))
...
{b'id': b'723116ee-577d-4ff5-929d-19b4ea60c0b0', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'ba78dcca-87d5-4d4c-8fed-f54d9d23f772', b'status': b'complete', b'start': b'START', b'end': b'END'}
{b'id': b'25a4759a-f991-422d-81ce-0f21a4ea362d', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'd2e27c65-7e05-4809-9a34-710d5ada14e4', b'status': b'complete', b'start': b'START', b'end': b'END'}
{b'id': b'd040fa8b-5519-4dc1-a184-c3cfaab69cd1', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'9102c507-89c9-4556-ab1c-c638d1dd2d53', b'status': b'in progress', b'start': b'START', b'end': b'END'}
{b'id': b'6ad0718e-4961-41cd-8327-4b23c4b56b96', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'dfd0313c-6db8-47cc-8255-f8ae17155c4a', b'status': b'complete', b'start': b'START', b'end': b'END'}
{b'id': b'd1d18ef7-68ef-47fc-b722-ba1fe6b79d63', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'61a5593b-0c67-4a1f-83c2-09191400888a', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'f2106e3b-86a0-4402-ae46-15242f9de219', b'status': b'complete', b'start': b'START', b'end': b'END'}
{b'id': b'db5178a3-68f1-44b9-bf3b-d7a7e7302ed2', b'status': b'complete', b'start': b'START', b'end': b'END'}
~~~

## Part C

After increasing the number of replicas to 2, I checked it using `kubectl get pods`
~~~
NAME                                           READY   STATUS    RESTARTS   AGE
oxygen-hw7-flask-deployment-74bc6f686-h25d6    1/1     Running   0          8m29s
oxygen-hw7-redis-deployment-5d4d9fdfc8-s6vjq   1/1     Running   0          8m5s
oxygen-hw7-worker-deployment-b456596d6-gghzx   1/1     Running   0          5s
oxygen-hw7-worker-deployment-b456596d6-xv5rg   1/1     Running   0          7m28s
py-debug-deployment-5cc8cdd65f-nqppt           1/1     Running   0          8m21s
~~~

Entering the debug pod and executing the following command...
~~~
curl -X POST -H "content-type: application/json" -d '{"start":"START", "end":"END"}' 10.99.66.186:5000/jobs
~~~
... returned the following output:
~~~
{"id": "b548d79d-53ea-4362-9c4d-516f805b5f79", "status": "submitted", "start": "START", "end": "END", "worker": "None"}
~~~

After submitting two jobs, I opened a `python` terminal to see if it worked.

~~~
Python 3.9.2 (default, Feb 19 2021, 17:11:58)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> rd = redis.StrictRedis(host="10.109.252.67", port=6379, db=0)
>>>
>>>
>>> for key in rd.keys():
...     print(rd.hgetall(key))
...
{b'id': b'4df6d7e7-a150-4ef4-8446-138c0f5151cf', b'status': b'complete', b'start': b'START', b'end': b'END', b'worker': b'10.244.12.187'}
{b'id': b'9102c507-89c9-4556-ab1c-c638d1dd2d53', b'status': b'complete', b'start': b'START', b'end': b'END'}
{b'id': b'848e1b59-4793-48c8-b42c-56221863865c', b'status': b'complete', b'start': b'START', b'end': b'END', b'worker': b'10.244.12.187'}
{b'id': b'dfd0313c-6db8-47cc-8255-f8ae17155c4a', b'status': b'complete', b'start': b'START', b'end': b'END'}
{b'id': b'723116ee-577d-4ff5-929d-19b4ea60c0b0', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'61a5593b-0c67-4a1f-83c2-09191400888a', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'd1d18ef7-68ef-47fc-b722-ba1fe6b79d63', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'f2106e3b-86a0-4402-ae46-15242f9de219', b'status': b'complete', b'start': b'START', b'end': b'END'}
{b'id': b'9017bfce-1cf1-46e0-b26b-8b2a3cad1e55', b'status': b'submitted', b'start': b'START', b'end': b'END', b'worker': b'None'}
{b'id': b'7db2604d-2021-47b6-8fab-dda6dfb3bbe0', b'status': b'submitted', b'start': b'START', b'end': b'END', b'worker': b'None'}
{b'id': b'6ad0718e-4961-41cd-8327-4b23c4b56b96', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'd040fa8b-5519-4dc1-a184-c3cfaab69cd1', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'fbaec13f-9b7d-4b31-b2c5-a5474d49db32', b'status': b'in progress', b'start': b'START', b'end': b'END', b'worker': b'10.244.12.187'}
{b'id': b'b548d79d-53ea-4362-9c4d-516f805b5f79', b'status': b'complete', b'start': b'START', b'end': b'END', b'worker': b'10.244.12.187'}
{b'id': b'd2e27c65-7e05-4809-9a34-710d5ada14e4', b'status': b'complete', b'start': b'START', b'end': b'END'}
{b'id': b'460dc091-0ea9-4d5c-ac53-a32b562a79f2', b'status': b'complete', b'start': b'START', b'end': b'END', b'worker': b'10.244.3.190'}
{b'id': b'db5178a3-68f1-44b9-bf3b-d7a7e7302ed2', b'status': b'complete', b'start': b'START', b'end': b'END'}
{b'id': b'ba78dcca-87d5-4d4c-8fed-f54d9d23f772', b'status': b'complete', b'start': b'START', b'end': b'END'}
{b'id': b'fd282a64-1703-4ac4-bd2a-953c4da6cf3b', b'status': b'in progress', b'start': b'START', b'end': b'END', b'worker': b'10.244.3.190'}
{b'id': b'76eab55c-9cb3-4a53-8922-8aea307f8485', b'status': b'complete', b'start': b'START', b'end': b'END', b'worker': b'10.244.3.190'}
{b'id': b'25a4759a-f991-422d-81ce-0f21a4ea362d', b'status': b'submitted', b'start': b'START', b'end': b'END'}
{b'id': b'73fc0f70-c54f-4749-97c0-118a63e581d1', b'status': b'submitted', b'start': b'START', b'end': b'END', b'worker': b'None'}
{b'id': b'dc5fb44e-7eb7-4669-84c3-496ff5e82767', b'status': b'complete', b'start': b'START', b'end': b'END', b'worker': b'10.244.12.187'}

~~~

I never cleared the redis database, so previous jobs remained that don't include the `worker` element in their dictionaries. I could remove previous entries using `rd.flushdb()` but I chose not to so I could see the updated dictionaries more easily. It looks like the two workers split the load 5 to 3 and two other jobs had yet to be updated (as indicated by the 'none' value under the 'worker' key). 