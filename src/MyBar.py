class MyBar:
    def __init__(self, state_code, state_name) -> None:
        self.state_code = state_code
        self.state_name = state_name
        self.plotMyBar()

    def plotMyBar(self) -> None:
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt 

        df = pd.read_csv('data/data_charts/cases_by_counties_states.csv', index_col=0)
    
        df_state = df[df['state_code']==int(self.state_code)].sort_values(by='cases', ascending=False).head(5)
        df_state['cases_pct'] = df_state['cases']/(df_state['cases'].sum()) *100

        name = df_state['county_name']
        price = df_state['cases_pct']

        # Figure Size
        fig, ax = plt.subplots(figsize=(8,2.5))

        # Horizontal Bar Plot
        ax.barh(name, price)

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
                        fontsize=8, 
                        fontweight='bold',
                    color='grey')

        # Add Plot Title
        ax.set_title('Top 5 Counties in Covid-19 Cases ',loc='left' )
        plt.xlabel("Percentage of cases (%)")
        fig.tight_layout()
        plt.savefig('./images/barchar_top5_counties.png',)
        print('passou aqui ')
        




















        plt.figure(figsize=(8,2.5))
        by_counties = sns.countplot(y = 'cases',  data = df, palette = "Set2")
        # Show the plot
        plt.title(f'Count By {"Counties"} Group')
        plt.ylabel("")
        plt.xlabel("Number of Cases");
        fig = by_counties.get_figure()
        fig.savefig('./images/barchart_counties.png')
        pass