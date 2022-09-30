# 메뉴 리뉴얼

def solution(orders, course):
    from itertools import combinations
    
    # 메뉴 갯수별 조합 가능한 메뉴 찾기
    def select_str(order, cnt):

        for i in combinations(order, cnt):
            if i not in comb_list:
                comb_list.append(i)

    # 조합메뉴가 포함되는지 체크
    def search_str(tg, s):
        if len(tg) > len(s):
            return False

        is_exist = False
        for t in tg:
            is_exist = True if t in s else False
            if is_exist == False:
                return False
        
        return is_exist
    
    result = []

    for c in course:
        comb_list = [['0']]
        # 세트 조합 찾기
        for order in orders:
            order = sorted(order)
            select_str(order, c)
        
        menus = {''.join(o):0 for o in comb_list}

        # 세트 메뉴 포함여부 확인
        for p in comb_list:
            for order in orders:
                if search_str(p, order):
                    s = ''.join(p)
                    menus[s] += 1

        max_cnt = 0
        max_menu = []
        
        # 가장 인기 많은 조합 찾기
        for menu, cnt in menus.items():
            if cnt > 1:
                if cnt > max_cnt:
                    max_cnt = cnt
                    max_menu = [menu]
                elif cnt == max_cnt:
                    max_menu.append(menu)
        
        result.extend(max_menu)
        result = sorted(result)

    return result

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
# solution(orders, course)
solution(["ABCD", "ABCD", "ABCD"], [2,3,4])
# ['AB', 'ABC', 'ABCD', 'ABD', 'AC', 'ACD', 'AD', 'BC', 'BCD', 'BD', 'CD']
