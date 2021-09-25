from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from logistic_regression_model.parameters.project_parameters import testing_dataset_path
from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    return pd.read_csv(testing_dataset_path)


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
