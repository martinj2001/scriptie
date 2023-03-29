from .score import Score
import json 
from .scores.completeness import Completeness

class ScoreValue():
    def __init__(self, score: Score) -> None:
        self.completeness:Completeness = score.completeness        
    
    def to_dict(self):
        return {'completeness' : self.completeness.__dict__}
        
        