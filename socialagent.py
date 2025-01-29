#/usr/bin/env python3
import os
import random

DEVICE = {'OPPO': [{'model': 'CPH1923','board': 'OP486C','vendor': 'mt6765','version': '9'},{'model': 'CPH2185','board': 'OP4F2F','vendor': 'mt6765','version': '10'},{'model': 'CPH2109','board': 'OP4BA5L1','vendor': 'qcom','version': '11'},{'model': 'CPH2135','board': 'OP4EFDL1','vendor': 'qcom','version': '12'},{'model': 'CPH2481','board': 'OP5709L1','vendor': 'mt6789','version': '13'}],'VIVO': [{'model': 'vivo 1910','board': '1910','vendor': 'qcom','version': '9'},{'model': 'vivo 1907','board': '1907','vendor': 'mt6768','version': '12'},{'model': 'vivo 1909','board': '1909','vendor': 'qcom','version': '11'},{'model': 'V2043_21','board': '2026','vendor': 'mt6765','version': '11'},{'model': 'vivo 1938','board': '1938','vendor': 'mt6765','version': '12'}],'REALME': [{'model': 'RMX3363','board': 'RE54ABL1','vendor': 'qcom','version': '12'},{'model': 'RMX3624','board': 'RE5894','vendor': 'qcom','version': '12'},{'model': 'RMX3201','board': 'RMX3201','vendor': 'mt6765','version': '11'},{'model': 'RMX3269','board': 'RED8F6','vendor': 'qcom','version': '11'},{'model': 'RMX2020','board': 'RMX2020','vendor': 'mt6768','version': '10'}],'XIAOMI': [{'model': 'Redmi 7','board': 'onc','vendor': 'qcom','version': '9'},{'model': 'Redmi 6','board': 'cereus','vendor': 'mt6765','version': '9'},{'model': 'Redmi Note 7 Pro','board': 'violet','vendor': 'qcom','version': '10'},{'model': 'Redmi Note 8 Pro','board': 'begonia','vendor': 'mt6785','version': '10'},{'model': 'Redmi Note 8','board': 'ginkgo','vendor': 'qcom','version': '11'}],'HUAWEI': [{'model': 'JLN-LX1','board': 'HWJLN-Q','vendor': 'qcom','version': '11'},{'model': 'LIO-L29','board': 'HWLIO','vendor': 'kirin990','version': '10'},{'model': 'HRY-LX1T','board': 'HWHRY-HF','vendor': 'kirin710','version': '10'},{'model': 'ELE-L29','board': 'HWELE','vendor': 'kirin980','version': '10'},{'model': 'MRD-LX1F','board': 'HWMRD-M1','vendor': 'mt6761','version': '10'}],'INFINIX': [{'model': 'Infinix X657B','board': 'Infinix-X657B','vendor': 'mt6761','version': '11'},{'model': 'Infinix X688B','board': 'Infinix-X688B','vendor': 'mt6765','version': '11'},{'model': 'Infinix X682B','board': 'Infinix-X682B','vendor': 'mt6769','version': '10'},{'model': 'Infinix X6515','board': 'Infinix-X6515','vendor': 'mt6761','version': '12'},{'model': 'Infinix X676B','board': 'Infinix-X676B','vendor': 'mt6789','version': '12'}],'SAMSUNG': [{'model': 'SM-A125F','board': 'a12','vendor': 'mt6765','version': '12'},{'model': 'SM-A127F','board': 'a12s','vendor': 'exynos850','version': '13'},{'model': 'SM-A225M','board': 'a22','vendor': 'mt6769t','version': '13'},{'model': 'SM-A127F','board': 'a12s','vendor': 'exynos850','version': '13'},{'model': 'SM-A135F','board': 'a13','vendor': 'exynos850','version': '13'}]}
COUNTRY = {'ID':{'number':'62','language':'id_ID'},'US':{'number':'1','language':'en_US'},'CN':{'number':'86','language':'zh_CN'},'IN':{'number':'91','language':'hi_IN'},'JP':{'number':'81','language':'ja_JP'},'BR':{'number':'55','language':'pt_BR'},'RU':{'number':'7','language':'ru_RU'},'DE':{'number':'49','language':'de_DE'},'NG':{'number':'234','language':'en_NG'},'MX':{'number':'52','language':'es_MX'},'AU':{'number':'61','language':'en_AU'},'CA':{'number':'1','language':'en_CA'},'GB':{'number':'44','language':'en_GB'},'FR':{'number':'33','language':'fr_FR'},'IT':{'number':'39','language':'it_IT'},'ES':{'number':'34','language':'es_ES'},'KR':{'number':'82','language':'ko_KR'},'SA':{'number':'966','language':'ar_SA'},'TR':{'number':'90','language':'tr_TR'},'AR':{'number':'54','language':'es_AR'},'PH':{'number':'63','language':'fil_PH'},'TH':{'number':'66','language':'th_TH'},'BD':{'number':'880','language':'bn_BD'},'MY':{'number':'60','language':'ms_MY'},'VN':{'number':'84','language':'vi_VN'}}
THREADS = [{'version': '346.0.0.40.110','code': '636112770'},{'version': '357.0.0.50.109','code': '662318283'},{'version': '359.0.0.61.109','code': '667551319'},{'version': '348.1.0.44.109','code': '640443180'},{'version': '295.1.0.18.61','code': '501823394'},{'version': '303.0.0.22.112','code': '521858775'},{'version': '333.0.0.41.109','code': '603983131'},{'version': '289.0.0.22.50','code': '489338310'},{'version': '289.0.0.77.109','code': '489720161'}]
FACEBOOK = [{'version': '443.0.0.23.229','code': '543547945'},{'version': '365.0.0.30.112','code': '367653576'},{'version': '305.1.0.40.120','code': '272401209'},{'version': '269.0.0.50.127','code': '212783074'},{'version': '268.1.0.54.121','code': '211681886'},{'version': '280.0.0.48.122','code': '233235247'},{'version': '263.0.0.46.121','code': '205281674'},{'version': '271.0.0.55.109','code': '215365668'},{'version': '263.0.0.46.121','code': '205281663'}]
INSTAGRAM = [{'version': '313.0.0.26.328','code': '554218546'},{'version': '309.0.0.40.113','code': '536988425'},{'version': '303.0.0.40.109','code': '522819744'},{'version': '303.0.0.40.109','code': '522819738'},{'version': '309.1.1.28.108','code': '537288535'},{'version': '311.0.2.23.115','code': '545017126'},{'version': '312.0.1.19.124','code': '548339486'},{'version': '305.0.0.34.110','code': '527673577'},{'version': '314.0.0.20.114','code': '556277179'},{'version': '313.0.0.26.328','code': '554218055'},{'version': '313.0.0.26.328','code': '554218466'},{'version': '280.0.0.48.122','code': '233235247'},{'version': '350.0.0.0.35','code': '642371207'},{'version': '207.0.0.39.120','code': '321039156'}]

