class MyMap:
    
    def __init__(self,state_code, state_name, st) -> None:
        self.state_code = state_code
        self.state_name = state_name
        self.load_data(st)
        
        pass


    def load_data(self,st)-> None:
        
        import pandas as pd
        from urllib.request import urlopen
        import json 
        import plotly.express as px
        from pathlib import Path
        import os
        import psycopg2
        
        engine = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="_healthshare123",
            host="healthshare.crpizus8bidb.us-east-2.rds.amazonaws.com",
            port='5432'
        )

        # df = pd.read_csv('./data/data_charts/cases_by_counties_states.csv', index_col=0, dtype={
        #     'state_code': int,
        #     'state_res': str,
        #     'state_name': str,
        #     'county_fips_code':	str,
        #     'county_name': str
        # })
        sql = "SELECT * FROM public.cases_by_counties_states_"
        
        df = pd.read_sql(sql, engine)

        # data = df[df['state_code']=='06']
        df['state_code'] =df['state_code'].astype('Int64')
        data = df[df['state_code']==int(self.state_code)]
        # print('hello:', self.state_code, df[df['state_code']=='53'].shape[0])
        print('State Code:', self.state_code)
        print('Number of Counties:', df[df['state_code']==int(self.state_code)].shape[0])

        with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
            counties = json.load(response)

        # df_lat_lon = pd.read_csv('./data/csv/us-state-capitals.csv')
        
        
       
        sql = "SELECT * FROM public.us_state_capitals_"
        
        df = pd.read_sql(sql, engine)
        
        df['latitude'] = df['latitude'].astype(float)
        df['longitude'] = df['longitude'].astype(float)
        df_lat_lon = df
        latitude = df_lat_lon[df_lat_lon['name']==self.state_name].iloc[0,2]
        longitude = df_lat_lon[df_lat_lon['name']==self.state_name].iloc[0,3]
        
        lat_log = dict(zip(['lat', 'lon'], [latitude, longitude]))
        print('Lat/log:', lat_log)
        print('=====================================')
        print(' ')

        fig = px.choropleth_mapbox(data, geojson=counties, locations='county_fips_code', color='cases',
                           color_continuous_scale="Viridis_r",
                        #    color_continuous_scale="Blues",
                           range_color=(0, 120000),
                           mapbox_style="carto-positron",
                           zoom=5, center = lat_log,
                           #zoom=1.5, 
                           # center = {"lat": 47.3225, "lon": -121.0520},
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

        fig.update_layout(modebar=config)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        #fig.write_html('./images/MyMap_'f'{self.state_name}.html')
        st.write("here!")
        print('Saving MyMap..')
        if not os.path.exists("./images"):
            os.mkdir("./images")

        with Path("./images/myMap.html").open("w") as f:
            f.write(fig.to_html())
        
        #fig.write_html('./images/mymap.html')
        fig.write_image("./images/myMap.png")
        fig.write_image("./images/myMap.svg")
        #fig.show()






