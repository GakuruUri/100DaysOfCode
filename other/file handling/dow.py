# han = open('mbox-short.txt')
#
# for line in han:
#     line = line.rstrip()
#     wsd = line.split()
#     # guardian script
#     if len(wds) < 3 or wds[0] != 'From' :
#     # if len(wsd) < 3:
#     #     continue
#     # if wsd[0] != 'From':
#         continue
#
#     print(wsd[2])


han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.strip()

    # Guardian in compound statement
    if len(wds) < 3 or wds[0] != 'From':
        continue

    print(wds[2])
