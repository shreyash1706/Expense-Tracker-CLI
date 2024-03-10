from datetime import *

class Expense:
    def __init__(self,name,category,amount,date=date.today()):
        self.name= name
        self.category = category
        self.amount= amount 
        self.date=date

    def __repr__(self) -> str:
        return f"Expense : {self.name} ,{self.category} ,{self.amount}"
    
