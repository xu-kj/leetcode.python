def countGroups(related):
    groups = 0

    related_ = [[int(c) for c in row] for row in related]

    for i in range(len(related)):
        if related_[i][i] == 1:
            groups += 1
            visit(related_, i)

    return groups

def visit(related, i):
    if related[i][i] == 0:
        return

    for j in range(len(related)):
        if related[i][j] == 1:
            related[i][j] = 0
            visit(related, j)
