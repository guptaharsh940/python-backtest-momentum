import requests
import pandas as pd


cookie = '_ga=GA1.1.500602646.1667295576; nsit=zK78ihpwfmxMZNMf4rGcRcrB; AKA_A2=A; defaultLang=en; ak_bmsc=E3BC33F8E84094EBC11A92A4F6520034~000000000000000000000000000000~YAAQy7YRYJC9EgKJAQAAfpSFAxS7KCfZK8141VFHJgs1a/0B/bWmqFkpyVmWhDX9RVvEvQ1tE85fnEjV5VspoRNOFkHA9MyTy0Vy8jpr6Cq2B/6pVVUKwsrJYOHoaMkgIa17WoaxXvSfp6WQxq3Q0llxW/Inp0cHEYpP8liMpzVfVsSUxWqORORRYS/Cv00xu5MZJUlLmc1NbKLMWXt5Ljrxcmp6QyXh0rouMHB75NXp6px8Cy/J0lGNOJ6Pf11huuhgKXruU1BmTTsfUOH21vkA555FkWrLRPSE7TE4rqm08BZJv+Du/PWGdikJ216ORposlR68oB7XRk50HJDU8Et753OpgTcF69yLf/17ML2CnCGr4q6HuHV/rHGLsVHfTMD3GMtNAhwYkWRNSWkWTvneEe9Y+jpD4szHOfghrDWI9RLSRfsaZEzNJzv5+0MnvFl/FGtentlZX3QsHGR/Phao8EujYID7YFuTVI3AQK8V/jcAQO1Dug4w1m4=; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY4Nzk4MTI0MCwiZXhwIjoxNjg3OTg4NDQwfQ.xNxly_slsC7uqGc_GT8msqajiVZBEEqzqZmNbUfhwds; _ga_PJSKY6CFJH=GS1.1.1687981232.38.1.1687981240.52.0.0; nseQuoteSymbols=[{"symbol":"RELIANCE","identifier":null,"type":"equity"}]; bm_sv=F33BA877E7BAB3EC0089C3C09C8002DC~YAAQy7YRYEK+EgKJAQAAxNWFAxQvkEEoIXUEOIHAGSm0rFBHX/2wAvyTaK7iSdDBK/NoCQwCNjQcq3WlN8PJuUBXve1PoazSFy4/eA8DDx/4jXd16BX2cnDhQlZFMtJQnvtLtptVpmK0YfIufttYl0XVFF4gZqNg7ntoMQho3n+4UA/jzxn9herrXN/XoBsuLVYTIIMAHzDw4glIfSCH+XMZ4N3ZWyjvLYZPeQuD2fvEgZ2gRlIHBlCZb5pDrPyPZeyX~1'
# The above cookie needs to be updated every 2-3 Hours
def get_data(ticker):
    global cookie
    if('&' in ticker):
        ticker = ticker.replace('&','%26')
    
    r=requests.get(url=f"https://www.nseindia.com/api/historical/cm/equity?symbol={ticker}&series=[%22EQ%22]&from=26-06-2022&to=26-06-2023&csv=true",headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                                                                        "Accept-Encoding":'gzip, deflate, br',
                                                                                        "Accept-Language":"en-US,en;q=0.9",
                                                                                        "Cache-Control":"max-age=0",
                                                                                        "Cookie":cookie,
                                                                                        "Dnt":"1",
                                                                                        "Sec-Ch-Ua":'"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                                                                                        "Sec-Ch-Ua-Mobile":"?0",
                                                                                        "Sec-Ch-Ua-Platform":"Windows",
                                                                                        "Sec-Fetch-Dest":"document",
                                                                                        "Sec-Fetch-Mode":"navigate",
                                                                                        "Sec-Fetch-Site":"none",
                                                                                        "Sec-Fetch-User":"?1",
                                                                                        "Upgrade-Insecure-Requests":"1",
                                                                                        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
                                                                                        })
    data = r
    open('sample.csv', 'wb').write(r.content)
    d1 = pd.read_csv("sample.csv")
    r=requests.get(url=f"https://www.nseindia.com/api/historical/cm/equity?symbol={ticker}&series=[%22EQ%22]&from=26-06-2021&to=26-06-2022&csv=true",headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                                                                        "Accept-Encoding":'gzip, deflate, br',
                                                                                        "Accept-Language":"en-US,en;q=0.9",
                                                                                        "Cache-Control":"max-age=0",
                                                                                        "Cookie":cookie,
                                                                                        "Dnt":"1",
                                                                                        "Sec-Ch-Ua":'"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                                                                                        "Sec-Ch-Ua-Mobile":"?0",
                                                                                        "Sec-Ch-Ua-Platform":"Windows",
                                                                                        "Sec-Fetch-Dest":"document",
                                                                                        "Sec-Fetch-Mode":"navigate",
                                                                                        "Sec-Fetch-Site":"none",
                                                                                        "Sec-Fetch-User":"?1",
                                                                                        "Upgrade-Insecure-Requests":"1",
                                                                                        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
                                                                                        })
    open('sample.csv', 'wb').write(r.content)
    d2 = pd.read_csv("sample.csv")

    r=requests.get(url=f"https://www.nseindia.com/api/historical/cm/equity?symbol={ticker}&series=[%22EQ%22]&from=26-06-2020&to=26-06-2021&csv=true",headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                                                                        "Accept-Encoding":'gzip, deflate, br',
                                                                                        "Accept-Language":"en-US,en;q=0.9",
                                                                                        "Cache-Control":"max-age=0",
                                                                                        "Cookie":cookie,
                                                                                        "Dnt":"1",
                                                                                        "Sec-Ch-Ua":'"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                                                                                        "Sec-Ch-Ua-Mobile":"?0",
                                                                                        "Sec-Ch-Ua-Platform":"Windows",
                                                                                        "Sec-Fetch-Dest":"document",
                                                                                        "Sec-Fetch-Mode":"navigate",
                                                                                        "Sec-Fetch-Site":"none",
                                                                                        "Sec-Fetch-User":"?1",
                                                                                        "Upgrade-Insecure-Requests":"1",
                                                                                        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
                                                                                        })
    open('sample.csv', 'wb').write(r.content)
    d3 = pd.read_csv("sample.csv")
    d = pd.concat([d1,d2,d3])
    d.reset_index(inplace=True)
    d=d.drop(['index'],axis=1)
    return d
