import pandas as pd

with open ("C:/Users/Harpreet/.rasabot/exp.csv",'rb')as file:
    reader =pd.read_csv(file)
intents=[i for i in reader['Intent']]
expressions=[i for i in reader["Expression"]]
intt=[]
for intent,expression in zip(intents,expressions):
    intt.append((intent,expression))

unique_intents =set(intents)
with open("C:/Users/Harpreet/.rasabot/train_csvtonlu.md",'w') as file:
    for intent in unique_intents:
        file.write("## intent: {}\n".format(intent))
        for element in intt:
            if element[0] == intent:
                file.write("- {}\n".format(element[1]))
