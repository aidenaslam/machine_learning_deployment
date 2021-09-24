import pickle

import joblib
from sklearn.feature_extraction.text import CountVectorizer

from logistic_regression_model.evaluation.model_evaluation import cross_validation
from logistic_regression_model.parameters.project_parameters import (
    file_path_model,
    file_path_tfidf,
    file_path_vec,
)

# Load trained model and vocabs to make predictions
trained_model = joblib.load(filename=file_path_model)
loaded_vec = CountVectorizer(vocabulary=pickle.load(open(file_path_vec, "rb")))
loaded_tfidf = pickle.load(open(file_path_tfidf, "rb"))


def test_cross_validation_score(sample_input_data):
    X = sample_input_data["Headline"].values.tolist()
    y = sample_input_data["Sport"]
    X_new_counts = loaded_vec.transform(X)
    X_new_tfidf = loaded_tfidf.transform(X_new_counts)
    models = ("Logistic Reg (baseline)", trained_model)
    cross_val = cross_validation(models, X_new_tfidf, y, 10)

    assert cross_val.mean() > 0.7
