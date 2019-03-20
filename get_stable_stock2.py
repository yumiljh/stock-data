import time
import pandas as pd

RECENT_DATE = time.strftime("%Y%m%d")
RECENT_YEAR = 2018
START_YEAR = 2010
START_DATE = '20100101'
LAST_TRADEDATE = '20180228'

def formatDate(temp):
    temp_date = str(temp)
    formated_date = temp_date[0:4] + "-" + temp_date[4:6] + "-" + temp_date[6:8]
    return formated_date

basic_df = DataAPI.EquGet(equTypeCD=u"A", listStatusCD=u"L", field=u"ticker,secShortName,ListSectorCD,listDate", pandas="1")
today_df = DataAPI.MktEqudGet(tradeDate=LAST_TRADEDATE, field=u"ticker,closePrice,PE,PB", pandas="1")
report_df = DataAPI.FdmtIndiPSPitGet(beginYear=START_YEAR, endYear=RECENT_YEAR, field=u"ticker,EPS,basicEPS,dilutedEPS,endDate", pandas="1")
result_df = pd.DataFrame(columns = ['code', 'name', 'listDate', 'trade', 'avg_close', 'change', 'pe', 'pb', 'avg_eps', 'min_eps', 'max_eps'])

for code in basic_df['ticker']:
    #name
    name = basic_df.query('ticker == "%s"' % code)['secShortName'].sum()
    #listSectorCD
    listSectorCD = basic_df.query('ticker == "%s"' % code)['ListSectorCD'].sum()
    #listDate
    listDate = basic_df.query('ticker == "%s"' % code)['listDate'].sum()
    #pe
    pe = today_df.query('ticker == "%s"' % code)['PE'].sum()
    #pb
    pb = today_df.query('ticker == "%s"' % code)['PB'].sum()
    #avg_eps
    avg_eps = None
    if report_df.query('ticker == "%s"' % code)['EPS'].count() != 0:
        avg_eps = report_df.query('ticker == "%s"' % code)['EPS'].sum() / report_df.query('ticker == "%s"' % code)['EPS'].count()
    else:
        avg_eps = 0
    #min_eps
    min_eps = report_df.query('ticker == "%s"' % code)['EPS'].min()
    #max_eps
    max_eps = report_df.query('ticker == "%s"' % code)['EPS'].max()
    
    if pe > 25 or pe <= 0 or pb > 1.5 or pb <= 0 or avg_eps <= 0 or min_eps <= 0:
        continue
    
    history_df = DataAPI.MktEqudAdjGet(ticker=code, beginDate=START_DATE, endDate=RECENT_DATE, field=u"ticker,tradeDate,closePrice", pandas="1")
    pehist_df = DataAPI.MktStockFactorsDateRangeGet(ticker=code, beginDate=START_DATE, endDate=RECENT_DATE, field=u"ticker,tradeDate,PE",pandas="1")
    
    #avg_close
    avg_close = None
    if history_df['closePrice'].count() != 0:
        avg_close = history_df['closePrice'].sum() / history_df['closePrice'].count()
    else:
        avg_close = 0
    #trade
    trade = today_df.query('ticker == "%s"' % code)['closePrice'].sum()
    #change
    change = None
    if avg_close != 0:
        change = trade / avg_close - 1
    else:
        change = 1
    
    if change <= 0:
        append_df = pd.DataFrame([{ 'code' : code, 'name' : name, 'listDate' : listDate, 'trade' : trade, 'avg_close' : avg_close, 'change' : change, 'pe' : pe, 'pb' : pb, 'avg_eps' : avg_eps, 'min_eps' : min_eps , 'max_eps' : max_eps }] , columns = ['code', 'name', 'listDate', 'trade', 'avg_close', 'change', 'pe', 'pb', 'avg_eps', 'min_eps', 'max_eps'])
        result_df = result_df.append(append_df)

result_df.to_csv("result.csv", encoding = "gbk") 
print 'Done!'
