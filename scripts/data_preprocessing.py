
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder     .appName("Data Preprocessing")     .getOrCreate()

# Input and output paths
input_path = "s3://your-bucket-name/raw/customer_data.csv"
output_train_path = "s3://your-bucket-name/processed/train_data.csv"
output_test_path = "s3://your-bucket-name/processed/test_data.csv"

# Load raw data
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Data cleaning
df_cleaned = df.filter(col("age").isNotNull())                .filter(col("income").isNotNull())                .filter(col("purchase_history").isNotNull())

# Split data into training and testing datasets
train_data, test_data = df_cleaned.randomSplit([0.8, 0.2], seed=42)

# Save processed datasets
train_data.write.csv(output_train_path, header=True, mode="overwrite")
test_data.write.csv(output_test_path, header=True, mode="overwrite")

# Stop the Spark session
spark.stop()
