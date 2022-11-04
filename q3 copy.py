# Imports
import pandas as pd
from datetime import datetime

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    d = {'nom': ['Valtonic', 'Oriol', 'Marta', 'Jordi'], 'data_ini': ['03/11/2017','01/11/2017','23/02/2018','16/10/2017']}
    df = pd.DataFrame(data=d)

    df['data_ini'] = pd.to_datetime(df['data_ini'])

    df.sort_values(by='data_ini',ascending=True, inplace=True)

    today = datetime.today()
    df['difference'] = (today - df['data_ini']).dt.days + 1
    print(df)


# -----------------------------------------------------------------------------
