# 第一个基础框架

我还在研究，大家先凑合着用

前端使用vue(暂时是vue3,可以切换vue2,大家先用着，我目前感觉区别不大) 

后端使用Flask

---

使用攻略v2.0

后端：保证你的python环境安装了flask和相关的东西（报错会有提示，pycharm会给你装）

运行EditEnd目录下的run.py，就可以启动后端

---

前端:打开EditFront/front目录下的package.json，你的专业版pycharm右下角会提示npm install

安装依赖后你的package.json的第六行左边会出现三角符号（也就是运行标志）点击一下就启动前端了


---

## 如何验证你是否配好了环境？

启动后端：

浏览器访问 http://localhost:5000/api/test 

应返回 JSON 数据：{"message": "Hello from Flask!"}。

启动前端：

浏览器访问 http://localhost:8080。

打开开发者工具（F12），检查控制台是否打印了从 Flask 获取的 Hello from Flask!。


