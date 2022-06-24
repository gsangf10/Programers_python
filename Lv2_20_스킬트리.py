# 스킬트리

def solution(skill, skill_trees):
    cnt = 0
    # 선행스킬 길이가 1이면 스킬트리 갯수 반환
    if len(skill) == 1:
      return len(skill_trees)

    for sk in  skill_trees:
      idx = 0
      # 선행스킬이 필요한 마지막 스킬부터 검사
      for i in range(len(skill)-1,0,-1):
        if skill[i] in sk:
          idx = sk.index(skill[i])
          # 선행스킬이 없으면 종료
          if skill[i-1] not in sk[:idx]:
            break
        if i == 1:
          cnt += 1

    return cnt

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)
