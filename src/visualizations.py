from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR=Path(__file__).resolve().parent.parent
DATA_PATH=BASE_DIR/"data"/"logistics_data.csv"
OUT=BASE_DIR/"visualizations"
OUT.mkdir(exist_ok=True)

def clean():
    df=pd.read_csv(DATA_PATH)
    for c in df.select_dtypes(include="number").columns:
        df[c]=df[c].fillna(df[c].median())
    for c in df.select_dtypes(exclude="number").columns:
        if df[c].isna().any(): df[c]=df[c].fillna(df[c].mode()[0])
    return df

def save(name):
    plt.tight_layout(); plt.savefig(OUT/name,dpi=200,bbox_inches="tight"); plt.close()

df=clean()

plt.figure(figsize=(8,5)); sns.histplot(df["Delivery_Time_min"],kde=True)
plt.title("Distribution of Delivery Time"); plt.xlabel("Delivery Time (minutes)"); plt.ylabel("Shipments"); save("delivery_time_distribution.png")

x=df.groupby("Region",as_index=False)["Delivery_Time_min"].mean()
plt.figure(figsize=(8,5)); sns.barplot(data=x,x="Region",y="Delivery_Time_min")
plt.title("Average Delivery Time by Region"); plt.xlabel("Region"); plt.ylabel("Minutes"); save("average_delivery_time_by_region.png")

x=df.groupby("Vehicle_Type",as_index=False)["Shipping_Cost"].mean()
plt.figure(figsize=(8,5)); sns.barplot(data=x,x="Vehicle_Type",y="Shipping_Cost")
plt.title("Average Shipping Cost by Vehicle Type"); plt.xlabel("Vehicle Type"); plt.ylabel("Cost"); save("shipping_cost_by_vehicle.png")

plt.figure(figsize=(8,5)); sns.scatterplot(data=df,x="Distance_km",y="Delivery_Time_min",hue="Traffic_Level")
plt.title("Distance vs Delivery Time"); plt.xlabel("Distance (km)"); plt.ylabel("Delivery Time (minutes)"); save("distance_vs_delivery_time.png")

plt.figure(figsize=(9,6)); sns.heatmap(df.select_dtypes("number").corr(),annot=True,fmt=".2f",cmap="Blues")
plt.title("Correlation Heatmap"); save("correlation_heatmap.png")
print("Charts saved in:",OUT)
