import pandas as pd
from .score import Score
from .score_value import ScoreValue
import json, jsonpickle
import pandas

class Scorer:
    @staticmethod
    def get_score(data:pandas.DataFrame):
        return ScoreValue(Score(data)).to_dict()
    
    