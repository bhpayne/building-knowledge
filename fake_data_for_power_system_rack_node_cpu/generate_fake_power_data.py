import random
from operator import add

number_of_cpus_per_node=4
number_of_nodes_per_rack=5
number_of_racks_per_system=3
number_of_time_steps=6

max_power_per_cpu=100 # Watts
min_power_per_cpu= 25 # Watts

# {'node index': 4, 'CPU index': 0, 'CPU power': [26, 91, 28, 80, 78, 29], 'rack index': 0}
# {'node index': 4, 'CPU index': 1, 'CPU power': [89, 53, 87, 56, 99, 60], 'rack index': 0}
# {'node index': 4, 'CPU index': 2, 'CPU power': [77, 40, 79, 70, 71, 76], 'rack index': 0}
# {'node index': 4, 'CPU index': 3, 'CPU power': [30, 53, 61, 80, 42, 62], 'rack index': 0}
# {'node index': 0, 'CPU index': 0, 'CPU power': [99, 67, 73, 87, 94, 75], 'rack index': 1}
# {'node index': 0, 'CPU index': 1, 'CPU power': [62, 39, 98, 45, 38, 55], 'rack index': 1}
# {'node index': 0, 'CPU index': 2, 'CPU power': [98, 26, 86, 76, 32, 83], 'rack index': 1}
# {'node index': 0, 'CPU index': 3, 'CPU power': [73, 84, 46, 71, 54, 46], 'rack index': 1}

list_of_components=[]
for rack_indx in range(number_of_racks_per_system):
	for node_indx in range(number_of_nodes_per_rack):
		for CPU_indx in range(number_of_cpus_per_node):
			this_component={}
			this_component["node index"]=node_indx
			this_component["rack index"]=rack_indx
			this_component["CPU index"]=CPU_indx
			time_sequence_of_CPU=[]
			for time_step in range(number_of_time_steps):
				time_sequence_of_CPU.append(random.randrange(min_power_per_cpu,max_power_per_cpu))
			this_component["CPU power"]=time_sequence_of_CPU
			list_of_components.append(this_component)
# for this_elem in list_of_components:
# 	print(this_elem)

for rack_indx in range(number_of_racks_per_system):
# 	print("rack index:"+str(rack_indx))
	power_per_rack=[0]*number_of_time_steps
	for this_component in list_of_components:
# 		print("local: "+str(this_component["rack index"]))
		if (this_component["rack index"]==rack_indx):
			power_per_rack=map(add, power_per_rack, this_component["CPU power"])
	print(power_per_rack)
