import datetime
# from datetime import datetime
import ephem  
o=ephem.Observer()  
o.lat='45'  
o.long='-124'  
s=ephem.Sun()  
s.compute()


pr = ephem.localtime(o.previous_rising(s))
ns = ephem.localtime(o.next_setting(s))
now = datetime.datetime.now()


sunrise = ephem.localtime(o.next_rising(s))
sunset = ephem.localtime(o.next_setting(s))


sunrise = ephem.localtime(o.next_rising(s))
sunset = ephem.localtime(o.next_setting(s))

print('Next Sunrise ',sunrise)
print('Next Sunset ', sunset)
print(now)
if now > sunset and now < sunrise:
    print('Day') 
else:
    print('Night')