def match_ends(words):
    count = 0
    for i in range(0, len(words)):
        str = words[i]
        if len(str) > 1 and str[0] == str[len(str)-1]:
            count += 1

    return(count)

def front_x(words):
    lst = []
    lst1 = []
    for i in range(0, len(words)):
        str = words[i]
        if str[0] == "x":
            lst.append(str)
            lst.sort()
        else:
            lst1.append(str)
            lst1.sort()
    lst.extend(lst1)
    return(lst)


def sort_last(tuples):
    lst = len(tuples) 
    for i in range(0, lst): 
        for j in range(0, lst-i-1): 
            if (tuples[j][-1] > tuples[j + 1][-1]): 
                temp = tuples[j] 
                tuples[j]= tuples[j + 1] 
                tuples[j + 1]= temp 
    return tuples 

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
  print('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

 
  print('front_x')
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
 
  print('sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()