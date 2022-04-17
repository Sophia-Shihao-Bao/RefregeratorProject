import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "student@electricats.com"  # 用户名
mail_pass = "1234Elec"  # 口令


sender = 'student@electricats.com'
receivers = ['sophiabaoz@icloud.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
opts = input('请输入您要干什么？1为储存菜品，2为查看冰箱里有什么')

def dieoralive(birthday,today):
    daydif = today-birthday
    if daydif<3:
        return '贼新鲜'
    elif daydif<5:
        return '毒不死'
    elif daydif<7:
        return '差不多该人了吧'
    else:
        return '大哥您当我是垃圾桶呢？臭晕了...'

if opts == '1':
    with open( 'foodinfridge.sophia' , 'a', encoding='utf-8' ) as file:
        localtime = time.localtime(time.time())
        veg = input('您买了什么菜？')
        file.write(veg+' ')
        for i in range (0,3):
            file.write(str(localtime[i]))
            file.write(' ')
        file.write('\n')

elif opts == '2':
    with open( 'foodinfridge.sophia' , 'r', encoding='utf-8' ) as file:
        foodlist = file.readlines()
        newfoodlist = []
        deadveg = []
        for i in foodlist:
            veginfo = i.split(' ')
            currentday = time.localtime().tm_year*365+time.localtime().tm_mon*30 + time.localtime().tm_mday
            vegday = int(veginfo[1])*365+int(veginfo[2])*30+int(veginfo[3])
            veginfo[4] = dieoralive(vegday,currentday)
            newfoodlist.append(veginfo)
            if veginfo [4] == '大哥您当我是垃圾桶呢？臭晕了...':
                deadveg.append(veginfo)
        print('\n'+'您冰箱里有以下蔬菜：'+'\n')
        for veg in newfoodlist:
            print('蔬菜名： '+ veg[0]+'  放入日期： '+veg[1]+' 年 '+veg[2]+' 月 '+veg[3]+' 日 '+' 健康度： '+veg[4])
            print()
        if len(deadveg)>0:
            deadvegname = ''
            for i in deadveg:
                deadvegname = deadvegname+i[0]+'、 '
            emailcontent = '主人您好:'+'\n'+'您在我这里存放的以下几个蔬菜水果已经壮烈牺牲了\n'+'如光您不尽快把它们清理掉的话，我可能很快也不行了\n'+'这是它们的名单：\n'+deadvegname
            message = MIMEText ( emailcontent, 'plain' , 'utf-8' )
            message['From'] = Header ( "来自您的智能冰箱" , 'utf-8' )
            message['To'] = Header ( "主人" , 'utf-8' )

            subject = '[URGENT]Your vegetable is going bad!'
            message['Subject'] = Header ( subject , 'utf-8' )
            try :
                smtpObj = smtplib.SMTP ()
                smtpObj.connect ( mail_host , 25 )  # 25 为 SMTP 端口号
                smtpObj.login ( mail_user , mail_pass )
                smtpObj.sendmail ( sender , receivers , message.as_string () )
                print ( "邮件发送成功" )
            except smtplib.SMTPException :
                print
                ("Error: 无法发送邮件")
        #print(foodlist)

else:
    print('您要干嘛？我没看懂')

