# 방문 길이

def solution(dirs):
    d_info = {"U":[0,1],"R":[1,0],"D":[0,-1],"L":[-1,0]}
    coordinate = [0,0]
    footprints = [[0,0]]
    
    for i in range(len(dirs)):
      f_idx = -1
      if coordinate in footprints:
        f_idx = footprints.index(coordinate)

      c_temp = []
      c_temp.extend(coordinate)
      c_temp[0] += d_info[dirs[i]][0]
      c_temp[1] += d_info[dirs[i]][1]
      if c_temp[0] not in range(-5,6) or c_temp[1] not in range(-5,6):
        continue
      coordinate = c_temp

      if f_idx != -1:
        if coordinate not in footprints[f_idx-1:f_idx+2]:
          footprints.append(coordinate)

    return len(footprints)-1

dirs = "ULURRDLLU"
dirs = "LULLLLLLU"
solution(dirs)
