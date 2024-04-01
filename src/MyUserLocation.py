
from src.MyConnection import *

class MyUserLocation:
    
    def __init__(self, zipcode, engine):
        
        
        self.zipcode = zipcode
        print('Getting user State and County codes..')
        self.getStateUser(engine)
        pass

    def getStateUser(self, engine):

        import pandas as pd
        import psycopg2
        
        sql = "SELECT * FROM public.zipcode_to_county_"
        df = pd.read_sql(sql, engine)
        print('opa',type(df.head()))

        sql = 'SELECT * FROM public.fips_state_'
        df_ = pd.read_sql(sql, engine)
        
        df_['id'] = df_['id'].astype('Int64')
        df_['region'] =df_['region'].astype('Int64')
        df_['division'] =df_['division'].astype(int)
        df_['state_fips'] =df_['state_fips'].astype('Int64')
        
        print("ui",df[df['ZTCA5']=='98125'])
        
        self.user_state = str(df[df['ZTCA5']==str(self.zipcode)].iloc[0]['STATE'])
        
        self.user_county = str(df[df['ZTCA5']==str(self.zipcode)].iloc[0]['COUNTY'])
        self.user_state_name = str(df_[df_['state_fips']==int(self.user_state)].iloc[0]['name'])


    