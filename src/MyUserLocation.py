class MyUserLocation:
    

    def __init__(self, zipcode):
        self.zipcode = zipcode
        print('Getting user State and County codes..')
        self.getStateUser()
        pass

    def getStateUser(self):
        import pandas as pd
        
        df = pd.read_csv('./data/csv/zipcode_to_county.csv')
        df.drop(columns='Unnamed: 0', inplace=True)
        df_ = pd.read_csv('./data/csv/fips_state.csv')
        
        self.user_state = str(df[df['ZCTA5']==int(self.zipcode)].iloc[0]['STATE'])
        self.user_county = str(df[df['ZCTA5']==int(self.zipcode)].iloc[0]['COUNTY'])
        self.user_state_name = str(df_[df_['State (FIPS)']==int(self.user_state)].iloc[0]['Name'])
        
    