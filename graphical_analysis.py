from matplotlib import pyplot as plt
import pandas as pd


expense_file_path="example.csv"
df=pd.read_csv(expense_file_path)
categories=df['Category'].unique()



# print(x.set_index('Category'))
class GraphAnalysis:
    def ExpenseDistPieChart(df: pd.DataFrame):
        category_exp=df.groupby('Category')['Amount'].sum()
        
        plt.pie(category_exp,labels=category_exp.index,startangle=90,autopct='%1.2f%%')
        plt.title('Expense Distribution')
        plt.axis('equal')

        plt.show()

    def Expense_Category_Lineplot(df: pd.DataFrame):
        df['Date']=pd.to_datetime(df['Date'],format='%d-%m-%Y')
        df=df.sort_values('Date')
        for category in categories:
            category_data = df[df['Category'] == category]
            plt.plot(category_data['Date'], category_data['Amount'], label=category)
        date_range=pd.date_range(start=df['Date'].min().date(),end=df['Date'].max().date(),freq='M')

        plt.xticks(date_range,date_range.strftime('%B %Y'),rotation=45)
        plt.legend()
        plt.xlabel('Dates')
        plt.ylabel('Amounts')
        plt.title("Expense distriution of different categories over time")
        plt.show()

    def Expense_Category_BarChart(df :pd.DataFrame):
        plt.figure(figsize=(10, 6))
        category_exp=df.groupby('Category')['Amount'].sum()
        dict_cat_exps=category_exp.to_dict()
        plt.bar(categories,dict_cat_exps.values())
        plt.show()
GraphAnalysis.Expense_Category_BarChart(df)