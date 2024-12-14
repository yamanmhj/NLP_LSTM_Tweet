




### Modular NLP Pipeline

Welcome to my first NLP project! This repository demonstrates a **modular NLP pipeline** built in Python. It is designed to orchestrate the complete workflow from data extraction to training and evaluation, while offering flexibility to adjust hyperparameters using YAML configuration files.

---

## Features

- **Sklearn Pipeline**: Orchestrates the entire process from data extraction to training to evaluation.
- **Hyperparameter Tuning**: Easily configure and experiment with hyperparameters via YAML files.
- **Custom Exception Handling**: Robust error management ensures smooth execution and helpful debugging.
- **Logging**: Comprehensive logging for easy tracking of pipeline progress.

---

## Project Structure

```
project_root/
|-- Load_data_here# Main entry point to trigger the pipeline
|   |-- artifacts # save trained models.h5 and tokernizers.pkl
|   |-- Loaded_dataset    # original datset
|   |-- Training_dataset # split dataset after pre processing
|   |-- Transformed_dataset.py    # transformed and preprocessed data
|-- components/
|   |-- data_ingestion.py # Handles data loading and preprocessing
|   |-- data_transformatioin.py    # Orchestrates the sklearn pipeline
|   |-- model_evaluation.py # Evaluates model performance
|   |-- model_training.py # Handles data loading and preprocessing
|   |-- select_model.py    # Orchestrates the sklearn pipeline
|-- pipeline/
|   |-- train_pipeline       # we have a pipeline to orcestrate the flow of this project
|-- config/
|   |-- config.yaml         # YAML file for hyperparameter configuration
|   |-- exception.py        # Custom exception handling
|   |-- logger.py           # Logging utility
```

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- Required Python libraries listed in `requirements.txt`

### Installation



2. Install dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Update `config.yaml` to specify the hyperparameters for your experiment.

---

## Usage

1. **Trigger the pipeline**:
   Run the `train_pipeline.py` file to start the pipeline:


2. **Modify Hyperparameters**:
   Adjust settings in `config/config.yaml` to fine-tune the model.

3. **Logs and Artifacts**:

   - Logs are stored in the `logs/` folder for debugging and tracking.
   - Processed data and trained model artifacts are saved in the `artifacts/` folder.

---

## Modules Overview

### Data Extraction

- Reads raw data fromcsv or cloud storage.

### NLP Pipeline

- Utilizes an sklearn pipeline to manage feature extraction, model training, and evaluation seamlessly.
- Includes steps like vectorization, tokenization, and classification.

### Model Evaluation

- Computes metrics such as accuracy, precision, recall, and F1-score.
- Provides insights into model performance.

### Exception Handling

- Custom `Exception` class ensures meaningful error messages for smooth debugging.

---

## Configuration

Edit the `config/params.yaml` file to customize the pipeline. Example:




## Requirements

The `requirements.txt` file includes the following dependencies:

```
numpy
pandas
tensorflow
matplotlib
seaborn
nltk
regex
scikit-learn
from-root
google-cloud-storage
fastapi
uvicorn
Jinja2
setuptools
-e .
```

Install all requirements using:

```bash
pip install -r requirements.txt
```

---

