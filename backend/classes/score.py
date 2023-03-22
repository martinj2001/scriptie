import pandas as pd
from enum import Enum
from .input_type import InputType
from .field import Field
from .scores.completeness import Completeness

class Score():
    def __init__(self, data:pd.DataFrame) -> None:
        self.data = data
        self.rowcount = len(self.data)
        self.completeness = Completeness()
        self.calculate_scores()
        
    def calculate_scores(self):
        self.calculate_completeness()
    
    #region Completeness    
    def calculate_completeness(self):
        self.calculate_empty_cells()
        
    def calculate_empty_cells(self):
        totalEmpty = self.data.isna().sum().sum()
        totalCells = self.data.shape[0] * self.data.shape[1]
        self.completeness.emptyValues = round((totalEmpty/totalCells) * 100, 2)
    #endregion
    
    #region Consistency
    def calculate_consistency(self):
        pass
    #endregion




        

    
        
