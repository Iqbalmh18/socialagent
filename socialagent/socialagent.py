#!/usr/bin/env python3
import random

COUNTRY = {'ID':'in_ID','US':'en_US','CN':'zh_CN','IN':'hi_IN','JP':'ja_JP','BR':'pt_BR','RU':'ru_RU','DE':'de_DE','NG':'en_NG','MX':'es_MX','AU':'en_AU','CA':'en_CA','GB':'en_GB','FR':'fr_FR','IT':'it_IT','ES':'es_ES','KR':'ko_KR','SA':'ar_SA','TR':'tr_TR','AR':'es_AR','PH':'fil_PH','TH':'th_TH','BD':'bn_BD','MY':'ms_MY','VN':'vi_VN'}
COUNTRY_CODE = list(COUNTRY.keys())
COUNTRY_LANG = list(COUNTRY.values())

THREADS = ['303.0.0.22.112|521858775','295.1.0.18.61|501823394','333.0.0.41.109|603983131','289.0.0.22.50|489338310']
FACEBOOK = ['345.0.0.34.118|332957647|334763932','365.0.0.30.112|367653576|369757394','305.1.0.40.120|272401209|273474118','233.0.0.16.158|172917909|175918965','196.0.0.29.99|135374479|138376409','280.0.0.48.122|233235247|235412020']
INSTAGRAM = ['163.0.0.45.122|250742113','247.0.0.17.113|388829083','218.0.0.19.108|345526700','172.0.0.21.123|269790803','146.0.0.27.125|221134032','207.0.0.39.120|321039149','309.1.0.41.113|541635892','305.0.0.34.110|527673577','314.0.0.20.114|556277179','313.0.0.26.328|554218055','313.0.0.26.328|554218466','189.0.0.41.121|293853435','215.0.0.27.359|337202351','145.0.0.32.119|219308759','193.0.0.45.120|300078998']

