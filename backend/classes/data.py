import pandas as pd
import numpy as np
import os 
from typing import Optional
import pandas 

class Data:
    
    def __init__(self) -> None:
        self.df = pd.read_csv('./data/algoritmeregister_20230523.csv')
        self.orient = 'records'
        
    def get_all_records(self) -> dict:
        """Get all records without filter

        Returns:
            dict: dict with all records
        """        
        return self.df.to_dict(orient=self.orient)
    
    def get_record_by_id(self, id:int) -> dict:
        """Get record by index id

        Args:
            id (int): id of algorithm

        Returns:
            dict: dict with the found record. Will return empty dict if not found
        """        
        return self.df.iloc[[id]].to_dict(orient=self.orient)[0] if id in self.df.index else {}
    
    def get_all_records_as_dataframe(self, organizations = None, fields = None) -> pandas.DataFrame:
        df = self.df
        if organizations is not None:
            print(organizations)
            df = df.loc[df['organization'].isin(organizations)]
        if fields is not None:
            df = df[fields]
        return df
    
    def get_record_by_id_as_dataframe(self, id:int) -> pandas.DataFrame:
        return self.df.iloc[[id]]
    
    def get_all_unique_organizations(self) -> list:        
        return list(self.df['organization'].unique())
    
    def get_all_fields(self) -> list:
        return list(self.df.columns)
    