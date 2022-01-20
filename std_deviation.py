import pandas as pd
import statistics
df=pd.read_csv(r"C:\Users\Vinod Thakare\Desktop\Standard_deviation-master\solution\data.csv")
data=df["Data"]
std=statistics.stdev(data)
print(std)