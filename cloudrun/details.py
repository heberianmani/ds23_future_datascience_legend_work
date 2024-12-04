import os
import streamlit as st
from google.cloud import bigquery
from google.cloud import storage
from google.oauth2 import service_account

# Google Cloud Storage bucket details
gcs_bucket_name = "appproject-data"
gcs_key_path = "appproject-10-f78db8e958bb.json"

# Define a custom local directory to store the downloaded service account key
local_key_dir = os.path.join(os.getcwd(), "keys")
os.makedirs(local_key_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Download the key file from Google Cloud Storage
# def download_service_account_key():
#     # Initialize the Google Cloud Storage client
#     storage_client = storage.Client()
    
#     # Specify the bucket and key file to download
#     bucket = storage_client.bucket(gcs_bucket_name)
#     blob = bucket.blob(gcs_key_path)
    
#     # Specify the local path to save the key file
#     local_key_path = os.path.join(local_key_dir, "service_account_key.json")
    
#     # Download the key file to a local path
#     blob.download_to_filename(local_key_path)
#     return local_key_path

# Path to save the key file inside the container
local_key_path = "D:\\Manikandan\\Documents\\Datascience_ML_DL_AI\\Programming\\GCP\\appproject-10\\key_444184261605\\appproject-10-f78db8e958bb.json"  # This can be any valid path inside the container

# Function to download the service account key from GCS
def download_service_account_key():
    # Initialize the Google Cloud Storage client
    storage_client = storage.Client()

    # Specify the GCS bucket and object to download
    bucket = storage_client.bucket(bucket)
    blob = bucket.blob(gcs_key_path)

    # Download the key to the specified local path
    blob.download_to_filename(local_key_path)
    print(f"Service account key downloaded to {local_key_path}")

# Call the function to download the key file
download_service_account_key()


# Now you can use the downloaded key for BigQuery authentication
from google.oauth2 import service_account
from google.cloud import bigquery


# Download the key file from GCS
# key_path = download_service_account_key()

# Create credentials from the downloaded service account key file
credentials = service_account.Credentials.from_service_account_file(local_key_path)

# Initialize BigQuery client with credentials
client = bigquery.Client(credentials=credentials, project="appproject-10")

# BigQuery dataset and table information
dataset_id = "details"
table_id = "employee_details"

# Function to fetch all employee names from BigQuery
def get_employee_names():
    query = f"SELECT name FROM `{dataset_id}.{table_id}`"
    query_job = client.query(query)
    results = query_job.result()
    return [row.name for row in results]

# Function to add a new employee to BigQuery
def add_employee(name, company, grade, salary):
    table_ref = client.dataset(dataset_id).table(table_id)
    rows_to_insert = [
        {u"name": name, u"company": company, u"grade": grade, u"salary": salary}
    ]
    errors = client.insert_rows_json(table_ref, rows_to_insert)
    return errors

# Function to remove an employee from BigQuery
def remove_employee(name):
    # Define the BigQuery SQL query to recreate the table without the row to delete
    query = f"""
    CREATE OR REPLACE TABLE `{dataset_id}.{table_id}` AS
    SELECT * FROM `{dataset_id}.{table_id}`
    WHERE name != @name
    """
    
    # Configure the query with the name parameter
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("name", "STRING", name)
        ]
    )
    
    # Run the query job
    query_job = client.query(query, job_config=job_config)
    query_job.result()  # Wait for the job to complete

# Streamlit App
def main():
    st.title("Employee Management System")
    st.write("Add or Remove Employee Details in Google BigQuery.")

    # Tabs for adding and removing employees
    action = st.radio("Select Action", ("Add Employee", "Remove Employee"))

    if action == "Add Employee":
        # Input fields for the form
        name = st.text_input("Name:")
        company = st.text_input("Company:")
        grade = st.text_input("Grade:")
        salary = st.number_input("Salary:", min_value=0.0, step=0.01)

        # Submit button for adding employee
        if st.button("Add Employee"):
            if name and company and grade and salary:
                # Add the employee to BigQuery
                errors = add_employee(name, company, grade, salary)
                if not errors:
                    st.success(f"Employee {name} added successfully!")
                else:
                    st.error(f"Encountered errors while adding data: {errors}")
            else:
                st.error("Please fill in all the fields before submitting.")
    
    elif action == "Remove Employee":
        # Fetch current employee names for removal
        employee_names = get_employee_names()

        if employee_names:
            name_to_remove = st.selectbox("Select Employee to Remove", employee_names)
            
            # Submit button for removing employee
            if st.button("Remove Employee"):
                remove_employee(name_to_remove)
                st.success(f"Employee {name_to_remove} removed successfully!")
        else:
            st.info("No employees available to remove.")

if __name__ == "__main__":
    main()
