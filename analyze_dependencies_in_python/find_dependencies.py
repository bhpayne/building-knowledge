import re
import sys # command line arguments
#print "This is the name of the script: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)

if (len(sys.argv)<2):
    print("need at least one file name specified")
    exit()


all_lines=[]
for this_file_indx in range(len(sys.argv)):
    list_of_lines=[]
    if (this_file_indx!=0): # this file
        print(sys.argv[this_file_indx])
        file_name=sys.argv[this_file_indx]
        
        with open(sys.argv[this_file_indx],"rb") as fpy:
            list_of_lines = fpy.readlines()

        list_of_lines = map(str.strip, list_of_lines)
        print("has "+str(len(list_of_lines))+" lines")

        number_of_empty_lines=0
        number_of_commented_lines=0
        add_line=True
        line_number=0
        for this_line in list_of_lines:
            line_number +=1
            this_line_cleaned=this_line.strip()
            this_line_dict={}
            this_line_dict['line number']=line_number
            this_line_dict['file name']=file_name
            this_line_dict['line']=this_line_cleaned
            if (this_line_cleaned==''):
                number_of_empty_lines+=1
                this_line_dict['type']="empty"
            elif (this_line_cleaned[0]=='#'): # line starts with #
                number_of_commented_lines+=1
                this_line_dict['type']="single-line comment"
            elif (this_line_cleaned[0:3]=="'''"):
                # I don't know how to catch multiline comments yet
                this_line_dict['type']="multi-line comment start"
            else:
                this_line_dict['type']="python code" # may contain comment
                split_on_comment=this_line_cleaned.split("#")
                if (len(split_on_comment)==1):
                    this_line_dict['code']=this_line_cleaned
                else:
                    this_line_dict['code']=split_on_comment[0]
#                    commented_line=
                
                all_lines.append(this_line_dict)
        print("has "+str(number_of_empty_lines)+" blank lines")
        print("has "+str(number_of_commented_lines)+" commented lines")
#        print("leaves "+str(len(all_lines))+" lines of Python")

number_of_classes=0
for this_line_dict in all_lines:
    if (this_line_dict['type']=="python code" and this_line_dict['line'][0:5]=="class"):
        number_of_classes+=1
        this_line_dict['type']="class"

print("there are "+str(number_of_classes)+" classes\n")


#print(all_lines)
number_of_decorators=0
for this_line_dict in all_lines:
    if (this_line_dict['type']=="python code" and this_line_dict['line'][0]=="@"):
        number_of_decorators+=1
        this_line_dict['type']="decorator"

print("there are "+str(number_of_decorators)+" decorators\n")

number_of_functions=0
functions_dict={}
for this_line_dict in all_lines:
    if (this_line_dict['type']=="python code" and this_line_dict['line'][0:3]=="def"):
        number_of_functions+=1
        this_line_dict['type']="function definition"
        m = re.search('def (.*)\(.*', this_line_dict['line'])
        if m:
            #print(m.group(1))
            this_line_dict['function name']=m.group(1)
        
print("\nthere are "+str(number_of_functions)+" functions")

for this_line_dict in all_lines:
    if (this_line_dict['type']=="function definition"):
        this_function=this_line_dict['function name']
        print(this_function+" on line "+str(this_line_dict['line number'])+" is called on line")
        for this_other_line_dict in all_lines:
            if (this_other_line_dict['type']=="python code" and this_function in this_other_line_dict['line']):
                print(this_other_line_dict['line number'])

