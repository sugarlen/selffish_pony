# 2
def selfish_climb(elevations, path, ponies):
    dic = dict()
    ponies = sorted(ponies, key=lambda x: x[0])
    time_step = 0
    pony_status = { pony[0]:True for pony in ponies }
    status = True
    while status: 
        ponies = dic[time_step-1] if time_step > 0 else ponies
        current_pony = []
        for pony in ponies:
            if pony[0] < time_step and pony_status[pony[0]]:
                current_location = pony[2][1]
                current_location_index = path.index(pony[2][1])
                if current_location_index == len(path)-1:
                    pony_status[pony[0]] = False
                    continue
                next_location = path[current_location_index + 1]
                distance = elevations[next_location[0]][next_location[1]] - elevations[current_location[0]][current_location[1]]
                new_energy = pony[2][0] - distance
                if new_energy < 0:
                    current_pony.append(pony)
                    pony_status[pony[0]] = False
                else:
                    current_pony.append((pony[0],pony[1],[new_energy,next_location]))
                    pony_status[pony[0]] = True
            else:
                current_pony.append(pony)  
        if list(pony_status.values()).count(True) >0 or time_step< len(ponies)+1:
            status = True
            dic[time_step] = sorted(current_pony, key=lambda x: x[0])
            time_step = time_step + 1
        else:
            status = False
    return dic

result1 = selfish_climb([[0, 32, 45], [2, 5, 19], [7, 6, 25]], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 's', [7, (0, 0)]), (1, 's', [2, (0, 0)]), (2, 's', [25, (0, 0)])])
result2 = selfish_climb([[0, 10, 20], [0, 0, 20], [0, 0, 0]], [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)], [(0, 's', [0, (0, 0)]), (1, 's', [0, (0, 0)])])
result3 = selfish_climb([[0, 0], [0, 0]], [(0, 0), (1, 0), (1, 1)], [(0, 's', [0, (0, 0)])])
result4 = selfish_climb([[100, 90, 80, 0], [30, 20, 40, 100], [31, 45, 0, 400]], [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)], [(0, 's', [0, (0, 0)]), (1, 's', [10, (0, 0)])])
print(result1,'\n',result2,'\n',result3,'\n',result4)
