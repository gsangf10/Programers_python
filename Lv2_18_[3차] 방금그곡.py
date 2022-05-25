# [3차] 방금그곡

def solution(m, musicinfos):
    # 음악 정보를 제목, 재생된 멜로디로 나누어서 저장
    music_info = []
    for m_info in musicinfos:
      info_list = list(m_info.split(','))
      st_time = list(map(int,info_list[0].split(':')))
      fn_time = list(map(int,info_list[1].split(':')))

      play_time = (fn_time[0]*60 + fn_time[1]) - (st_time[0]*60 + st_time[1])

      title = info_list[-2]
      melody = info_list[-1]
      play_melody = ''
      m_cnt = 0
      # 붙은 멜로디 처리
      while m_cnt <= play_time:
        for i in range(len(melody)):
          if melody[i] != '#' and m_cnt > play_time:
            break
          play_melody += melody[i]
          if melody[i] == '#':
            continue
          m_cnt += 1
      
      music_info.append([title,play_melody,play_time])
    
    # 해당 멜로디 찾기
    music_name = '(None)'
    play_max = 0
    for m_info in music_info:
      is_equal = False
      for i in range(len(m_info[1])):
        if m_info[1][i:i+len(m)] == m:
          if i+len(m) == len(m_info[1]):
            is_eqaul = True
            break
          if m_info[1][i+len(m)] != '#':
            is_equal = True
            break
      
      if is_equal:
        # 재생된 시간이 가장 긴 곡 담기
        if m_info[2] > play_max:
          play_max = m_info[2]
          music_name = m_info[0]

    return music_name

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# m = "CCB"
# musicinfos = ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]
solution(m,musicinfos)
