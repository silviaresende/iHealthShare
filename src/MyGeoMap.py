class MyGeoMap:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        #self.urlopen = urlopen
        print("objeto instanciado referente ao estado de ", self.zipcode)

### Importing libraries ### 
from urllib.request import urlopen
import json 
import plotly.express as px
import pandas as pd
from pathlib import Path
import os
###########################

#### Code from covid_cases_map.ipynb

### Getting data from Github ###
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
df_ = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

## Loading local datasets ###
print("Loading datasets for GeoMaps..")
df_zipcodes = pd.read_csv('../data/csv/zipcode_to_county.csv')
df = pd.read_csv('../data/csv/covid_cases_fips_wa.csv')
df.drop(columns='Unnamed: 0', inplace=True)
df.sort_values(by='nr_fips',ascending=True)


### Plotting Map ###
# fig = px.choropleth(df, 
                    # geojson=counties, 
                    # locations='nr_fips', 
                    # color='nr_cases',
                    # color_continuous_scale="Blues",
                    # range_color=(0, 120000),
                    # scope="usa",
                    # labels={'unemp':'unemployment rate'}
                        #   )
# fig.update_geos(fitbounds="locations", visible=False)
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()


fig = px.choropleth_mapbox(df, geojson=counties, locations='nr_fips', color='nr_cases',
                           color_continuous_scale="Viridis",
                        #    color_continuous_scale="Blues",
                           range_color=(0, 120000),
                           mapbox_style="carto-positron",
                           zoom=5.2, 
                           center = {"lat": 47.3225, "lon": -121.0520},
                           opacity=0.5,
                           labels={'nr_cases':'Qtd Cases', 
                                   'nr_fips': 'FIP County ' }
                          )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()


print("..Done!")

### Creating a Folder images
if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_html("../images/mymap.html")
### Saving and exporting Maps as HTML
print("Generating html..")
#with Path("images/myfile.html").open("w") as f:
#    f.write(fig.to_html())

#with Path("images/myfile.html").open("w") as f:
 #   f.write(fig.to_html())

### Saving Maps as Images files
print("Saving images in directory..")
fig.write_image("../images/map1.png")
#fig.write_image("images/fig1.jpeg")
fig.write_image("../images/map1.svg")
#fig.write_image("images/fig1.pdf")