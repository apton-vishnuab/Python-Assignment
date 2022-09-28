from fileinput import filename
import sys
import re
import os
import shutil
from os.path import basename
import zipfile
 
def get_special_paths(dir):
  result = []
  paths = os.listdir(dir)  
  for i in paths:
    match = re.search(r'__(\w+)__', i)
    if match:
      result.append(os.path.abspath(os.path.join(dir, i)))
  return(result)
 
 
def copy_to(paths, to_dir):
  for i in paths:
    f = os.path.basename(i)
    shutil.copy(i, os.path.join(to_dir, f))
 
 
def zip_to(paths, dir):
  with zipfile.ZipFile(dir,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for i in paths:
      base=os.path.basename(i)
      z.write(base)


def main():
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
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
  for dir in args:
    paths.extend(get_special_paths(dir))
 
  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths,tozip)
  else:
    print ('\n'.join(paths))

if __name__ == "__main__":
  main()