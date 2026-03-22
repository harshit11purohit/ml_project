import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

PROJECT_NAME="ML_PROJECT"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/data_ingestion.py",
    f"src/{PROJECT_NAME}/components/data_transformation.py",
    f"src/{PROJECT_NAME}/components/model_training.py",
    f"src/{PROJECT_NAME}/components/model_training.py",
    f"src/{PROJECT_NAME}/components/model_monitoring.py",
    f"src/{PROJECT_NAME}/pipelines/__init__.py",
    f"src/{PROJECT_NAME}/pipelines/training_pipeline.py",
    f"src/{PROJECT_NAME}/pipelines/prediction_pipeline.py",
    f"src/{PROJECT_NAME}/utils.py",
    f"src/{PROJECT_NAME}/exception.py",
    f"src/{PROJECT_NAME}/logger.py",
    "main.py",
    "app.py",
    "dockerfile",
    "requirements.py",           
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # Create the folder (but don't crash if it already exists).
        logging.info(f"Creating directory:{filedir} for the file {filename}")


    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:  # Create/Reset the file to be a blank slate for your code.
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
        # If the file already exists and has actual code inside it, do nothing.
        
        
#__init__.py as the "Entry Permit" for a folder. Without this file,
# Python just sees a folder full of text; with it, Python sees an Official Package
# STEP 1: Define the list of files and folders needed for a Professional ML structure.
# STEP 2: Loop through each path and split it into "Folder Name" and "File Name".
# STEP 3: If a folder is mentioned, create it (but only if it's not already there).
# STEP 4: Create the file ONLY if it is missing or empty (this prevents deleting your code).
# STEP 5: Log every action so the developer can see exactly what was built or skipped.