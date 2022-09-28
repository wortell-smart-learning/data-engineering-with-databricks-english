# Databricks notebook source
# MAGIC %run ./_utility-methods

# COMMAND ----------

DA = DBAcademyHelper(**helper_arguments) # Create the DA object
DA.reset_environment()                   # Reset by removing databases and files from other lessons
DA.init(install_datasets=True,           # Initialize, install and validate the datasets
        create_db=False)                 # Continue initialization, create the user-db
DA.conclude_setup()                      # Conclude setup by advertising environmental changes

