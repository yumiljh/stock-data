import tushare as ts
import sys,os
import time

reload(sys)
sys.setdefaultencoding("utf-8")

date2=time.strftime("%Y-%m-%d")

df = ts.get_stock_basics()
#test_arr = ['601398']

counter = 1

filepath='/home/ali/Documents/stocks/'

for strx in df.index:
#for x in test_arr:
#strx=str(x)
    if counter == 0:
        break

    date1=df.ix[strx]['timeToMarket']
#namepart=str(df.ix[strx]['industry']).decode(encoding="utf-8")
    date1=str(date1)
    date1=date1[0:4]+"-"+date1[4:6]+"-"+date1[6:8]
    date1 = '2017-01-01'
#filename=filepath + namepart + "/" + strx + ".csv"
    filename = filepath + strx + ".csv"
    if os.path.exists(filename):
        continue
    else:
        dataframe=ts.get_h_data(strx,start=date1,end=date2,retry_count=30,pause=3)
        dataframe['code'] = strx
        dataframe.to_csv(filename, header=None, encoding='gb2312')
    counter = counter -1

