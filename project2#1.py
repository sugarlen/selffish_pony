def read_ponies(filename):
    elevation = []
    path = []
    ponies = []
    result = ([elevation, path, ponies])
    with open(filename, mode='r', encoding='utf-8') as f:
        t = []

        for line in f:
            if line.isspace():
                continue
            else:
                t.append(line.strip())

        for i in range(1, 4):

            t[i] = t[i].split(',')

            for i1 in range(len(t[i])):
                t[i][i1] = t[i][i1].replace(' ', '')
                t[i][i1] = int(t[i][i1])

            elevation.append(t[i])

        for k in range(5, 10):
            t[k] = t[k].split(',')
            for k1 in range(len(t[k])):
                t[k][k1] = t[k][k1].replace('(', '')
                t[k][k1] = t[k][k1].replace(')', '')
                t[k][k1] = int(t[k][k1])

            t[k] = tuple(t[k])
            path.append(t[k])

        for n in range(11, 14):
            t[n] = t[n].strip().split(',', 2)
            t[n][0] = int(t[n][0])

            t[n][2] = t[n][2].replace('[', '')
            t[n][2] = t[n][2].replace(']', '')
            t[n][2] = t[n][2].split(',', 2)
            t[n][2][0] = int(t[n][2][0])
            t[n][2][1] = t[n][2][1].replace('(', '')
            t[n][2][2] = t[n][2][2].replace(')', '')
            t[n][2][1] = int(t[n][2][1])
            t[n][2][2] = int(t[n][2][2])
            t[n][2][2] = (t[n][2][1], t[n][2][2])

            t[n][2].pop(1)

            ponies.append(tuple(t[n]))

    return result
