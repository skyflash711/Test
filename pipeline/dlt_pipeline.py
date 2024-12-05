# Databricks notebook source
import notebooks.my_module as my_module
# import dlt

# COMMAND ----------

# Step 1: Read from the Source Table
@dlt.table(
    comment="Raw streaming source table"
)
def source_stream():
  print(my_module.hello_world())
  table_name = "main.default.dummy_streaming_table"
  checkpoint_directory = "/Volumes/main/default/sarvesh_experiment/"
  source_format = "delta"
  source_table_name = "main.default.dummy_streaming_source"
  return (
        spark.readStream
                  .format("cloudFiles")
                  .option("cloudFiles.format", source_format)
                  .option("cloudFiles.schemaLocation", checkpoint_directory)
                  .option("skipChangeCommits", "true")
                  .table(source_table_name)
    )

# COMMAND ----------


