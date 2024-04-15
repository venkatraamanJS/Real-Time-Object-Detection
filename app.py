from signLanguage.exception import SignException
from signLanguage.logger import logging
import sys, os

logging.info("Welcome to Friday-night")

try:
    a= 7/'9'
except Exception as e:
    raise SignException(e,sys) from e


 
