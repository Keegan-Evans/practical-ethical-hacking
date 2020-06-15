# Users and Priviliges

inside of a directory you can type:

' ls -la '

to show all of the contents of a folder and information about each file or
directory. The output for each line will look something like this:

> drwxr-xr-x 2 username my-group 4096 Jun 12 15:32 directory-name

The first place string of letters at the beginning tells you if it is
a file or directory:
- -: a file
- d: a directory

The three groups of three places tells about file permissions. The groups
are as follows:
- owner of the file
- the group that owns the file
- all other users

Breaking the groups down:
- ***r*** this user can read the file
- ***w*** this user can write the file
- ***x*** this user can execute the file

A script needs full access to be able to run. We can use a function called
change mode or chmod. You can use numbers to change permissions by group,
for example to change permission to all permissions for all users:

' chmod 777 example.txt '
