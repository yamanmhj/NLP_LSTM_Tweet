import os
import sys
sys.path.append("/Users/yamanmaharjan/Documents/Personal_yaman/NLP_LSTM_TWEET/NLP_MODULE/src")
sys.path.append("/Users/yamanmaharjan/Documents/Personal_yaman/NLP_LSTM_TWEET/NLP_MODULE")

from dataclasses import dataclass
from NLP_MODULE.config import LoadConfig
from NLP_MODULE.src.components.data_transformation import DataTransformation
from exception import CustomeException
import zipfile

@dataclass
class DataIngestionConfig:
    Load_data_main_path_root: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__name__))))))
    Loaded_data_path = os.path.join(Load_data_main_path_root,'Load_data_here','Loaded_dataset')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

        
    def extract_zip_files(self):
            print('Extracting zip files')
            for file_name in os.listdir(self.ingestion_config.Loaded_data_path):
             if file_name.endswith('.zip'):
                  zip_file_path = os.path.join(self.ingestion_config.Loaded_data_path, file_name)
            # Extract the ZIP file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.ingestion_config.Loaded_data_path)
            print(f'Extracted: {file_name}')






    