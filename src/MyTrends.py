class MyTrends:
    
    def __init__(self, state_code, state_name, engine) -> None:
        
        self.state_code = state_code
        self.state_name = state_name
        self.GetTrends(engine)

    def GetTrends(self, engine) -> None:
        
        import pandas as pd
        import matplotlib.pyplot as plt 
        from pathlib import Path
        import os 
        import psycopg2
        from sqlalchemy import text

        sql = "SELECT * FROM public.six_months_cases_"
        df = pd.read_sql(sql, engine)
        df['state_fips_code'] = df['state_fips_code'].astype(float)
        
        df_cases = df[df['state_fips_code']==float(self.state_code)];
        df_cases.set_index('case_month')
        plt.switch_backend('Agg') 
        ax =  df_cases.plot(figsize=(8,2.5));

        # Add Plot Title
        ax.grid(visible=True, color='grey',
                        linestyle='-.', linewidth=0.5,
                        alpha=0.2)
        plt.xlabel("")
        plt.ylabel("Number of Cases  ")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.get_xaxis().set_ticks([])       
        ax.legend().set_visible(False)

        print('Saving Trends..')
        if not os.path.exists("./images"):
            os.mkdir("./images")
        plt.savefig('./images/myTrends.png');
        print('.. Done!')