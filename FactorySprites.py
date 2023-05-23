class FactorySprites():
    def __init__(self, prototypes, periods, event_types):
        self._prototypes = prototypes 
        self.periods = periods
        self.event_types = event_types
    
    def make(self, event_type):
       return self._prototypes[event_type - self.event_types[0]].clone()
