import pandas as pd
from datetime import datetime

class Transf:
    
    def __init__(self, path_csv, path_class, columns):

        self.columns = columns
        self.path_csv = path_csv
        self.path_class = path_class

        self.df = self.importData()
        self.df = self.columnSelect()
        self.df.date = self.stringToDate() # replaces values with new types
        self.df = self.joinClass()

    def importData(self):
        # Import file into pandas dataframe
        df = pd.read_csv(self.path_csv)
        return df
    
    def columnSelect(self):
        return self.df[self.columns]
    
    def stringToDate(self):
        dates = [] # list where dates will be appended
        for date in self.df.date.values:
            d = datetime.strptime(date[0:19], '%Y-%m-%d %H:%M:%S') # this method converts string into datetime type
            dates.append(d)
        return pd.Series(data=dates, index=self.df.index) # converts list to series
    
    def joinClass(self):
        class_col = pd.read_csv(self.path_class)
        return self.df.join(class_col.set_index('id'), on='id')

    def returnData(self):
        return self.df
