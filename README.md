# [Web App](https://tennis-ml-predictor.onrender.com/)
---
Welcome to the code for my Machine Learning based Tennis Match Predictor.

This repository is aligned with Django's framework. 

The ML_data_and_models directory is independent of Django's framework. This folder holds historic match data, cleans the data, and generates data read of ML models to be created (particularly in the generating_match_history file). Next our three ML models are created/fitted: Random Forest, Logistic Regression, Decision Tree.

Django's base site directory/app is Tennis_ML_Predictor, here we handle the web app functionality and allow users to input matchups between players to simulate using our three ML models.

To clone this repository and use yourselves will require few changes, Django is set to use a local SQLite server which does not need any setting up. Simply set debug to False in settings to deplopy Django locally.




