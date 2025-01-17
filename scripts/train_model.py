
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import boto3

# Load training data from S3
s3 = boto3.client("s3")
bucket_name = "your-bucket-name"
train_data_key = "processed/train_data.csv"

obj = s3.get_object(Bucket=bucket_name, Key=train_data_key)
data = pd.read_csv(obj["Body"])

# Prepare training data
X = data[["age", "income", "purchase_history"]]
y = data["churn_label"]

# Split data into training and validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = xgb.XGBClassifier()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
print(f"Model Accuracy: {accuracy}")

# Save model to S3
model.save_model("xgboost_model.json")
s3.upload_file("xgboost_model.json", bucket_name, "models/xgboost_model.json")
