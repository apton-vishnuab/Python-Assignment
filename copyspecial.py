import sys
import re
import os
import shutil
from pathlib import Path
from unittest.mock import patch

def get_special_paths(dir):
    file_content = []
    ln = len(dir)
    
    for i in range(ln):
      path = os.listdir(dir[i])
      file_content.extend(path)

    str_match = [s for s in file_content if "__" in s]
    print("Folders having Special files are\n")
    for i in range(0, len(str_match)):
          print(os.path.abspath(str_match[i]))

def main():
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
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

  get_special_paths(args)
 
if __name__ == "__main__":
  main()


