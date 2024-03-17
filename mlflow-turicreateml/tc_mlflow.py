import mlflow
import re
import subprocess

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

result=subprocess.run(["python3", "train.py"], check=True, stdout=subprocess.PIPE)
#print(result)
log_output = result.stdout.decode()
#print(log_output)
algorithms = parse_log_output(log_output)
print(algorithms)
with mlflow.start_run():
    for algorithm, metrics in algorithms.items():
        for iteration, metric_values in metrics.items():
            mlflow.log_metrics(metric_values, prefix=f"{algorithm}_{iteration}")
    mlflow.log_artifacts('Model1_sensor_raw', artifact_path='models')
