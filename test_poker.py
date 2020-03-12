
import pytest

def poker(str1):
    player_Black=str1[7:21]
    player_White=str1[29:]
    type_Black=judge_type(player_Black)
    type_White=judge_type(player_White)
    if type_Black>type_White:
        result='Black wins'
    elif type_Black<type_White:
        result='White wins'
    else:
        result=Judge_Size(type_White,player_Black,player_White)
    return result

def judge_type(player):
    #判断牌属于哪种类型，从大到小依次为9-1
    type=1
    list1=translate(player) ##将牌面取出来成为一个int列表

    count=[0]*5##用于计算牌面出现的次数
    for i in range(0,len(list1)):
        count[i]=list1.count(list1[i])
    if count.count(2)==2:
        type=2      #是对子的情况还有可能是同花和葫芦
    if count.count(2)==4:
        type=3      #是两对的情况还有可能是同花，在这不返回
    if 3 in count :
        type=4      #是三条，但还有可能是葫芦或者同花，因此在这不返回
    if 4 in count:
        type=8
        return type  #判断为铁支的话则不可能为其他种类，在这结束
    if (3 in count) & (2 in count):
        type=7
        return type  #是葫芦也不可能是其他种类，在这返回

    shunzi = 1  ##判断是否为顺子
    for index, val in enumerate(list1[:4]):
        j = list1[index + 1]
        if j - val != 1:
            shunzi = 0
    if shunzi==1:
        type=5 #是顺子还有可能是同花顺，在这不返回


    if ((player[1] == player[4]) &( player[1] == player[7]) & (player[1] == player[10]) &( player[1] == player[13])): ##判断是否为相同花色
        if shunzi!=1:
            type = 6  ##非同花顺，只是同花
        else:
            type = 9  ##同花顺

    return type

def Judge_Size(type,player_Black,player_White):
    list_Black=translate(player_Black)
    list_White=translate(player_White)  #先将两人的牌面提取出来，生成int类型列表

    count_Black = [0] * 5
    count_White = [0] * 5
    for i in range(0, len(list_Black)):
        count_Black[i] = list_Black.count(list_Black[i])
        count_White[i] = list_White.count(list_White[i]) #计算其中每个字符出现的次数

    if type==1:
        list_Black.sort(reverse=True)
        list_White.sort(reverse=True)
        Black_wins=1
        tie=1
        for i in range(0,len(list_White)):
            if list_Black[i]!=list_White[i]:
                tie=0
            if list_Black[i]<list_White[i]:
                Black_wins=0
        if tie==1:
            result='Tie'
        elif Black_wins==1:
            result='Black wins'
        else:
            result='White wins'
        return result

    elif type==2:
        for i in range(0,len(count_Black)):
            if count_Black[i]==2:
                common_Black=list_Black[i]#将对子挑出来
        for i in range(0,len(count_White)):
            if count_White[i]==2:
                common_White=list_White[i]
        if common_White>common_Black:
            result='White wins'
        elif common_White<common_Black:
            result='Black wins'
        else:
            list_White.remove(common_White)
            list_Black.remove(common_Black)
            list_Black.sort(reverse=True)
            list_White.sort(reverse=True)
            Tie=1
            Black_wins=1
            for i in range(0,len(list_Black)):
                if list_Black[i]!=list_White[i]:
                    Tie=0
                if list_Black[i]<list_White[i]:
                    Black_wins=0
            if Tie==1:
                result='Tie'
            elif Black_wins==1:
                result='Black wins'
            else:
                result='White wins'
        return result
    elif type==3:
        list_Black=list(set(list_Black))
        list_White=list(set(list_White))
        list_Black.sort(reverse=True)
        list_White.sort(reverse=True)
        Tie=1
        Black_wins=1
        for i in range(0,len(list_White)):
            if list_Black[i]!=list_White[i]:
                Tie=0
            if list_Black[i]<list_White[i]:
                Black_wins=0
        if Tie==1:
            result='Tie'
        elif Black_wins==1:
            result='Black wins'
        else:
            result='White wins'
        return result
    elif type==4:
        for i in range(0,len(count_Black)):
            if count_Black[i]==3:
                common_Black=list_Black[i]#将条子挑出来
        for i in range(0,len(count_White)):
            if count_White[i]==3:
                common_White=list_White[i]
        if common_Black>common_White:
            result='Black wins'
        elif common_Black<common_White:
            result='White wins'
        else:
            result='Tie'
        return result
    elif type==5:
        list_White.sort(reverse=True)
        list_Black.sort(reverse=True)
        if list_Black[0]>list_White[0]:
            result='Black wins'
        elif list_Black[0]<list_White[0]:
            result='White wins'
        else:
            result='Tie'
        return result
    elif type==6:
        list_Black.sort(reverse=True)
        list_White.sort(reverse=True)
        Black_wins = 1
        tie = 1
        for i in range(0, len(list_White)):
            if list_Black[i] != list_White[i]:
                tie = 0
            if list_Black[i] < list_White[i]:
                Black_wins = 0
        if tie == 1:
            result = 'Tie'
        elif Black_wins == 1:
            result = 'Black wins'
        else:
            result = 'White wins'
        return result
    elif type==7:
        for i in range(0,len(count_Black)):
            if count_Black[i]==3:
                common_Black=list_Black[i]#将条子挑出来
        for i in range(0,len(count_White)):
            if count_White[i]==3:
                common_White=list_White[i]
        if common_Black>common_White:
            result='Black wins'
        elif common_Black<common_White:
            result='White wins'
        else:
            result='Tie'
        return result
    elif type==8:
        for i in range(0,len(count_Black)):
            if count_Black[i]==4:
                common_Black=list_Black[i]#将条子挑出来
        for i in range(0,len(count_White)):
            if count_White[i]==4:
                common_White=list_White[i]
        if common_Black>common_White:
            result='Black wins'
        elif common_Black<common_White:
            result='White wins'
        else:
            result='Tie'
        return result
    else:
        list_White.sort(reverse=True)
        list_Black.sort(reverse=True)
        if list_Black[0] > list_White[0]:
            result = 'Black wins'
        elif list_Black[0] < list_White[0]:
            result = 'White wins'
        else:
            result = 'Tie'
        return result












