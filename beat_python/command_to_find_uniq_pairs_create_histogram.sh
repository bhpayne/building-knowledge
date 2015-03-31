while read line; do echo $line `cat pairs_list.dat | awk '{ print $2, $3 }' | grep $line | sed 's/'$line'//' | sed 's/ //' | sort | uniq | wc -l`; done < uniq_node.dat

