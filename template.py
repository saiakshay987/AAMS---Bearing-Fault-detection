import os
from pathlib import Path
import logging

# Set up logging to output progress to the terminal
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define your core package name
package_name = "fault_detection"

list_of_files = [
    # CI/CD Pipeline configuration
    ".github/workflows/.gitkeep",
    
    # Data schemas and exploratory sandbox
    "data_schema/schema.yaml",
    "notebooks/eda_sandbox.ipynb",
    
    # Core Source Package
    f"{package_name}/__init__.py",
    f"{package_name}/cloud/__init__.py",
    
    # ML Lifecycle Components
    f"{package_name}/components/__init__.py",
    f"{package_name}/components/data_ingestion.py",
    f"{package_name}/components/data_validation.py",
    f"{package_name}/components/data_transformation.py",
    f"{package_name}/components/model_trainer.py",
    
    # Constants & Configurations
    f"{package_name}/constant/__init__.py",
    f"{package_name}/constant/training_pipeline/__init__.py",
    
    # Input/Output Definitions (Entities)
    f"{package_name}/entity/__init__.py",
    f"{package_name}/entity/config_entity.py",
    f"{package_name}/entity/artifact_entity.py",
    
    # Custom Error Handling & Tracking
    f"{package_name}/exception/__init__.py",
    f"{package_name}/exception/exception.py",
    f"{package_name}/logging/__init__.py",
    f"{package_name}/logging/logger.py",
    
    # Execution Pipelines
    f"{package_name}/pipeline/__init__.py",
    f"{package_name}/pipeline/training_pipeline.py",
    f"{package_name}/pipeline/batch_prediction.py",
    
    # Helper Utilities
    f"{package_name}/utils/__init__.py",
    f"{package_name}/utils/common.py",
    
    # Root Level Configuration & Orchestration Files
    "Dockerfile",
    ".dockerignore",
    ".env",
    ".gitignore",
    "requirements.txt",
    "setup.py",
    "main.py",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")
        
    # Create empty files if they don't exist or are empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists.")