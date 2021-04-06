# Part A:
<br>
	1. The yaml file is `partA-pod.yml` and the command used was `kubectl -f apply partA-pod.yml`
<br>
	2. Using the command `kubectl get pods --selector "greeting"` outputs the following:
> <br> ```
>    NAME    READY   STATUS    RESTARTS   AGE
>    hello   1/1     Running   0          5m10s
> ```
<br>
	3. Using the commande `kubectl logs hello` returns the output `Hello, !`
<br>
	4. I deleted the pod using `kubectl delete pods hello`
<br>

# Part B:
<br>
	1. The yaml file is `partB-pod.yml` and the command used was `kubectl -f apply partB-pod.yml`
<br>
	2. Using the command `kubectl get pods --selector "greeting"` outputs the following:
> <br> ```
> NAME    READY   STATUS    RESTARTS   AGE
> <br>
> hello   1/1     Running   0          3m22s
> ```
<br>
	3. Using the commande `kubectl logs hello` returns the output `Hello, Cameron!`
<br>
	4. I deleted the pod using `kubectl delete pods hello`
<br>

# Part C:
<br>
	1. The yaml file is `partC-deployment.yml` and the command used was `kubectl -f apply partC-deployment.yml`
<br>
	2. Using `kubectl get pods -o wide` outputs the following:

> <br> ```
> 	NAME                                  READY   STATUS    RESTARTS   AGE     IP             NODE   NOMINATED NODE   READINESS GATES
> <br>
> 	hello-deployment-55f4459bf-xmmtr      1/1     Running   143        5d23h   10.244.4.99    c02    <none>           <none>
> <br>
> 	hello-pvc-deployment-65d77855-dg9td   1/1     Running   168        7d      10.244.5.35    c04    <none>           <none>
> <br>
> 	part-c-deployment-674477dcf9-7jks9    1/1     Running   0          5m10s   10.244.5.90    c04    <none>           <none>
> <br>
> 	part-c-deployment-674477dcf9-l6cbk    1/1     Running   0          5m10s   10.244.4.124   c02    <none>           <none>
> <br>
> 	part-c-deployment-674477dcf9-q7kq4    1/1     Running   0          5m10s   10.244.3.60    c01    <none>           <none>
> ```
<br>
	3. Using `kubectl logs --selector "greeting"` outputs the following:

> <br> ```
> 	Hello, Cameron from IP 10.244.5.90
> <br>
> 	Hello, Cameron from IP 10.244.4.124
> <br>
> 	Hello, Cameron from IP 10.244.3.60
> ```
<br>
	This is consistent with output detailed in question 2 (looking at the last three pods)