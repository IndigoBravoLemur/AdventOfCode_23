g_map = [ [c for c in line.strip()] for line in open("input.txt")]
empty_rows = []
empty_cols = []
galaxies = []

for i in range(len(g_map)):
    is_empty = True
    for r in range(len(g_map)):
        if g_map[r][i] == "#":
            is_empty = False
    if is_empty:
        empty_cols.append(i)
for i,row in enumerate(g_map):
    if "#" not in row:
        empty_rows.append(i)

for r in range(len(g_map)):
    for ci, c in enumerate(g_map[r]):
        if c == "#":
            galaxies.append([r,ci])

for g in galaxies:
    gr, gc = g
    colexpansion = 0
    rowexpansion = 0

    for ec in empty_cols:
        if gc>ec:
            colexpansion += 999999
    g[1] += colexpansion

    for er in empty_rows:
        if gr>er:
            rowexpansion += 999999
    g[0] += rowexpansion

diff_sum = 0
for gi, g in enumerate(galaxies):
    gr, gc = g
    for gp in galaxies[gi:]:
        # Get shortest distance from the current to all galaxies beyond
        gpr, gpc = gp
        diff = abs(gpr-gr) + abs(gpc-gc)
        diff_sum += diff

print(diff_sum)
#print(galaxies)
#print(empty_cols)
#print(empty_rows)