import sys

# +++your code here+++
def print_words(filename):
    f = open(filename, "r")
    dict = {}
    for line in f:
        line = line.strip()
        line = line.casefold()
        words = line.split(" ")
        words.sort()
        for word in words:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1


    for key in list(dict.keys()):
        print(key, ":", dict[key])
    f.close()


def print_top(filename):
    f = open(filename, "r")
    dict = {}
    for line in f:
        line = line.strip()
        line = line.casefold()
        words = line.split(" ")
        for word in words:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1

    sort_orders = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    print("Top 20 Words are:")

    for i in range(20):
        print("{} : {}".format(sort_orders[i][0],sort_orders[i][1]))

    f.close()


# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

# This basic command line argument parsing code is provided and calls the print_words() and print_top() functions which you must define.

def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()