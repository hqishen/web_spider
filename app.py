import requests
import re
import pprint

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}

def getProxyServerInfo(url):
    response = requests.get(url, headers=headers)
    html = response.text
    # re.S 忽略换行的干扰
    ips = re.findall("<td>(\d+\.\d+\.\d+\.\d+)</td>", html, re.S)
    ports = re.findall("<td>(\d+)</td>", html, re.S)
    return ips, ports

if __name__ == "__main__":
    for x in range(1, 60):
        url = "https://www.xicidaili.com/nn/{}".format(x)
        print(url)
        ips , ports = getProxyServerInfo(url)
        for ip in zip(ips, ports):
            proxies = {
                 "http"  : "http://"+ ip[0] + ":" + ip[1]
                ,"https" : "http://"+ ip[0] + ":" + ip[1]
            }
            #判断ip是否可用
            try:
                res = requests.get("www.baidu.com", proxies=proxies, timeout=3)
                print("可以使用")
                with open("ip_table.txt", mode="a+") as f:
                    f.write(":", ip)
            except Exception as e:
                print(ip[0], ip[1], "cannot use")