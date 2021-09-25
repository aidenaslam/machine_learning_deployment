import numpy as np

from logistic_regression_model.modelling_evaluation.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    expected_no_predictions = 228

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, np.ndarray)
    assert isinstance(predictions[0], str)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions


# In this file we are making predictions on the test dataset (sample_input_data comes from conftest.py).
# We are then making various assertions on our predictions e.g. expected no. of predictions, errors etc.
