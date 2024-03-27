# -*- coding: utf-8 -*-
# @Author  : relakkes@gmail.com
# @Time    : 2024/3/27 22:47
# @Desc    : 分别使用两个库演示如何提取html文档结构数据
from bs4 import BeautifulSoup


class NoteContent:
    title: str = ""
    author: str = ""
    publish_date: str = ""
    detail_link: str = ""

    def __str__(self):
        return f"{self.title}_{self.detail_link}"


def parse_html_use_bs(html_content: str):
    """
    使用BeautifulSoup提取帖子标题、作者、发布日期，基于css选择器提取
    :param html_content: html源代码内容
    :return:
    """
    # 初始化一个帖子保存容器
    note_content = NoteContent()
    # 初始化bs查询对象
    soup = BeautifulSoup(html_content)
    # 提取标题并去左右除换行空格字符
    note_content.title = soup.select("div.r-ent div.title a")[0].text.strip()
    # 提取作则
    print(soup)


def parse_html_use_parse(html_content: str):
    """
    使用parse提取帖子标题、作者、发布日期，基于xpath选择器提取
    :param html_content: html源代码内容
    :return:
    """
    pass


if __name__ == '__main__':
    ori_html = """
    <div class="r-ent">
        <div class="nrec"><span class="hl f3">11</span></div>
        <div class="title">

            <a href="/bbs/Stock/M.1711544298.A.9F8.html">[新聞] 童子賢：用稅收補貼電費非長久之計 應共</a>

        </div>
        <div class="meta">
            <div class="author">addy7533967</div>
            <div class="article-menu">

                <div class="trigger">⋯</div>
                <div class="dropdown">
                    <div class="item"><a href="/bbs/Stock/search?q=thread%3A%5B%E6%96%B0%E8%81%9E%5D+%E7%AB%A5%E5%AD%90%E8%B3%A2%EF%BC%9A%E7%94%A8%E7%A8%85%E6%94%B6%E8%A3%9C%E8%B2%BC%E9%9B%BB%E8%B2%BB%E9%9D%9E%E9%95%B7%E4%B9%85%E4%B9%8B%E8%A8%88+%E6%87%89%E5%85%B1">搜尋同標題文章</a></div>

                    <div class="item"><a href="/bbs/Stock/search?q=author%3Aaddy7533967">搜尋看板內 addy7533967 的文章</a></div>

                </div>

            </div>
            <div class="date"> 3/27</div>
            <div class="mark"></div>
        </div>
    </div>
    """
    parse_html_use_bs(ori_html)
