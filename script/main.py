import akshare as ak
import requests
import os

def main():
    # 从环境变量读取 Token，保证安全性
    token = os.environ.get('PUSHPLUS_TOKEN')
    symbol = "600519"  # 这里改成你想监控的股票代码
    
    # 获取数据
    df = ak.stock_zh_a_spot_em()
    data = df[df['代码'] == symbol].iloc[0]
    
    name = data['名称']
    pct = data['涨跌幅']
    vol = data['成交量']
    
    # 推送逻辑
    msg = f"股票：{name}<br>涨跌幅：{pct}%<br>成交量：{vol}"
    url = f"http://www.pushplus.plus/send?token={token}&title=股票监控提醒&content={msg}"
    
    if token:
        requests.get(url)
        print("发送成功")
    else:
        print("未配置Token")

if __name__ == "__main__":
    main()

