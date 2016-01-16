import math
import csv
import numpy

# http://www.johndcook.com/blog/python_longitude_latitude/ 
def distance_on_unit_sphere(lat1, long1, lat2, long2):
    lat1=float(lat1)
    long1=float(long1)
    lat2=float(lat2)
    long2=float(long2)
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
         
    # Compute spherical distance from spherical coordinates.
         
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
     
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc
    
all_pair_distances=[]
with open('lat_longs.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for first_loc in spamreader:
        for second_loc in spamreader:
            all_pair_distances.append(distance_on_unit_sphere(first_loc[1],first_loc[2],second_loc[1],second_loc[2]))

# https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.histogram.html
[counts,bin_edges]=numpy.histogram(all_pair_distances,bins=10)
print(counts)
print(bin_edges)

