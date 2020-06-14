import sys

def main():
  input = sys.stdin.readline
  print = sys.stdout.write
  
  n = int(input())
  hate = [[] for i in range(n+1)]
  for i in range(1, n+1):
    hate[i] = list(map(int, input().split()[1:]))

  toVisit = [1]
  idx = 0
  cnt = 1
  groups = [0 for i in range(n+1)]
  visited = [False for i in range(n+1)]
  visited[1] = True

  while idx < cnt:
    atual = toVisit[idx]
    for o in hate[atual]:
      if not visited[o]:
        visited[o] = True
        groups[o] = not groups[atual]
        toVisit.append(o)
        cnt += 1
    idx += 1

  for i in range(2):
    pr = False
    for j in range(1, n+1):
      if groups[j] == i:
        if pr:
          print(" ")
        print(str(j))
        pr = True
    print("\n")


if __name__ == "__main__":
  main()
