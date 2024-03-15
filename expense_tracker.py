from datetime import *
from expense import Expense
from time import sleep
import os


def main():
    #Ask for Budget
    budget=get_Budget()
    sleep(1)
    #Ask Expense
    expense=get_Expense()
    print(expense,'💵')
    sleep(1)
    #Storing Expenses in a CSV file
    expense_file_path="expense.csv"
    store_Expense(expense,expense_file_path)

def get_Budget():
    print("💰 Do you want to allocate month bugdet")
    ch=''
    while ch!='y' or ch!='n':
        ch=input("y for yes /n for no \n")
        if ch=='y':
            bugdet=float(input("Enter your budget:\n"))
            print(f"Budget allocated for this month is {bugdet:.2f}Rs")
            return bugdet
        elif(ch=='n'):
            return None            
        else:
            print("Invalid Input. Please select either y or n")

def get_Expense():
    print("Enter Expense")
    #name
    name=input("Enter Expense Name:\n")
    #category
    exp_categorys=['💼 Work','🏠 Home','🎮 Fun','🍜 Food','🚌 Transport','🏥 HealthCare','🏋️ PersonalCare','💭 Others']
    for i,cat in enumerate(exp_categorys):
        print(f'{i+1}. {cat}')
    while True:
        ch=int(input('Select a number for your category: '))
        if ch in range(len(exp_categorys)+1):    
            category=exp_categorys[ch-1][2:]
            break
        else:
            print(f"Entered Nummber has to be in range [0-{len(exp_categorys)+1}]")
    #amount
    amount=float(input("Enter Expense Amount:\n"))
    #date(optional)
    print("Is This Expense for Today?")
    while ch!='y' or ch!='n':
        ch=input("y/n\n")
        if ch=='y':
            print("Expense Added for today:")
            return Expense(name=name,category=category,amount=amount)
        elif ch=='n':
            #TODO: might fail in certain conditions
            date_str=input("Enter date for this expense(dd-mm-yyyy format)\n")
            print(f"Expense Added for date {date_str}:")
            return Expense(name=name,category=category,amount=amount,date=date_str)

def store_Expense(expense: Expense,expense_file_path):
    print("Saving Expense to CSV file")
    with open(expense_file_path,"a",encoding="utf-8") as file:
        file.write(f"{expense.name},{expense.category},{expense.amount},{expense.date}\n")
    file.close()




if __name__ =="__main__":
    main()