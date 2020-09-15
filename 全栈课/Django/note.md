# Django系统
- 环境
    - python3.6
    - django1.8
# 环境搭建、
- anaconda+pycharm
- anaconda使用
    - conda list:显示当前环境安装的包
    - conda env list:显示安装的虚拟环境你列表
    - conda create -n env_name python=3.6
- pip install django==1.8

# 后台需要的流程

# 创建第一个django程序
- 命令行启动
        django-admin startporject tulingxueyuan
        cd tulingxueyaun
        python manage.py runserver
        
- pycharm启动
    - 需要配置
    
# 路由系统-urls
- 创建app 
    - app：负责一个具体业务或者1一类具体业务的模块
    - python manage.py startapp teacher
- 路由
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能模块
    - django的信息控制中枢
    - 本质上是接受URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用了RE
    - URL的具体格式为urls.py中所示
- 需要关注两点
    1.接受的URL是什么，即如何用RE对传入URl进行匹配
    2.已知URL匹配到哪个处理模块