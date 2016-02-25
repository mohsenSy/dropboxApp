import dropbox

f = open("TOKEN","r");

token = f.read().strip('\n');

dbx = dropbox.Dropbox(token);

ac = dbx.users_get_current_account();

print "Account name is " + ac.name.display_name


## test file upload

#dbx.files_upload("Test upload from python API, How are you Mr. Abed Androon", '/Lecture stuff/HiAbed.txt');

#print "Upload done"

## test folder create

#folder = dbx.files_create_folder("/PythonSDK");

#print "Created folder with name " + folder.name;

## test folder list

#list = dbx.files_list_folder("/Screenshots");

#for i in list.entries:
#	print i.name

## test files copy

#dbx.files_copy("/Lecture stuff/HiAbed.txt", "/PythonSDK/testCopy.txt");

#print "Copy done";

## test file download

file, res = dbx.files_download("/Screenshots/Screenshot 2015-09-09 19.40.58.png");

# write response content to a file

f = open(file.name,"w");

f.write(res.content);
f.close();













