import os
import sys
import re
import zipfile
import shutil

def get_special_paths(dir):
    result=[]
    for file in range(len(dir)):
        path=os.listdir(dir[file]) 
        for j in range(len(path)):
          if re.match("_.*_",path[j]):
            os.chdir("/home/anandhuor/Documents/PyExercise")
            result.append(os.path.abspath(path[j])) 
    return result

def copy_to(paths,dir):
  for i in range(len(paths)):
    shutil.copy(paths[i],dir)

def zip_to(paths,dir):
  os.chdir("/home/anandhuor/Documents/PyExercise")
  with zipfile.ZipFile(dir,'w',compression=zipfile.ZIP_DEFLATED) as zipobj:
    for file in paths:
      os.chdir("/home/anandhuor/Documents/PyExercise/thisdir")
      base=os.path.basename(file)
      zipobj.write(base)

def main():
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)


  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2] 

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)

  paths = []
  paths.extend(get_special_paths(args))

  if todir: 
    copy_to(paths, todir)
  elif tozip: 
    zip_to(paths, tozip)
  else:
    print ('\n'.join(paths))
 
if __name__ == "__main__":
  main()