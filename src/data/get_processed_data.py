import numpy as np
import pandas as pd
import os 

def read_data():
    # set the path of the raw data
    raw_data_path = os.path.join(os.path.pardir,'data','raw')

    train_file_path=os.path.join(raw_data_path,'hungarian.processed.data')
    test_file_path=os.path.join(raw_data_path,'cleveland.processed.data')
    # read the data with all default parameters
    train_df=pd.read_csv(train_file_path, header=None)
    test_df=pd.read_csv(test_file_path, header=None)
    test_df['diagnosed'] = -888
    df = pd.concat((train_df, test_df), axis=0)
    return df



def process_data(df):
    # using the method chaining concept
    return (df

         # working missing values - start with this
         .pipe(fill_missing_values)
         # create fare bin feature
         .assign(trestbps_Bin = lambda x: pd.qcut(x.trestbps, 4, labels=['very_low','low','high','very_high']))
         # create age state
         .assign(AgeState = lambda x : np.where(x.age >= 60, 'OldAdult','MiddleAdult'))
          # create cat feature
         .assign(cat = lambda x : x.thalach.map(get_deck))
         # feature encoding 
          .pipe(pd.get_dummies, columns=['trestbps_Bin', 'AgeState', 'cp', 'cat'])
         # reorder columns
         .pipe(reorder_columns)
         )

# extract first character of Cabin string to the deck
def get_deck(thalach):
    if thalach < 100 : cat = 'A'
    elif thalach < 120 : cat = 'B'
    elif thalach < 140 : cat = 'C'
    elif thalach < 160 : cat = 'D'
    elif thalach < 180 : cat = 'E'
    elif thalach < 200 : cat = 'F'
    else               : cat = 'G'
    return np.where(pd.notnull(thalach), cat,'Z')

def fill_missing_values(df):
    # replace the missing values with '0'
    df.restecg.fillna('0', inplace=True)
    # trestbps
    median_trestbps = df.loc[(df.cp==4) & (df.restecg == '0'), 'trestbps'].median()
    df.trestbps.fillna(median_trestbps, inplace=True)
    return df

def reorder_columns(df):
    # reorder columns
    columns = [column for column in df.columns if column !='diagnosed']
    columns = ['diagnosed'] + columns
    df = df[columns]
    return df 

    
def write_data(df):
    processed_data_path = os.path.join(os.path.pardir,'data','processed')
    write_train_path=os.path.join(processed_data_path,'train.csv')
    write_test_path = os.path.join(processed_data_path,'test.csv')
    # train data
    df.loc[df.diagnosed !=-888].to_csv(write_train_path)
    
    #test data
    #columns = [column for column in df.columns if column !='diagnosed']
    #df.loc[df.diagnosed == -888, columns].to_csv(write_test_path)
    df.loc[df.diagnosed == -888].to_csv(write_test_path)

if __name__ == '__main__':
    df = read_data()
    df = process_data(df)
    write_data(df)
