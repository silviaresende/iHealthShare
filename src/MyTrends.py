class MyTrends:
    def __init__(self, state_code, state_name) -> None:
        self.state_code = state_code
        self.state_name = state_name
        self.GetTrends()

    def GetTrends(self) -> None:
        import pandas as pd
        import matplotlib.pyplot as plt 

        
        
        df = pd.read_csv('./data/data_charts/6_months_cases_by_counties_states.csv', index_col=0)
        
        data = df[df['state_fips_code']==int(self.state_code)];
        data['case']= 1
        df_cases = data[['case_month', 'case']]
        df_cases= pd.DataFrame(df_cases.groupby(by='case_month').value_counts())
        df_cases.plot(figsize=(8,2.5), title="Number of Covid-19 Cases over 6 months");
        
        print('Saving Trends plot..')
        plt.savefig('./images/state_trends.png');
        print('.. Done!')
        
