🛡️ Improved Hybrid Algorithm for IoT Cyber Attack Detection

An improved hybrid machine learning and deep learning approach for detecting and classifying cyber attacks in IoT environments.

The project provides a desktop-based application for loading IoT network datasets, preprocessing data, extracting important features, training detection models, identifying attack types, and comparing model performance.

📌 Project Overview

The increasing number of IoT devices has created a larger attack surface for cyber threats. IoT networks can be targeted by different types of attacks, including malicious response injection, command injection, malicious function code injection, and Denial-of-Service attacks.

This project implements a hybrid cyber-attack detection approach that combines:

- Data preprocessing and normalization
- Autoencoder-based feature extraction
- Principal Component Analysis (PCA)
- Decision Tree classification
- CNN-LSTM based attack detection
- Attack-type identification
- Performance comparison using classification metrics

The project is implemented as a Python desktop application using a Tkinter-based graphical user interface.

🎯 Objectives

The main objectives of the project are:

- Detect cyber attacks in IoT environments
- Preprocess and normalize IoT network traffic data
- Extract important features using an Autoencoder
- Reduce feature dimensionality using PCA
- Classify attack categories using machine learning
- Apply CNN-LSTM based deep learning for attack detection
- Compare the performance of different detection approaches
- Provide a simple graphical interface for performing the detection process


## 🏗️ System Workflow

                    IoT Dataset
                         │
                         ▼
                ┌─────────────────┐
                │ Dataset Loading │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Preprocessing   │
                │ & Normalization │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Autoencoder   │
                │ Feature         │
                │ Extraction      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │       PCA       │
                │ Dimensionality  │
                │ Reduction       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Decision Tree   │
                │ Classification  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   CNN-LSTM      │
                │ Attack Detection│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Attack Type     │
                │ Detection       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Model Performance│
                │ Comparison       │
                └─────────────────┘


🧠 Detection Approach
1. Dataset Loading
The application allows the user to select an IoT dataset through the graphical interface.
The project includes:
Dataset/
├── iot_dataset.csv
└── testData.csv
The dataset contains IoT traffic records and attack classifications.

2. Data Preprocessing
Before model training, the dataset is processed by:
- Handling missing values
- Separating input features and labels
- Shuffling records
- Applying Min-Max normalization
- Converting class labels into categorical representation
- Splitting the data into training and testing sets
The application also stores the scaler used during preprocessing.

3. Autoencoder
An Autoencoder is used to learn a representation of the input data and extract important features.
The implementation uses a neural network architecture with an encoding layer and decoding layer.
The extracted representation is subsequently used for further classification.

4. PCA
Principal Component Analysis (PCA) is applied to the extracted features to reduce dimensionality.
The reduced feature representation is then used by the Decision Tree classifier.

5. Decision Tree
A Decision Tree classifier is trained using the features extracted from the Autoencoder and reduced using PCA.
The Decision Tree is used to classify the IoT traffic and support attack-type prediction.

6. CNN-LSTM
The project also implements an LSTM-based deep learning model for attack detection.
The extracted feature representation is reshaped into a sequential format and processed using an LSTM network.
The model contains:
- LSTM layer
- Dropout layer
- Dense layer
- Output layer with softmax activation
The trained model can be stored and reused from the model/ directory.

🚨 Attack Categories
The project works with the following attack categories:
Category	Description
Normal	Normal IoT network activity
NMRI	Naive Malicious Response Injection
Malicious	Malicious activity
CMRI	Complex Malicious Response Injection
MSCI	Malicious State Command Injection
MPCI	Malicious Parameter Command Injection
MFCI	Malicious Function Code Injection
DoS	Denial-of-Service attack


📊 Dataset Distribution
The project dataset contains multiple categories of IoT traffic and cyber attacks.
The application generates a visualization showing the distribution of different attack categories.

📈 Model Performance
The project evaluates the detection models using:
- Accuracy
- Precision
- Recall
- F1 Score
The implemented models include:
- Autoencoder
- Decision Tree with PCA
- CNN-LSTM
The recorded results from the project execution demonstrate that the CNN-LSTM approach achieved the strongest overall performance among the evaluated models.
Performance Comparison

📊 Example Results
Autoencoder
The project execution produced the following recorded results:
- Accuracy: approximately 89.94%
- Precision: approximately 73.46%
- Recall: approximately 74.54%
- F1 Score: approximately 73.94%

Decision Tree with PCA
The Decision Tree trained on the features extracted from the Autoencoder produced:
- Accuracy: approximately 90.46%
- Precision: approximately 73.30%
- Recall: approximately 74.63%
- F1 Score: approximately 73.92%

CNN-LSTM
The CNN-LSTM implementation produced the strongest recorded performance among the evaluated approaches.

🖥️ Application Interface
The project provides a graphical interface through which the user can perform the major stages of the detection workflow.
Available operations include:
- Upload IoT Dataset
- Preprocess Dataset
- Run AutoEncoder Algorithm
- Run Decision Tree with PCA
- Run CNN-LSTM Algorithm
- Detection of Attack Type
- Comparison Graph
- Comparison Table

🔬 Project Execution Screenshots
Dataset Loaded
The application displays the selected dataset and sample dataset records.

