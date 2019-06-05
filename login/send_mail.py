from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def send_mail(email, code):
    subject = '来自Nucan的测试邮件'
    text_content = '一切必死的/一旦睁开眼/走上属于自己的小径/谁个不喜欢/取最短的道回归宇宙；故山涧奔涌而下/寻求眠息'
    html_content = '''<p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>点击验证</a></p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
