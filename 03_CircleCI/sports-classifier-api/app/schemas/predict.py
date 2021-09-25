from typing import Any, List, Optional

from logistic_regression_model.data_prep.validation import HeadlinesInputSchema
from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    predictions: Optional[List[str]]


class MultipleHeadlinesInputs(BaseModel):
    inputs: List[HeadlinesInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [{"Headline": "Barcelona will not win la liga this year"}]
            }
        }
