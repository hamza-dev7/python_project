import datetime

today = datetime.datetime.now(tz=datetime.timezone.utc).date() + datetime.timedelta(days=30)
str_today = today.strftime('%Y-%m-%d')
date_today = datetime.datetime.strptime(str_today, '%Y-%m-%d').date()  # noqa: DTZ007
print(str_today)
print(type(str_today))
print(date_today)
print(type(date_today))
