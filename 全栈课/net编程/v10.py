from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("Hello world", "plain", "utf-8")
header_from = Header("从图灵学院发出去<TuLingXueYuan@qq.com>","utf-8")
msg['From'] = header_from

# 填写接受者信息
header_to = Header("取王晓静的地方<wangxiaojgin@sina.com>", 'utf-8')
msg['To'] = header_to

header_sub = Header("这是图灵学院的主题", 'utf-8')
msg["Subject"] = header_sub

from_addr = '1286542042@qq.com'
# 此处密码是经过申请设置后的授权码
from_pwd = "szribwlnphnfhgjg"

# 收件人信息
# 此处使用qq邮箱，我给自己发送
to_addr = '168237970@qq.com'

# 输入SMTP服务器地址
# 此处根据不同的邮件服务商有不同的值
# 现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
# 腾讯qq邮箱所在的smtp地址是smtp.qq.com

smtp_srv = 'smtp.qq.com'

try:
    import smtplib
    # 两个参数
    # 第一个是服务器地址，但一定是bytes格式，所以需要编码
    # 第二个参数是服务器的接受访问端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # SMTP协议默认端口25
    # 登录邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # 1.发送地址
    # 2.接受地址，必须是list形式
    # 3.发送内容，作为字符串发送
    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print(e)