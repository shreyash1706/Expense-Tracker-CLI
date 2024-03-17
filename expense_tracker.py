from datetime import *
from expense import Expense
from time import sleep
import os
import pandas as pd
from expense_analysis import *
from graphical_analysis import * 


def main():
    #Ask for Budget
    if is_first_day_of_month() or is_first_time_running():
        budget=get_Budget()
        with open("budget.txt","w") as b:
            b.write(budget)
        b.close()
    sleep(1)
    #Ask Expense
    expense=get_Expense()
    
    sleep(1)
    #Storing Expenses in a CSV file
    expense_file_path="expense.csv"
    store_Expense(expense,expense_file_path)
    sleep(1)
    
    while True:
        print("Would you like to track another expense?")
        ch=input("(y/n)\n")
        if ch=='y':
            expense=get_Expense()
            store_Expense(expense,expense_file_path)
        else:
            break
    sleep(1)
    print("Would you like to see the analysis of the expenditure?")
    c=input("y/n")
    if c=='y':
        df=pd.read_csv(expense_file_path)
        #Analysis of Expense Data
        print("Analysis of Expenditure")
        #Expense for today
        print("Expense for today")
        x=ExpenseForToday(df)
        print(f"Total Expense for Today: {x}Rs")
        sleep(1)
        #Distribution by category
        print("This is the distribution by categories:")
        amount_by_category(df)
        print("Here is a Pie Chart for the distribution")
        sleep(2)
        GraphAnalysis.ExpenseDistPieChart(df)
        print("and a bar chart for the actual price comparision")
        sleep(2)
        GraphAnalysis.Expense_Category_BarChart(df)
        print("Lineplot to represent the change in the pattern of spending over time")
        sleep(2)
        GraphAnalysis.Expense_Category_Lineplot(df)
        print("Would you] like to see the Expense for the month?")
        print("1. Current Month")
        print("2. Other")
        ch=input()
        
        if ch==1:
            Expense_for_the_month(df)
        else:
            mon=input("Enter the month in (mm/yy) format")
            Expense_for_the_month(df,mon)
        sleep(4)
        print("Finally here is the average expenditure for each day")
        avg_expense_by_day(df)
    else:
        exit()

def get_Budget():
    print("💰 Do you want to allocate month bugdet")
    ch=''
    while ch!='y' or ch!='n':
        ch=input("y for yes /n for no \n")
        if ch=='y':
            bugdet=float(input("Enter your budget:\n"))
            print(f"Budget allocated for this month is {bugdet:.2f}Rs")
            print("remaining day in the month ")
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
            expense= Expense(name=name,category=category,amount=amount)
            print(expense,'💵')
            with open("budget.txt","r") as b:
                budget=b.read()
            b.close()
            if budget!=None:
                print(f"Amount remaining from budget {budget-amount}Rs")
        elif ch=='n':
            #TODO: might fail in certain conditions
            date_str=input("Enter date for this expense(dd-mm-yyyy format)\n")
            print(f"Expense Added for date {date_str}:")
            expense=Expense(name=name,category=category,amount=amount,date=date_str)
            print(expense,'💵')        
        return expense

def store_Expense(expense: Expense,expense_file_path):
    print("Saving Expense to CSV file")
    with open(expense_file_path,"a",encoding="utf-8") as file:
        file.write(f"{expense.name},{expense.category},{expense.amount},{expense.date}\n")
    file.close()

def is_first_day_of_month():
    current_date = datetime.now()
    return current_date.day == 1

def is_first_time_running():
    try:
        pd.read_csv('expenses.csv')
        return False
    except FileNotFoundError:
        return True

if __name__ =="__main__":
    main()