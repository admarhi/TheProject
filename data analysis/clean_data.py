import pandas as pd
import os

#paths input stats and output cleared stats
filename = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'stats.csv')
outname = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'stats_clear.csv')

data=pd.read_csv(filename, sep=',')

#clearing the commas and dollar signs from respectable fields
data['market_cap'] = data['market_cap'].str.replace(",", "").map(lambda x: x.lstrip('$'))
data['value'] = data['value'].str.replace(",", "").map(lambda x: str(x).lstrip('$'))

#clearing the all volume field and converting short B to proper billion
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
#print(data.dtypes)