# 방문 길이

def solution(dirs):
    # 방향에 따른 증감값 설정
    d_info = {"U":[0,1],"R":[1,0],"D":[0,-1],"L":[-1,0]}
    loc = [0,0] # 초기 위치
    paths = [[0,0]] # 지나온 경로
    
    for s in dirs:
      loc_temp = []
      loc_temp.extend(loc)
      loc_temp[0] += d_info[s][0]
      loc_temp[1] += d_info[s][1]

      # 지도를 벗어나면 무시
      if loc_temp[0] not in range(-5,6) or loc_temp[1] not in range(-5,6):
        continue

      route = [loc, loc_temp]

      # 중복된 경로가 없으면 경로 추가
      for i in range(len(paths)):
        if loc in paths[i] and loc_temp in paths[i]:
          break
        if i == len(paths)-1:
          paths.append(route)
      
      loc = loc_temp

    return len(paths)-1

dirs = "ULURRDLLU"
# dirs = "LULLLLLLU"
dirs = "UUUUDUDUDUUU"
# dirs = 'LRLRLUDUD'
solution(dirs)