def translate(list): #将牌面提取出来并转换为int
    list1 = [list[0], list[3], list[6],list[9],list[12]]
    if ('T' in list1):  # 将英文字符转换为数字后续转换
        list1 = [c.replace('T', '10') for c in list1];
    if ('J' in list1):  # 将英文字符转换为数字后续转换
        list1 = [c.replace('J', '11') for c in list1];
    if ('Q' in list1):  # 将英文字符转换为数字后续转换
        list1 = [c.replace('Q', '12') for c in list1];
    if ('K' in list1):  # 将英文字符转换为数字后续转换
        list1 = [c.replace('K', '13') for c in list1];
    if ('A' in list1):  # 将英文字符转换为数字后续转换
        list1 = [c.replace('A', '14') for c in list1];
    list1 = [int(x) for x in list1]
    return list1

    



##以下为对类型的测试

def test_judge_type9():
    result='2H 3H 4H 5H 6H'
    assert judge_type(result)==9

def test_judge_type9():
    result='9H TH JH QH KH'
    assert judge_type(result)==9

def test_judge_type8():
    result='9H 9H 9H 9H KH'
    assert judge_type(result)==8

def test_judge_type7():
    result='9H 9H 9H KH KH'
    assert judge_type(result)==7

def test_judge_type6():
    result='1H 6H 9H TH KH'
    assert judge_type(result)==6

def test_judge_type5():
    result='1D 2H 3H 4H 5H'
    assert judge_type(result)==5

def test_judge_type5():
    result='TD JH QH KH AH'
    assert judge_type(result)==5

def test_judge_type4():
    result='TD TH TH KH AH'
    assert judge_type(result)==4

def test_judge_type4():
    result='TH TH TH KH AH'
    assert judge_type(result)==6 #是三条的情况同时还是同花，判断为同花

def test_judge_type3():
    result='TD TH KH KH AH'
    assert judge_type(result)==3

def test_judge_type3():
    result='TH TH KH KH AH'
    assert judge_type(result)==6 #是两对但是为同花，判断为同花

def test_judge_type2():
    result='TD TH QH KH AH'
    assert judge_type(result)==2

def test_judge_type2():
    result='TD TD QD KD AD'
    assert judge_type(result)==6 #是对子但是是同花，判断为同花

def test_judge_type2():
    result='TD TD QD QD QD'
    assert judge_type(result)==7 #是对子，是同花也是葫芦，判断为葫芦

