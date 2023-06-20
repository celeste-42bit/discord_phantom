from abc import ABC, abstractmethod
class reactionInterface(ABC):
    @abstractmethod
    def addReaction(self):
        pass
    
    @abstractmethod
    def removeReaction(self):
        pass