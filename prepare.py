import pandas as pd

def combine_codeup_data(logs, cohorts):
    """
    Accepts logs and cohorts data frames. Merges DFs on cohort ID while preserving all log rows. Adds datetime index. 
    Returns updated DF.
    """
    # concat date and time columns to create datetime column
    logs['datetime'] = logs['date'] + ' ' + logs['time']

    # convert datetime column type to datetime data type
    logs['datetime'] = pd.to_datetime(logs.datetime)

    # dropping date and time columns since we combined them for index
    logs.drop(columns = ['date', 'time'], inplace=True)

    # performing left join to combine DFs while preserving all log data rows 
    # since some rows don't have a cohort id to join on
    combo = pd.merge(left = logs, right = cohorts, how = 'left', left_on = 'cohort_id', right_on = 'cohort_id')

    # set index to datetime column
    combo = combo.set_index('datetime')

    # returning DF
    return combo

def null_filler(df):
    """
    Accepts DF. Fills null values with values specified in notebook. Returns DF.
    """
    # using fillna to fill null values with specified values
    df['page_viewed'] = df['page_viewed'].fillna('PageUnknown')
    df['cohort_id'] = df['cohort_id'].fillna(0)
    df['name'] = df['name'].fillna('unknown')
    df['start_date'] = df['start_date'].fillna('01-01-1900')
    df['end_date'] = df['end_date'].fillna('01-01-1900')
    df['program_id'] = df['program_id'].fillna(0)

    # returning df
    return 