def test_judge_type2():
    result='TH TD QD QD QD'    
    assert judge_type(result)==7 #是对子也是葫芦，判断为葫芦

def test_judge_type1():
    result= '2H 6D 8D TD QD'
    assert judge_type(result)==1

#以上是对所有类型的测试

#当两人牌面类型不同时，进行测试

def test_different_whitewins():
    input='Black: 2H 3D 5S 9C KD White: 2H 3H 4H 5H 6H'
    assert poker(input)=='White wins'

def test_different_blackwins():
    input='Black: 2H 3D 4S 5C 6D White: 2C 3H 4S 8C KH'
    assert poker(input)=='Black wins'

#以上是对牌面不同时候的测试

#以下是对牌面相同时比大小的测试

def test_common_type1_BlackWins():
    assert Judge_Size(1,'2H 3D 5S 9C KD','2C 3H 4S 8C KH')=='Black wins'

def test_common_type1_WhiteWins():
    assert Judge_Size(1,'2C 3H 4S 8C KH','2H 3D 5S 9C KD')=='White wins'

def test_common_type1_Tie():
    assert Judge_Size(1,'2H 3D 5S 9C KD','2D 3H 5C 9S KH')=='Tie'

def test_common_type2_BlackWins_inside_pair():
    assert Judge_Size(2,'2H 4D 5S 9C 9D','2D 3H 3C 9S KH')=='Black wins'

def test_common_type2_Whitewins_inside_pair():
    assert Judge_Size(2,'2H 2D 5S 9C KD','2D 3H 3C 9S KH')=='White wins'

def test_common_type2_BlackWins_outside_pair():
    assert Judge_Size(2,'2H 3D 5S 9C 9D','2D 3H 4C 9S 9H')=='Black wins'

def test_common_type2_Tie():
    assert Judge_Size(2,'2H 3D 5S 9C 9D','2D 3H 5C 9S 9H')=='Tie'

def test_common_type3_Tie():
    assert Judge_Size(3,'2H 2D 5S 9C 9D','2D 2H 5C 9S 9H')=='Tie'

def test_common_type3_BlackWins():
    assert Judge_Size(3,'2H 2D 5S TC TD','2D 2H 5C 9S 9H')=='Black wins'

def test_common_type4_BlackWins():
    assert Judge_Size(4,'5H 5D 5S TC AD','2D 2H 2C TS QH')=='Black wins'

def test_common_type4_Tie():
    assert Judge_Size(4,'5H 5D 5S TC AD','5D 5H 5C TS QH')=='Tie'

def test_common_type5_BlackWins():
    assert Judge_Size(5,'4H 5D 6S 7C 8D','3D 4H 5C 6S 7H')=='Black wins'

def test_common_type5_Tie():
    assert Judge_Size(5,'4H 5D 6S 7C 8D','4D 5H 6C 7S 8H')=='Tie'

#type6因为按照散排规则，散牌规则已经测试过，不再进行测试
#type7因为是按照条子规则来比较，条子规则已经测试过，不再进行测试

def test_common_type8_Tie():
    assert Judge_Size(8,'4H 4D 4S 4C 8D','2D 4H 4C 4S 4H')=='Tie'

def test_common_type8_BlackWins():
    assert Judge_Size(8,'4H 4D 4S 4C 8D','2D 2H 2C 2S 4H')=='Black wins'

def test_common_type9_BlackWins():
    assert Judge_Size(9,'4H 5H 6H 7H 8H','2D 3D 4D 5D 6D')=='Black wins'

def test_common_type9_Tie():
    assert Judge_Size(9,'4H 5H 6H 7H 8H','4D 5D 6D 7D 8D')=='Tie'

#以上就是所有对于牌面大小的测试

#接下来按照标准输入输出进行测试
def test_Standard_IO_WhiteWins():
    assert poker('Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH')=='White wins'

def test_Standard_IO_BlackWins():
    assert poker('Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S')=='Black wins'

def test_Standard_IO_BlackWins():
    assert poker('Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C KH') == 'Black wins'

def test_Standard_IO_BlackWins():
    assert poker('Black: 2H 3D 5S 9C KD White: 2D 3H 5C 9S KH') == 'Tie'

#以上就是本次的所有测试内容
if __name__ =="__main__":
    pytest.main()
