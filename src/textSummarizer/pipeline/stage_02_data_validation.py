from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValiadtion 
from textSummarizer.logging import logger



class ValidationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise e
    