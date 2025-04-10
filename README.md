# 关于作者
大家好，我是程序员阿江-Relakkes，近期我会给大家出一些爬虫方面的教程，爬虫入门、进阶、高级都有，有需要的朋友，star仓库并持续关注本仓库的更新。

- [Github万星开源自媒体爬虫仓库MediaCrawler作者](https://github.com/NanmiCoder/MediaCrawler)
- 全栈程序员，熟悉Python、Golang、JavaScript，工作中主要用Golang。
- 曾经主导并参与过百万级爬虫采集系统架构设计与编码
- 爬虫是一种技术兴趣爱好，参与爬虫有一种对抗的感觉，越难越兴奋。

## 查看教程
在线链接：https://nanmicoder.github.io/CrawlerTutorial/

对应的视频链接近期也会同步更新出来，[查看B站合集地址](https://space.bilibili.com/434377496/channel/collectiondetail?sid=4035213&ctype=0)

## 爬虫交流群
可以加作者wx拉进群: yzglan，备注来自github爬虫教程.


## 免责声明
>本仓库的所有内容仅供学习和参考之用，禁止用于商业用途。任何人或组织不得将本仓库的内容用于非法用途或侵犯他人合法权益。本仓库所涉及的爬虫技术仅用于学习和研究，不得用于对其他平台进行大规模爬虫或其他非法行为。对于因使用本仓库内容而引起的任何法律责任，本仓库不承担任何责任。使用本仓库的内容即表示您同意本免责声明的所有条款和条件。


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=NanmiCoder/CrawlerTutorial&type=Date)](https://star-history.com/#NanmiCoder/CrawlerTutorial&Date)

# PTT股票版爬虫

这是一个简单的爬虫程序，用于爬取台湾PTT论坛的股票版(Stock)帖子列表数据。

## 功能

- 爬取首页的帖子列表
- 提取帖子标题、作者、发布日期、推文数量和链接
- 提供同步和异步两种实现方式

## 文件说明

- `ptt_stock_crawler.py`: 异步版本爬虫，使用httpx和parsel库
- `ptt_stock_crawler_sync.py`: 同步版本爬虫，使用requests和BeautifulSoup库

## 环境要求

需要安装以下Python库：

```bash
pip install httpx parsel requests beautifulsoup4
```

## 使用方法

### 异步版本

```bash
python ptt_stock_crawler.py
```

### 同步版本

```bash
python ptt_stock_crawler_sync.py
```

## 输出示例

```
共爬取到 20 条帖子:

--- 帖子 1 ---
标题: [新聞] 證交所：下半年新上市櫃公司將增二成
作者: jason888
日期: 4/12
推文数: 3
链接: https://www.ptt.cc/bbs/Stock/M.1712894044.A.CC3.html

--- 帖子 2 ---
标题: [請益] 股票當沖零股
作者: loveponypony
日期: 4/12
推文数: 1
链接: https://www.ptt.cc/bbs/Stock/M.1712893980.A.3A3.html

...
```

## 注意事项

1. 该爬虫仅用于学习和研究，请勿用于商业用途
2. 请遵守PTT论坛的爬虫规则和使用条款
3. 爬虫频繁请求可能会被网站限制IP，请合理控制请求频率

## 扩展功能

可以进一步扩展以下功能：

1. 爬取多页数据
2. 爬取帖子内容和评论
3. 数据存储到数据库
4. 添加代理IP池
5. 添加错误重试机制
