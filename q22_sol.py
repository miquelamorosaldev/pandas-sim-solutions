# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: WRITE YOUR NAME HERE
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: get_total_deaths()
# -----------------------------------------------------------------------------
# 
# - You are given the fixed Tycho dataset.
# - Write a function to view the ranking of diseases by number of total deaths 
# - at year 1896 in Massachussetts state (MA).
# 
# - Return parameters:
#   - Return a dataframe.
#   - The dataframe must have 3 columns in this order: ranking, disease, num_deaths.
#   - The ranking must start at 1
#   - The index must be numerical, starting from 0.
# 
# - Hint:
# - A Percentage is calculated by the mathematical formula of dividing the value by the sum of 
# - all the values and then multiplying the sum by 100. 
# - This is also applicable in Pandas Dataframes. 
# - The pre-defined sum() method of pandas series is used to compute the sum 
# - of all the values of a column.
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - Run pytest to make sure you succeeded.
# -----------------------------------------------------------------------------


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_total_deaths(entries: pd.DataFrame) -> pd.DataFrame:

    ranking_deaths: pd.DataFrame = ( entries.loc[:, ['year', 'disease', 'num_deaths', 'state']]
                                    .query('year == 1896')
                                    .query('state == "MA"')
                                    .groupby(by='disease')
                                    .sum()
                                    .sort_values(by='num_deaths', ascending=False)
                                    .reset_index()
                                    .assign(ranking=lambda df: df.index + 1)
                                )


    # entries.loc[:, ['num_deaths']].sum() => counts 
    ranking_deaths = ranking_deaths.reindex(columns=['ranking', 'disease', 'num_deaths'])

    return ranking_deaths


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed22.csv", sep=",")
    print(entries.dtypes)

    ranking_deaths:  pd.DataFrame = get_total_deaths(entries)
    print (ranking_deaths)
    
    # Percent of deaths compared to total population in MA state.
    total_pop_1896 = 2505346

    percent_deaths = (ranking_deaths.loc[:,'num_deaths'].sum() 
        / total_pop_1896 ) * 100

    print(percent_deaths, " %")


# -----------------------------------------------------------------------------
