# end to end ml project
# https://dagshub.com/harshitpurohit953/ml_project.mlflow

MLFLOW_TRACKING_USERNAME=harshitpurohit953
import dagshub
dagshub.init(repo_owner='harshitpurohit953', repo_name='ml_project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


  MLflow Tracking URI
https://dagshub.com/harshitpurohit953/ml_project.mlflow