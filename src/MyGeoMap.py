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
df_zipcodes = pd.read_csv('./data/csv/zipcode_to_county.csv')

df = pd.read_csv('./data/csv/covid_cases_fips_wa.csv')

df.drop(columns='Unnamed: 0', inplace=True)
df.sort_values(by='county_fips_code',ascending=True)


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


fig = px.choropleth_mapbox(df, geojson=counties, locations='county_fips_code', color='case_month',
                           color_continuous_scale="Viridis",
                        #    color_continuous_scale="Blues",
                           range_color=(0, 120000),
                           mapbox_style="carto-positron",
                           zoom=5.2, 
                        #    center = {"lat": 47.3225, "lon": -121.0520},
                           opacity=0.5,
                           labels={'nr_cases':'Qtd Cases', 
                                   'nr_fips': 'FIP County ' },
                          )
config = {
    'color':'#1f77b4',
    'remove':[ "autoScale2d", "autoscale", "editInChartStudio", "editinchartstudio", 
              "hoverCompareCartesian", "hovercompare", "lasso", "lasso2d", "orbitRotation", 
              "orbitrotation", "pan", "pan2d", "pan3d", "reset", "resetCameraDefault3d", 
              "resetCameraLastSave3d", "resetGeo", "resetSankeyGroup", "resetScale2d", "resetViewMapbox", 
              "resetViews", "resetcameradefault", "resetcameralastsave", "resetsankeygroup", "resetscale", 
              "resetview", "resetviews", "select", "select2d", "sendDataToCloud", "senddatatocloud", "tableRotation", 
              "tablerotation", "toImage", "toggleHover", "toggleSpikelines", "togglehover", "togglespikelines", "toimage",
                "zoom", "zoom2d", "zoom3d", "zoomIn2d", "zoomInGeo", "zoomInMapbox", "zoomOut2d", "zoomOutGeo", 
                "zoomOutMapbox", "zoomin", "zoomout"] ,
    'orientation':'h'


 }
#     'scrollZoom': False,
#     # 'templateitemname':False,
#     # 'visible': False,
#     # 'displayModeBar': True,
#     # 'editable': True,
#     # 'showLink':False,
#     # 'displaylogo': False
# }


# print("dsfhsldkfh:",type(fig))
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, config=config)
# fig.update_layout(config = {'displayModeBar': False})
# print(fig.layout.__setattr__.
# print(fig.__dict__['_config'].keys())
# __setattr__('displayModeBar',False)

#fig._config['displayModeBar'] = False
# fig.show(config = {'displayModeBar': False})
# fig.__dict__['modebar_orientation']=  'v'
# fig.__dict__['modebar_orientation']=  'v'   
fig.update_layout(modebar=config)




print("..Done!")

### Creating a Folder images
if not os.path.exists("./images"):
    os.mkdir("./images")
fig.write_html("./images/mymap.html")
### Saving and exporting Maps as HTML
print("Generating html..")
#with Path("images/myfile.html").open("w") as f:
#    f.write(fig.to_html())

#with Path("images/myfile.html").open("w") as f:
 #   f.write(fig.to_html())

### Saving Maps as Images files
print("Saving images in directory..")

fig.write_image("./images/map1.png")
print("Saving images in directory..!")
#fig.write_image("images/fig1.jpeg")
fig.write_image("./images/map1.svg")
#fig.write_image("images/fig1.pdf")