import pandas as pd
from .score import Score
from .score_value import ScoreValue

class Scorer:
    
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data

    def get_overall_score(self):
        return ScoreValue(Score(self.data))
    
    