import sys
import os
import dropbox

f = open("TOKEN");
token = f.read().strip('\n');
commands = ["list","download","upload","delete","mkdir"]

def usage():
	print sys.argv[0], "command remote local"

def list_folder(remote):
	dbx = dropbox.Dropbox(token);
	list = dbx.files_list_folder(remote)

	for i in list.entries:
		print i.name

def download(remote, local):
	dbx = dropbox.Dropbox(token);
	file, res = dbx.files_download(remote);

	if(len(local) == 0):
		local = file.name;

	f = open(local,"w");
	f.write(res.content);
	f.close()

def upload(remote, local):
	dbx = dropbox.Dropbox(token);
	f = open(local,'r');

	dbx.files_upload(f, remote + "/" + os.path.basename(local));
	f.close();

def delete(remote):
	dbx = dropbox.Dropbox(token)

	dbx.files_delete(remote)

def mkdir(remote):
	dbx = dropbox.Dropbox(token);

	dbx.files_create_folder(remote);

if(len(sys.argv) < 3):
	usage()
	exit(1)

com = sys.argv[1]
remote = sys.argv[2]

if( com not in commands):
	print "command ", com ," is not avaiable"
	print "Available commands are:"
	for i in commands:
		print i
	exit(1)

if((com == "upload") & (len(sys.argv) < 3)):
	usage()
	exit(1)
local = ""

try:
	local = sys.argv[3]
except Exception as er:
	pass

if(com == "list"):
	if(remote == "/"):
		remote = ""
	list_folder(remote)

if(com == "download"):
	download(remote, local)

if(com == "upload"):
	upload(remote, local)

if(com == "delete"):
	delete(remote)

#if(com == "mkdir"):
#	mkdir(remote)

dbx = dropbox.Dropbox(token)

m = dbx.files_get_metadata("/Marks/test.txt")

if( isinstance(m, dropbox.files.FileMetadata)):
	print "file"
else:
	print "folder"

f.close()
