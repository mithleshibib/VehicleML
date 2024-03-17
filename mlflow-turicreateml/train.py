import turicreate as tc
import os
import pandas as pd
import warnings
import catboost as cbt
from catboost import CatBoostClassifier

warnings.filterwarnings("ignore")

data=tc.SFrame.read_csv("sensor_raw.csv")
data=data.shuffle()
data_train,data_test=tc.SFrame.random_split(data,0.7)
data_test1, data_validation=tc.SFrame.random_split(data_test,0.5)

model=tc.classifier.create(data,target='Target(Class)',validation_set=data_test1)

model.save("Model1_sensor_raw")


