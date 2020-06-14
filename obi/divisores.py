## this is a template example

import sys

def main():
  input = sys.stdin.readline
  print = sys.stdout.write

  n = int(input())
  div = n

  ans = 1
  i = 2
  while i <= n:
    exp = 0
    while div % i == 0:
      exp += 1
      div = div // i
    ans *= (exp+1)
    i += 1


  print(str(ans));



# do not change
if __name__ == "__main__":
  main()
