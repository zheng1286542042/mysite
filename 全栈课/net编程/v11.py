from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#构建一个HTML邮件内容
msg = MIMEMultipart("alternative")

# 构建一个HTML邮件内容
html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h1>哈哈，北京欢迎你</h1>
        </body>
        </html>

"""

msg_html = MIMEText(html_content,"html","utf-8")
msg.attach(msg_html)

msg_text = MIMEText("just text content","plain","utf-8")
msg.attach(msg_text)

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