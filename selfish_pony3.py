import copy
# 3
def  teamwork_climb(elevations, path, ponies):
    dic = dict()
    ponies = sorted(ponies, key=lambda x: x[0])
    time_step = 0
    pony_status = { pony[0]:True for pony in ponies }
    status = True
    while status: 
        ponies = dic[time_step-1] if time_step > 0 else ponies
        current_pony = []
        for pony in ponies:
            pony_a = copy.deepcopy(pony)
            if pony[0] < time_step and pony_status[pony[0]]:
                current_location = pony[2][1]
                current_location_index = path.index(pony[2][1])
                if current_location_index == len(path)-1:
                    pony_status[pony[0]] = False
                    current_pony.append(pony)
                    continue
                next_location = path[current_location_index + 1]
                distance = elevations[next_location[0]][next_location[1]] - elevations[current_location[0]][current_location[1]]
                # --- start teamwork for a ---
                if pony[1] == 'a':
                    stuck_pony_list = [ item for i,item in enumerate(current_pony) if item[2][1] == pony[2][1]
                    and distance>0 and item[2][0] < distance ]
                    if len(stuck_pony_list) >0 :
                        share_pony = sorted(stuck_pony_list, key=lambda x: x[0])[0]
                        if pony_a[2][0] >= distance - share_pony[2][0]:
                            current_pony[share_pony[0]] = (share_pony[0],share_pony[1],[distance,share_pony[2][1]])
                            pony_a[2][0] = pony_a[2][0] - distance + share_pony[2][0]
                            pony_status[share_pony[0]] = True
                # -----
                current_energy = pony[2][0] if pony[1] == 's' else pony_a[2][0]
                new_energy = current_energy - distance
                if new_energy < 0:
                    current_pony.append(pony if pony[1] == 's' else pony_a)
                    pony_status[pony[0]] = False
                else:
                    current_pony.append((pony[0],pony[1],[new_energy,next_location]))
                    pony_status[pony[0]] = True
            else: 
                current_pony.append(pony)   
        if list(pony_status.values()).count(True) > 0 or time_step< len(ponies)+1:
            status = True
            dic[time_step] = sorted(current_pony, key=lambda x: x[0])
            time_step = time_step + 1
        else:
            status = False
    return dic

result1 = teamwork_climb([[0, 2, 5], [0, 0, 10]], [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 's', [2, (0, 0)]), (1, 's', [6, (0, 0)]), (2, 'a', [14, (0, 0)])])
result2 = teamwork_climb([[0, 0], [10, 0]], [(0, 0), (1, 0), (1, 1)], [(0, 's', [0, (0, 0)]), (1, 'a', [10, (0, 0)])])
result3 = teamwork_climb([[0], [15]], [(0, 0), (1, 0)], [(0, 's', [0, (0, 0)]), (1, 'a', [10, (0, 0)])])
result4 = teamwork_climb([[0, 0], [10, 20]], [(0, 0), (1, 0), (1, 1)], [(0, 's', [10, (0, 0)]), (1, 'a', [30, (0, 0)])])
print(result1,'\n',result2,'\n',result3,'\n',result4)