import tushare as ts 
import pandas as pd
import numpy as np

#--test 1--
"""
class MyDataFrame:
	df = None

	def __init__(self,df = None):
		self.df = df

	def append(self,df):
		if self.df is None:
			self.__init__(df)
		else:
#self.df.append(df)
			self.df = self.df.append(df, ignore_index = True)

#--main entrance--
if __name__ == '__main__':
	df1 = pd.DataFrame({'A' : np.random.randint(1, 10, size = 3),
			'B' : np.random.randint(11, 20, size = 3),
			'C' : np.random.randint(101, 200, size = 3)})
	print "df1 :", df1
	
	df2 = pd.DataFrame({'A' : np.random.randint(1, 10, size = 3),
			'B' : np.random.randint(11, 20, size = 3),
			'C' : np.random.randint(101, 200, size = 3)})
	print "df2 :", df2
	
	t1 = MyDataFrame()
	t2 = MyDataFrame(df1)

	t1.append(df1)
	print "t1 :", t1.df

	t2.append(df2)
#t2.df.append(df2, ignore_index = True)
	print "t2 :", t2.df
"""

#--test 2--
"""
df = pd.DataFrame(columns = ['A'])
print df

df1 = pd.DataFrame({'A' : np.random.randint(1, 10, size = 3)})

df = df.append(df1)
print df
"""

#--test 3--
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
		'B' : ['one', 'one', 'two', 'three','two', 'two', 'four', 'three'],
		'C' : np.random.randn(8),
		'D' : np.random.randn(8)})

print df

#grouped = df.groupby('A').get_group('foo')['C']
#grouped = df['C']

#print grouped.count()
#print grouped.sum()
#print grouped.min()
#print grouped.max()
#print grouped.sum()/grouped.count()

ss = "four"
print df.query('B == "%s"' % ss)['C']

