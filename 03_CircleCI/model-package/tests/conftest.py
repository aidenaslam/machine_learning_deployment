import pandas as pd
import pytest

from logistic_regression_model.parameters.project_parameters import testing_dataset_path


@pytest.fixture()
def sample_input_data():
    return pd.read_csv(testing_dataset_path)
