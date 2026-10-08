# 🛡️ Improved Hybrid Algorithm for IoT Cyber Attack Detection

An improved hybrid deep-learning based intrusion detection system designed to detect and classify cyber attacks in IoT environments.

The project combines **CNN + LSTM**, preprocessing, dimensionality reduction, anomaly detection, and traditional machine-learning models to analyze network traffic and identify malicious activity.

---

## 📌 Project Overview

The rapid growth of Internet of Things (IoT) devices has increased the attack surface of modern networks.

Traditional intrusion detection systems may struggle to identify complex and evolving attacks because IoT traffic contains large volumes of high-dimensional and imbalanced data.

This project proposes an **improved hybrid intrusion detection framework** that combines:

- Convolutional Neural Networks (CNN)
- Long Short-Term Memory (LSTM)
- Principal Component Analysis (PCA)
- Autoencoders
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- Deep Neural Network techniques

The system processes network traffic, extracts important features, detects anomalies, and classifies cyber attacks.

---

## 🎯 Objectives

- Detect malicious activity in IoT network traffic.
- Reduce the dimensionality of large network datasets.
- Detect anomalous traffic using Autoencoders.
- Capture spatial patterns using CNN.
- Capture temporal patterns using LSTM.
- Compare the hybrid model with traditional machine-learning approaches.
- Improve the reliability of IoT cyber-attack detection.
- Provide an interactive interface for running the detection pipeline.

---

## 🧠 Proposed Architecture

