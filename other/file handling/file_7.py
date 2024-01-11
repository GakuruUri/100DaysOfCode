fh = open('../../mbox-short.txt')
print(fh)

for lx in fh:
    ly: str = lx.rstrip()
    print(ly.upper())
