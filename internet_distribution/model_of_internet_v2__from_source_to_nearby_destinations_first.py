#!/bin/python
# Ben Payne
import random
import math

def distance_between_points(a,b):
    return math.sqrt( (a[1]-b[1])**2 + (a[0]-b[0])**2 )

def list_of_closest_n_points_to_seed(seed_indx,list_of_house_locations,number_of_neighbors):
    closest_n_points=[]
    dic_of_distances_from_seed=list_of_house_locations[seed_indx]['distances'].copy()
#    print("dic of distances")
#    print(dic_of_distances_from_seed)

    for indx in range(number_of_neighbors+1):
        min_dist=100000
        for key in dic_of_distances_from_seed:
            if (dic_of_distances_from_seed[key]<min_dist and \
                   list_of_house_locations[key]['is house connected']==False):
                min_dist=dic_of_distances_from_seed[key]
                min_key=key
#            print(min_dist)
#            print(min_key)
        closest_n_points.append(min_key)
        dic_of_distances_from_seed.pop(min_key)
    closest_n_points.pop(seed_indx)
    return closest_n_points

def place_houses(rectangle_length,rectangle_width,number_of_points):
    list_of_house_locations=[]
    for indx in range(number_of_points): # source = index 0
        this_house={}
        this_house['x']=int(random.random()*rectangle_length)
        this_house['y']=int(random.random()*rectangle_width)
        if (indx==0): # source starts connected
            this_house['is house connected']=True
        else:
            this_house['is house connected']=False
        this_house['index']=indx
        list_of_house_locations.append(this_house)
    return list_of_house_locations

rectangle_length=100
rectangle_width=100
number_of_points=100
number_of_iterations=10

list_of_house_locations = place_houses(rectangle_length,rectangle_width,number_of_points)

#for this_dic in list_of_house_locations:
#    print(this_dic)

#ary_of_distances=[]
for source_house_indx in range(number_of_points):
    source_house_dic={}
    for dest_house_indx in range(number_of_points):
        source_house_coords=[]
        source_house_coords.append(list_of_house_locations[source_house_indx]['x'])
        source_house_coords.append(list_of_house_locations[source_house_indx]['y'])
        dest_house_coords=[]
        dest_house_coords.append(list_of_house_locations[dest_house_indx]['x'])
        dest_house_coords.append(list_of_house_locations[dest_house_indx]['y'])
        separation_between_houses=distance_between_points(source_house_coords,\
                                                          dest_house_coords)
        source_house_dic[dest_house_indx]=separation_between_houses
    #ary_of_distances.append(source_house_list)
    list_of_house_locations[source_house_indx]['distances']=source_house_dic

#print("all points:")    
#for this_dic in list_of_house_locations:
#    print(this_dic)
#print("done with all points")
    
number_of_connected_points=1 # source (index 0) starts connected
seed_indx=0
number_of_neighbors=5
list_of_edges=[]
#print("list of house locations for seed "+str(seed_indx)+":")
#print(list_of_house_locations[seed_indx])

closest_n_points=list_of_closest_n_points_to_seed(seed_indx,list_of_house_locations,number_of_neighbors)
#print("closest "+str(number_of_neighbors)+" points")
#print(closest_n_points)
for point_indx in range(number_of_neighbors):
    indx_of_closest_house=closest_n_points[point_indx]
    list_of_edges.append([seed_indx,indx_of_closest_house])
    number_of_connected_points = number_of_connected_points+1
    list_of_house_locations[indx_of_closest_house]['is house connected']=True

    closest_n_points_level2=list_of_closest_n_points_to_seed(indx_of_closest_house,list_of_house_locations,number_of_neighbors)
    for point_indx in range(number_of_neighbors):
        indx_of_closest_house_level2=closest_n_points_level2[point_indx]
        list_of_edges.append([indx_of_closest_house,indx_of_closest_house_level2])
        number_of_connected_points = number_of_connected_points+1
        list_of_house_locations[indx_of_closest_house_level2]['is house connected']=True


print(list_of_edges)
    
#while (number_of_connected_points<number_of_points):
#    for 

