import os
import random
import networkx as nx
import matplotlib.pyplot as plt # draw plot
import graphviz # sudo pip install graphviz; sudo pip install pydot2
import time

# def print_node_list(G):
#     node_list=G.nodes(data=True)
#     for this_node in node_list:
#         if 'type' not in this_node[1]:
#             print this_node
#     return

def print_node_list(G):
    node_list=G.nodes(data=True)
    for this_node in node_list:
        print this_node
    return

def print_edge_list(G):
    edge_list=G.edges(data=True)
    for this_edge in edge_list:
        print this_edge
    return

def add_node_labels(G,key_for_label):
    node_list=G.nodes(data=True)
    node_labels_dic={}
    for this_node in node_list:
#         print(this_node)
        node_labels_dic[this_node[0]]=this_node[1][key_for_label]
    return node_labels_dic

def plot_graph(G,use_labels):

# # http://networkx.lanl.gov/reference/drawing.html
# nx.draw(G,pos=nx.spring_layout(G))
# #nx.draw_networkx(G)
# # nx.draw(G)
# # plt.draw()
# plt.show()

    pos=nx.spring_layout(G)
    if (use_labels):
        node_labels_dic=add_node_labels(G,'display')
        nx.draw_networkx_labels(G,pos,node_labels_dic,font_size=16)
    nx.draw(G,pos)
    plt.show()
    return

def get_new_rand_indx(list_of_indices,index_range_start,index_range_end):
  index=-1
  found_new_index=False
  while(not found_new_index):
    index=random.randrange(index_range_start,index_range_end)
    if (index not in list_of_indices):
      found_new_index=True
      break
  list_of_indices.append(index)    
  return index,list_of_indices

#   determine whether dir already exists as a node in the graph
def does_node_exist(G,ary_of_keys,ary_of_values):
    entry_already_exists_in_graph_as_node=False
    node_ID=0
    for this_node in G.nodes(data=True):
        ary_of_booleans=[]
        for indx in range(len(ary_of_keys)):
#             print(this_node[1])
#             print(ary_of_keys)
#             print(ary_of_keys[indx])
            if ary_of_keys[indx] in this_node[1]:
#                 print("no problem")
                ary_of_booleans.append(this_node[1][ary_of_keys[indx]]==ary_of_values[indx])
            else: # key of interest does not exist in this node
#                 print("problem")
                continue
        if (sum(ary_of_booleans)==len(ary_of_keys)):
            entry_already_exists_in_graph_as_node=True
            node_ID=this_node[0]
            break
    return entry_already_exists_in_graph_as_node,node_ID

def find_all_paths(path_to_files):
    # find all paths; equivalent to linux's "find"
    list_of_files=[]
    list_of_directories=[]
    # http://www.tutorialspoint.com/python/os_walk.htm
    for dirpath, dirnames, filenames in os.walk(path_to_files): # https://docs.python.org/2/library/os.html#os.walk
        for name in filenames:
            list_of_files.append(os.path.join(dirpath, name))
        for name in dirnames:
            list_of_directories.append(os.path.join(dirpath, name))
    return list_of_files,list_of_directories

start_time=time.time()

G=nx.DiGraph()

# path_to_files='/Users/benpayne/Desktop/to_digest/'
# path_to_files='/Users/benpayne/version_controlled/building-knowledge'
path_to_files='/Users/benpayne/version_controlled/building-knowledge/shannon_entropy_calculation/'
index_range_start=100000
index_range_end=  999999
max_display_length=10

[list_of_files,list_of_directories]=find_all_paths(path_to_files)
# for this_file in list_of_files:
#     print(this_file)
# print("\n")
# print("list of directories:")
# for this_dir in list_of_directories:
#     print(this_dir)
# print("\n")

# parity check for whether there are duplicate file
# print(len(list_of_files))
# print(len(set(list_of_files)))
# parity check for whether there are duplicate directories
# print(len(list_of_directories))
# print(len(set(list_of_directories)))


list_of_indices=[]
    
for this_dir in list_of_directories:
    full_path_split_on_slash=this_dir.split('/')
    dir_name=full_path_split_on_slash[len(full_path_split_on_slash)-1]
    parent_dir=full_path_split_on_slash[len(full_path_split_on_slash)-2]
    parent_dir_full_path='/'.join(full_path_split_on_slash[0:len(full_path_split_on_slash)-1])

    [this_dir_node_indx,list_of_indices]=get_new_rand_indx(list_of_indices,index_range_start,index_range_end)
    G.add_node(this_dir_node_indx, {'type':'directory', 'full_path':this_dir, 'display':dir_name[:max_display_length], 'dir name':dir_name} )

#     print("added node")
#     print_node_list(G)

#   determine whether dir already exists as a node in the graph
    ary_of_keys=['full_path','display','type']
    ary_of_values=[parent_dir_full_path,parent_dir,'directory']
    [parent_dir_already_exists_in_graph_as_node,parent_node_ID]=\
           does_node_exist(G,ary_of_keys,ary_of_values)
#     print(parent_dir_already_exists_in_graph_as_node)
#     print(parent_node_ID)
    if (not parent_dir_already_exists_in_graph_as_node):
        [parent_node_ID,list_of_indices]=get_new_rand_indx(list_of_indices,index_range_start,index_range_end)
        G.add_node(parent_node_ID, {'type':'directory', 'full_path':parent_dir_full_path, 'display':parent_dir[:max_display_length], 'dir name':parent_dir} )

#     print("after parent detection")
#     print_node_list(G)

    G.add_edge(parent_node_ID,this_dir_node_indx,{'description':'contains'})
#     print_edge_list(G)
#     break

