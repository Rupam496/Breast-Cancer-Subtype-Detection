# Breast Cancer Subtype Prediction

A machine learning web application for predicting **breast cancer molecular subtypes** from gene-expression data. The project uses a trained machine learning model exposed through a **FastAPI backend** and a **Streamlit frontend**.

> **Disclaimer:** This project is intended for educational and research purposes only. It is not a medical diagnostic tool and should not be used for clinical decision-making.

## 🚀 Features

* Breast cancer multiclass subtype prediction
* High-dimensional gene-expression data processing
* Feature selection and preprocessing
* Machine learning-based classification
* FastAPI REST API for prediction
* Streamlit-based interactive user interface
* Model deployment support with Render

## 🧬 Predicted Subtypes

The model performs multiclass classification of breast cancer into the following molecular subtypes:

* **Luminal A (LumA)**
* **Luminal B (LumB)**
* **Basal**
* **HER2-enriched (Her2)**
* **Normal-like (Normal)**

## 🏗️ Project Architecture

```text
                         User
                           │
                           ▼
                    Streamlit Frontend
                           │
                           │ HTTP Request
                           ▼
                     FastAPI Backend
                           │
                           ▼
                  Preprocessing Pipeline
                           │
                           ▼
                  Trained ML Model
                           │
                           ▼
                    Prediction Result
                           │
                           ▼
                    Streamlit UI
```

## 📁 Project Structure

```text
Breast-Cancer-Subtype-Detection/
│
├── app.py                  # FastAPI application
├── frontend.py             # Streamlit frontend
├── model.pkl               # Trained machine learning model
├── requirements.txt        # Python dependencies
├── start.sh                # Startup script for deployment
├── README.md               # Project documentation
└── ...
```

> The exact file names may differ depending on the final project structure.

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* NumPy
* Pandas
* Scikit-learn
* Joblib / Pickle

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Deployment

* Render

## 📊 Dataset

The project uses a high-dimensional breast cancer gene-expression dataset containing thousands of genomic features.

The classification task is challenging because the dataset has:

* A very large number of features
* A relatively small number of samples
* Multiple target classes
* Class imbalance

Example class distribution used during development:

| Subtype | Samples |
| ------- | ------: |
| LumA    |     111 |
| LumB    |      51 |
| Basal   |      36 |
| Normal  |      35 |
| Her2    |      15 |

Because the number of features is much larger than the number of samples, dimensionality reduction and feature selection are important parts of the machine learning pipeline.

## 🔬 Machine Learning Pipeline

The general workflow is:

```text
Raw Gene Expression Data
          │
          ▼
     Data Cleaning
          │
          ▼
   Train/Test Split
          │
          ▼
   Feature Selection
          │
          ▼
    Preprocessing
          │
          ▼
   Model Training
          │
          ▼
   Model Evaluation
          │
          ▼
     Model Saving
          │
          ▼
 FastAPI + Streamlit
```

Feature selection is particularly important because directly working with the complete high-dimensional feature space can require substantial memory and computational resources.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Rupam496/Breast-Cancer-Subtype-Detection.git
```

Move into the project directory:

```bash
cd Breast-Cancer-Subtype-Detection
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application Locally

### Start the FastAPI Backend

Run:

```bash
uvicorn app:app --host 127.0.0.1 --port 8000
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI also provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

### Start the Streamlit Frontend

In another terminal:

```bash
streamlit run frontend.py
```

Streamlit will provide a local URL, typically:

```text
http://localhost:8501
```

The Streamlit application communicates with the FastAPI backend to obtain predictions.

## 🌐 Running Both Together

For local development, the backend and frontend can be started separately.

For a single-service deployment, the project can use a startup script such as:

```bash
#!/bin/bash

uvicorn app:app --host 127.0.0.1 --port 8000 &
streamlit run frontend.py --server.address 0.0.0.0 --server.port $PORT
```

The corresponding Render start command is:

```bash
bash start.sh
```

## ☁️ Deployment on Render

The application can be deployed as a single Render Web Service.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
bash start.sh
```

Render provides the `$PORT` environment variable, which is used by Streamlit as the publicly accessible port.

The FastAPI backend runs internally on port `8000`.

```text
                    Render
                       │
                 Public $PORT
                       │
                       ▼
                  Streamlit
                       │
                localhost:8000
                       │
                       ▼
                   FastAPI
                       │
                       ▼
                  ML Model
```

## 🔌 API

The FastAPI backend exposes an endpoint for making predictions.

Example request:

```text
POST /predict
```

The exact request format depends on the features expected by the trained model.

FastAPI's interactive documentation can be accessed through:

```text
/docs
```

when the backend is running.

## 📈 Model Evaluation

The model should be evaluated using metrics appropriate for multiclass classification, such as:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

For an imbalanced dataset, **macro-averaged precision, recall, and F1-score** can provide a more informative evaluation than accuracy alone.

## ⚠️ Limitations

This project has several limitations:

1. The dataset contains a very high number of features relative to the number of samples.
2. The target classes are imbalanced.
3. Model performance depends heavily on preprocessing and feature selection.
4. Predictions are based on the dataset and trained model and may not generalize to clinical data.
5. The application has not been validated for clinical use.

## 🔮 Future Improvements

Possible future improvements include:

* More robust feature-selection techniques
* Hyperparameter optimization
* Ensemble learning
* Deep learning approaches
* Explainable AI techniques such as SHAP
* Improved handling of class imbalance
* Cross-validation and external validation
* Model monitoring after deployment
* Improved frontend visualization
* Containerized deployment using Docker

## 👨‍💻 Author

**Rupam Das**

M.Sc. in Data Science and Artificial Intelligence
Ramakrishna Mission Vivekananda Educational and Research Institute (RKMVERI)

## 📜 License

This project is intended for educational and research purposes. Add an appropriate open-source license to the repository if you intend to distribute the code publicly.
