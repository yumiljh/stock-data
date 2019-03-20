import tushare as ts
import os,sys

reload(sys)
sys.setdefaultencoding("utf-8")

df = ts.get_stock_basics()

filename='/home/ali/Documents/stocks/stock_basics2.csv'
if os.path.exists(filename):
    df.to_csv(filename,mode='a',header=None,encoding='gb2312')
else:
    df.to_csv(filename,header=None,encoding='gb2312')


