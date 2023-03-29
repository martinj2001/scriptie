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
        self.calculate_empty_cells_percentage()
        self.calculate_empty_cells_per_column()
        self.calculate_empty_cells_per_organization()
        
    def calculate_empty_cells_percentage(self):
        totalEmpty = self.data.isna().sum().sum()
        totalCells = self.data.shape[0] * self.data.shape[1]
        self.completeness.emptyValuesPercentage = round((totalEmpty/totalCells) * 100, 2)
        
    def calculate_empty_cells_per_column(self):
        sums = self.data.isna().sum()
        self.completeness.emptyValuesPerColumn = self.sort_dict(
            {k:round(v/self.data.shape[0]*100, 2) 
             for (k,v) in sums.to_dict().items()})
        
        
    def calculate_empty_cells_per_organization(self):
        count = self.data.groupby(self.data['organization']).count()        
        self.completeness.emptyValuesPerOrganisation = self.sort_dict(
            {i:round(100 - count.loc[i].sum()/
                     (count.loc[i]['name']*self.data.shape[1])*100, 2) 
             for i in count.index})
        
        
    
    #endregion
    
    #region Consistency
    def calculate_consistency(self):
        pass
    #endregion
    
    def sort_dict(self, dict_to_be_sorted: dict, 
                  descending: bool = True):
        return dict(sorted(dict_to_be_sorted.items(), key=lambda x:x[1], reverse=descending))
        
        




        

    
        
