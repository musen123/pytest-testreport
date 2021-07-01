# pytest-testreport

### 1、pytest-testreport介绍

pytest-testreport是一个针对pytest的生成html报告的插件，使用起来非常简单，安装好pytest-testreport之后，运行用例时加上参数即可生成报告

###### 注意点：如果安装了pytest-html这个插件，请先卸载，不然会有冲突

##### 使用案例：

- ###### 命令行执行： pytest 运行测试时加上参数--report 指定报告文件名

    ```shell
    # 指定报告文件名
    pytest --report=musen.html
    
    #其他配置参数
    --title=指定报告标题
    --tester=指定报告中的测试者
    --desc = 指定报告中的项目描述
    
    # 同时使用多个参数
    pytest --report=musen.html --title=测试报告 --tester=测试菜鸟 --desc=项目描述
    ```
    
- ###### pytest.main执行

    ```shell
    import pytest
    
    pytest.main(['--report=musen.html',
                 '--title=测试报告标题',
                 '--tester=木森',
                 '--desc=报告描述信息'])
    ```

    

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

