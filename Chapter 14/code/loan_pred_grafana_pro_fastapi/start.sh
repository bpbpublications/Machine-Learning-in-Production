#!/bin/bash

pip install src/
python src/prediction_model/train_pipeline.py
python main.py