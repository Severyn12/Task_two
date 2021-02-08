'''
In this module were implemented functions
that check if the board is correctly built.
>>> validate_board(["****4****","***21****"," 26****","* 5 2****",\
"  04 8 2 "," 7  65  4","12  34 ","  456 ***","  1 3****"])
False
'''


def rule2(lst:list)->bool:
    '''
    Checks if there is no similar elements
    in lines.
    If there similar elements returns False.
    Otherwise returns True.
    >>> rule2([[1,2,13,4],[1,3,4,5]])
    False
    '''
    check = []
    count = 0
    while count < len(lst[0]):
        for ele in lst:
            if ele[count] not in ('*',' '):
                if ele[count] in check:
                    return False
                check.append(ele[count])
        count += 1
        check.clear()
    return True


def rule1(lst:list)->bool:
    '''
    Checks if there is no similar elements
    in rows.
    If there similar ele returns False.
    Otherwise returns True.
    >>> rule1([['*','*',1,'*'],['*','*',3,'*']])
    True
    '''
    temp = []
    for row in lst:
        for ele in row:
            if ele not in ('*',' '):
                if ele in temp:
                    return False
                temp.append(ele)
        temp.clear()
    return True


def rule3(lst:list)->bool:
    '''
    Checks if each of coloured lines doesn't have
    similar elements.
    >>> rule3(["**** ****","***1 ****","  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  ","  8  2***","  2  ****"])
    False
    '''
    num = 0
    county = 4
    check = []
    while county > 0:
        for i,row in enumerate(lst[num:]):
            if row[county] not in ('*',' '):
                if row[county] in check:
                    return False
                check.append(row[county])
            if i == 4:
                for ele in row[county+1:]:
                    if (ele not in ('*',' ')) and (ele in check):
                        return False
                    check.append(ele)
        num += 1
        county = -1
        check.clear()
    return True


def validate_board(lst:list)->bool:
    '''
    Cheks if bord is built correctly.
    >>> validate_board(["**** ****","***1 ****","  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  ","  8  2***","  2  ****"])
    False
    '''
    opt1 = rule1(lst)
    opt2 = rule2(lst)
    opt3 = rule3(lst)
    if opt1 and opt2 and opt3:
        return True
    return False
