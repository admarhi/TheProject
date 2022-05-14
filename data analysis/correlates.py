import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

filename = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'stats_clear.csv')
data=pd.read_csv(filename, sep=',')
#plottable_data = data[data['value']<1000] 
print(data.columns)
#plotting 
plt.figure(figsize=(30,5))

data['value tresholds'] = pd.cut(data["value"], [0, 10, 500, 5000, 50000], labels=["<10$","10-500$", "500-5000$", ">5000"])

plot = sns.scatterplot(data=data, x="currency", y="volume", hue='change', size='value tresholds', sizes={"<10$":10,"10-500$":50, "500-5000$":150, ">5000":300},)#, palette=['turquoise', 'orange','crimson'])
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
fig = plot.get_figure()
outplotname = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'volume, change and value of each currency.png')
fig.savefig(outplotname, bbox_inches='tight') 

'''
plt.figure(figsize=(20,5))
plot = sns.scatterplot(data=data, x="currency", y="change")
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
fig = plot.get_figure()
outplotname = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'out2.png')
fig.savefig(outplotname) 


plt.figure(figsize=(20,5))
plot = sns.scatterplot(data=data, x="currency", y="market_cap")
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
fig = plot.get_figure()
outplotname = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'outmc.png')
fig.savefig(outplotname) 
'''

plt.figure(figsize=(20,20))
plot = sns.scatterplot(data=data, x="value", y="market_cap")
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
fig = plot.get_figure()
outplotname = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'value vs market cap.png')
fig.savefig(outplotname, bbox_inches='tight') 


#change in value vs (volume traded/marketcap *100)
data['vol_per_mc100'] = data['volume']/(data['market_cap']*100)
plt.figure(figsize=(20,20))
plot = sns.scatterplot(data=data, x="change", y="vol_per_mc100", size="value tresholds", sizes={"<10$":10,"10-500$":50, "500-5000$":150, ">5000":300})
'''
#I want to have labels on each point, undone
#
for i in range(data.shape[0]):
    plt.text(x=data['change'][i]+0.3,y=data.GA[i]+0.3)
'''
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
fig = plot.get_figure()
outplotname = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'change_vs_vol_per_mc100.png')
fig.savefig(outplotname) 


#easy to do:
all_mean_values = data.mean(axis=0)
print(all_mean_values)

all_std_values = data.std(axis=0)
print(all_std_values)
