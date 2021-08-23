# Mask-Up

Hacked together for **Ignite Hacks**, Mask-Up is a web app that determines whether a person is wearing a face mask and applies it to a transit system entry gate (say Delhi Metro's) through a demonstrative simulation. 

## The Problem
Living through the ongoing **COVID-19** pandemic has made us realize how important face masks are for **public health**. While brainstorming for our SpiritHack1.0 idea, we realized that currently, transit systems make use of security personnel to ensure compliance with **COVID-19 protocol**, particularly face masks.

## A Realization, a Solution and Viability!
It then struck us that we can leverage the power of **Computer Vision** and **Machine Learning** to determine whether a person is wearing a mask, and all that without the need for any human involvement! This would not only help protect these personnel, but also potentially help save on human resource costs.  
Further, we also realized that the most viable and optimal solution for this would be to integrate the detection system with the transit system's entry gates, which already act as checkpoints and having already been equipped with a basic computing system, would only require **basic hardware upgrades** to use this solution. The camera system used can be one among the many **CCTV cameras** already in use!

## Constraints, Limitations and Compromises
Since we didn't have the time or the resources to make a functioning hardware implementation, we decided to implement a simulation of sorts within a simple **web app** - Mask-Up! 
Mask-Up **snaps a picture of the user** using their webcam and requires the user's current **transit pass balance**, only allowing an entry event if the person is both **wearing a mask** and their transit pass balance is at least equal to the minimum cost of travel in the transit system. 

## Advantages
The base functionality, implemented in python using the fantastic **Tensorflow** ML library, can **run on low cost hardware** and consumes only minimal resources. It is also **fast enough to be used on a video feed**, being able to determine for each frame, in real time, whether the person in focus is masked!

## Current Limitations and Future Solutions
As for problems, as it stands it's not possible to get results for each frame for the browser based interface due to the limitations for the client-server architecture.

## Installation and Usage
While this simulation is at best for demonstrative purposes, it can easily be installed and used even on low powered machines such as the Raspberry Pi. 
The only pre-requisites are a fairly recent installation of `python3` (v3.6 - v3.8) along with a working installation of `git` (to clone this repository). Given that you have a suitable version of python installed, the following steps should get `mask-up` running on most machines.:

1. `git clone https://github.com/atag-21/mask-up-f.git mask-up`

2. `cd mask-up`

3. `pip install -r requirements.txt`

4. `flask run`  
