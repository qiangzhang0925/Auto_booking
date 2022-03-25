# Auto_booking
东南大学体育场馆自动预定python文件,**本项目仅供学习交流使用！！！**

> 环境 ： python3.7

### 使用步骤
- 安装依赖包
``` pip install -r requirements.txt```
- 在__main__中添加预约信息
```
username = ''#一卡通
password = ''#统一身份密码
ids = #常用联系人代号,可以登陆http://yuyue.seu.edu.cn/eduplus/order/order/order/getContacts.do?sclId=1&flag=order，搜索邀请人，在你要邀请的人那个方框右键点击“检查”或“审查元素”，查看对应的value值
phoneNum = ''#手机号
session = getsession(username,password)#获取登录后的会话
changguanID = 10 #九龙湖 羽毛球10  兵乓球7  篮球8
target_day_flag = []#格式'2022-03-22'  为空自动预约包含今天在内的下三天内
target_time = ['14','15','16','17'] #如14:00-15:00 则填'15'即可 列表模式
```