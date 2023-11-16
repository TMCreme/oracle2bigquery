# Data Pipeline to extract Oracle db data into Biquery

### Description
This project connects to the Oracle db and extracts data from a particular table and insert into a big query table in GCP

### Features
* Mock data that is loaded into the Oracle DB
* Creation of the Oracle DB 
* Docker compose that sets up a free version of the Oracle db. 
* Creation of the BigQuery Table - Assumes that the project and DataSet exists in Bigquery prior
* Extract and load data 

## Running the code
* Create a virtual environment in Python 
```sh
    virtualenv venv
```
* Activate the virtualenv if you haven't done so
    * MAC and Linux
``` source venv/bin/activate```
    * Windows ```venv/Scripts/activate```
* Install the required packages 
```sh
    pip install -r requirements.txt
```
* [Optional] if you don't have an Oracle DB to connect to, run the docker-compose to create one. It might take a while because the DB docker image is huge
```sh
docker-compose up
```
* Once it is done, you can run the `create_data` module with the following command in the virtual environment to create the table in the database
```sh 
python create_table.py
```
* Insert sample data into Oracle db by running the following command
```sh
python insert_data.py
```
* Set the Project credentials in the `main.py` file and run the `main` module to create the Table in BigQuery
```sh 
python main.py
```
* To run the Extraction and loading, run the `source` module
```sh
 python source.py
```
-----------------

### Running the Google Cloud Docker-Compose
* Check to confirm a `config` directory else create a `config` directory/folder and put your service account credential file in it. 
* Open the `docker-compose-gcp.yml` file and under the volumes section, change the name of the credential 
* Change the value of the environmental variable `GOOGLE_APPLICATION_CREDENTIALS` as well
* Run the following command to create a python environment with gcloud set up
```sh
docker-compose -f docker-compose-gcp.yml up
```



