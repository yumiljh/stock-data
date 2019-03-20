import tushare as ts
import sys,os

reload(sys)
sys.setdefaultencoding("utf-8")

df = ts.get_report_data(2007,1)

filename='/home/ali/Documents/stocks/report_data.csv'
if os.path.exists(filename):
    df.to_csv(filename,mode='a',header=None)
else:
    df.to_csv(filename)


