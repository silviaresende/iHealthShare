class MyBarChart:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        print("Generating barchart referente ao estado de ", self.zipcode)

## importing libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import os

### Code from barcharts.ipynb
print("Loadiing  datasets for BarChart visualizations..")
df = pd.read_csv('../data/cdc_covid_geo.csv',
                 dtype={"county_fips_code": str, 
                 "state_fips_code": str})
print("..Done!")

df.drop(columns='Unnamed: 0', inplace=True)

df_barchar = df['res_state'].value_counts(normalize=True, ascending=True)
df_cases_state = pd.DataFrame(df_barchar) 

plt.figure(figsize=(15, 10));

by_states = sns.barplot(data=df_cases_state, x=df_cases_state.index, y=df_cases_state['res_state']);
by_states.set_xticklabels(by_states.get_xticklabels(), 
                          rotation=90, 
                          horizontalalignment='right');

fig = by_states.get_figure()
print("saving barplot in images directory")
if not os.path.exists("../images"):
    os.mkdir("../images")
fig.savefig('../images/barchart_state.png')
