# -*- coding: utf-8 -*-
# @Author: 您
# @Time: 此刻
# @Desc: PTT股票版爬虫-同步版本

import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class StockPost:
    """股票帖子信息类"""
    title: str  # 帖子标题
    author: str  # 作者
    date: str  # 发布日期
    link: str  # 详情链接
    push_count: Optional[str] = None  # 推文数量

def crawl_ptt_stock():
    """爬取PTT股票版首页帖子列表"""
    url = "https://www.ptt.cc/bbs/Stock/index.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    
    # 创建session来保持cookie
    session = requests.Session()
    
    # 获取年龄验证的cookie
    response = session.get("https://www.ptt.cc/ask/over18?from=/bbs/Stock/index.html", headers=headers)
    
    # 提交年龄验证表单
    data = {
        "from": "/bbs/Stock/index.html",
        "yes": "yes"
    }
    session.post("https://www.ptt.cc/ask/over18", headers=headers, data=data)
    
    # 使用session访问目标页面
    response = session.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return []
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = []
    
    # 提取所有帖子元素
    post_elements = soup.select("div.r-ent")
    
    for element in post_elements:
        # 提取标题和链接
        title_element = element.select_one("div.title a")
        title = title_element.text.strip() if title_element else "已删除"
        link = title_element.get('href', '') if title_element else ""
        
        # 提取作者
        author = element.select_one("div.meta div.author").text.strip() if element.select_one("div.meta div.author") else ""
        
        # 提取日期
        date = element.select_one("div.meta div.date").text.strip() if element.select_one("div.meta div.date") else ""
        
        # 提取推文数量
        push_element = element.select_one("div.nrec span")
        push_count = push_element.text if push_element else ""
        
        # 创建帖子对象并添加到列表
        post = StockPost(
            title=title,
            author=author,
            date=date,
            link=f"https://www.ptt.cc{link}" if link else "",
            push_count=push_count
        )
        posts.append(post)
        
    return posts

def main():
    """主函数"""
    posts = crawl_ptt_stock()
    print(f"共爬取到 {len(posts)} 条帖子:")
    
    for i, post in enumerate(posts, 1):
        print(f"\n--- 帖子 {i} ---")
        print(f"标题: {post.title}")
        print(f"作者: {post.author}")
        print(f"日期: {post.date}")
        print(f"推文数: {post.push_count}")
        print(f"链接: {post.link}")

if __name__ == "__main__":
    main() 