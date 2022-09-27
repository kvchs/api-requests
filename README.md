### 整体框架结构
```
1、common，公共方法层：封装一些常用的方法、日志配置文件、
2、config，配置层：日志级别、mysql数据库信息、账号信息
3、data，数据层：测试用例
4、img，图片层：页面报错截图
5、logs，日志文件层：脚本运行日志
6、output，测试报告层
7、pages，业务逻辑层
8、testcases，测试逻辑层
9、main文件：脚本入口
```

### 特点
```
特点：
1、通过pytest单元测试框架组织管理测试用例
2、引入page object思想对用例进行分层设计，业务代码和测试代码相分离
3、页面元素共性操作提取：basepage封装，实现实时执行日志输出，异常实时捕获，用例失败截图
4、测试用例中，使用数据驱动
5、logging日志引入，问题定位
6、allure报表，用例失败后截图
7、用例失败重试，提高用例稳定性
8、集成到jenkins中，每天\小时构建多次
```

### TODO list
```commandline
给几个建议
1：封装 request 方法，可以写成一个方法，吧 method 当作参数写进去，其他需要什么 response，就传什么参数
.request(method, url, params=params, data=data, json=json, timeout=timeout, files=files, headers=headers,
stream=stream,verify=False )
2：登录 可以考虑用 requset session 方法，是全局的
3：关于日志，还是账户密码等配置。 pytest 有 pytest.ini 配置文件，可以直接配置，然后读取。很方便
```

### requests 的底层实现其实就是 urllib3
Python的标准库中 urllib2 模块已经包含了平常我们使用的大多数功能，但是它的 API 使用起来让人感觉不太好，而 Requests 自称 “HTTP for Humans”，说明使用更简洁方便。

### 执行用例
pytest testcases/login_success.py --alluredir=output --clean-alluredir
allure serve ./result 

### 并发执行用例
pip install pytest-xdist

### 完整执行步骤
```commandline
方式一
生成测试结果数据
pytest --alluredir=output/result --clean-alluredir 
生成allure报告路径
allure generate output/result -o output/allure-report --clean 
手动打开报告
allure open output/allure-report/

方式二
自动生成报告并打开
allure serve output/result

```
参考：https://blog.csdn.net/weixin_39891694/article/details/110889605
