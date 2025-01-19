from datetime import datetime
from typing import Self

#--------------------good method---------------------
def get_time() ->str:
    now: datetime = datetime.now()
    return f'{now:%X}'

print(get_time())

#-------------------instance method-------------------
class Calculator:
    def __init__(self,version) -> None:
        self.version = version

    def des(self):
        print(f'currrentl running Calculator on version :{self.version}')

    @staticmethod
    def add_number(*num:float)-> float:
        return sum(num)
    
    @classmethod                                                                 # change variable of class for all
    def popular_versions(cls,pop_version: float) -> Self:
        popular_version: float=pop_version
        return cls(popular_version)     # cls(keyword) calling __init__
    
print(Calculator.add_number(10,20,30,40)) # with out instance

version1 = Calculator(3.4)
version1.des()
version2 = Calculator.popular_versions(3.2)
version2.des()
version1.des()


def notfixedpara(*num):
    for i in num:
        print(i)

notfixedpara("onepara")
notfixedpara("first","second")