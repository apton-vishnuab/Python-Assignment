import functools
import os
import re
import sys
import urllib.request, urllib.parse, urllib.error
import time
import sys
import webbrowser

def read_urls(filename):
    ub = filename.index('_') # Getting the index of '_' in the filename that given as args.
    host = filename[ub + 1:] # Getting the host name followed after the '_' .
    url_dict = {}
    f = open(filename)
    for i in f:
        match = re.search(r'"GET (\S+)', i) # Regex operation on Log file for finding the rest of URL.
        if match:
            path = match.group(1) # The first parenthesized subgroup.
            if 'puzzle' in path:
                url_dict['http://' + host + path] = 1
    
    
    def sort(url):
        match = re.search(r'-(\w+)-(\w+)\.\w+', url)
        if match:
            return match.group(2)
        else:
            return url
    
    return sorted(list(url_dict.keys()), key=sort)

def download_images(img_urls, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    index = open(os.path.join(dest_dir, 'index.html'), 'w')
    index.write('<html><body>\n')
    i = 0
    print("Getting Url's, Please wait...")
    
    for img_url in img_urls:
        local_name = 'img%d' % i
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        urllib.request.urlretrieve(img_url, os.path.join(dest_dir, local_name))
        index.write('<img src="%s">' % (local_name,))
        i += 1
    
    print("\n")
    index.write('\n</body></html>\n')
    index.close()
    print("Opening image in browser..")
    filename = "/home/anandhuor/Documents/PyExercise/Log_Files/index.html"
    webbrowser.open('file://' + os.path.realpath(filename))
    exit(0)

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