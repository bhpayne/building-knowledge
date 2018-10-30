import commands
import sys
import datetime

if (len(sys.argv)==1):
    print("Usage: "+sys.argv[0]+" \"command to run\" \"another command\"")
    print("Error: minimum 1 command to run")
    exit()

now = datetime.datetime.now()

print("{")
print("  \"current datetime in python\":\""+str(now)+"\",")
for arg_indx,this_arg in enumerate(sys.argv[1:len(sys.argv)+1]):
    reslt_tuple = commands.getstatusoutput(this_arg)
    output_as_list=reslt_tuple[1].split('\n')
#    print(len(sys.argv))
#    print(arg_indx)
    if (arg_indx == len(sys.argv)-2):
        end_of_line=""
    else:
        end_of_line=","
    if (len(output_as_list)==1):
        print("  \""+this_arg+"\":\""+output_as_list[0]+"\""+end_of_line)
    else:
        print("  \""+this_arg+"\": {")
        for indx,this_line in enumerate(output_as_list):
            if (this_line!=""):
                if (indx == len(output_as_list)-1):
                    end_of_line=""
                else:
                    end_of_line=","
                print("    \"line "+str(indx)+"\":\""+this_line+"\""+end_of_line)
        print("  }")
print("}")
