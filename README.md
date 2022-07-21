# TESSEL.CORE_AI
This repository is the Core AI Tessel Project for Viettel, containing 2 services for auto-training and inference models. 

Two services intergrates mutually by gRPC protocol (currently is HTTP) in 2 different servers.

## How to start project
1- Create env by conda, docker or virtual env.

2- Install packages by 
```bash
pip install -r requirements.txt
```
3- python run.py (will be configured by flask os env later)
