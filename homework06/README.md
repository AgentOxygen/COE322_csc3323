# Homework 6
Cameron Cummins (csc3323)

## Step 1

The yaml file is `oxygen-test-redis-pvc.yml` and the command used was `kubectl apply -f oxygen-test-redis-pvc.yml`
Returning the following:
~~~
persistentvolumeclaim/oxygen-test-pvc created
~~~

## Step 2

The yaml file is `oxygen-test-redis-deployment.yml` and the command used was `kubectl apply -f oxygen-test-redis-deployment.yml`
Returning the following:
~~~
deployment.apps/oxygen-test-redis-deployment created
~~~
## Step 3

The yaml file is `oxygen-test-redis-service.yml` and the command used was `kubectl apply -f oxygen-test-redis-service.yml`
Returning the following:
~~~
service/oxygen-test-redis-service created
~~~

Checking the service using `kubectl get services` returned:
~~~
NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
oxygen-test-redis-service   ClusterIP   10.104.246.169   <none>        6379/TCP   7m34s
~~~

To test that everything has worked so far, I created a python debug container using `development-python-debug.yml` with the command `kubectl apply -f development-python-debug.yml`

Then using the command `kubectl get pods` returned the following:
~~~
NAME                                            READY   STATUS    RESTARTS   AGE
oxygen-test-redis-deployment-685c8689dd-xbvvx   1/1     Running   0          4m8s
py-debug-deployment-5cc8cdd65f-65j54            1/1     Running   0          34s
~~~
To  access the new debug container, I used `kubectl exec -it py-debug-deployment-5cc8cdd65f-ktxr9 -- /bin/bash`
Changing the shell to
~~~
root@py-debug-deployment-5cc8cdd65f-65j54:/#
~~~
I then use the following sequence of commands to install redis, open a python terminal, and test the redis server.
~~~
root@py-debug-deployment-5cc8cdd65f-65j54:/# pip3 install redis
Collecting redis
  Downloading redis-3.5.3-py2.py3-none-any.whl (72 kB)
       |████████████████████████████████| 72 kB 997 kB/s
  Installing collected packages: redis
  Successfully installed redis-3.5.3

root@py-debug-deployment-5cc8cdd65f-65j54:/# python3

Python 3.9.4 (default, Apr 10 2021, 15:31:19)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> rd = redis.StrictRedis(host="10.104.246.169", port=6379)
>>> rd.set('hello', 'world')
True
>>> rd.get('hello')
b'world'
~~~

I was successfully able to set and get a key from the redis server! :)


## Step 4

The yaml file is `oxygen-test-flask-deployment.yml` and the command used was `kubectl apply -f oxygen-test-flask-deployment.yml`
Returning the following:
~~~
deployment.apps/oxygen-test-flask-deployment created
~~~

## Step 5

The yaml file is `oxygen-test-flask-service.yml` and the command used was `kubectl apply -f oxygen-test-flask-service.yml`
Returning the following:
~~~
service/oxygen-test-flask-service created
~~~

To make sure all pods were running properly, I used `kubectl get pods` which returned the following:
~~~
NAME                                            READY   STATUS    RESTARTS   AGE
oxygen-test-flask-deployment-645d84ff67-24cfm   1/1     Running   0          2m37s
oxygen-test-flask-deployment-645d84ff67-qgn4m   1/1     Running   0          2m37s
oxygen-test-redis-deployment-685c8689dd-xbvvx   1/1     Running   0          16m
py-debug-deployment-5cc8cdd65f-65j54            1/1     Running   0          12m
~~~

To view the services, I then used `kubectl get services` which returned the following:
~~~
NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
oxygen-test-flask-service   ClusterIP   10.98.45.182     <none>        5000/TCP   3m19s
oxygen-test-redis-service   ClusterIP   10.104.246.169   <none>        6379/TCP   16m
 ~~~

I then accessed the debug container to see if my flask server was running using the following sequence of commands:
~~~
[oxygen@isp02 data]$ kubectl exec -it py-debug-deployment-5cc8cdd65f-65j54 -- /bin/bash
root@py-debug-deployment-5cc8cdd65f-65j54:/#
root@py-debug-deployment-5cc8cdd65f-65j54:/# curl 10.98.45.182:5000
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
 ~~~
I successfully connected to my flask server! The 404 error is to be expected since I have no routes yet, but a running server nonetheless.
       
