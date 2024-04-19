import sys, os
from signLanguage.pipeline.training_pipeline import TrainPipeline
from signLanguage.exception import SignException
from signLanguage.logger import logging

logging.info("Welcome to Friday-night")

try:
    obj=TrainPipeline()
    obj.run_pipeline()
except Exception as e:
    raise SignException(e,sys) from e


