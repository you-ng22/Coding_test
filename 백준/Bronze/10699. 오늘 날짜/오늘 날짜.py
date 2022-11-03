#오늘 날짜
#서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.
import datetime as dt

date = dt.datetime.now()
print(date.strftime('%Y-%m-%d'))