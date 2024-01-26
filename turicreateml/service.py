import turicreate as tc

# Load the model
model = tc.load_model('Model1_sensor_raw/')

print("Load success")

new_data=tc.SFrame({'GyroX':[-0.9236641221374046],'GyroY':[3.6946564885496183],'GyroZ':[0.8244274809160306],'AccX':[0.1625976562],'AccY':[-0.086669921875],'AccZ':[-0.969482421875]})

new_data.export_csv(filename='my_data.csv')

my_data=tc.SFrame.read_csv('my_data.csv')

predictions = model.predict(my_data)
print(predictions)


from flask import Flask, request, jsonify, render_template
import turicreate as tc

app = Flask(__name__)

# Load the Turi Create model
model_path = "Model1_sensor_raw/"
model = tc.load_model(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.json
        input_data = tc.SFrame(data['features'])

        # Make predictions using the Turi Create model
        predictions = model.predict(input_data)

        # Convert the predictions to a list and return as JSON
        response_data = {'predictions': predictions.tolist()}
        
        print('Response:', response_data)  # Log the response data
        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)




# You can use the loaded model for predictions or further analysis
# For example, if it's a classifier, you can make predictions on new data
# predictions = model.predict(new_data)

# Make sure to replace 'path_to_model_folder' with the actual path to the folder containing your model files.

