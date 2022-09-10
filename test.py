import datetime
def get_day_interval(str1, str2):
    date1 = datetime.datetime.strptime(str1[0:10], "%Y-%m-%d")
    date2 = datetime.datetime.strptime(str2[0:10], "%Y-%m-%d")
    num = (date1 - date2).days
    return num


str1 = '2022-09-01 15:57:13.522721'
str2 = '2022-09-10 15:57:13.522721'
print(get_day_interval(str2, str1))