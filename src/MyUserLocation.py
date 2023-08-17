class MyUserLocation:
    

    def __init__(self, zipcode):
        self.zipcode = zipcode
        print('Getting user State and County codes..')
        self.getStateUser()
        pass

    def getStateUser(self):
        import pandas as pd
        import psycopg2
        
        engine = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="_healthshare123",
            host="healthshare.crpizus8bidb.us-east-2.rds.amazonaws.com",
        port='5432')

        # df = pd.read_csv('../data/csv/zipcode_to_county.csv')
        # df.drop(columns='Unnamed: 0', inplace=True)
        sql = "SELECT * FROM public.zipcode_to_county_"
        df = pd.read_sql(sql, engine)

        sql = 'SELECT * FROM public.fips_state_'
        df_ = pd.read_sql(sql, engine)
        # df_ = pd.read_csv('../data/csv/fips_state.csv')
        df_['id'] = df_['id'].astype('Int64')
        df_['region'] =df_['region'].astype('Int64')
        df_['division'] =df_['division'].astype(int)
        df_['state_fips'] =df_['state_fips'].astype('Int64')
        print("zipcode")
        self.user_state = str(df[df['zcta5']==int(self.zipcode)].iloc[0]['state'])
        self.user_county = str(df[df['zcta5']==int(self.zipcode)].iloc[0]['county'])
        self.user_state_name = str(df_[df_['state_fips']==int(self.user_state)].iloc[0]['name'])
        
    