class MyTrends:
    def __init__(self, state_code, state_name) -> None:
        self.state_code = state_code
        self.state_name = state_name
        self.GetTrends()

    def GetTrends(self) -> None:
        import pandas as pd
        import matplotlib.pyplot as plt 
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
        sql = "SELECT * FROM public.six_months_cases_by_counties_states_"
        print("ops aqui")
        df = pd.read_sql(sql, engine)
        print("Chegou aqui e leu o dado")
        # df = pd.read_csv('./data/data_charts/6_months_cases_by_counties_states.csv', index_col=0)
        df['state_fips_code'] = df['state_fips_code'].astype(float)
        
        data = df[df['state_fips_code']==float(self.state_code)];
        # data = df[df['state_fips_code']==float(self.state_code)];
        data['case']= 1;
        df_cases = data[['case_month', 'case']]
        df_cases= pd.DataFrame(df_cases.groupby(by='case_month').value_counts())
        # df_cases.plot(figsize=(8,2.5), title="Number of Covid-19 Cases over 6 months");
        
        ax =  df_cases.plot(figsize=(8,2.5));

        # Add Plot Title
        ax.grid(visible=True, color='grey',
                        linestyle='-.', linewidth=0.5,
                        alpha=0.2)
        ax.set_title("Trends Over Last Six Months",loc='left' )
        plt.xlabel("")
        plt.ylabel("Number of Cases  ")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.get_xaxis().set_ticks([])
        #ax.get_yaxis().set_ticks([])        
        ax.legend().set_visible(False)


        print('Saving Trends..')
        if not os.path.exists("./images"):
            os.mkdir("./images")
        plt.savefig('./images/myTrends.png');
        print('.. Done!')
        engine.close()
        

       
