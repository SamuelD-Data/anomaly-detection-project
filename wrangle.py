import pandas as pd

def get_codeup_data():
    """
    No argument(s) needed. Acquires codeup curriculum visitor data and returns as DF with datetime column set as index.
    """
    # read data from local csv file
    data = pd.read_csv('anonymized-curriculum-access.txt', sep=" ", header=None, na_values='"-"')

    # set column names for DF
    data.columns=['date', 'time', 'page_viewed','user_id','cohort_id','ip']

    # concat date and time columns to create datetime column
    data['datetime'] = data['date'] + ' ' + data['time']

    # convert datetime column type to datetime data type
    data['datetime'] = pd.to_datetime(data.datetime)

    # set index to datetime column
    data = data.set_index('datetime')

    return data