import sys

def main():
  input = sys.stdin.readline
  print = sys.stdout.write

  d = [0 for i in range(70)]
  e = [0 for i in range(70)]
  n = int(input())
  for i in range(n):
    t, l = input().split()
    t = int(t)
    if l == 'E':
      e[t] += 1
    else:
      d[t] += 1
  
  ans = 0
  for i in range(70):
    ans += min(d[i], e[i])

  print(str(ans))

  

if __name__ == "__main__":
  main()
