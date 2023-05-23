class FactorySprites():
    def __init__(self, prototypes, periods, event_types):
        self._prototypes = prototypes 
        self._periods = periods
        self._event_types = event_types
    
    def make(self, event_type):
        return [self._prototypes[event_type - (self._event_types + i)].clone() for i in range(len(self._periods))]
    
    def get_period(self):
        return self._periods
    
    def get_event_types(self):
        event_types = []
        for i in range(len(self._periods)): # potser un +1?
            event_types.append(self._event_types + i)
        return event_types