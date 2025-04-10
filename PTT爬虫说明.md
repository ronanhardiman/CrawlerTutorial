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

## 代码说明

### 异步版本实现关键点

1. 使用`httpx`库进行HTTP请求，支持异步操作
2. 使用`parsel`库解析HTML内容
3. 通过`async/await`语法实现异步爬取
4. 处理PTT的年龄验证，获取cookie后进行访问

### 同步版本实现关键点

1. 使用`requests`库进行HTTP请求
2. 使用`BeautifulSoup`库解析HTML内容
3. 使用`Session`对象保持cookie状态
4. 处理PTT的年龄验证

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