class socialagent:
    
    def __init__(self):
        self.device = {'oppo':['CPH1909','CPH1911','CPH1969','CPH2119','CPH2285','CPH2185','CPH2271','PGIM10','CPH2305','CPH1877'],'vivo':['V1838A','V1824A','V2218A','V2163A','V2207A','V2208A','V2254A','V2001A','I2126','V2241HA'],'realme':['CPH1861','RMX1945','RMX3630','RMX3617','RMX3663','RMX3661','RMX3771','RMX2202','RMX2161','RMX3235'],'huawei':['OCE-AN10','NOH-NX9','NOH-AN00','CET-AL00','DCO-AL00','ALN-AL00','ALN-AL10','CTR-AL00','MAO-AL00','CTR-AL20'],'google':['GT-P8110','G025J','GA02099','G020P','G025I','G9S9B16','GLUOG','GC3VE','G1MNW','G9FPL'],'infinix':['X688B','X688C','X689B','X689D','X668C','X6823C','X6525B','X663C','X6528B','X656'],'samsung':['SM-M536B','SM-M625F','SM-A025G','SM-A105G','SM-A245M','SM-G973F','SM-A7160','SM-A9100','SM-M107F','SM-M326B']}
        self.device_dpi = ['480dpi; 1080x2400','480dpi; 720x1600','480dpi; 720x1560','480dpi; 1080x2376','480dpi; 1080x2404','480dpi; 1080x2408','320dpi; 1080x2340','560dpi; 1440x3040','560dpi; 1440x3088','560dpi; 1080x2400','320dpi; 1600x2560','320dpi; 720x1568','560dpi; 1440x2560','480dpi; 1344x2772']
        self.device_build = ['SP1A','QP1A','RP1A','TP1A','RKQ1','SKQ1']
        self.device_vendor = ['qcom','mt6769','mt6893','mt6769','mt6765','mt6771','mt6893','mt6762','exynos5','exynos7904']
        self.device_armeabi = ['arm64-v8a','armeabi-v8a','armeabi-v7a:armeabi','arm64-v8a:armeabi-v7a:armeabi','x86_64:x86:x86_64','x86_64:arm64-v8a:x86_64']
        self.device_density = ['{density=3.0,width=1080,height=2068}','{density=3.0,width=1080,height=1920}','{density=2.3,width=2149,height=1117}','{density=1.0,width=2060,height=1078}','{density=1.8,width=1582,height=558}','{density=3.0,width=1080,height=1920}','{density=2.0,width=720,height=1193}','{density=2.1,width=1814,height=1023}']
        self.device_version = ['9','10','11','12','13']
        self.device_operator = ['AIS','AIRTEL','ZONG','TELKOMSEL','INDOSAT','AXIS','XL','3','VELCOM','ARIA','BYU','CELLONE','METFONE']
    
    def dalvik(self, device_model=None, device_version=None):
        device = random.choice(list(self.device.keys()))
        device_build = f'{random.choice(self.device_build)}.{str(random.randint(200999,220905))}.0{random.choice(["01","02","03","04","05","06","07","08","09","10","11","12"])}'
        device_model = device_model or random.choice(self.device[device])
        device_version = device_version or random.choice(self.device_version)
        return f'Dalvik/2.1.0 (Linux; U; Android {device_version}; {device_model} Build/{device_build})'
    
    def chrome(self, webview=False, device_model=None, device_version=None, chrome_version=None):
        device = random.choice(list(self.device.keys()))
        device_build = f'{random.choice(self.device_build)}.{str(random.randint(200999,220905))}.0{random.choice(["01","02","03","04","05","06","07","08","09","10","11","12"])}'
        device_model = device_model or random.choice(self.device[device])
        device_version = device_version or random.choice(self.device_version)
        chrome_version = chrome_version or f'{str(random.randint(80,112))}.0.{str(random.randint(2024,3058))}.0{str(random.randint(10,99))}'
        if webview: return f'Mozilla/5.0 (Linux; Android {device_version}; {device_model} Build/{device_build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'
        else: return f'Mozilla/5.0 (Linux; Android {device_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'
    
    def threads(self, device=None, device_dpi=None, device_model=None, device_vendor=None, device_version=None, device_language=None, threads_code=None, threads_version=None):
        device = device if device in list(self.device.keys()) else random.choice(list(self.device.keys()))
        device_dpi = device_dpi or random.choice(self.device_dpi)
        device_build = f'{random.choice(self.device_build)}.{str(random.randint(200999,220905))}.0{random.choice(["01","02","03","04","05","06","07","08","09","10","11","12"])}'
        device_model = device_model or random.choice(self.device[device])
        device_vendor = device_vendor or random.choice(self.device_vendor)
        device_version = device_version or random.choice(self.device_version)
        device_language = device_language or random.choice(COUNTRY_LANG)
        device_sdkversion = str(19 + int(device_version))
        threads = random.choice(THREADS).split('|')
        threads_code = threads_code or threads[1]
        threads_version = threads_version or threads[0]
        return f'Barcelona {threads_version} Android ({str(device_sdkversion)}/{device_version}; {device_dpi}; {device.capitalize()}; {device_model}; {device_model}; {device_vendor}; {device_language}; {threads_code})'

    def facebook(self, dalvik=False, device=None, device_model=None, device_armeabi=None, device_density=None, device_version=None, device_language=None, device_operator=None, facebook_code=None, facebook_build=None, facebook_version=None, facebook_package=None):
        device = device if device in list(self.device.keys()) else random.choice(list(self.device.keys()))
        device_model = device_model or random.choice(self.device[device])
        device_version = device_version or random.choice(self.device_version)
        device_armeabi = device_armeabi or random.choice(self.device_armeabi)
        device_density = device_density or random.choice(self.device_density)
        device_language = device_language or random.choice(COUNTRY_LANG)
        device_operator = device_operator or random.choice(self.device_operator)
        facebook = random.choice(FACEBOOK).split('|')
        facebook_code = facebook_code or facebook[1]
        facebook_build = facebook_build or facebook[2]
        facebook_version = facebook_version or facebook[0]
        facebook_package = facebook_package or random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.lite','com.facebook.mlite'])
        facebook_useragent = f'[FBAN/FB4A;FBAV/{facebook_version};FBBV/{facebook_code};FBDM/{device_density};FBLC/{device_language};FBRV/{facebook_build};FBCR/{device_operator};FBMF/{device.lower()};FBBD/{device.lower()};FBPN/{facebook_package};FBDV/{device_model};FBSV/{device_version};FBOP/1;FBCA/{device_armeabi}:;]'
        if dalvik: return self.dalvik(device_model, device_version) + ' ' + facebook_useragent
        else: return facebook_useragent
    
    def instagram(self, device=None, device_dpi=None, device_model=None, device_vendor=None, device_version=None, device_language=None, instagram_code=None, instagram_version=None):
        device = device if device in list(self.device.keys()) else random.choice(list(self.device.keys()))
        device_dpi = device_dpi or random.choice(self.device_dpi)
        device_build = f'{random.choice(self.device_build)}.{str(random.randint(200999,220905))}.0{random.choice(["01","02","03","04","05","06","07","08","09","10","11","12"])}'
        device_model = device_model or random.choice(self.device[device])
        device_vendor = device_vendor or random.choice(self.device_vendor)
        device_version = device_version or random.choice(self.device_version)
        device_language = device_language or random.choice(COUNTRY_LANG)
        device_sdkversion = str(19 + int(device_version))
        instagram = random.choice(INSTAGRAM).split('|')
        instagram_code = instagram_code or instagram[1]
        instagram_version = instagram_version or instagram[0]
        return f'Instagram {instagram_version} Android ({str(device_sdkversion)}/{device_version}; {device_dpi}; {device.capitalize()}; {device_model}; {device_model}; {device_vendor}; {device_language}; {instagram_code})'
