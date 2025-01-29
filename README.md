**socialagent** is a Python module designed for generating user agents specific to social media platforms under Meta (formerly Facebook). It provides functionalities to create user agents for various platforms such as Dalvik, Chrome, Threads, Facebook, and Instagram. This module helps in mimicking different device configurations and language settings commonly used across these platforms.

## installation
install using pip
```bash
pip install socialagent
```
## socialagent
importing
```python
import socialagent
```
## device
generate device for user agent
```python
# random
device = socialagent.device()

# custom (parameters)
default = True # default: False -> random
brand = 'INFINIX' # default: None -> random
country = 'ID' # default: None -> random

device = socialagent.device(default=default, brand=brand, country=country)
print(device)
```
output (type: dict/dictionary)
```bash
{'device': {'brand': 'INFINIX', 'build': 'SP1A.201789.008', 'board': 'Infinix-X6515', 'model': 'Infinix X6515', 'vendor': 'mt6761', 'version': '12', 'sdk': '31', 'sim': 'XL', 'dpi': '480dpi; 1344x2772', 'number': '62', 'country': 'ID', 'armeabi': 'armeabi-v7a:armeabi', 'density': '{density=2.0,width=720,height=1193}', 'language': 'id_ID'}}
```
## dalvik
generate dalvik user agent
```python
# random
dalvik = socialagent.dalvik()

# custom
default = True # default: False -> random
device_brand = 'Xiaomi' # default None -> random
device_build = 'RKQ1.210790.008' # default None -> random
device_model = 'Redmi 6' # default None -> random
device_version = '9' # default None -> random

dalvik = socialagent.dalvik(default=default, device_brand=device_brand, device_build=device_build, device_model=device_model, device_version=device_version)
print(dalvik)
```
output (type: str/string)
```bash
'Dalvik/2.1.0 (Linux; U; Android 9; Redmi 6 Build/RKQ1.210790.008)'
```
## chrome
generate chrome user agent
```python
# random
chrome = socialagent.chrome()

# custom
default = True # default: False -> random
webview = True # default: False
device_brand = 'Xiaomi' # default None -> random
device_build = 'SKQ1.211019.001' # default None -> random
device_model = 'Redmi Note 9 Pro' # default None -> random
device_version = '12' # default None -> random
chrome_version = '111.0.2679.062' # default: None -> random

chrome = socialagent.chrome(default=default, webview=webview, device_brand=device_brand, device_build=device_build, device_model=device_model, device_version=device_version)
print(chrome)
```
output (type: str/string)
```bash
'Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2679.062 Mobile Safari/537.36'
```
## threads
generate threads user agent
```python
# random
threads = socialagent.threads()

# custom
default = True  # default: False -> random
device_sdk = '33'  # default None -> random
device_dpi = '480dpi; 1080x2400'  # default None -> random
device_brand = 'Samsung'  # default None -> random
device_board = 'exynos'  # default None -> random
device_model = 'Galaxy S21'  # default None -> random
device_vendor = 'Exynos'  # default None -> random
device_version = '13'  # default None -> random
device_language = 'en_US'  # default None -> random
threads_code = '667551319'  # default None -> random
threads_version = '359.0.0.61.109'  # default None -> random

threads = socialagent.threads(default=default, device_sdk=device_sdk, device_dpi=device_dpi, device_brand=device_brand, device_board=device_board, device_model=device_model, device_vendor=device_vendor, device_version=device_version, device_language=device_language, threads_code=threads_code, threads_version=threads_version)
print(threads)
```
output (type: str/string)
```bash
'Barcelona 359.0.0.61.109 Android (33/13; 480dpi; 1080x2400; Samsung; Galaxy S21; exynos; Exynos; en_US; 667551319)'
```
## facebook
generate facebook user agent
```python
# random
facebook = socialagent.facebook()

# custom
default = True  # default: False -> random
dalvik = True  # default: False
device_sdk = '33'  # default None -> random
device_sim = 'Telkomsel'  # default None -> random
device_dpi = '480dpi; 1080x2400'  # default None -> random
device_brand = 'Samsung'  # default None -> random
device_board = 'exynos'  # default None -> random
device_model = 'Galaxy S21'  # default None -> random
device_vendor = 'Exynos'  # default None -> random
device_version = '13'  # default None -> random
device_armeabi = 'arm64-v8a'  # default None -> random
device_density = '{density=3.0,width=1080,height=1920}'  # default None -> random
device_language = 'en_US'  # default None -> random
facebook_code = '543547945'  # default None -> random
facebook_version = '443.0.0.23.229'  # default None -> random
facebook_package = 'com.facebook.katana'  # default None -> default package

facebook = socialagent.facebook(default=default, dalvik=dalvik, device_sdk=device_sdk, device_sim=device_sim, device_dpi=device_dpi, device_brand=device_brand, device_board=device_board, device_model=device_model, device_vendor=device_vendor, device_version=device_version, device_armeabi=device_armeabi, device_density=device_density, device_language=device_language, facebook_code=facebook_code, facebook_version=facebook_version, facebook_package=facebook_package)
print(facebook)
```
output for ```dalvik = True``` (type: str/string)
```bash
'Dalvik/2.1.0 (Linux; U; Android 13; Galaxy S21 Build/SKQ1.211019.001) [FBAN/FB4A;FBAV/443.0.0.23.229;FBBV/543547945;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/Telkomsel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Galaxy S21;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]'
```
output for ```dalvik = False``` (type: str/string)
```bash
'[FBAN/FB4A;FBAV/443.0.0.23.229;FBBV/543547945;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/Telkomsel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Galaxy S21;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]'
```
## instagram
generate instagram user agent
```python
# random
instagram = socialagent.instagram()

# custom
default = True  # default: False -> random
device_sdk = '33'  # default None -> random
device_dpi = '480dpi; 1080x2400'  # default None -> random
device_brand = 'Samsung'  # default None -> random
device_board = 'exynos'  # default None -> random
device_model = 'Galaxy S21'  # default None -> random
device_vendor = 'Exynos'  # default None -> random
device_version = '13'  # default None -> random
device_language = 'en_US'  # default None -> random
instagram_code = '554218546'  # default None -> random
instagram_version = '313.0.0.26.328'  # default None -> random

instagram = socialagent.instagram(default=default, device_sdk=device_sdk, device_dpi=device_dpi, device_brand=device_brand, device_board=device_board, device_model=device_model, device_vendor=device_vendor, device_version=device_version, device_language=device_language, instagram_code=instagram_code, instagram_version=instagram_version)
print(instagram)
```
output (type: str/string)
```bash
'Instagram 313.0.0.26.328 Android (33/13; 480dpi; 1080x2400; Samsung; Galaxy S21; exynos; Exynos; en_US; 554218546)'
```
