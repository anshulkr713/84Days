from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self,name:str,description:str,**kwargs):
        ''' This is the auto initializing method with every object call'''
        self.name=name
        self.description=description

    @abstractmethod
    async def execute(self,state:dict) -> dict:
        print("hi")
        print("Windows")


