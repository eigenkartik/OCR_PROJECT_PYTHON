import abc
#abstract class
class MedicalDocParser(metaclass=abc.ABCMeta):
    def __init__(self,text):
        self.text=text

    @abc.abstractmethod  #child class won't be able to use this method
    def parse(self):
        pass
