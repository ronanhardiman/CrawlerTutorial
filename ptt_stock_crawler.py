# -*- coding: utf-8 -*-
# @Author: 您
# @Time: 此刻
# @Desc: PTT股票版爬虫-简单版本

import httpx
from parsel import Selector
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

async def crawl_ptt_stock():
    """爬取PTT股票版首页帖子列表"""
    url = "https://www.ptt.cc/bbs/Stock/index.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    
    # 首先需要获取over18页面的cookie
    async with httpx.AsyncClient() as client:
        # 获取年龄验证的cookie
        response = await client.get("https://www.ptt.cc/ask/over18?from=/bbs/Stock/index.html", headers=headers)
        cookies = response.cookies
        
        # 提交年龄验证表单
        data = {
            "from": "/bbs/Stock/index.html",
            "yes": "yes"
        }
        response = await client.post("https://www.ptt.cc/ask/over18", headers=headers, data=data, cookies=cookies)
        cookies = response.cookies
        
        # 使用获取的cookie访问目标页面
        response = await client.get(url, headers=headers, cookies=cookies)
        
        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            return []
        
        # 使用parsel解析HTML
        selector = Selector(text=response.text)
        posts = []
        
        # 提取所有帖子元素
        post_elements = selector.css("div.r-ent")
        
        for element in post_elements:
            # 提取标题和链接
            title_element = element.css("div.title a")
            title = title_element.css("::text").get("").strip() if title_element else "已删除"
            link = title_element.css("::attr(href)").get("") if title_element else ""
            
            # 提取作者
            author = element.css("div.meta div.author::text").get("").strip()
            
            # 提取日期
            date = element.css("div.meta div.date::text").get("").strip()
            
            # 提取推文数量
            push_element = element.css("div.nrec span::text").get("")
            
            # 创建帖子对象并添加到列表
            post = StockPost(
                title=title,
                author=author,
                date=date,
                link=f"https://www.ptt.cc{link}" if link else "",
                push_count=push_element
            )
            posts.append(post)
            
        return posts

async def main():
    """主函数"""
    posts = await crawl_ptt_stock()
    print(f"共爬取到 {len(posts)} 条帖子:")
    
    for i, post in enumerate(posts, 1):
        print(f"\n--- 帖子 {i} ---")
        print(f"标题: {post.title}")
        print(f"作者: {post.author}")
        print(f"日期: {post.date}")
        print(f"推文数: {post.push_count}")
        print(f"链接: {post.link}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 