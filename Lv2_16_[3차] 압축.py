# [3차] 압축

def solution(msg):
    idx_list = [''] + [chr(s) for s in range(65,91)]
    d_list = []
    while len(msg) != 0:
      for i in range(len(msg),-1,-1):
        if msg[:i] in idx_list:
          d_list += [idx_list.index(msg[:i])]
          idx_list += [msg[:i+1]]
          msg = msg[i:]
          break

    return d_list

msg = "KAKAO"
solution(msg)
