from .score import Score
import json 
from .scores.completeness import Completeness
from .scores.correctness import Correctness
from .scores.accessibility import Accessibility

class ScoreValue():
    def __init__(self, score: Score) -> None:
        self.completeness:Completeness = score.completeness  
        self.correctness:Correctness = score.correctness
        self.accessibility:Accessibility = score.accessibilty
    
    def to_dict(self):
        return {'completeness' : self.completeness.__dict__,
                'correctness' : self.correctness.__dict__,
                'accessibility' : self.accessibility.__dict__}
        
        