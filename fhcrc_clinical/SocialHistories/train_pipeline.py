# train classifiers and extractors and output models
import time

from fhcrc_clinical.SocialHistories.DataLoading import DataLoader
from fhcrc_clinical.SocialHistories.Extraction.EventDetection import Training as EventDetectionTraining
from fhcrc_clinical.SocialHistories.Extraction.StatusClassification import Training as StatusClassificationTraining
from fhcrc_clinical.SocialHistories.Extraction.EventAttributeLinking import Training as EventFillerTraining
from fhcrc_clinical.SocialHistories.Extraction.AttributeExtraction import Training_CRFSuite
from fhcrc_clinical.SocialHistories.SystemUtilities.Stopwatch import stopWatch


def main():
    start = time.time()  # Start a timer to see how long training takes

    # Load Data
    patients = DataLoader.main("Train")  # list of filled Patient objects

    # Event Detection
    EventDetectionTraining.train_event_detectors(patients)

    # Status classification
    StatusClassificationTraining.train_status_classifier(patients)

    # Attribute Extraction
    Training_CRFSuite.train(patients)

    # Event Filling
    EventFillerTraining.train_event_fillers(patients)

    end = time.time()
    print "Training completed in: " + str(stopWatch(end - start))

if __name__ == '__main__':
    main()
