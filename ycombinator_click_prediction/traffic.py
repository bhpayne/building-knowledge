from HN.models import ycombinator
import geocoder,re 
data=[x[0] for x in ycombinator.objects.values_list('ip_address')]
unique_ips=set(data)
traffic_stats=[(x,re.sub(',\sUS.*','',str(geocoder.ip(x)).split('[')[-1]),data.count(x)) for x in unique_ips]
results=sorted(traffic_stats,key=lambda x: -x[2])