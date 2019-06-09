

def GetColumn(CSVmovies,Colind):
    Column =[]
    for row in [di[Colind] for di in CSVmovies[0:]]:
        Column.append(row)
    return Column

