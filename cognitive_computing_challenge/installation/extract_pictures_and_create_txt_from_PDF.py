# check dependencies
# prompt for directory containing PDFs
import os
import glob
import shutil
import subprocess
import yaml # used to read "config.input"

def get_filename_with_and_without_extension(path_to_file):
	split_path=path_to_file.split('/')
	filename_with_extension= split_path[len(split_path)-1]
	split_filename=filename_with_extension.split('.')
	extension=split_filename[len(split_filename)-1]
	filename=filename_with_extension[0:len(filename_with_extension)-len(extension)-1]
	path_to_file_without_name=path_to_file[0:len(path_to_file)-len(filename_with_extension)-1]
	return filename_with_extension,filename,path_to_file_without_name

#runs a shell command 
def runShellCmd(cmd):
    run = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = run.communicate()
    if err:
        print err

# https://yaml-online-parser.appspot.com/
input_stream=file('config.input','r')
input_data=yaml.load(input_stream)
path_to_PDFs=input_data["path_to_PDFs"]

list_of_full_path_to_PDFs=glob.glob(path_to_PDFs+"*.pdf") # need to go back and make search insensitive to case for extention
#print list_of_full_path_to_PDFs
extracted_content_path= path_to_PDFs+'content_extracted_from_documents/'
if not os.path.exists(extracted_content_path):
	os.makedirs(extracted_content_path)
# for each PDF in path_to_PDFs, create a new directory with that name
list_of_PDF_per_dir=[]
for path_to_PDF in list_of_full_path_to_PDFs:

	[filename_with_extension,filename,path_to_file_without_name]=get_filename_with_and_without_extension(path_to_PDF)
	dir_per_PDF=extracted_content_path+filename+'/'
	list_of_PDF_per_dir.append(dir_per_PDF)
	if not os.path.exists(dir_per_PDF):
		os.makedirs(dir_per_PDF)
	# copy the PDF into that directory
	shutil.copy(path_to_PDF,dir_per_PDF)

print("starting pictures")
# for each PDF in each directory, extract the pictures
for path_to_PDF in list_of_PDF_per_dir:
	pdf_name=glob.glob(path_to_PDF+"*.pdf")
	cmd = 'pdfimages -j %s %s' % ( pdf_name[0],path_to_PDF+"image")
	runShellCmd(cmd)

print("finished pictures; starting pdf2txt")
# for each PDF in each directory, run pdftotext
for path_to_PDF in list_of_PDF_per_dir:
	print(path_to_PDF)
	pdf_name=glob.glob(path_to_PDF+"*.pdf")
	cmd = 'pdf2txt.py -o %spdf2txt.txt %s' % ( path_to_PDF,pdf_name[0])
	runShellCmd(cmd)

print("finished pdf2txt, starting pdftotext")
# for each PDF in each directory, run pdf2text; source = https://pypi.python.org/pypi/pdfminer/, see tools/pdf2text.py
for path_to_PDF in list_of_PDF_per_dir:
	pdf_name=glob.glob(path_to_PDF+"*.pdf")
	cmd = 'pdftotext -layout %s %spdftotext.txt' % (pdf_name[0],path_to_PDF) #-layout preserves the layout of the pdf file 
	runShellCmd(cmd)

# push contents from pdf2text output into REDIS database
# push contents from OCR opus into REDIS database
# present query interface
# present results

