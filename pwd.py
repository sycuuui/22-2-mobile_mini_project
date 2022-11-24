dict={}
def pwd():
    try:
        file = open('./pwd/info.txt','r')
    except:
        return 
    else:
        for aline in file.readlines():
            list = aline.split(',')
            userNum=list[0]
            userPwd=list[1].strip()
            dict[userNum]=userPwd
        file.close()
    return dict