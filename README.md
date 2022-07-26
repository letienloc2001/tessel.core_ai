# TESSEL.CORE_AI
This repository is the Core AI Tessel Project for Viettel, containing 2 services for auto-training and inference models. 

Two services intergrates mutually by gRPC protocol (currently is HTTP) in 2 different servers.

## How to start project
1- Create env by conda, docker or virtual env.
```bash
cd tessel.core_ai
conda activate tessel.core_ai
```

2- Download some necessary stuffs: [here](https://drive.google.com/drive/folders/1Rd5HVlbnOxxxgZai2BUcIyCAjLpIzoYk?usp=sharing)
```bash
pip install gdown

# Anti-spoofing model
gdown -q "1xWZIAbrXN77KVVsPQvwoZMje7beJp7Ok" --output anti-spoofing-classification.zip
unzip -q anti-spoofing-classification.zip    
rm -f -r __MACOSX anti-spoofing-classification.zip
```
```bash
# Detection models
gdown -q "11p5AIvHp0_I_cu0LWPkfQVAfCvvH2h9P" --output detection.zip
unzip -q detection.zip
rm -f -r __MACOSX detection.zip
```
```bash
# Dataset, configuration file for testing API
gdown -q "10MS39ynZdmACbxIoIFFxtrDd9xmmzHnM" --output test.zip
unzip -q test.zip
rm -f -r __MACOSX test.zip
```
```bash
# Postman .json
gdown -q "1u_D2fXRLPnFtnU_ZZtvA3dfZxqR6VknU" --output postman-collection.zip
unzip -q postman-collection.zip
rm -f -r __MACOSX postman-collection.zip
```
3- Install packages by 
```bash
pip install -r requirements.txt
```
4- Run
```bash
python run.py
```
5- Send request by Postman

