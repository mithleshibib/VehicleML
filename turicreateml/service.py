import turicreate as tc

# Load the model
model = tc.load_model('Model1_sensor_raw/')

print("Load success")

new_data=tc.SFrame({'GyroX':[-0.9236641221374046],'GyroY':[3.6946564885496183],'GyroZ':[0.8244274809160306],'AccX':[0.1625976562],'AccY':[-0.086669921875],'AccZ':[-0.969482421875]})

new_data.export_csv(filename='my_data.csv')

my_data=tc.SFrame.read_csv('my_data.csv')

predictions = model.predict(my_data)
print(predictions)
# You can use the loaded model for predictions or further analysis
# For example, if it's a classifier, you can make predictions on new data
# predictions = model.predict(new_data)

# Make sure to replace 'path_to_model_folder' with the actual path to the folder containing your model files.

