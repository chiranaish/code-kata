from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, concat_ws

# Initialize Spark session
spark = SparkSession.builder.appName('AnonymizeCSV').getOrCreate()

# Load CSV into DataFrame
df = spark.read.csv('input.csv', header=True)

# Anonymize sensitive columns
df_anonymized = df.withColumn('first_name', sha2('first_name', 256)) \
                  .withColumn('last_name', sha2('last_name', 256)) \
                  .withColumn('address', sha2('address', 256))

# Save the anonymized file
df_anonymized.write.csv('output_anonymized.csv', header=True)

spark.stop()
