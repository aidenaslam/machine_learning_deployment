from typing import Any, List, Optional

from pydantic import BaseModel
from logistic_regression_model.data_prep.validation import HeadlinesInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    predictions: Optional[List[str]]


#class HeadlinesInputSchema(BaseModel):
    #Headline: Optional[Any]

class MultipleHeadlinesInputs(BaseModel):
    inputs: List[HeadlinesInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Headline": "Barcelona will not win la liga this year"                        
                    } 
                    ]
                
            }
        }
