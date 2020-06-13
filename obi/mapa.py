def search(visitados, matrix, i, j, lin, col):

    if i > 0 and matrix[i-1][j] == 'H' and not (i-1, j) in visitados:
        visitados.append((i-1, j))
        matrix[i][j] = '.'
        return search(visitados, matrix, i-1, j, lin, col) 
    
    if i <lin-1 and matrix[i+1][j] == 'H' and not (i+1, j) in visitados:
        visitados.append((i+1, j))
        matrix[i][j] = '.'
        return search(visitados, matrix, i+1, j, lin, col)
        
    if j<col-1 and matrix[i][j+1] == 'H' and not (i, j+1) in visitados:
        visitados.append((i, j+1))
        matrix[i][j] = '.'
        return search(visitados, matrix, i, j+1, lin, col)
        
    if j>0 and matrix[i][j-1] == 'H' and not (i, j-1) in visitados:
        visitados.append((i, j-1))
        matrix[i][j] = '.'
        return search(visitados, matrix, i, j-1, lin, col)
        
    return visitados[len(visitados)-1]


lin, col = map(int, input().split())
matrix = [list(input()) for i in range(lin)]


for i in range(lin):
    for j in range(col):
        if matrix[i][j] == 'o':
            start_pos_i = i
            start_pos_j = j
        
visita = True
visitados = [(start_pos_i, start_pos_j)]
i = start_pos_i
j = start_pos_j
while visita:
    visita = False
    if i > 0 and matrix[i-1][j] == 'H':
        matrix[i][j] = '.'
        i = i-1
        visita=True
    
    if i <lin-1 and matrix[i+1][j] == 'H':
        matrix[i][j] = '.'
        i = i+1
        visita=True
        
    if j<col-1 and matrix[i][j+1] == 'H':
        matrix[i][j] = '.'
        j = j+1
        visita=True
        
    if j>0 and matrix[i][j-1] == 'H':
        matrix[i][j] = '.'
        j = j-1
        visita=True

# visitados = search(visitados, matrix, start_pos_i, start_pos_j, lin, col)
print("{} {}".format(i+1, j+1))

