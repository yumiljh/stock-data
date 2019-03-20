import tushare as ts
import os,sys

reload(sys)
sys.setdefaultencoding("utf-8")

df = ts.get_today_all()

filename='/home/ali/Documents/stocks/20180206.csv'
if os.path.exists(filename):
    df.to_csv(filename,mode='a',header=None,encoding='utf-8')
else:
    df.to_csv(filename,header=None,encoding='utf-8')


