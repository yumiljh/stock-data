import tushare as ts
import pandas as pd
import numpy as np
import sys,os
import time

reload(sys)
sys.setdefaultencoding("utf-8")

#--parameters definitions--
RECENT_DATE = time.strftime("%Y-%m-%d")
RECENT_YEAR = 2018
START_YEAR = 2012
START_DATE = '2012-01-01'
FILEPATH = '/home/ali/Documents/stocks/'
FILENAME = '/home/ali/Documents/stocks/test.csv'
COUNTER = 100

#--class definitions--
class MyDataFrame:
	df = None

	def __init__(self, df = None):
		self.df = df

	def append(self,df):
		if self.df is None:
			self.__init__(df)
		else:
			self.df = self.df.append(df, ignore_index = True)

#--function definitions--
#
# IPO_DATE = formatDate(basic.df.ix[strx]['timeToMarket'])
#
def formatDate(temp):
	temp_date = str(temp)
	formated_date = temp_date[0:4] + "-" + temp_date[4:6] + "-" + temp_date[6:8]
	return formated_date

#--main entrance--
if __name__ == '__main__':
	result = pd.DataFrame(columns = ['code', 'trade', 'avg_close', 'change', 'pe', 'pb', 'esp', 'avg_esp', 'min_esp'])
	basic = MyDataFrame(ts.get_stock_basics())
	today = MyDataFrame(ts.get_today_all())
	report = MyDataFrame()
	for i in range(START_YEAR, RECENT_YEAR):
		for j in range(1,5):
			report.append(ts.get_report_data(i, j))

	for code in basic.df.index:
		COUNTER = COUNTER - 1
		if COUNTER == 0:
			break
	
		pe = basic.df.ix[code]['pe'].sum()	#pe
		pb = basic.df.ix[code]['pb'].sum()	#pb
		esp = basic.df.ix[code]['esp'].sum()	#esp
		grouped = report.df.query('code == "%s"' % code)['eps']
		avg_esp = grouped.sum()	#avg_esp
		min_esp = grouped.min()	#min_esp
		if pe > 30 or pe <=0 or pb > 3 or pb <=0 or esp <= 0 or avg_esp <= 0 or min_esp <= 0:
			continue

		df = ts.get_h_data(code, start = START_DATE, end = RECENT_DATE, retry_count = 30, pause = 3)
		df['code'] = code
		history = MyDataFrame(df)
		grouped = history.df['close']
		avg_close = grouped.sum()/grouped.count()	#avg_close
		trade = today.df.query('code == "%s"' % code)['trade'].sum()	#trade
		change = trade / avg_close - 1	#change

		if change <= 0 and 0 < pe <= 30 and 0 < pb <= 3 and esp > 0 and avg_esp > 0 and min_esp > 0:
			append_df = pd.DataFrame({'code' : code,
					'trade' : trade,
					'avg_close' : avg_close,
					'change' : change,
					'pe' : pe,
					'pb' : pb,
					'esp' : esp,
					'avg_esp' : avg_esp,
					'min_esp' : min_esp})
			result.append(append_df)

	result.df.to_csv(FILENAME)

#dataframe.to_csv(filename, header=None, encoding='gb2312')

