from urllib.request import urlopen
import os

def wget2(url):
  try:
    ufile = urlopen(url)
    if ufile.info().get_content_type() == 'text/html':
        url_content = ufile.read()
        dest_dir = "/home/anandhuor/Documents/PyExercise/test_folder"
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        index = open(os.path.join(dest_dir, 'index.html'), 'wb')
        index.write(url_content)

  except IOError:
    print('problem reading url:', url)

url = "https://developers.google.com/edu/python/utilities"

wget2(url)