```text
                    IoT Network Traffic
                            │
                            ▼
                    Dataset Collection
                            │
                            ▼
                    Data Preprocessing
                            │
                            ▼
                  Feature Engineering
                            │
                            ▼
                         PCA
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
        Autoencoder                 ML Baselines
       Anomaly Detection       Decision Tree / RF / SVM
              │
              ▼
         CNN Feature
          Extraction
              │
              ▼
        LSTM Temporal
          Learning
              │
              ▼
       Hybrid CNN + LSTM
              │
              ▼
       Attack Classification
              │
              ▼
        Detection Results

🔬 Dataset
The project works with network intrusion-detection datasets containing benign and malicious network traffic.
The implementation includes support for datasets such as:
- CIC-IDS2017
- UNSW-NB15
- IoT network traffic datasets
Dataset Processing
The preprocessing pipeline includes:
- Missing-value handling
- Feature selection
- Data cleaning
- Encoding categorical features
- Feature scaling
- Dimensionality reduction
- Train/test splitting
- Class balancing where required
⚙️ Technologies Used
Programming
- Python
Machine Learning
- Scikit-learn
- Decision Tree
- Random Forest
- Support Vector Machine
- PCA
Deep Learning
- TensorFlow / Keras
- CNN
- LSTM
- Autoencoder
Data Processing
- Pandas
- NumPy
- Matplotlib
- Seaborn
Security
- Intrusion Detection
- Network Traffic Analysis
- Anomaly Detection
- Cyber Attack Classification
- IoT Security
🔄 Detection Workflow
Dataset
   │
   ▼
Data Loading
   │
   ▼
Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
PCA
   │
   ▼
Autoencoder
   │
   ▼
CNN
   │
   ▼
LSTM
   │
   ▼
Attack Classification
   │
   ▼
Performance Evaluation

📸 Project Screenshots
🖥️ Project Interface

📂 Dataset Loaded

⚙️ Dataset Preprocessing

🧠 Autoencoder Results

🌳 Decision Tree + PCA

🔥 CNN-LSTM Results

📊 Model Performance Comparison

🚨 Attack Detection

🤖 Models Implemented
1. Decision Tree
A Decision Tree classifier is used as one of the traditional machine-learning baselines.
It provides an interpretable classification approach for detecting malicious network traffic.
2. Random Forest
Random Forest combines multiple decision trees to improve classification robustness and reduce overfitting.
3. Support Vector Machine
SVM is used as another traditional machine-learning baseline for separating malicious and benign traffic.
4. PCA
Principal Component Analysis is used for dimensionality reduction.
It helps reduce the number of input features while retaining important information from the original dataset.
5. Autoencoder
The Autoencoder is used for anomaly detection.
The model learns the representation of normal traffic and identifies unusual patterns based on reconstruction behavior.
6. CNN
The Convolutional Neural Network is used to extract important spatial and feature-level patterns from network traffic.
7. LSTM
The Long Short-Term Memory network is used to learn temporal relationships within network traffic sequences.
8. Hybrid CNN + LSTM
The proposed hybrid architecture combines:
CNN
 │
 ├── Spatial / Feature Extraction
 │
 ▼
LSTM
 │
 ├── Temporal Pattern Learning
 │
 ▼
Attack Classification

This allows the system to capture both feature-level and sequential characteristics of network traffic.
📈 Model Evaluation
The models can be evaluated using common classification metrics:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Detection Rate
- False Positive Rate
The performance comparison helps identify the effectiveness of the proposed hybrid CNN-LSTM approach against traditional machine-learning models.
🛡️ Cyber Attacks
The system is designed to identify malicious network behavior and attack categories represented in the selected dataset.
Depending on the dataset, attack categories may include:
- DoS
- DDoS
- Brute Force
- Port Scanning
- Web Attacks
- Botnet Activity
- Infiltration
- Other Network-Based Attacks
🖥️ Project Interface
The project includes an interface that allows users to interact with the detection pipeline.
The interface provides functionality for:
- Dataset loading
- Dataset preprocessing
- Model execution
- Attack detection
- Result visualization
- Model comparison
📁 Project Structure
Improved-Hybrid-Algorithm-IoT-Cyber-Attack-Detection/
│
├── Dataset/
│   └── Dataset files
│
├── model/
│   └── Trained model files
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
├── README.md
└── .gitignore

🚀 Installation
Clone the repository:
git clone https://github.com/Mudimanchi-Pranay/Improved-Hybrid-Algorithm-IoT-Cyber-Attack-Detection.git

Navigate into the project:
cd Improved-Hybrid-Algorithm-IoT-Cyber-Attack-Detection

Install the required Python packages:
pip install -r requirements.txt

If a requirements.txt file is not included, install the required libraries manually:
pip install pandas numpy scikit-learn tensorflow matplotlib seaborn

▶️ Running the Project
Run the main application:
python Main.py

Follow the interface to:
1. Load the dataset.
2. Preprocess the data.
3. Perform feature engineering.
4. Run the machine-learning models.
5. Run the Autoencoder.
6. Run the CNN-LSTM model.
7. Analyze the attack detection results.
8. Compare model performance.
📊 Results
The project compares traditional machine-learning approaches with the proposed hybrid deep-learning architecture.
The main objective is to demonstrate how combining:
CNN + LSTM + PCA + Autoencoder

can provide a stronger framework for IoT intrusion detection.
The included screenshots demonstrate the complete workflow from dataset loading to attack detection and model comparison.
🌐 Applications
This project can be applied to:
- IoT Security
- Network Intrusion Detection
- SOC Monitoring
- Cyber Attack Detection
- Anomaly Detection
- Network Traffic Analysis
- Security Analytics
- Smart Device Security
🔮 Future Enhancements
Potential improvements include:
- Real-time network traffic monitoring
- Integration with SIEM platforms
- Live packet capture
- Automated alert generation
- Explainable AI for security alerts
- Real-time SOC dashboard
- Cloud deployment
- Continuous model retraining
- Improved handling of class imbalance
- Integration with threat-intelligence feeds
🏆 Academic Project
Project Title:
An Improved Hybrid Algorithm for Cyber Attack Detection from IoT Environment

This project was developed as an academic cybersecurity and machine-learning project focusing on intrusion detection in IoT environments.
📚 Research
The work is associated with research on:
“An Improved Hybrid Algorithm for Cyberattack Detection from IoT Environment”

The project explores the use of hybrid machine-learning and deep-learning techniques for improving cyberattack detection in IoT environments.
👨‍💻 Author
Pranay Kumar
Cybersecurity Graduate | SOC Analyst | Cybersecurity Analyst
Areas of Interest
- SOC Operations
- SIEM
- Incident Response
- Threat Detection
- Threat Hunting
- Network Security
- Digital Security
- Machine Learning for Cybersecurity
🔗 Connect With Me
GitHub
https://github.com/Mudimanchi-Pranay
LinkedIn
https://www.linkedin.com/in/pranay4638/
⭐ If you find this project useful
Consider giving the repository a ⭐ on GitHub.
