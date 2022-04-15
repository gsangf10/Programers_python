# 신고 결과 받기

def solution(id_list, report, k):
    complain_cnt = dict.fromkeys(id_list,0)
    email_list = dict.fromkeys(id_list,0)
    
    # 중복 제거 (하나의 계정에서 같은 계정을 신고 한 횟수는 1회로 한다.)
    report = list(set(report))
    
    # 계정당 신고받은 횟수 count
    for i in report:
      reporter = i.split()
      complain_cnt[reporter[1]] += 1

    # 신고받은 계정이 이용정지 조건에 만족하면 메일 발송 count
    for i in report:
      reporter = i.split()
      if complain_cnt[reporter[1]] >= k:
        email_list[reporter[0]] += 1

    # 메일 발송 횟수를 정답처리로 변환
    answer = list(email_list.values())
    
    return answer


# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
solution(id_list, report, k)
