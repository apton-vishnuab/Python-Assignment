import re

def verbing(s):
    n = len(s)
    if n >= 3:
        end_check = s[n- 3 : n]
        if end_check == "ing":
            s = s + "ly"
            return(s)
        else:
            return(s + "ing")
    else:
        return(s)

def not_bad(s):
    x = s.find("not")
    y = s.find("bad")
    if x < y:
        s = re.sub("not.*bad","good", s)
    return(s)
        
def front_back(a, b):
    x = len(a)
    y = len(b)
    if x % 2 == 0:
        ai = x // 2
    else:
        ai = (x // 2) + 1
    if y % 2 == 0:
        bi = y // 2
    else:
        bi = (y // 2) + 1
    
    a_front = a[0:ai]
    a_back = a[ai:]
    b_front = b[0:bi]
    b_back = b[bi:]
    return(a_front + b_front + a_back + b_back)

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

 
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()