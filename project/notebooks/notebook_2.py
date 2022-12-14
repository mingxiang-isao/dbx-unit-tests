# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 2

# COMMAND ----------

from pyspark.sql import SparkSession

def generate_data(table_name="test_table"):
    df = SparkSession.getActiveSession().range(0, 10)
    df.write.format("delta").mode("overwrite").saveAsTable(table_name)

# COMMAND ----------

# DBTITLE 1,Test SQL command
# MAGIC %sql
# MAGIC SELECT * FROM test_table

# COMMAND ----------

# MAGIC %fs ls /tmp
