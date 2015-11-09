import os, datetime, errno

# TODO: 
# add argments.
# add multiple file extensions
#

CWD = os.getcwd()
ext = ['.mkv']

def create_file_list(CWD):
    """ takes string as path, returns tuple(files,date) """

    files_with_mtime = []
    files = []
    for filename in os.listdir(CWD):
        if os.path.splitext(os.path.join(CWD,filename))[1] in ext:
            files.append(filename)
    for fi in files:
        files_with_mtime.append((fi,datetime.datetime.fromtimestamp(os.stat(fi).st_mtime).strftime('%Y-%m-%d')))
    return files_with_mtime


def create_directories(files):
    """ takes tuple(file,date) from create_file_list() """

    m = []
    for i in files:
        m.append(i[1])
    for i in set(m):
        try:
            os.makedirs(os.path.join(CWD,i))
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

def move_files_to_folders(files):
    """ gets tuple(file,date) from create_file_list() """
    for i in files:
        if os.path.exists(os.path.join(CWD,i[1])):
            try:
                os.rename(os.path.join(CWD,i[0]), os.path.join(CWD,(i[1] + '/' + i[0])))
            except Exception as e:
                raise 
    return len(files)

files = create_file_list(CWD)
create_directories(files)
print "Moved %i files" % move_files_to_folders(files)

