import pandas as pd

def get_codeup_data():
    """
    No argument(s) needed. Acquires and returns codeup curriculum page logs and cohort data.
    """
    # reading in log data from local csv file and converting to DF
    logs = pd.read_csv('anonymized-curriculum-access.txt', sep=" ", header=None, na_values='"-"')

    # set column names for logs DF
    logs.columns=['date', 'time', 'page_viewed','user_id','cohort_id','ip']

    # reading in cohort data from local csv file and converting to DF
    cohorts = pd.read_csv('cohorts.csv')

    return logs, cohorts