import pandas as pd
from enum import Enum

class Score():
    
    def __init__(self, data:pd.DataFrame) -> None:
        self.data = data
        self.rowcount = len(self.data)
        self.completeness = 0
        self.calculate_scores()
        
    
    def calculate_scores(self):
        self.calculate_completeness()
        
    def calculate_completeness(self):
        totalEmpty = self.data.isna().sum().sum()
        totalCells = self.data.shape[0] * self.data.shape[1]
        self.completeness = round((totalEmpty/totalCells) * 100, 2)
        
    def calculate_consistency(self):
        pass

class InputType(Enum):
    TEXT = 1
    
fields = {
    'name' : {
        'inputType' : InputType.TEXT,
        'alwaysShow' : True,
        'maxChar' : 100,
        'minChar' : 25
    },
    'organization' : {
        'inputType' : InputType.TEXT,
        'alwaysShow' : True,
        'maxChar' : 100,
        'minChar' : 25
    }
    
    #"department","description_short","type","category","website","status","inzet.goal","inzet.impact","inzet.proportionality","inzet.decision_making_process","inzet.documentation","juridisch.competent_authority","juridisch.lawful_basis","juridisch.iama","juridisch.iama_description","juridisch.dpia","juridisch.dpia_description","juridisch.objection_procedure","metadata_algorithm.schema_metadata","metadata_algorithm.uuid","metadata_algorithm.url","metadata_algorithm.contact_email","metadata_algorithm.area","metadata_algorithm.lang","metadata_algorithm.revision_date","toepassing.description","toepassing.application_url","toepassing.publiccode","toepassing.mprd","toepassing.source_data","toepassing.methods_and_models","toezicht.monitoring","toezicht.human_intervention","toezicht.risks","toezicht.performance_standard"
}



        

    
        
