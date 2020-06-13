dona = int(input())
filhoUm = int(input())
filhoDois = int(input())

filhoTres = dona-(filhoDois+filhoUm)
print(max(filhoTres, max(filhoUm, filhoDois)))