import random

for indx in range(250000):

    day=str(random.randint(1,30))
    month=str(random.randint(1,12))
    year="2015"
    hour=str(random.randint(1,12))
    minute=str(random.randint(1,60))
    lat_major=str(random.randint(-45,45))
    lat_minor=str(random.randint(0,100))
    long_major=str(random.randint(-45,45))
    long_minor=str(random.randint(0,100))
    rot_major=str(random.randint(-90,90))
    rot_minor=str(random.randint(0,100))
    print(day+"/"+month+"/"+year+" "+hour+":"+minute+", "+lat_major+"."+lat_minor+", "+long_major+"."+long_minor+", "+rot_major+"."+rot_minor)