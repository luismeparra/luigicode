import pandas as pd
import os
import requests

class DataRetriever:
    def __init__(self, url, save_dir):
        self.url = url
        self.save_dir = save_dir

    def retrieve_data(self):
        # Create the data directory if it doesn't exist
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        # Download the data
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.content
            with open(os.path.join(self.save_dir, 'retrieved_data.csv'), 'wb') as file:
                file.write(data)
            return "Data retrieval successful."
        else:
            return "Data retrieval failed."

 