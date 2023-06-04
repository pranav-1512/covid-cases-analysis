import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def main_menu():
    print("----------------------------------")
    print("              MENU                ")
    print("----------------------------------")
    print("1. CSV file to DataFrame")
    print("2. Line Chart")
    print("3. Bar Chart")
    print("4. Pie Chart")
    print("5. Scatter Plot")
    print("6. Sorting Data")
    print("7. Reading specific records")
main_menu()

def Read_CSV():
    df=pd.read_csv("COVIDCASES.csv")
    print(df)

def line_plot():
        df=pd.read_csv("COVIDCASES.csv")
        dist= df['DISTRICT']
        tot=df['Total cases']
        rec=df['Recoveries']
        det=df['Deaths']
        d1=df['3-Nov']
        d2=df['4-Nov']
        d3=df['5-Nov']
        d4=df['6-Nov']
        d5=df['7-Nov']
        d6=df['8-Nov']
        d7=df['9-Nov']
        plt.plot(dist, d1, label='3Nov')
        plt.plot(dist, d2, label='4Nov')
        plt.plot(dist, d3, label='5Nov')
        plt.plot(dist, d4, label='6Nov')
        plt.plot(dist, d5, label='7Nov')
        plt.plot(dist, d6, label='8Nov')
        plt.plot(dist, d7, label='9Nov') 
        plt.xticks(fontsize=12, rotation=30)
        plt.yticks(fontsize=12, rotation=30)
        plt.xlabel('Districts', fontsize=16)
        plt.ylabel('No of cases', fontsize=16)
        plt.legend(loc='upper left')
        plt.title('Line plot- Districtwise Covid cases', fontsize=1)
        plt.grid(True)
        plt.show()
def Bar_Chart():
    df=pd.read_csv("COVIDCASES.csv")
    dist= df['DISTRICT']
    tot=df['Total cases']
    rec=df['Recoveries']
    det=df['Deaths']
    d1=df['3-Nov']
    d2=df['4-Nov']
    d3=df['5-Nov']
    d4=df['6-Nov']
    d5=df['7-Nov']
    d6=df['8-Nov']
    d7=df['9-Nov']
    plt.bar(dist,tot)
    plt.xlabel("DISTRICTS")
    plt.ylabel("TOTAL CASES")
    plt.title("Districtwise Total Cases")
    plt.show()
def Pie_Chart():
    df=pd.read_csv("COVIDCASES.csv")
    dist= df['DISTRICT']
    tot=df['Total cases']
    rec=df['Recoveries']
    det=df['Deaths']
    d1=df['3-Nov']
    d2=df['4-Nov']
    d3=df['5-Nov']
    d4=df['6-Nov']
    d5=df['7-Nov']
    d6=df['8-Nov']
    d7=df['9-Nov']
    expl=[0,0.15,0,0.2,0]
    plt.title("Districtwise Deaths")
    plt.pie(det, labels=dist,explode=expl, autopct="%5.2f%%")
    plt.show()

def Scatter_Plot():
    df=pd.read_csv("COVIDCASES.csv")
    dist= df['DISTRICT']
    tot=df['Total cases']
    rec=df['Recoveries']
    det=df['Deaths']
    d1=df['3-Nov']
    d2=df['4-Nov']
    d3=df['5-Nov']
    d4=df['6-Nov']
    d5=df['7-Nov']
    d6=df['8-Nov']
    d7=df['9-Nov']
    ax=plt.gca()
    ax.scatter(dist, tot, color='b', label="Districtwise Total cases")
    ax.scatter(dist, rec, color='r', label="Districtwise Recovered cases")
    ax.scatter(dist, det, color='g', label="Ditrictwise Deaths")
    plt.xlabel("District")
    plt.xticks(rotation='vertical')
    plt.title("Complete Scatter chart")
    plt.legend()
    plt.show()
def data_sorting():
    df=pd.read_csv("COVIDCASES.csv")
    df.sort_values(["Total cases"], inplace=True)
    print(df)
    
        
def specific_records():
    df=pd.read_csv("COVIDCASES.csv")                   
    dist= df['DISTRICT']
    tot=df['Total cases']
    rec=df['Recoveries']
    det=df['Deaths']
    d1=df['3-Nov']
    d2=df['4-Nov']
    d3=df['5-Nov']
    d4=df['6-Nov']
    d5=df['7-Nov']
    d6=df['8-Nov']
    d7=df['9-Nov']
    top=int(input("How many records to display from top:"))
    print("First", top, "records")
    print(df.head(top))
        
op=int(input("Choose an option:"))
if op==1:
    Read_CSV()
elif op==2:
    print("LINE PLOT")
    line_plot()
elif op==3:
    print("BAR CHART")
    Bar_Chart()
elif op==4:
    print("PIE CHART")
    Pie_Chart()
elif op==5:
    print("SCATTER PLOT")
    Scatter_Plot()
elif op==6:
    data_sorting()
elif op==7:
    specific_records()
else:
    print("Wrong Input")
