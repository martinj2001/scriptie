class Accessibility(dict):
    def __init__(self) -> None:
        self.readability:float = 0
        self.readabilityPerColumn:dict = {}
        self.readabilityPerOrganization:dict = {}
        
    