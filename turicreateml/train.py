import turicreate as tc
import os
import pandas as pd
import bentoml
import warnings
import catboost as cbt
from catboost import CatBoostClassifier

warnings.filterwarnings("ignore")

data=tc.SFrame.read_csv("sensor_raw.csv")
data=data.shuffle()
data_train,data_test=tc.SFrame.random_split(data,0.7)
data_test1, data_validation=tc.SFrame.random_split(data_test,0.5)

model=tc.classifier.create(data,target='Target(Class)',validation_set=data_test1)

#model = cbt.CatBoostClassifier(
#    iterations=2,
#    depth=2,
#    learning_rate=1,
#    loss_function="Logloss",
#    verbose=False,
#)
#X=data.drop("Target(Class)", axis=1)
#X= X.to_dataframe()
#Y= data_train.iloc[:,0]
#Y=pd.DataFrame(data_train['Target(Class)'])
#Y=data_train[["Target(Class)"]]
#Z=Y.to_dataframe()
#model.fit(X,Y)
#bento_model = bentoml.catboost.save_model("catboost_Sensor_raw", model)


model.save("Model1_sensor_raw")
#bento_model = bentoml.catboost.save_model("catboost_Sensor_raw", model)

#model1 = tc.load_model('Model1_sensor_raw')


print("save success")

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
