if __name__ == '__main__':
    # baseQQList = [
    #     '3307855877',
    #     '692861774',
    #     '2311158845',
    #     '1640004311',
    #     '3586135098',
    #     '2995442553',
    #     '2363529760',
    #     '2960514620',
    #     '200833728',
    #     '2075433830',
    #     '3407433504',
    #     '2535720182',
    #     '640377115',
    #     '1121103265',
    #     '2816752986',
    #     '2157336037',
    #     '1849133273',
    #     '2715767228',
    #     '2861046949',
    #     '2806797204',
    #     '1652580776',
    #     '203022439',
    #     '2311714400',
    #     '2504772239',
    #     '2472443327',
    #     '2083248362',
    #     '3224037773',
    #     '3194484652',
    #     '3433727132',
    #     '1905155473',
    #     '1409572099',
    #     '1283576093',
    #     '2245556036',
    #     '3152108217',
    #     '2679985381',
    #     '3325753892',
    #     '2689140566',
    #     '2180719626',
    #     '1830924003',
    #     '3382458622',
    #     '3190332298',
    #     '1878363445',
    #     '2457556994',
    #     '2938532290',
    #     '3442961619',
    #     '2894069095',
    #     '2694038468',
    #     '16198640202',
    #     '2524894584',
    #     '3348228595',
    #     '3036026791',
    #     '2709673395',
    #     '3442835558',
    #     '2652522514',
    #     '1295643167',
    #     '205768324',
    #     '3234490154',
    #     '3055586383',
    #     '1035762728',
    #     '2978633163',
    #     '2670811289',
    #     '3123285407',
    #     '996821629',
    #     '1437317522',
    #     '3479995447',
    #     '3353095646',
    #     '2134074136',
    #     '1317187525',
    #     '2953429767',
    # ]

    tmp = []
    baseQQList = []

    with open('./base.txt') as f:
        lf = f.readlines()
        tmp = lf

    for i in tmp:
        baseQQList.append(i.strip())

    queryQQList = []

    try:
        with open('./querylist.txt') as f:
            lf = f.readlines()
            tmp = lf

        for i in tmp:
            queryQQList.append(i.strip())
    except Exception as e:
        print('querylist.txt 文件不存在或格式错误')
        print('\n')
        input('按回车退出')
        exit()


    print('比对库中的数据：', baseQQList)
    print('\n')
    print('准备对比的数据：', queryQQList)

    alertList = []
    for i in queryQQList:
        if i in baseQQList:
            alertList.append(i)

    print('\n')
    if alertList != []:
        print('存在的项目: ', alertList)
    else:
        print('没有匹配的项目')
    print('\n')
    input('按回车退出...')
