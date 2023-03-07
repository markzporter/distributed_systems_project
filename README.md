This is a project for the Distributed Systems 2023 course at the University of Oulu.

**What is it?**
The goal of this project is RSA codebreaking for reasonably sized input. Given a RSA number N, we'd like to find it's factors 
such that we could break a code that is encoded using it. We do this by creating a system which runs a distributed version of the [Quadratic Sieve](https://en.wikipedia.org/wiki/Quadratic_sieve) method for factoring large primes. 

## How to run it

There is a Makefile in this directory. You need Docker v20.10.6 or greater in order to run it. `make up` should build and run the project. If you wish to make changes and restart you can run `make recompose`. To stop, you can run `make down`. You can also change the number of workers by updating the `--scale` parameter in the Makefile. 

## How to use it 

There is a simple frontend for this application in the `/front/index.html` file. This can be opened in your browser. You can generate new example input here: https://bigprimes.org/RSA-challenge. You can also verify that the primes we found are correct here 🤠.  Alternatively, the API can be accessed directly at 0.0.0.0:5000/api/factorize/<Integer to factorize>. 

## Observability

This project has some observability options. You can see some metrics on the processes at `0.0.0.0:8889` where a [Flower](https://flower.readthedocs.io/en/latest/index.html) app is running. You should also be able to see docker compose rainbow logs from your `make up` command for all the containers.  

## Architecture 

<img width="729" alt="architecture_diagram" src="https://user-images.githubusercontent.com/15064171/223143558-61ddc076-e11e-479c-8855-bc9014118a86.png">

In this diagram you can see the main flow of the application. Our user input comes from a simple HTML frontend. It makes an HTTP request to our main node which is responsible for coordinating the work associated with factoring the integer provided. The main node queues up work in our RabbitMQ worker queue which is a Celery task queue. The workers are each Celery worker nodes which pull tasks off of the queue and place the result in a Redis database. The main node then collects these results and does some further calculations with the aggregated results. The result is then returned in the same original HTTP request. 

## Distributed Algorithm
  
A bit of explanation on the distributed nature of this problem. The Quadratic Sieve algorithm lends itself well to parallelization and we attempt to take advantage of this in this system by distributing the independent work across multiple nodes. The idea being that this could potentially scale and result in faster performance. We distribute the work in two different places where there is often a bottleneck and also where there is clearly independent work. 

  
![image](https://user-images.githubusercontent.com/15064171/223447783-1bdf83e6-6867-4375-bc3c-9d390c9013a8.png)

In both the factor base discovery and the B-smooth searching, we dole out the parallel work to our workers so that it may be completed concurrently. 

## Technologies used
  
 - We used Docker and docker compose for our container and orchestration layer. These tools are familiar and well suited to this sort of standalone toy project. 
 - We used [Celery](https://docs.celeryq.dev/en/stable/) for our distributed task queue. This is because it's scalable and quick to set up a main node with a worker queue. Our workflow is quite simple so mostly we wanted something that would be straightforward to implement.
- We used [Redis](https://redis.io/) as our backend for the task result queue. Redis is highly scalable and fast database which really should have no performance bottlenecks at our scale. 
- We used [RabbitMQ](https://www.rabbitmq.com/) as our MQTT message broker since MQTT is the supported protocol in Celery and Rabbit is a well-known broker for this protocol.
- We used Flask for our HTTP API since it is a standard and simple way to create HTTP servers in Python. 
- 
