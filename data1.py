from tkinter import S
import pandas as pd
import random
import statistics   


df = pd.read_csv("data.csv")

data = df["reading_time"].tolist()

allaverages=[]
for h in range(0,100):  
    sample_100=[]
    for m in range(0,100):
        s=random.randint(0,11126)
        d=data[s]
        sample_100.append(d)
    sample_100average=statistics.mean(sample_100)
    allaverages.append(sample_100average)

samplingmean=statistics.mean(allaverages)
print(samplingmean)

mean=statistics.mean(data)
print(mean)





            


