### **admin接口自动化运行环境**

1、安装Python环境

    官网下载：
    https://www.python.org/downloads/
    或使用package里的执行文件安装
    配置环境变量
    验证环境：python3 --version
    
2、安装Python虚拟环境

    豆瓣源安装：
    多个python版本，例如安装了2和3版本，3版本安装使用pip3 install xxx
    pip3 install -i https://pypi.douban.com/simple virtualenvwrapper
    创建虚拟环境：mkvirtualenv xxx
    切换/进入虚拟环境：workon xxx
    删除虚拟环境：rmvirtualenv xxx
    
3、安装根目录下requirements.txt依赖

    pip3 install -r requirements.txt
    豆瓣源安装：
    pip3 install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com -r requirements.txt
    如果涉及权限问题，可以如下:
    pip3 install --user -i http://pypi.douban.com/simple --trusted-host pypi.douban.com -r requirements.txt


4、配置allure环境
    
    解压package目录中的allure-2.13.2.zip
    配置环境变量
    验证环境：allure --version
    
5、运行/测试
    
    
    进入根目录，运行run.py文件
    python3 run.py
    

