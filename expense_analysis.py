from datetime import *
import pandas as pd
# import sklearn

expense_file_path="example.csv"
df=pd.read_csv(expense_file_path)

def ExpenseForToday(df: pd.DataFrame):
    # df['Date']=pd.to_datetime(df['Date'],format='%d-%m-%Y')
    today=datetime.today()
    today=today.strftime('%d-%m-%Y')
    
    df=df.loc[df.Date==today]
    print(df)
    return df['Amount'].sum()
    
def amount_by_category(df: pd.DataFrame):

    category_exp=df.groupby('Category')['Amount'].sum()
    dict_cat_exps=category_exp.to_dict()
    print("Expense by Categories:")
    for key,value in dict_cat_exps.items():
        print(f"{key}: {value}Rs")

def Expense_for_the_month(df: pd.DataFrame,now=date.today()):
    df['Date']=pd.to_datetime(df['Date'],format='%d-%m-%Y')
    df['year'], df['month'] = df['Date'].dt.year, df['Date'].dt.month
    
    print(df[(df['month']==now.month) & (df['year']==now.year)])
    # print("Would you] like to see the Expense for the month?")
    # print("1. Current Month")
    # print("2. Other")
    # ch=input()
    # mon=input("Enter the month in (mm/yy) format")
    # if ch==1:

def avg_expense_by_day(df: pd.DataFrame):
    v=df.groupby('Date').Amount.sum()
    print(v.sum()/len(v))


 