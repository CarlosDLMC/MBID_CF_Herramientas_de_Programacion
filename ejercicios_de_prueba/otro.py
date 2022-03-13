from pandas import date_range

h1 = '2012-11-28'
h2 = '2016-07-09'
h3 = '2020-05-11'

ath1 = '2013-12-04'
ath2 = '2017-12-17'

periods = len(date_range(start=h2, end=ath2)) + len(date_range(start=h2, end=ath2)) - len(date_range(start=h1, end=ath1))

print(periods)
print(date_range(start=h3, periods=periods))