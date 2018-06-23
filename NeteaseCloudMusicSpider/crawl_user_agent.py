import urllib3
from lxml import etree

if __name__ == '__main__':
    pool = urllib3.PoolManager()
    resp = pool.request('GET', 'http://www.useragentstring.com/pages/useragentstring.php?name=All')
    if resp.status == 200:
        root = etree.HTML(resp.data)
        items = root.xpath('//*[@id="liste"]/ul/li/a/text()')
        with open('user_agent.txt', 'w') as f:
            for item in items:
                f.write(item)
                f.write('\n')
    else:
        print("捕捉失败")