for this_file in list_of_files:
    full_path_split_on_slash=this_file.split('/')
    file_name=full_path_split_on_slash[len(full_path_split_on_slash)-1]
    parent_dir=full_path_split_on_slash[len(full_path_split_on_slash)-2]
    parent_dir_full_path='/'.join(full_path_split_on_slash[0:len(full_path_split_on_slash)-1])

    [file_node_indx,list_of_indices]=get_new_rand_indx(list_of_indices,index_range_start,index_range_end)
    G.add_node(file_node_indx, {'type':'file', 'full_path':this_file, 'display':file_name[:max_display_length], 'file name':file_name} )


    ary_of_keys=['full_path','display','type']
    ary_of_values=[parent_dir_full_path,parent_dir,'directory']
    [parent_dir_already_exists_in_graph_as_node,parent_node_ID]=\
           does_node_exist(G,ary_of_keys,ary_of_values)
    if (not parent_dir_already_exists_in_graph_as_node):
        [parent_node_ID,list_of_indices]=get_new_rand_indx(list_of_indices,index_range_start,index_range_end)
        G.add_node(parent_node_ID, {'type':'directory', 'full_path':parent_dir_full_path, 'display':parent_dir[:max_display_length], 'dir name':parent_dir} )

    G.add_edge(parent_node_ID,file_node_indx,{'description':'contains'})

file_and_dir_time=time.time()-start_time
print(str(file_and_dir_time)+" seconds parsing file and dir names")

# for jpg on linux, "identify -verbose filename.jpg" # https://gnutips.wordpress.com/2010/08/10/view-image-file-metadata-from-the-command-line/

# print_node_list(G)

for indx in range(1):
    node_list=G.nodes(data=True)
    for this_node in node_list:
        if (this_node[1]['type']=='file'):
            f=open(this_node[1]['full_path'])
            # for each file, store blob of content
            file_content=f.read()
            f.close()
            [file_content_node_ID,list_of_indices]=get_new_rand_indx(list_of_indices,index_range_start,index_range_end)
            G.add_node(file_content_node_ID, {'type':'file contents', 'display':file_content[:max_display_length], 'file content':file_content})
            G.add_edge(this_node[0],file_content_node_ID,{'description':'contains'})
            # for each text file, parse line-by-line
            ary_of_lines=file_content.split('\n')
            print(this_node[1]['full_path'])
            print(len(ary_of_lines))
            for line_indx,this_line in enumerate(ary_of_lines):
                if (len(this_line)==0):
                    break
                ary_of_keys=['type','display']
                ary_of_values=['line',this_line]
                [line_already_exists_in_graph_as_node,line_node_ID]=\
                  does_node_exist(G,ary_of_keys,ary_of_values)
                if (not line_already_exists_in_graph_as_node):
                    [line_node_ID,list_of_indices]=get_new_rand_indx(list_of_indices,index_range_start,index_range_end)
                    G.add_node(line_node_ID, {'type':'line', 'display':this_line[:max_display_length], 'line content':this_line})
                G.add_edge(file_content_node_ID,line_node_ID,{'line_index':line_indx, 'description':'contains'})
#                 print("this line")
#                 print(len(this_line))
                # for each line, parse words by space-separation
                ary_of_words=this_line.split(' ')
                for word_indx,this_word in enumerate(ary_of_words):
                    if (len(this_word)==0):
                        break
                    ary_of_keys=['type','line']
                    ary_of_values=['word',this_word]
                    [word_already_exists_in_graph_as_node,word_node_ID]=\
                      does_node_exist(G,ary_of_keys,ary_of_values)
                    if (not word_already_exists_in_graph_as_node):
                        [word_node_ID,list_of_indices]=get_new_rand_indx(list_of_indices,index_range_start,index_range_end)
                        G.add_node(word_node_ID, {'type':'word', 'display':this_word[:max_display_length], 'word':this_word})
                    G.add_edge(line_node_ID,word_node_ID,{'word_index':word_indx, 'description':'contains'})
                    # for each word, parse by character
                    for character_indx,this_character in enumerate(this_word):
                        ary_of_keys=['type','display']
                        ary_of_values=['character',this_character]
                        [char_already_exists_in_graph_as_node,character_node_ID]=\
                          does_node_exist(G,ary_of_keys,ary_of_values)
                        if (not char_already_exists_in_graph_as_node):
                            [character_node_ID,list_of_indices]=get_new_rand_indx(list_of_indices,index_range_start,index_range_end)
                            G.add_node(character_node_ID, {'type':'character', 'display':this_character})
                        G.add_edge(word_node_ID,character_node_ID,{'character_index':character_indx, 'description':'contains'})
                                    
                        # for each character, split into binary

content_analysis_time=time.time()-start_time-file_and_dir_time
print(str(content_analysis_time)+" seconds for content analysis")

print("number of nodes: "+str(len(G.nodes()))+", number of edges: "+str(len(G.edges()))+" ratio of e/n: "+str(len(G.edges())/(len(G.nodes())*1.0)))

root_node_ID=random.choice(G.nodes())
for this_node in G.nodes(data=True):
    if (this_node[0]==root_node_ID):
        print("random root node:")
        print(this_node)
print("neighbors:")
for neighbor_node_ID in list(nx.all_neighbors(G,root_node_ID)):
    for this_node in G.nodes(data=True):
        if (this_node[0]==neighbor_node_ID):
            print(this_node)

# print_node_list(G)
# print_edge_list(G)

# plot_graph(G,use_labels=True)

# nx.write_dot(G,'this_graph.dot')
# print("Now run: neato -Tpng this_graph.dot >grid.png")

# done_time=time.time()-start_time-content_analysis_time
# print(str(done_time)+" seconds to plot")

print(str(time.time()-start_time)+" seconds total")
