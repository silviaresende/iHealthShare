class MyUserLocation:
    

    def __init__(self, zipcode):
        self.zipcode = zipcode
        print('Initializing..')
        self.getStateUser()
        pass

    def getStateUser(self):
        import pandas as pd
        print('entrouno methodo')
        df = pd.read_csv('./data/csv/zipcode_to_county.csv')
        df.drop(columns='Unnamed: 0', inplace=True)
        
        self.user_state = df[df['ZCTA5']==int(self.zipcode)].iloc[0]['STATE']
        self.user_county = df[df['ZCTA5']==int(self.zipcode)].iloc[0]['COUNTY']
