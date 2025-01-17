
# Machine Learning Pipelines with Apache Spark and Amazon SageMaker

This repository demonstrates a machine learning pipeline for building predictive models. The pipeline processes raw data, trains a model, and deploys it for real-time inference.

---

## 🛠️ **Use Case Overview**

### Objective
- Predict customer churn using historical data.
- Build a pipeline for data preprocessing, model training, and deployment.

### Workflow
1. **Data Ingestion**:
   - Load raw customer data from Amazon S3.

2. **Data Processing**:
   - Use Apache Spark on EMR Serverless to clean and preprocess data.

3. **Model Training**:
   - Train a churn prediction model using XGBoost on SageMaker.

4. **Deployment**:
   - Deploy the model as a SageMaker endpoint for real-time inference.

---

## 📋 **Sample Data**

| customer_id | age | income  | purchase_history | churn_label |
|-------------|-----|---------|------------------|-------------|
| 1           | 35  | 50000  | 100              | 0           |
| 2           | 42  | 62000  | 200              | 1           |

---

## ⚙️ **How to Run**

### Prerequisites
1. AWS CLI installed and configured.
2. Amazon EMR Serverless and SageMaker permissions.

### Steps
1. **Data Preprocessing**:
   ```bash
   aws s3 cp data_preprocessing.py s3://your-bucket-name/scripts/
   aws emr-serverless start-job-run        --application-id <application-id>        --execution-role-arn <execution-role-arn>        --job-driver '{
           "sparkSubmit": {
               "entryPoint": "s3://your-bucket-name/scripts/data_preprocessing.py"
           }
       }'
   ```

2. **Model Training**:
   ```bash
   python train_model.py
   ```

3. **Model Deployment**:
   ```bash
   python deploy_model.py
   ```

---

## 📊 **Expected Outcome**
- **Trained Model**: Stored in Amazon S3.
- **Real-Time Predictions**: Available via SageMaker endpoint.

---

## 📧 **Contact**
For questions or suggestions:
- **Email**: kanthravulapati@gmail.com 
- **GitHub**: [https://github.com/krishnaravulapati](https://github.com/krishnaravulapati)
