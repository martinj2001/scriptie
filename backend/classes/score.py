import pandas as pd
from enum import Enum
from .input_type import InputType
from .field import Field
from .fields import fields
from .input_type import InputType
from .scores.completeness import Completeness
from .scores.correctness import Correctness
from .scores.accessibility import Accessibility
import datetime
import validators
from email_validator import validate_email, EmailNotValidError
from textstat import textstat
import numpy as np

fields = fields['0.3.1a']

class Score():
    def __init__(self, data:pd.DataFrame) -> None:
        self.data = data
        self.rowcount = len(self.data)
        self.completeness = Completeness()
        self.correctness = Correctness()
        self.accessibilty = Accessibility()
        self.calculate_scores()
        
    def calculate_scores(self):
        self.calculate_completeness()
        self.calculate_correctness()
        self.calculate_accessibility()
    
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
    
    
    #region Correctness
    
    def calculate_correctness(self):
        self.calculate_date_correctness()
        self.calculate_url_correctness()
        self.calculate_email_correctness()
        self.calculate_type_correctness()
    
    def get_columns_for_type(self, input_type:InputType):
        fieldsList = []
        for column in self.data.columns:
            if column in fields:
                if type(fields[column]) == list:
                    for field in fields[column]:
                        if field.inputType == input_type:
                            fieldsList.append(column)
                else:
                    if fields[column].inputType == input_type:
                        fieldsList.append(column)
        return fieldsList
    
    def get_columns_for_type_and_max_char(self, input_type:InputType, max_char:int):
        fieldsList = []
        for column in self.data.columns:
            if column in fields:
                if type(fields[column]) == list:
                    for field in fields[column]:                        
                        if field.inputType == input_type and field.maxChar == max_char:
                            fieldsList.append(column)
                else:
                    if fields[column].inputType == input_type and fields[column].maxChar == max_char:
                        fieldsList.append(column)
        return fieldsList
    
    def calculate_date_correctness(self):
        fieldsList = self.get_columns_for_type(InputType.DATE)
        if len(fieldsList):
            self.correctness.dateCorrectness = self.get_percentage_date_correctness(fieldsList)
            
    def get_percentage_date_correctness(self, fieldsList:list):
        errorCount = 0
        correctCount = 0
        for field in fieldsList:
            values = self.data[field]
            for value in values:
                try:
                    d = datetime.datetime.strptime(str(value), "%Y-%m-%d %H:%M:%S")
                    correctCount += 1
                except ValueError:
                    errorCount += 1
        return round(correctCount / (errorCount+correctCount) * 100, 2)
                    
    def calculate_url_correctness(self):
        fieldsList = self.get_columns_for_type(InputType.URL)
        if len(fieldsList):
            self.correctness.urlCorrectness = self.get_percentage_url_correctness(fieldsList)
        
    def get_percentage_url_correctness(self, fieldsList:list):
        errorCount = 0
        correctCount = 0
        for field in fieldsList:
            values = self.data[field]
            for value in values:
                if validators.url(str(value)):
                    correctCount += 1
                else:
                    errorCount += 1
        return round(correctCount / (errorCount + correctCount) * 100, 2)
    
    def calculate_email_correctness(self):
        fieldsList = self.get_columns_for_type(InputType.EMAIL)
        if len(fieldsList):
            self.correctness.emailCorrectness = self.get_percentage_email_correctness(fieldsList)
        
    def get_percentage_email_correctness(self, fieldsList:list):
        errorCount, correctCount = 0, 0
        for field in fieldsList:
            values = self.data[field]
            for value in values:
                try:
                    validation = validate_email(str(value), check_deliverability=False)
                    correctCount += 1
                except EmailNotValidError as e:
                    errorCount += 1
                    
        return round(correctCount / (correctCount+errorCount) * 100, 2)
        
    def calculate_type_correctness(self):
        errorCount, correctCount = 0, 0
        for index, row in self.data.iterrows():
            if 'type' in row:
                if row['type'] in ['Zelflerend', 'Regelgebaseerd']:
                    correctCount += 1
                else:
                    errorCount += 1
        self.correctness.typeCorrectness = round(correctCount / (correctCount + errorCount) * 100, 2)
        
    #endregion
    
    #region Accessibility
    
    def calculate_accessibility(self):
        self.calculate_overall_readability()
        self.calculate_readibility_per_organization()
        self.calculate_readibility_per_column()
    
    def calculate_overall_readability(self):
        fieldsList = self.get_columns_for_type_and_max_char(InputType.TEXT, 5000)
        if len(fieldsList):
            res, dictio = self.get_flesch_reading_ease_score(fieldsList)
            self.accessibilty.readability = res
            
    def calculate_readibility_per_organization(self):
        fieldsList = self.get_columns_for_type_and_max_char(InputType.TEXT, 5000)
        if len(fieldsList):
            self.accessibilty.readabilityPerOrganization = self.get_flesch_reading_ease_score_per_organization(fieldsList)
    
    def calculate_readibility_per_column(self):
        fieldsList = self.get_columns_for_type_and_max_char(InputType.TEXT, 5000)
        if len(fieldsList):
            self.accessibilty.readabilityPerColumn = self.get_flesch_reading_ease_score_per_column(fieldsList)
        
    def get_flesch_reading_ease_score(self, fields:list, data:pd.DataFrame = None):
        
        textstat.set_lang('nl')
        mean_scores = {}
        
        for field in fields:
            if data is None:
                values = self.data.loc[self.data[field].notnull(), [field]][field]
            else:
                values = data.loc[data[field].notnull(), [field]][field]
            if not len(values):
                continue
            scores = np.empty(len(values), dtype=float)
            i = 0
            
            for value in values:       
                score = textstat.flesch_reading_ease(value)
                score = 0 if score < 0 else score
                scores[i] = score                
                i += 1            
            mean_scores[field] = scores.mean()
        
        correctCount, errorCount = 0, 0
        for value in mean_scores.values():
            if 50 < value <= 100:
                correctCount += 1
            else:
                errorCount += 1

        return round(correctCount / (correctCount + errorCount) * 100, 2), mean_scores            
    
    def get_flesch_reading_ease_score_per_field(self, fields:list):
        textstat.set_lang('nl')
        scores = {}
        
        for field in fields:
            values = self.data.loc[self.data[field].notnull(), [field]][field]
            correctCount, errorCount = 0, 0
            
            for value in values:
                score = textstat.flesch_reading_ease(value)
                score = 0 if score < 0 else score
                
                if 50 < score <= 100:
                    correctCount += 1
                else:
                    errorCount += 1
            scores[field] = round(correctCount / (correctCount + errorCount) * 100, 2 ) if correctCount+errorCount > 0 else 0
        return scores
    
    def get_flesch_reading_ease_score_per_organization(self, fields:list):
        textstat.set_lang('nl')
        results = {}
        for i in self.data['organization'].unique():
            rows = self.data.loc[self.data['organization'] == i]
            score, dictio = self.get_flesch_reading_ease_score(fields, rows)
            results[i] = score
        return self.sort_dict(results)
        
    def get_flesch_reading_ease_score_per_column(self, fields: list):
        return self.sort_dict(self.get_flesch_reading_ease_score_per_field(fields))
        
        
        
    #endregion
    
    #region Consistency
    def calculate_consistency(self):
        pass
    #endregion
    
    def sort_dict(self, dict_to_be_sorted: dict, 
                  descending: bool = True):
        return dict(sorted(dict_to_be_sorted.items(), key=lambda x:x[1], reverse=descending))
        
        




        

    
        
