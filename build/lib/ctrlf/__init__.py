import os
import re
class main_class():
    def __init__(self,path = None):
        if not path:
            # path    = os.path.splitdrive(os.getcwd())[0] + '\\'
            path  = os.getcwd()
        os.chdir(path)
        print(os.getcwd())
        assert len(os.sys.argv) > 1 , "enter the file/dir name or rexgex"
        pattern = re.compile(os.sys.argv[-1])
        try:
            os.sys.stdout  = open('res.txt',"w")
            ok = True
        except Exception as exc:
            print(exc)
            ok = False
        dirs = set()
        print('found files...')
        for dirpath,dirnames,filenames in os.walk(os.getcwd()):
            for filename in filenames:
                if re.match(pattern,filename):
                    print(filename,dirpath,sep = '  -->  ')
            for dirname in dirnames:
                if re.match(pattern,dirname):
                    dirs.add("{} --> {}".format(dirname,dirpath))
        print('found directories...')
        for dir_ in dirs:
            print(dir_)
        if ok:
            os.sys.stdout.close()
            os.system("res.txt")
def tsmain():
    print('ts')
