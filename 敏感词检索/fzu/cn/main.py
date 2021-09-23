#拼音和偏旁部首还没做，还请手下留情


import sys

if __name__ == '__main__':

    #将敏感词文件导入Words
    try:
        SensitiveWords = open(sys.argv[1], 'r', encoding='UTF-8')
        Words = SensitiveWords.readlines()
        SensitiveWords.close()
    except:
        print("读取内容出错")

    #将原文导入File
    try:
        OrgFile = open(sys.argv[2], 'r', encoding='UTF-8')
        File = OrgFile.readlines()
        OrgFile.close()
    except:
        print("读取内容出错")

    #将ans文件打开，改为覆盖写模式
    AnsFile = open(sys.argv[3], 'w', encoding='UTF-8')

    #计算出敏感词和原文的行数，方便后续循环
    lineNum1 = list.__len__(Words)
    lineNum2 = list.__len__(File)

    #total是查询到的敏感词总数
    total = 0
    #
    for i in range(lineNum1):

        #敏感词的第一个字
        FirstWord = Words[i][0]

        #判断敏感词有几个字，将敏感词的最后一个字存入LastWord
        if str.__len__(Words[i]) == 2:
            LastWord = Words[i][1]
        elif str.__len__(Words[i]) == 1:
            LastWord = Words[i][0]
        else:
            LastWord = Words[i][-2:-1]

        #原文逐行判断是否存在敏感词
        for n in range(lineNum2):

            #flag代表是否在原文中查询到了第一个敏感字
            flag = 0

            #原文一行有多少字
            for m in range(str.__len__(File[n])):
                char = File[n][m]

                #出现字符与敏感词第一个字相同
                if char == FirstWord:
                    flag = 1

                    #记录下第一个字在原文的位置
                    first = m

                #出现字符与敏感词最后一个字相同
                if char == LastWord and flag == 1:

                    #记录下最后一个字在原文的位置
                    last = m

                    #查询到的敏感词总数+1
                    total += 1

                    #开始写入文件ans
                    AnsFile.write("Line")
                    AnsFile.write("{}:<".format(n+1))

                    if last == str.__len__(File[n]):
                        AnsFile.write("{}>{}\n".format(Words[i][:-1], File[n][first:]))
                    else:
                        AnsFile.write("{}>{}\n".format(Words[i][:-1], File[n][first:last+1]))

                    #为了防止后续还有敏感词最后一个字出现，跳到下一行
                    break

#最后在首行加上total的输出（不知道为啥加上后第二行line3没了）
f = open(sys.argv[3], "r+", encoding='UTF-8')
old = f.read()
f.seek(0)
f.write("total:{}\n".format(total))
f.write(old)
