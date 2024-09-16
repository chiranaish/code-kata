#!/bin/bash

# Ensure the script is executable
# chmod +x anonymize_data.sh

# Check if PySpark is installed
PYSPARK_VERSION=$(pip show pyspark 2>&1 >/dev/null | grep 'Version')
if [[ -z "$PYSPARK_VERSION" ]]; then
  echo "PySpark not found! Installing PySpark..."
  pip install pyspark
fi

# Run the PySpark script
echo "Running PySpark anonymization script..."
spark-submit --master yarn --deploy-mode cluster --num-executors 4 --executor-memory 16G --executor-cores 2 --driver-memory 16G anonymize_data.py > anonymize_data.out
echo "Anonymization process completed and output is written to out_anonym.csv file"
