import cPickle as Pickle
from sklearn.externals import joblib
import numpy as np

from DataModeling.DataModels import Event
from Extraction.StatusClassification.Shared_Processing import get_feature_vectors
from SystemUtilities import Debugger
from Extraction import Classification
from Extraction.Classification import vectorize_sentence, classify_many_instances
from SystemUtilities.Configuration import *
from SystemUtilities.Globals import *


def classify_sentence_status(sentences):

    for event_type in SUBSTANCE_TYPES:
        # load classifiers and feature map
        classifier, feature_map = load_classifier(event_type)

        # extract features
        feature_vectors = get_feature_vectors(sentences)

        # classify sentences
        classifications, probabilities = classify_many_instances(classifier, feature_map, feature_vectors)

        # assign classification directly to the sentence
        for i in range(0, len(sentences), 1):
            sent = sentences[i]
            assigned = False
            for event in sent.predicted_events:
                if event.substance_type == event_type:
                    assigned = True
                    event.status = classifications[i]
                    event.set_confidence(probabilities[i])

            # if all existing events are checked and there was no match (Event detection error), create the event
            if not assigned:
                new_event = Event(event_type)
                new_event.status = classifications[i]
                new_event.set_confidence(probabilities[i])
                sent.predicted_events.append(new_event)


        # DEBUG
        Debugger.print_status_classification_results(sentences, classifications, event_type)
        # end DEBUG
    pass


def load_classifier(event_type):
    classifier_file = os.path.join(MODEL_DIR, event_type+ STATUS_CLASSF_MODEL_SUFFIX)
    feature_map_file = os.path.join(MODEL_DIR, event_type+ STATUS_CLASSF_FEATMAP_SUFFIX)

    classifier, feature_map = Classification.load_classifier(classifier_file, feature_map_file)

    return classifier, feature_map
