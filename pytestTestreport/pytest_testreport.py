# -*- coding: utf-8 -*-
import datetime
import os
import time
import pytest
from jinja2 import Environment, FileSystemLoader
import logging
test_result = {
    "title": "",
    "tester": "",
    "desc": "",
    "cases": {},
    'rerun':0,
    "failed": 0,  # 失败用例
    "passed": 0,  # 成功用例
    "skipped": 0,  # 跳过的用例
    "error": 0,
    "start_time": 0,  # 开始运行时间
    "run_time": 0,  # 运行时间
    "begin_time": "",
    "all": 0,
    "testModules": set()
}


def pytest_make_parametrize_id(config, val, argname):
    return val.get('title') or val.get('desc')


def pytest_runtest_logreport(report):
    # 获取用例执行的结果
    report.duration = '{:.6f}'.format(report.duration)
    test_result['testModules'].add(report.fileName)
    # 用例总数加1
    if report.when == 'call':
        test_result[report.outcome] += 1
        test_result["cases"][report.nodeid] = report
    elif report.outcome == 'failed':
        report.outcome = 'error'
        test_result['error'] += 1
        test_result["cases"][report.nodeid] = report
    elif report.outcome == 'skipped':
        test_result[report.outcome] += 1
        test_result["cases"][report.nodeid] = report



def pytest_sessionstart(session):
    """整个用例执行之前，获取时间信息"""
    start_ts = datetime.datetime.now()
    test_result["start_time"] = start_ts.timestamp()
    test_result["begin_time"] = start_ts.strftime("%Y-%m-%d %H:%M:%S")


def pytest_sessionfinish(session):
    """在整个测试运行完成之后调用的钩子函数,可以在此处生成测试报告"""
    report = session.config.inicfg.config.sections.get('report')
    report2 = session.config.getoption('--report')
    if report:
        test_result['title'] = gbk_change_utf8(report.get('title')) or '测试报告'
        test_result['tester'] = gbk_change_utf8(report.get('tester')) or '小测试'
        test_result['desc'] = gbk_change_utf8(report.get('desc')) or '无'
        name = gbk_change_utf8(report.get('file_name')) or 'report.html'
    elif report2:
        test_result['title'] = '测试报告'
        test_result['tester'] = '小测试'
        test_result['desc'] = '无'
        name = report2
    else:
        return
    if not name.endswith('.html'):
        file_name = time.strftime("%Y-%m-%d_%H_%M_%S") + name + '.html'
    else:
        file_name = time.strftime("%Y-%m-%d_%H_%M_%S") + name

    if os.path.isdir('reports'):
        pass
    else:
        os.mkdir('reports')
    file_name = os.path.join('reports', file_name)
    # 获取结束运行的时间
    test_result["run_time"] = '{:.6f} S'.format(time.time() - test_result["start_time"])
    test_result['all'] = len(test_result['cases'])
    # 计算用例通过率
    if test_result['all'] != 0:
        test_result['pass_rate'] = '{:.2f}'.format(test_result['passed'] / test_result['all'] * 100)
    else:
        test_result['pass_rate'] = 0
    # 渲染测试报告
    template_path = os.path.join(os.path.dirname(__file__), './templates')
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('templates.html')
    report = template.render(test_result)
    with open(file_name, 'wb') as f:
        f.write(report.encode('utf8'))


def gbk_change_utf8(string: str):
    if isinstance(string, str):
        try:
            res = string.encode('gbk').decode('utf-8')
        except:
            return string
        else:
            return res
    else:
        return string


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """功能未知：为运行的测试用例设置一个报告"""
    outcome = yield
    report = outcome.get_result()
    fixture_extras = getattr(item.config, "extras", [])
    plugin_extras = getattr(report, "extra", [])
    report.extra = fixture_extras + plugin_extras
    report.fileName = item.location[0]
    if hasattr(item, 'callspec'):
        report.desc = item.callspec.id or item._obj.__doc__
    else:
        report.desc = item._obj.__doc__
    report.method = item.location[2].split('[')[0]


def pytest_addoption(parser):
    group = parser.getgroup("testreport")
    group.addoption(
        "--report",
        action="store",
        metavar="path",
        default=None,
        help="create html report file at given path.",
    )