class SocialAgent:

    DEVICE_LIST = [line for line in list(DEVICE.keys())]
    COUNTRY_LIST = [line for line in list(COUNTRY.keys())]
    
    def device(self, default: bool = False, brand: str = None, country: str = None):
        if default and os.path.isdir('/data/data/com.termux/'):
            brand = os.popen('getprop ro.product.manufacturer','r').read().strip()
            build = os.popen('getprop ro.product.build.id','r').read().strip()
            board = os.popen('getprop ro.product.board','r').read().strip()
            model = os.popen('getprop ro.product.model','r').read().strip()
            vendor = os.popen('getprop ro.hardware','r').read().strip()
            version = os.popen('getprop ro.product.build.version.release','r').read().strip()
            sdk = os.popen('getprop ro.product.build.version.sdk','r').read().strip()
            sim = os.popen('getprop gsm.sim.operator.alpha','r').read().strip()
            armeabi = os.popen('getprop ro.product.cpu.abi','r').read().strip()
            country = os.popen('getprop ro.product.locale.region','r').read().strip()
        else:
            brand = brand if brand in self.DEVICE_LIST else random.choice(self.DEVICE_LIST)
            device = random.choice(DEVICE[brand.upper()])
            build = '{}.{}'.format(random.choice(['SP1A','QP1A','RP1A','TP1A','RKQ1','SKQ1']), str(random.randint(200999,220905)) + '.0{}'.format(random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16'])))
            board = device['board']
            model = device['model']
            vendor = device['vendor']
            version = device['version']
            sdk = str(19 + int(version))
            sim = random.choice(['AIS','AIRTEL','ZONG','TELKOMSEL','ISAT-PEMILUDAMAI','LIFECELL','XL','4KA-SK','VELCOM','ARIA','CLARO','CELLONE','CHN-UNICOM'])
            armeabi = random.choice(['arm64-v8a','armeabi-v8a:armeabi','armeabi-v7a:armeabi','x86_64:x86:x86_64','x86_64:arm64-v8a:x86_64'])
            country = country if country in self.COUNTRY_LIST else random.choice(self.COUNTRY_LIST)
        return {
            'device': {
                'brand': brand,
                'build': build,
                'board': board,
                'model': model,
                'vendor': vendor,
                'version': version,
                'sdk': sdk,
                'sim': sim,
                'dpi': random.choice(['480dpi; 1080x2400','480dpi; 720x1600','480dpi; 720x1560','480dpi; 1080x2376','480dpi; 1080x2404','480dpi; 1080x2408','320dpi; 1080x2340','560dpi; 1440x3040','560dpi; 1440x3088','560dpi; 1080x2400','320dpi; 1600x2560','320dpi; 720x1568','560dpi; 1440x2560','480dpi; 1344x2772']),
                'number': COUNTRY[country.upper()]['number'],
                'country': country,
                'armeabi': armeabi,
                'density': random.choice(['{density=3.0,width=1080,height=2068}','{density=3.0,width=1080,height=1920}','{density=2.3,width=2149,height=1117}','{density=1.0,width=2060,height=1078}','{density=1.8,width=1582,height=558}','{density=3.0,width=1080,height=1920}','{density=2.0,width=720,height=1193}','{density=2.1,width=1814,height=1023}']),
                'language': COUNTRY[country.upper()]['language']}}
    
    def dalvik(self, default: bool = False, device_brand: str = None, device_build: str = None, device_model: str = None, device_version: str = None):
        device_brand = device_brand if device_brand in self.DEVICE_LIST else random.choice(self.DEVICE_LIST)
        device = self.device(default=default, brand=device_brand)['device']
        return f'Dalvik/2.1.0 (Linux; U; Android {device_version or device["version"]}; {device_model or device["model"]} Build/{device_build or device["build"]})'
    
    def chrome(self, default: bool = False, webview: bool = False, device_brand: str = None, device_build: str = None, device_model: str = None, device_version: str = None, chrome_version: str = None):
        chrome_version = chrome_version or str(random.randint(80,112)) + '.0.' + str(random.randint(2024,3058)) + '.0' + str(random.randint(10,99))
        device_brand = device_brand if device_brand in self.DEVICE_LIST else random.choice(self.DEVICE_LIST)
        device = self.device(default=default, brand=device_brand)['device']
        return f'Mozilla/5.0 (Linux; Android {device_version or device["version"]}; {device_model or device["model"]} Build/{device_build or device["build"]}{"; wv" if webview else ""}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'
    
    def threads(self, default: bool = False, device_sdk: str = None, device_dpi: str = None, device_brand: str = None, device_board: str = None, device_model: str = None, device_vendor: str = None, device_version: str = None, device_language: str = None, threads_code: str = None, threads_version: str = None):
        device_brand = device_brand if device_brand in self.DEVICE_LIST else random.choice(self.DEVICE_LIST)
        device = self.device(default=default, brand=device_brand)['device']
        threads = random.choice(THREADS)
        return f'Barcelona {threads_version or threads["version"]} Android ({device_sdk or device["sdk"]}/{device_version or device["version"]}; {device_dpi or device["dpi"]}; {device_brand or device["brand"]}; {device_model or device["model"]}; {device_board or device["board"]}; {device_vendor or device["vendor"]}; {device_language or device["language"]}; {threads_code or threads["code"]})'
    
    def facebook(self, default: bool = False, dalvik: bool = False, device_sdk: str = None, device_sim: str = None, device_dpi: str = None, device_brand: str = None, device_board: str = None, device_model: str = None, device_vendor: str = None, device_version: str = None, device_armeabi: str = None, device_density: str = None, device_language: str = None, facebook_code: str = None, facebook_version: str = None, facebook_package: str = None):
        device_brand = device_brand if device_brand in self.DEVICE_LIST else random.choice(self.DEVICE_LIST)
        device = self.device(default=default, brand=device_brand)['device']
        facebook = random.choice(FACEBOOK)
        agent = f'[FBAN/FB4A;FBAV/{facebook_version or facebook["version"]};FBBV/{facebook_code or facebook["code"]};FBDM/{device_density or device["density"]};FBLC/{device_language or device["language"]};FBRV/0;FBCR/{device_sim or device["sim"]};FBMF/{device_brand or device["brand"]};FBBD/{device_brand or device["brand"]};FBPN/{facebook_package or "com.facebook.katana"};FBDV/{device_model or device["model"]};FBSV/{device_version or device["version"]};FBOP/1;FBCA/{device_armeabi or device["armeabi"]}:;]'
        return self.dalvik(device_brand=device_brand, device_build=device['build'], device_model=device['model'], device_version=device['version']) + ' ' + agent if dalvik else agent
    
    def instagram(self, default: bool = False, device_sdk: str = None, device_dpi: str = None, device_brand: str = None, device_board: str = None, device_model: str = None, device_vendor: str = None, device_version: str = None, device_language: str = None, instagram_code: str = None, instagram_version: str = None):
        device_brand = device_brand if device_brand in self.DEVICE_LIST else random.choice(self.DEVICE_LIST)
        device = self.device(default=default, brand=device_brand)['device']
        instagram = random.choice(INSTAGRAM)
        return f'Instagram {instagram_version or instagram["version"]} Android ({device_sdk or device["sdk"]}/{device_version or device["version"]}; {device_dpi or device["dpi"]}; {device_brand or device["brand"]}; {device_model or device["model"]}; {device_board or device["board"]}; {device_vendor or device["vendor"]}; {device_language or device["language"]}; {instagram_code or instagram["code"]})'

socialagent = SocialAgent()
device = socialagent.device
dalvik = socialagent.dalvik
chrome = socialagent.chrome
threads = socialagent.threads
facebook = socialagent.facebook
instagram = socialagent.instagram