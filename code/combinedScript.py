#model1
import turicreate as tc
import os

#path= os.getcwd() + '/'

data=tc.SFrame.read_csv("sensor_raw.csv")
data
data.show()
data=data.shuffle()
data_train,data_test=tc.SFrame.random_split(data,0.7)
data_test1, data_validation=tc.SFrame.random_split(data_test,0.5)

model=tc.classifier.create(data,target='Target(Class)',validation_set=data_test1)

result=model.predict(data_validation)
right=0
wrong=0
for i in range(len(result)):
    if result[i]==data_validation['Target(Class)'][i]:
        right+=1
    else:
        wrong+=1
print("Right=",right)
print("Wrong=",wrong)

path="/home/ubuntu/VehicleML/code/MendeleyData/Features By Window Size/"
filename=os.listdir(path)
for i in (filename):
    data=tc.SFrame.read_csv(path+i,verbose=False)
    data=data.shuffle()
    data_train,data_test=tc.SFrame.random_split(data,0.7)
    data_test1, data_validation=tc.SFrame.random_split(data_test,0.5)
    model=tc.classifier.create(data,target='Target',validation_set=data_test1,verbose=False)
    model.save("Features By Window Size Model/Model1_"+i)
    with open("ModelDetails.txt","a") as file:
        file.write("\n\n")
        file.write("#####################################################\n\n")
        file.write(i+"\n\n")
        file.write(model.summary(output="str"))
    
#tc.visualization.columnwise_summary(data)

#model2
import pandas as pd 
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from  sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,f1_score
from catboost import CatBoostClassifier

df= pd.read_csv("sensor_raw.csv")
df_train,df_test= train_test_split(df,random_state=2021,test_size=0.2)
df_train
df_test

df_train['Target(Class)'].value_counts(),df_test['Target(Class)'].value_counts()

df_test.to_csv("test.csv",index=False)
df_train.to_csv("train.csv",index=False)

X_train = df_train.iloc[:,1:]
y_train = df_train.iloc[:,:1]

X_test = df_test.iloc[:,1:]
y_test = df_test.iloc[:,:1]

#normalizing
scaler=MinMaxScaler(feature_range=(-1,1))

X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

#random forest
rfc= RandomForestClassifier()
rfc.fit(X_train_scaled,y_train)
y_pred=rfc.predict(X_test_scaled)

print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

filename = 'random_forest.sav'
pickle.dump(rfc, open(filename, 'wb'))

rfc.get_params()

#catboost 

cfc = CatBoostClassifier(learning_rate=0.1,
                         iterations=5000
                        )
cfc.fit(X_train_scaled,y_train)

y_pred=cfc.predict(X_test_scaled)

print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

cfc.get_all_params()

filename = 'catboost_classifier.sav'
pickle.dump(rfc, open(filename, 'wb'))

#model3
data=tc.SFrame.read_csv("crash1.csv",column_type_hints=[str]*78+[int])
data2=tc.SFrame.read_csv("nearcrash1.csv",column_type_hints=[str]*78+[int])
data=data.append(data2)

data.export_csv("CompleteData.csv")

data=data.shuffle()
data_train,data_test=tc.SFrame.random_split(data,0.7)
data_test1, data_validation=tc.SFrame.random_split(data_test,0.5)

model=tc.classifier.create(data,target='Targets',validation_set=data_test1)

result=model.predict(data_validation)
right=0
wrong=0
for i in range(len(result)):
    if result[i]==data_validation['Targets'][i]:
        right+=1
    else:
        wrong+=1
print("Right=",right)
print("Wrong=",wrong)

model.save("Model3")