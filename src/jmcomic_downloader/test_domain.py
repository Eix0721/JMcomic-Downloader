"""
测试当前ip可以访问哪些禁漫域名
修改取自JMcomic Crawler Python文档
https://jmcomic.readthedocs.io/zh-cn/latest/tutorial/8_pick_domain/
"""

import traceback

from .config import cfgs
from jmcomic import JmOption, JmcomicText, JmModuleConfig, disable_jm_log, multi_thread_launcher


option = JmOption.default()
domain_status_dict = {}
disable_jm_log()


def get_all_domain():
    template = "https://jmcmomic.github.io/go/{}.html"
    url_ls = [template.format(i) for i in range(300, 309)]
    domain_set = set()

    def fetch_domain(url):
        from curl_cffi import requests as postman

        text = postman.get(url, allow_redirects=False).text

        for domain in JmcomicText.analyse_jm_pub_html(text):
            if domain.startswith("jm365.work"):
                continue
            domain_set.add(domain)

    multi_thread_launcher(
        iter_objs=url_ls,
        apply_each_obj_func=fetch_domain,
    )

    return domain_set


def test_domain(domain: str):
    client = option.build_jm_client(impl="html", domain_list=[domain])
    status = "ok"

    try:
        client.get_album_detail("350234")
    except Exception as e:
        status = str(e.args)

    domain_status_dict[domain] = status


def test_all_domains():
    try:
        domain_set = get_all_domain()
        print(f"获取到 {len(domain_set)} 个域名，开始测试…")

        multi_thread_launcher(
            iter_objs=domain_set,
            apply_each_obj_func=test_domain,
        )

        for domain, status in domain_status_dict.items():
            print(f"{domain}: {status}")

    except Exception as err:
        print(f"测试过程中发生错误：{type(err).__name__}:{err}")
        traceback.print_exc()
    finally:
        JmModuleConfig.FLAG_ENABLE_JM_LOG = cfgs.show_jm_log
