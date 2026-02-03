""" 
测试当前ip可以访问哪些禁漫域名 
修改取自JMcomic Crawler Python文档
https://jmcomic.readthedocs.io/zh-cn/latest/tutorial/8_pick_domain/ 
**含有部分AI生成的代码
"""

import traceback
import sys
import os
from libs.self.config import cfgs
from jmcomic import JmOption, JmcomicText, JmModuleConfig, disable_jm_log, multi_thread_launcher, Set
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))



option = JmOption.default()

domain_status_dict = {}   # ✔ 先定义
disable_jm_log()          # ✔ 提前关闭日志


def get_all_domain():
    template = 'https://jmcmomic.github.io/go/{}.html'
    url_ls = [template.format(i) for i in range(300, 309)]
    domain_set: Set[str] = set()

    def fetch_domain(url):
        from curl_cffi import requests as postman
        text = postman.get(url, allow_redirects=False).text

        for domain in JmcomicText.analyse_jm_pub_html(text):
            if domain.startswith('jm365.work'):
                continue
            domain_set.add(domain)

    multi_thread_launcher(
        iter_objs=url_ls,
        apply_each_obj_func=fetch_domain,
    )

    return domain_set


def test_domain(domain: str):
    global domain_status_dict   # ✔ 声明 global

    client = option.build_jm_client(impl='html', domain_list=[domain])
    status = 'ok'

    try:
        client.get_album_detail('350234')
    except Exception as e:
        status = str(e.args)

    domain_status_dict[domain] = status


def test_all_domains():
    try:
        # ✔ 先获取所有域名
        domain_set = get_all_domain()
        print(f'获取到 {len(domain_set)} 个域名，开始测试…')

        # ✔ 再进行测试
        multi_thread_launcher(
            iter_objs=domain_set,
            apply_each_obj_func=test_domain,
        )

        # ✔ 输出结果
        for domain, status in domain_status_dict.items():
            print(f'{domain}: {status}')

    except Exception as err:
        print(f'测试过程中发生错误：{type(err).__name__}:{err}')
        traceback.print_exc()
    finally:
        # ✔ 恢复日志开关
        JmModuleConfig.FLAG_ENABLE_JM_LOG = cfgs.SHOW_JM_LOG

