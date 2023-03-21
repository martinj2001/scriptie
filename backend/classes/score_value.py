from .score import Score
import json 

class ScoreValue():
    def __init__(self, score: Score) -> None:
        self.completeness = score.completeness
    
    def toJSON(self):
        return self.__dict__