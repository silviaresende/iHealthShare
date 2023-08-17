class MyBar:
    def __init__(self, state_code, state_name, engine) -> None:
        self.state_code = state_code
        self.state_name = state_name
        self.plotMyBar(engine)

    def plotMyBar(self, engine) -> None:
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt
        from pathlib import Path
        import os 
        import psycopg2
        from sqlalchemy import text

        
        sql = "SELECT * FROM public.cases_by_counties_states_"
        
        # df = pd.read_sql(sql, engine)
        df = pd.read_sql_query(text(sql), engine)
        #df = pd.read_csv('./data/data_charts/cases_by_counties_states.csv', index_col=0)
        df['state_code'] = df['state_code'].astype('Int64')
        df_state = df[df['state_code']==int(self.state_code)].sort_values(by='cases', ascending=False).head(5)
        df_state['cases_pct'] = df_state['cases']/(df_state['cases'].sum()) *100

        name = df_state['county_name']
        price = df_state['cases_pct']

        # Figure Size
        fig, ax = plt.subplots(figsize=(7,2.5))

        # Horizontal Bar Plot
        ax.barh(name, price, color='purple')

        # Add padding between axes and labels
        ax.xaxis.set_tick_params(pad=2)
        ax.yaxis.set_tick_params(pad=2)

        # Add x, y gridlines
        ax.grid(visible=True, color='grey',
                linestyle='-.', linewidth=0.5,
                alpha=0.2)

        # Show top values
        ax.invert_yaxis()

        # Add annotation to bars
        for i in ax.patches:
            plt.text(	i.get_width()+0.1, 
                        # i.get_width()+0.2, 
                        i.get_y()+0.5,
                        str(round((i.get_width()), 1)),
                        fontsize=9, 
                        # fontweight='bold',
                    color='black')

        # Add Plot Title
        #ax.set_title('Top 5 Counties in Covid-19 Cases ',loc='left' )
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.get_xaxis().set_ticks([])
        # ax.get_yaxis().set_ticks([])
        plt.xlabel("Percentage of cases (%)")
        fig.tight_layout()

        print('Saving BarChart..')
        if not os.path.exists("./images"):
            os.mkdir("./images")
        fig.savefig('./images/myBarChart.png',)
        
       