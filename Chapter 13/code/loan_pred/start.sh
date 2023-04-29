#!/bin/bash

pip install app/src/
python app/src/prediction_model/train_pipeline.py
python app/main.py