from datetime import datetime
import pandas as pd
# import sklearn

expense_file_path="example.csv"
df=pd.read_csv(expense_file_path)

def ExpenseForToday(df: pd.DataFrame):
    # df['Date']=pd.to_datetime(df['Date'],format='%d-%m-%Y')
    today=datetime.today()
    df=df.loc[df.Date==str(today)]
    return df['Amount'].sum()
    
def amount_by_category(df: pd.DataFrame):

    category_exp=df.groupby('Category')['Amount'].sum()
    dict_cat_exps=category_exp.to_dict()
    print("Expense by Categories:")
    for key,value in dict_cat_exps.items():
        print(f"{key}: {value}Rs")
 