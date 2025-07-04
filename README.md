# Network Security Project: Malicious URL Detection using MLOPS
🚀 This repository presents a complete end-to-end MLOps project for detecting malicious URLs 🛡️ using XGBoost . It ensures user safety by identifying harmful links through machine learning. The project uses key tools and best practices to build a robust, scalable, and production-ready MLOps pipeline 🛠️. By combining data ingestion, model training, deployment, and monitoring, it offers a full solution for both real-time and batch URL safety assessments ✅.

## INTRODUCTION TO THE PROJECT -
Malicious URLs are links that lead to harmful websites 🛑, often used by cybercriminals through phishing emails, social engineering, and other deceptive tactics 🎣. This project uses machine learning 🤖 to detect such URLs and offers both single and batch predictions through an interactive UI 💻.

---  

![Architecture](https://github.com/user-attachments/assets/2f1b37a7-d64e-40f4-9750-42ec43dcc972)

## **Tech Stack** 🛠️

| **Category**             | **Tools/Technologies**                                  | **Description**                                                |
|--------------------------|---------------------------------------------------------|----------------------------------------------------------------|
| **Frontend**             | Streamlit                                               | Provides a simple UI for real-time single URL predictions.     |
| **Backend**              | FastAPI                                                 | Handles batch predictions and API endpoints.                   |
| **Modeling**             | XGBoost, Python                                         | Machine learning model for detecting malicious URLs.           |
| **Database**             | MongoDB                                                 | Stores data records for ingestion and model training.          |
| **Orchestration**        | Apache Airflow                                          | Orchestrates training, retraining, and batch prediction pipelines. |
| **Experiment Tracking**  | MLflow                                                  | Tracks model metrics like F1-score, Precision, and Recall.     |
| **CI/CD**                | GitHub Actions                                          | Automates CI/CD pipelines, including Docker build and deployment. |
| **Containerization**     | Docker, AWS ECR                                         | Docker images stored securely in **ECR** for consistent deployment. |
| **Cloud Storage**        | AWS S3                                                  | Stores artifacts, trained models, and logs.                    |
| **Cloud Hosting**        | AWS EC2 Instance                                        | Serves as a **self-hosted runner** for GitHub Actions, enabling deployment. |

---
## **Highlights** 🌟

- **Real-time Single URL Predictions**: Users can interact with the model via a **Streamlit** app to get instant safety assessments.
- **Batch Predictions for Large Datasets**: Handle multiple URLs at once through **FastAPI** for efficient bulk predictions.
- **End-to-End MLOps Pipeline**: Covers data ingestion, transformation, validation, model training, and evaluation, ensuring a robust workflow.
- **Model Retraining Pipeline**: Retrain models manually or through **Apache Airflow**, ensuring the model stays up-to-date with new data.
- **Metrics Tracking with MLflow**: All experiments are tracked with **MLflow** for easy comparison and monitoring.
- **Artifact & Model Storage**: Models and intermediate artifacts are stored securely in **AWS S3**, with deployment readiness at every step.
- **Deployment-Ready Model**: Models are exposed via **FastAPI** and **Streamlit** for end-user interaction.
- **Version Control for Data**: Tracks data schema and detects any drift to maintain high data quality.
- **CI/CD Pipeline**: Fully automated using **GitHub Actions**, with Docker images pushed to **Amazon ECR** and deployed to **AWS EC2**.



