## Running the code for Data Preparation

Python 3.6.8

Unzip ../data/Electronics.json.gz.

Run datasplit.py to split the data into separate files for each product. I did this to make it easier to read, load and process. There are about 7.5M products, so feel free to only run the datasplit loop for as long as you need to.

Run the cells in dataPreparation.ipynb

To run clause extraction, run the following commands

pip install -U spacy
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0-py3-none-any.whl
