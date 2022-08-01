![](https://siddhi.io/images/siddhi-logo.svg)
# siddhi-python
This repository is a production-ready Siddhi (stream processing and complex event processing system) dockerized and ready
to be utilized with its Python client.

Siddhi is a fully open source, cloud native, scalable, micro streaming, and complex event processing system capable of
building event-driven applications for use cases such as real-time analytics, data integration, notification management,
and adaptive decision-making. Using this repository, you would have a ready to use Siddhi client that works perfectly
with its official Python library. Therefore, there is no need to do any adjustment and configuration manually,
just build and run the provided dockerized implementation.

__What is the difference with the official Pysiddhi Library?__  
Pysiddhi is the official library for Siddhi in Python, but needs lots of configuration to have a successful connection 
with the core of Siddhi. Using this repo Pysiddhi connects to the core of Siddhi without any further 
configuration. 

A trivial sample of how to send and process messages has been added to the main.py module.
This is the sample provided by Siddhi's official documentation, so adjust it by your usecase.

After running the application, you would be able to communicate with it, using gRPC, message broker or any other 
communication tool.