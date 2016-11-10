from sklearn.externals import joblib
import cPickle as Pickle
from SocialHistories.SystemUtilities.Configuration import *
from SocialHistories.Extraction import Classification
import Processing
from SocialHistories.SystemUtilities.Globals import EVENT_FILLER_MODEL_NAME, EVENT_FILLER_FEATMAP_NAME


def train_event_fillers(patients):
    # Train model
    features, labels = Processing.features_and_labels(patients)
    classifier, feature_map = Classification.train_classifier(features, labels)

    # Write models to file
    classf_file = os.path.join(MODEL_DIR, EVENT_FILLER_MODEL_NAME)
    featmap_file = os.path.join(MODEL_DIR, EVENT_FILLER_FEATMAP_NAME)

    joblib.dump(classifier, classf_file)
    Pickle.dump(feature_map, open(featmap_file, "wb"))
