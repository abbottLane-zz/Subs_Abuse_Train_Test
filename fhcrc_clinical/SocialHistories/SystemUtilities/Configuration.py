# Contains tunable system parameters
import os

# Data directories
DATA_DIR = os.path.join(os.getcwd(),"fhcrc_clinical","SocialHistories", "DataDir")
MODEL_DIR = os.path.join(DATA_DIR, "SVMModels")
ATTRIB_EXTRACTION_DIR_HOME = os.path.join(DATA_DIR, "CRFModels")