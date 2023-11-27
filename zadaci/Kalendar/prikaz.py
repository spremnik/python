from datetime import datetime
import kalendar

danas = datetime.now()
k = kalendar.Kalendar(danas.day,danas.month,danas.year)
print(k.ispis())
