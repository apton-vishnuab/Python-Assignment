import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  dict = {}
  f = open(filename, 'r')
  text = (f.read()).split()
  f.close()
  for i in range(len(text)-1):
    if text[i] in dict.keys():
      dict[text[i]] += [text[i+1]]
    else:
      dict[text[i]] = [text[i+1]]

  #print(dict)
  return dict

def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""

  for i in range(200):
    keys = list(mimic_dict.keys())
    random_key = random.choice(keys)
    random_value = mimic_dict[random_key]

  if word not in mimic_dict:
    random_value = None
  
  else:
    value_list = mimic_dict[word]
    if [] == value_list:
      random_value = None
    else:
      random_value = random.choice(value_list)
  print(word)
  
  if not (word in mimic_dict):
    current_word = random_key
  else:
    current_word = word

  for i in range(0, 200):
            print(current_word)
            proposed_word = random_value
            if (proposed_word is None):
                current_word = random_key
            else:
                current_word = proposed_word


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print ('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()