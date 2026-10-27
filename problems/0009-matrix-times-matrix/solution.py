def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    
    rowa = len(a)
    cola = len(a[0])
    rowb = len(b)
    colb = len(b[0])

    result = [[0.0 for _ in range(colb)] for _ in range(rowa)]

    
    if cola != rowb:
        return -1
    else:
        for i in range(rowa):
            for j in range(colb):
                    for k in range(cola):
                        result[i][j] += a[i][k]*b[k][j]
        
        return result