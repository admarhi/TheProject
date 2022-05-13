import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

#input stats and output cleared stats
filename = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'stats.csv')
outname = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'out.csv')

data=pd.read_csv(filename, sep=',')

#clearing stats
data['market_cap'] = data['market_cap'].str.replace(",", "").map(lambda x: x.lstrip('$'))
data['value'] = data['value'].str.replace(",", "").map(lambda x: str(x).lstrip('$'))

series_volume = []
for r in data['volume']:
    r = r.split()[0].lstrip('$').replace(",", "")
    if 'B' in r:
        r = float(r.rstrip('B'))
        r = r*1000000000
    series_volume.append(r)

data['volume'] = pd.Series(series_volume)

#changing to numbers
#data['value'] = pd.to_numeric(data['value'])
data = data.astype({'market_cap': 'float64', 'change': 'float64', 'value': 'float64', 'volume':'float64'})
data.to_csv(outname, index=False) 
print(data.dtypes)
#plottable_data = data[data['value']<1000]


#some sketchy plots
plt.figure(figsize=(20,5))
plot = sns.scatterplot(data=data, x="currency", y="value")
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
fig = plot.get_figure()
outplotname = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'out.png')
fig.savefig(outplotname) 


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


plt.figure(figsize=(20,20))
plot = sns.scatterplot(data=data, x="value", y="market_cap")
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
fig = plot.get_figure()
outplotname = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'value_mc.png')
fig.savefig(outplotname) 


#change in value vs (volume traded/marketcap *100)
data['vol_per_mc100'] = data['volume']/(data['market_cap']*100)
plt.figure(figsize=(20,20))
plot = sns.scatterplot(data=data, x="change", y="vol_per_mc100")
'''
#I want to have labels on each point, undone
for i in range(data.shape[0]):
    plt.text(x=data['change'][i]+0.3,y=data.GA[i]+0.3)
'''
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
fig = plot.get_figure()
outplotname = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'change_vol_per_mc100.png')
fig.savefig(outplotname) 


#easy to do:
all_mean_values = data.mean(axis=0)
print(all_mean_values)

all_std_values = data.std(axis=0)
print(all_std_values)
