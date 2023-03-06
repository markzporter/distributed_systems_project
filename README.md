This is a project for the Distributed Systems 2023 course at the University of Oulu.

**What is it?**
The goal of this project is RSA codebreaking for reasonably sized input. Given a RSA number N, we'd like to find it's factors 
such that we could break a code that is encoded using it. We do this by creating a system which runs a distributed version of the [Quadratic Sieve](https://en.wikipedia.org/wiki/Quadratic_sieve) method for factoring large primes. 

## How to run it

There is a Makefile in this directory. You need Docker v20.10.6 or greater in order to run it. `make up` should build and run the project. If you wish to make changes and restart you can run `make recompose`. To stop, you can run `make down`. You can also change the number of workers by updating the `--scale` parameter in the Makefile. 

## How to use it 

There is a simple frontend for this application in the `/front/index.html` file. This can be opened in your browser. You can generate new example input here: https://bigprimes.org/RSA-challenge. You can also verify that the primes we found are correct here 🤠.  Alternatively, the API can be accessed directly at 0.0.0.0:5000/api/factorize/<Integer to factorize>. 

## Observability

This project has some observability options. You can see some metrics on the processes at `0.0.0.0:8889` where a [Flower](https://flower.readthedocs.io/en/latest/index.html) app is running. You should also be able to see rainbow logs from your `make up` command for all the containers.  

## Architecture 

<img width="729" alt="architecture_diagram" src="https://user-images.githubusercontent.com/15064171/223143558-61ddc076-e11e-479c-8855-bc9014118a86.png">

In this diagram you can see the main flow of the application. 
