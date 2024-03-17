import turicreate as tc
import os
import pandas as pd
import warnings
import catboost as cbt
from catboost import CatBoostClassifier
import mlflow
from io import StringIO
import sys
import re
#import mlflow.turicreate

#def parse_log_output(log_output):
#    metrics = {}
#    for line in log_output.split('\n'):
#        match = re.match(r'\| (\d+) +\| .* \| (\d+\.\d+) +\| (\d+\.\d+) +\| (\d+\.\d+) +\| (\d+\.\d+) +\|', line)
#        if match:
#            iteration = int(match.group(1))
#            training_accuracy = float(match.group(2))
#            validation_accuracy = float(match.group(3))
#            training_log_loss = float(match.group(4))
#            validation_log_loss = float(match.group(5))
#            metrics[iteration] = {
#                'training_accuracy': training_accuracy,
#                'validation_accuracy': validation_accuracy,
#                'training_log_loss': training_log_loss,
#                'validation_log_loss': validation_log_loss
#            }
#    return metrics

def parse_log_output(log_output):
    algorithms = {}
    current_algorithm = None

    for line in log_output.split('\n'):
        if line.startswith("PROGRESS:"):
            if "BoostedTreesClassifier" in line:
                current_algorithm = "BoostedTreesClassifier"
                algorithms[current_algorithm] = {}
            elif "RandomForestClassifier" in line:
                current_algorithm = "RandomForestClassifier"
                algorithms[current_algorithm] = {}
            elif "DecisionTreeClassifier" in line:
                current_algorithm = "DecisionTreeClassifier"
                algorithms[current_algorithm] = {}
            elif "LogisticClassifier" in line:
                current_algorithm = "LogisticClassifier"
                algorithms[current_algorithm] = {}
        elif current_algorithm:
            match = re.match(r'\| (\d+) +\| .* \| (\d+\.\d+) +\| (\d+\.\d+) +\| (\d+\.\d+) +\| (\d+\.\d+) +\|', line)
            if match:
                iteration = int(match.group(1))
                training_accuracy = float(match.group(2))
                validation_accuracy = float(match.group(3))
                training_log_loss = float(match.group(4))
                validation_log_loss = float(match.group(5))
                algorithms[current_algorithm][iteration] = {
                    'training_accuracy': training_accuracy,
                    'validation_accuracy': validation_accuracy,
                    'training_log_loss': training_log_loss,
                    'validation_log_loss': validation_log_loss
                }

    return algorithms

warnings.filterwarnings("ignore")

data=tc.SFrame.read_csv("sensor_raw.csv")
data=data.shuffle()
data_train,data_test=tc.SFrame.random_split(data,0.7)
data_test1, data_validation=tc.SFrame.random_split(data_test,0.5)
stdout = sys.stdout
sys.stdout = StringIO()

model=tc.classifier.create(data,target='Target(Class)',validation_set=data_test1)

log_output = sys.stdout.getvalue()

model.save("Model1_sensor_raw")
#bento_model = bentoml.catboost.save_model("catboost_Sensor_raw", model)

#model1 = tc.load_model('Model1_sensor_raw')
#metrics = parse_log_output(log_output)
algorithms = parse_log_output(log_output)
sys.stdout = stdout

print("save success")
model = tc.load_model('Model1_sensor_raw')
print('tc_model loaded successfully')

learning_rate = 0.001
num_epochs = 10

with mlflow.start_run():
    # Log your model to MLflow
    #mlflow.turicreate.log_model(model, "model")
    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("num_epochs", num_epochs)
    #for iteration, metric_values in metrics.items():
    #    mlflow.log_metrics(metric_values)
    for algorithm, metrics in algorithms.items():
        for iteration, metric_values in metrics.items():
            mlflow.log_metrics(metric_values, prefix=f"{algorithm}_{iteration}")
    mlflow.log_artifacts('Model1_sensor_raw', artifact_path='models')


#path="Features_By_Window_Size/"
#filename=os.listdir(path)
#for i in (filename):
#    data=tc.SFrame.read_csv(path+i,verbose=False)
#    data=data.shuffle()
#    data_train,data_test=tc.SFrame.random_split(data,0.7)
#    data_test1, data_validation=tc.SFrame.random_split(data_test,0.5)
#    model=tc.classifier.create(data,target='Target',validation_set=data_test1,verbose=False)
#    model.save("Features_By_Window_Size_Model/Model1_"+i)
#    bento_model = bentoml.catboost.save_model("Features_By_Window_Size_Catboost_Model/catboost_Model1_"+i, model)
#    with open("ModelDetails.txt","a") as file:
#        file.write("\n\n")
#        file.write("#####################################################\n\n")
#        file.write(i+"\n\n")
#        file.write(model.summary(output="str"))
