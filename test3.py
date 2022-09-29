import os
import re
import urllib.request, urllib.parse, urllib.error
import sys
import webbrowser


def read_urls(filename):
    ub = filename.index('_') 
    host = filename[ub + 1:] 
    url_dict = {}
    with open(filename) as f:
        for i in f:
            match = re.search(r'"GET (\S+)', i) 
            if match:
                path = match.group(1) 
                if 'puzzle' in path:
                    url_dict['http://' + host + path] = 1
    
    url_lst = list(url_dict.keys())
    url_lst.sort()
    return url_lst

def download_images(img_urls, dest_dir):
    file = open(os.path.join(dest_dir, 'index.html'), 'w')
    file.write('<html><body>\n')
    i = 0
    print("Getting Url's, Please wait...")
    
    for url in img_urls:
        local_name = 'img%d' % i
        print(url)
        urllib.request.urlretrieve(url, os.path.join(dest_dir, local_name))
        file.write('<img src="%s">' % (local_name,))
        i += 1
    
    print("\n")
    file.write('\n</body></html>\n')
    file.close()
    print("Opening image in browser..")
    filename = "/home/anandhuor/Documents/PyExercise/Log_Files/index.html" # Location of generated "index.html" file.
    webbrowser.open('file://' + os.path.realpath(filename)) # Opening file in browser

def main():
    args = sys.argv[1:]
    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
        
    img_urls = read_urls(args[0])
    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()