Dataset Preprocessing
The dataset is normalized before being passed to the machine learning and deep learning models.

Autoencoder Results
The Autoencoder performance metrics are displayed through the application.

Decision Tree with PCA
The extracted features are reduced using PCA and classified using a Decision Tree.

CNN-LSTM Results
The CNN-LSTM model is evaluated for attack detection.

Model Comparison
The application provides a comparison of the evaluated models.

Attack Detection
The application provides an interface for detecting attack types from IoT data.

🛠️ Technologies Used
Programming Language
- Python
Machine Learning
- Scikit-learn
- Decision Tree
- PCA
- Min-Max Scaling
- K-Nearest Neighbors
Deep Learning
- TensorFlow
- Keras
- Autoencoder
- LSTM
- Dense Neural Networks
- Dropout
Data Processing
- NumPy
- Pandas
Visualization
- Matplotlib
User Interface
- Tkinter
Model Storage
- Pickle
- HDF5
- JSON

  
📁 Repository Structure
Improved-Hybrid-Algorithm-IoT-Cyber-Attack-Detection/
│
├── Dataset/
│   ├── iot_dataset.csv
│   └── testData.csv
│
├── model/
│   ├── minmax.txt
│   ├── lstm_history.pckl
│   ├── lstm_weights.hdf5
│   ├── encoder_history.pckl
│   ├── encoder_model.json
│   └── encoder_model_weights.h5
│
├── screenshots/
│   ├── 01-project-interface.png
│   ├── 02-dataset-loaded.png
│   ├── 03-dataset-preprocessing.png
│   ├── 04-autoencoder-results.png
│   ├── 05-decision-tree-pca-results.png
│   ├── 06-cnn-lstm-results.png
│   ├── 07-model-performance-comparison.png
│   └── 08-attack-detection.png
│
├── Main.py
├── test.py
├── run.bat
├── table.html
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Main Components
Main.py
The primary application file containing:
- Graphical user interface
- Dataset loading
- Preprocessing
- Autoencoder implementation
- Decision Tree classification
- PCA processing
- CNN-LSTM implementation
- Attack-type detection
- Performance evaluation
- Visualization

Dataset/
Contains the IoT datasets used by the project.
model/
Contains saved model architectures, weights, preprocessing objects, and training history.
screenshots/
Contains screenshots demonstrating the application workflow and results.
requirements.txt
Contains the Python packages required by the project.
run.bat
Windows batch file associated with launching the application.

🔄 End-to-End Detection Process
The complete workflow can be summarized as:
Load Dataset
      ↓
Preprocess Dataset
      ↓
Normalize Features
      ↓
Train / Load Autoencoder
      ↓
Extract Features
      ↓
Apply PCA
      ↓
Train Decision Tree
      ↓
Generate Attack Predictions
      ↓
CNN-LSTM Detection
      ↓
Calculate Metrics
      ↓
Compare Models
      ↓
Identify Attack Type

📌 Key Features
- 🗂️ IoT dataset loading
- 🔄 Dataset preprocessing
- 📊 Feature normalization
- 🧠 Autoencoder feature extraction
- 📉 PCA-based dimensionality reduction
- 🌳 Decision Tree classification
- 🧬 LSTM-based deep learning
- 🚨 Cyber attack detection
- 🔎 Attack-type classification
- 📈 Performance comparison
- 🖥️ Tkinter graphical interface
- 💾 Saved model support
- 📊 Result visualization
  
🎓 Project Purpose
This project was developed as a final-year cybersecurity and machine learning project to explore automated cyber-attack detection in IoT environments.
The project combines machine learning and deep learning techniques to analyze IoT network data and identify malicious activity.
It demonstrates practical experience in:
- Cybersecurity
- IoT security
- Machine learning
- Deep learning
- Data preprocessing
- Feature extraction
- Classification
- Model evaluation
- Python development
  
🚀 Future Improvements
Potential improvements to the project include:
- Integration with real-time IoT network traffic
- Real-time attack detection
- SIEM integration
- Automated alert generation
- Improved handling of imbalanced datasets
- Additional deep learning architectures
- Explainable AI for attack classification
- Web-based monitoring dashboard
- Real-time visualization of detected attacks
- Integration with threat intelligence sources
  
⚠️ Disclaimer
This project is intended for educational, research, and defensive cybersecurity purposes.
The datasets and experiments should be used only in controlled and authorized environments. Users are responsible for ensuring that any testing or deployment is performed on systems and networks for which they have appropriate authorization.

👤 Author
Pranay Kumar
Cybersecurity | SOC Analyst | Security Operations
GitHub: Mudimanchi-Pranay

⭐ Project Summary
Improved Hybrid Algorithm for IoT Cyber Attack Detection combines Autoencoder-based feature extraction, PCA, Decision Tree classification, and CNN-LSTM based detection to analyze IoT traffic and identify different categories of cyber attacks.
IoT Data
   ↓
Preprocessing
   ↓
Autoencoder
   ↓
Feature Extraction
   ↓
PCA + Decision Tree
   ↓
CNN-LSTM
   ↓
Attack Detection
   ↓
Performance Evaluation

Built as a practical final-year project for IoT cybersecurity and automated cyber-attack detection.
