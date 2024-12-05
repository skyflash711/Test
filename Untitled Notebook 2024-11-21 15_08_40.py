# Databricks notebook source
import os
import subprocess

# Change to the project directory
project_path = '/Workspace/Users/sarvesh.maheshwari@databricks.com/Test'

# Ensure DBFS path exists
if not os.path.exists(project_path):
    raise FileNotFoundError(f"Path {project_path} does not exist.")

# Build the wheel
command = f"cd {project_path} && python setup.py bdist_wheel"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Output the results of the build process
if result.returncode == 0:
    print("Wheel built successfully.")
    print(result.stdout)
else:
    print("Error building wheel.")
    print(result.stderr)

# COMMAND ----------

os.path.exists('/Workspace/Users/sarvesh.maheshwari@databricks.com/Test/dist/notebooks-0.1.0-py3-none-any.whl')

# COMMAND ----------



# COMMAND ----------

from notebooks import my_module

print(my_module.hello_world())  # Replace with your function

# COMMAND ----------


