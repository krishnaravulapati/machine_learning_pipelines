
import boto3

# SageMaker client
sagemaker = boto3.client("sagemaker")

# Define model information
model_name = "xgboost-churn-predictor"
s3_model_uri = "s3://your-bucket-name/models/xgboost_model.json"
role_arn = "arn:aws:iam::your-account-id:role/service-role/AmazonSageMaker-ExecutionRole"

# Create SageMaker model
sagemaker.create_model(
    ModelName=model_name,
    PrimaryContainer={
        "Image": "683313688378.dkr.ecr.us-west-2.amazonaws.com/sagemaker-xgboost:latest",
        "ModelDataUrl": s3_model_uri
    },
    ExecutionRoleArn=role_arn
)

# Deploy model as endpoint
sagemaker.create_endpoint_config(
    EndpointConfigName=model_name + "-config",
    ProductionVariants=[
        {
            "VariantName": "AllTraffic",
            "ModelName": model_name,
            "InstanceType": "ml.m5.large",
            "InitialInstanceCount": 1
        }
    ]
)

sagemaker.create_endpoint(
    EndpointName=model_name,
    EndpointConfigName=model_name + "-config"
)
print(f"Model deployed at endpoint: {model_name}")
