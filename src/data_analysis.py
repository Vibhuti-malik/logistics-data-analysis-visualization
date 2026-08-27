from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "logistics_data.csv"

def load_data():
    return pd.read_csv(DATA_PATH)

def clean_data(df):
    df=df.copy()
    for c in df.select_dtypes(include="number").columns:
        df[c]=df[c].fillna(df[c].median())
    for c in df.select_dtypes(exclude="number").columns:
        if df[c].isna().any():
            df[c]=df[c].fillna(df[c].mode()[0])
    return df

def iqr_outliers(df,column):
    q1=df[column].quantile(.25); q3=df[column].quantile(.75)
    iqr=q3-q1
    return df[(df[column]<q1-1.5*iqr)|(df[column]>q3+1.5*iqr)]

def main():
    df=load_data()
    print("Shape:",df.shape)
    print("\nMissing values:\n",df.isna().sum())
    print("\nDescriptive statistics:\n",df.describe(numeric_only=True).round(2))
    clean=clean_data(df)
    print("\nAverage delivery time by region:\n",clean.groupby("Region")["Delivery_Time_min"].mean().round(2))
    print("\nAverage cost by vehicle:\n",clean.groupby("Vehicle_Type")["Shipping_Cost"].mean().round(2))
    print("\nOn-time rate:",round((clean["On_Time_Delivery"]=="Yes").mean()*100,2),"%")
    print("\nPotential delivery-time outliers:",len(iqr_outliers(clean,"Delivery_Time_min")))
    print("\nCorrelation matrix:\n",clean.select_dtypes("number").corr().round(2))
    clean.to_csv(BASE_DIR/"data"/"cleaned_logistics_data.csv",index=False)

if __name__=="__main__":
    main()
