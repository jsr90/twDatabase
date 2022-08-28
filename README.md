# How to use twDatabase

## Data transformation

From csv files and predictions obtained in previous projects ([twStrap](https://github.com/jsr90/twScrap) and [twNLP](https://github.com/jsr90/twNLP)), we can get a new dataframe with necessary columns to fill our database. To do so, I have created the Transf class which quickly returns our new dataframe:


```python
from classes.Transf import Transf

csv_path = 'data/input/tweets_svq.csv'
class_path = 'data/input/preds_svq.csv'
columns = ['id', 'date', 'user', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount']

df_svq = Transf(csv_path, class_path, columns).returnData()
df_svq.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>user</th>
      <th>replyCount</th>
      <th>retweetCount</th>
      <th>likeCount</th>
      <th>quoteCount</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1523089210047344640</td>
      <td>2022-05-07 23:55:39</td>
      <td>https://twitter.com/jachainv</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1523088314697494529</td>
      <td>2022-05-07 23:52:06</td>
      <td>https://twitter.com/GP_Zuri</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1523086850583580672</td>
      <td>2022-05-07 23:46:17</td>
      <td>https://twitter.com/Verde_seguro</td>
      <td>3</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1523085987911733248</td>
      <td>2022-05-07 23:42:51</td>
      <td>https://twitter.com/GhoulRas</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1523084505380237315</td>
      <td>2022-05-07 23:36:58</td>
      <td>https://twitter.com/albarsnchez</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_svq.isna().sum()
```




    id              0
    date            0
    user            0
    replyCount      0
    retweetCount    0
    likeCount       0
    quoteCount      0
    class           0
    dtype: int64




```python
from classes.Transf import Transf

csv_path = 'data/input/tweets_mlg.csv'
class_path = 'data/input/preds_mlg.csv'

df_mlg = Transf(csv_path, class_path, columns).returnData()
df_mlg.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>user</th>
      <th>replyCount</th>
      <th>retweetCount</th>
      <th>likeCount</th>
      <th>quoteCount</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1561140591320260609</td>
      <td>2022-08-20 23:58:16</td>
      <td>https://twitter.com/MalacitanoWeb</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1561140440426061826</td>
      <td>2022-08-20 23:57:40</td>
      <td>https://twitter.com/MalacitanoWeb</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1561140425376808960</td>
      <td>2022-08-20 23:57:36</td>
      <td>https://twitter.com/shotbymarcos</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1561139949973405697</td>
      <td>2022-08-20 23:55:43</td>
      <td>https://twitter.com/claunavarro777</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1561139807484518402</td>
      <td>2022-08-20 23:55:09</td>
      <td>https://twitter.com/TheSenior_</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_mlg.isna().sum()
```




    id              0
    date            0
    user            0
    replyCount      0
    retweetCount    0
    likeCount       0
    quoteCount      0
    class           0
    dtype: int64



## Database

### Connection to the database

I have previously installed and configured MySQL in my system.


```python
from classes.Db import TwDb
import mysql.connector

host = 'localhost'
user = 'root'
passwd = 'rootROOT90.'
database = 'tweets_db'

db = TwDb(host, user, passwd, database)
db.conn()
```

    Connection stablished.


### Execute queries

#### Create table


```python
# Drop table if already exists
query = 'DROP TABLE IF EXISTS tblTweets'
db.executeQuery(query)

# Create the table Tweets
query='''
CREATE TABLE tblTweets (id VARCHAR(30) NOT NULL,
					date DATETIME NOT NULL,
                    user VARCHAR(50) NOT NULL,
                    replyCount SMALLINT UNSIGNED NOT NULL,
                    retweetCount SMALLINT UNSIGNED NOT NULL,
					likeCount INT UNSIGNED NOT NULL,
                    quoteCount SMALLINT UNSIGNED NOT NULL,
                    class SMALLINT NOT NULL,
                    PRIMARY KEY(id));
                    '''
db.executeQuery(query)
```

    Query successfully executed.
    Query successfully executed.


#### Fill table from dataframes


```python
db.fillTable(df_svq, 'tblTweets')
db.fillTable(df_mlg.drop(index=1264), 'tblTweets')
```

    The table tblTweets has been filled.
    The table tblTweets has been filled.


#### Show results from query


```python
a = db.executeQuery('''SELECT * FROM tblTweets ORDER BY likeCount DESC LIMIT 15;''')
a.head()
```

    Query successfully executed.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>user</th>
      <th>replyCount</th>
      <th>retweetCount</th>
      <th>likeCount</th>
      <th>quoteCount</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1560610627189673984</td>
      <td>2022-08-19 12:52:22</td>
      <td>https://twitter.com/galiindo13</td>
      <td>1040</td>
      <td>25154</td>
      <td>199185</td>
      <td>1855</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1560611935481126912</td>
      <td>2022-08-19 12:57:34</td>
      <td>https://twitter.com/FonsiLoaiza</td>
      <td>461</td>
      <td>9223</td>
      <td>16258</td>
      <td>225</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1559935276403027968</td>
      <td>2022-08-17 16:08:46</td>
      <td>https://twitter.com/RubenSanchezTW</td>
      <td>211</td>
      <td>2125</td>
      <td>8805</td>
      <td>52</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1521750798287351811</td>
      <td>2022-05-04 07:17:17</td>
      <td>https://twitter.com/NoaGresiva</td>
      <td>108</td>
      <td>2258</td>
      <td>6447</td>
      <td>33</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1522246171305123841</td>
      <td>2022-05-05 16:05:43</td>
      <td>https://twitter.com/Yolanda_Diaz_</td>
      <td>807</td>
      <td>829</td>
      <td>5917</td>
      <td>124</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



#### Close connection


```python
db.disconn()
```

    Connection closed.


The database is now filled and ready to use.
