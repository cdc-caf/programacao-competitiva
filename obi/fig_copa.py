n, c, m = map(int, input().split())

figCarimbadas = list(map(int, input().split()))
figCompradas = list(map(int, input().split()))

soma = 0
for i in range(len(figCarimbadas)):
    if not figCarimbadas[i] in figCompradas:
        soma+=1
print(soma)