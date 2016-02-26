import sys
import os
import dropbox

f = open("TOKEN");
token = f.read().strip('\n');
commands = ["list","download","upload","delete","mkdir"]

def usage():
	print sys.argv[0], "command remote local"

dbx = dropbox.Dropbox(token);

def list_folder(remote):
	try:
		list = dbx.files_list_folder(remote)
	except dropbox.exceptions.ApiError as ex:
		if(ex.user_message_text != None):
			print ex.user_message_text
		else:
			print "path", remote, "not found"
		return

	for i in list.entries:
		if(isinstance(i, dropbox.files.FilesMetadata)):
			print "F ", i.name
		else:
			print "D ", i.name

def download(remote, local):
	file, res = dbx.files_download(remote);

	if(len(local) == 0):
		local = file.name;

	f = open(local,"w");
	f.write(res.content);
	f.close()

def upload(remote, local):
	f = open(local,'r');

	dbx.files_upload(f, remote + "/" + os.path.basename(local));
	f.close();

def delete(remote):
	dbx.files_delete(remote)

def mkdir(remote):
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

if(com == "mkdir"):
	mkdir(remote)


f.close()
