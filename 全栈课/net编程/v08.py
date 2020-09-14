import smtplib
from email.mime.text import MIMEText

mail_content = """
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

msg = MIMEText(mail_content, "html", 'utf-8')

# 构建发送者地址和登录信息
from_addr = "1286542042@qq.com"
from_pwd = "szribwlnphnfhgjg"

# 构建邮件接收者信息
to_addr = "168237970@qq.com"
smtp_srv = 'smtp.qq.com'

try:
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