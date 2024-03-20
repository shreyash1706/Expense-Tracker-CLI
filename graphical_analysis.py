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
            plt.plot(category_data['Date'], category_data['Amount'], marker= 'o', linestyle='-', label=category)
        date_range=pd.date_range(start=df['Date'].min().date(),end=df['Date'].max().date(),freq='M')

        plt.xticks(date_range,date_range.strftime('%B %Y'),rotation=45)
        plt.legend()
        plt.xlabel('Dates')
        plt.ylabel('Amounts')
        plt.title("Expense distriution of different categories over time")
        plt.grid(True, linestyle='--', color='gray', alpha=0.5)
        plt.show()

    def Expense_Category_BarChart(df :pd.DataFrame):
        plt.figure(figsize=(10, 6))
        category_exp=df.groupby('Category')['Amount'].sum()
        categories = category_exp.index.tolist()
        dict_cat_exps=category_exp.to_dict()
        colors = ['indianred', 'lightgreen', 'lightblue', 'orange', '#6A5ACD', 'lightgray', 'pink', '#FFFF99'] 
        plt.bar(categories,dict_cat_exps.values(), color=colors, edgecolor='black')
        plt.show()

    #TODO: if time remaining make heatmap
    # def Expense_Heatmap_ByMonth(df :pd.DataFrame):
    #     df['Date']=pd.to_datetime(df['Date'],format='%d-%m-%Y')
    #     df['year'], df['month'] = df['Date'].dt.year, df['Date'].dt.month
    #     year_month=df.groupby(['Category','year','month']).Amount.sum()
    #     print(year_month)
    #     z=df['month'].unique().max()
        
        # for i in range(1,z+1):
        #    print(year_month[year_month.index.get_level_values('month') == i].mean())
# GraphAnalysis.Expense_Heatmap_ByMonth(df)
# GraphAnalysis.Expense_Category_Lineplot(df)