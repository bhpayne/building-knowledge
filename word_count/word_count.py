# example input source:
# http://shakespeare.mit.edu/romeo_juliet/full.html

with open('input.dat', 'r') as f:
    read_data = f.read()
f.closed

# original input data
print(read_data)

split_data=read_data.replace('!',' ').replace(':',' ').replace(';',' ').replace('-',' ').replace(',',' ').replace('\'',' ').replace('?',' ').replace('\n',' ').replace('.',' ').split(' ')
split_data = filter(None,split_data) # eliminate empty strings

# result: all the data split, no punctuation
print(split_data)

# count frequencies in the list
#http://stackoverflow.com/questions/2870466/python-histogram-one-liner
hist = {}
for x in split_data: hist[x] = hist.pop(x,0) + 1  # x=statement_punid

# produced sorted list by frequency
# http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
for w in sorted(hist, key=hist.get, reverse=False):
  print w, hist[w]  
  
#for w in sorted(hist, key=hist.get, reverse=True):
#  print w, hist[w]