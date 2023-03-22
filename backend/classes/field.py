from enum import Enum
from .input_type import InputType

class Field():
    
    def __init__(self, 
                 inputType:InputType,
                 alwaysShow:bool,
                 maxChar:int,
                 minChar:int,
                 dependentOn:str=None
                 ) -> None:
        self.inputType = inputType
        self.alwaysShow = alwaysShow
        self.maxChar = maxChar
        self.minChar = minChar
        self.dependentOn = dependentOn
    
    

