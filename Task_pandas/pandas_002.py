import pandas as pd

k = pd.read_csv("uk-50_trial.csv")
data = pd.DataFrame(k)
head1 = data.head(15)
#print(head1.to_csv("new_uk.csv"))

new = pd.read_csv("new_uk.csv")
data2 = pd.DataFrame(new)
#print(data2)

for i in range(1,5):
    if i==2:
        l = data2.loc[i]
        #print(l.to_json("01new.json"))

json01 = pd.read_json("01new.json")
j = pd.DataFrame(json01)
print(j)