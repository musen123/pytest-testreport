# pytest-testreport

### 1、pytest-testreport介绍

pytest-testreport是一个针对pytest的生成html报告的插件，使用起来非常简单，只需要再pytest.ini文件中做简单的配置即可实现html报告的生成

####使用案例：
- 方式一：在pytest.ini文件加入如下配置，即可实现生成html报告
    ```ini
    [report]
    file_name = report.html
    ```
- 方式二： pytest 运行测试时加上参数--report 指定报告文件名

    ```pytest --report=musen.html```


### 2、安装pytest-testreport

pytest-testreport是基于python3.6开发的，安装前请确认你的python版本>3.6

安装命令

```pip install pytest-testreport```

### 3、使用文档：
https://unittestreport.readthedocs.io/en/latest/doc9_pytest/
### 备注：

- ##### 开发者：柠檬班—木森、柠檬班—雨泽

- ##### E-mail:musen_nmb@qq.com

- ##### 大家在使用过程中发现bug,可以联系我，以便优化解决！

