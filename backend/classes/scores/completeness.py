class Completeness(dict):
    
    def __init__(self) -> None:
        self.emptyValuesPercentage:float = 0
        self.emptyValuesPerColumn:dict = {}
        self.emptyValuesPerOrganisation:dict = {}