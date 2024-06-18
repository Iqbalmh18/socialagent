**socialagent** is a Python module designed for generating user agents specific to social media platforms under Meta (formerly Facebook). It provides functionalities to create user agents for various platforms such as Dalvik, Chrome, Threads, Facebook, and Instagram. This module helps in mimicking different device configurations and language settings commonly used across these platforms.

## installation
install using pip
```bash
pip install socialagent
```
## example usage
importing socialagent
```python
from socialagent import socialagent
```
## dalvik user agent
generate dalvik user agent
```python
from socialagent import socialagent

ua = socialagent()

# generate dalvik user agent
dalvik_user_agent = ua.dalvik()
print(dalvik_user_agent)

# generate dalvik user agent with custom parameters
device_model = 'SM-A105G' # default None -> random
device_version = '9' # default None -> random

dalvik_user_agent = ua.dalvik(device_model=device_model,
                              device_version=device_version)
print(dalvik_user_agent)
```
## chrome user agent
generate chrome user agent
```python
from socialagent import socialagent

ua = socialagent()

# generate chrome user agent
chrome_user_agent = ua.chrome()
print(chrome_user_agent)

# generate chrome user agent with custom parameters
webview = True # default False
device_model = 'SM-A105G' # default None -> random
device_version = '9' # default None -> random
chrome_version = '83.0.4103.101' # default None -> random

chrome_user_agent = ua.chrome(webview=webview, device_model=device_model,
                              device_version=device_version, chrome_version=chrome_version)
print(chrome_user_agent)
```
## threads user agent
generate threads user agent
```python
from socialagent import socialagent

ua = socialagent()

# generate threads user agent
threads_user_agent = ua.threads()
print(threads_user_agent)

# generate threads user agent with custom parameters
device = 'samsung' # default None -> random
device_model = 'SM-A105G' # default None -> random
device_dpi = '480dpi; 1080x2400' # default None -> random
device_vendor = 'qcom' # default None -> random
device_version = '9' # default None -> random
device_language = 'en_US' # default None -> random
threads_code = '521858775' # default None -> random
threads_version = '303.0.0.22.112' # default None -> random

threads_user_agent = ua.threads(device=device, device_model=device_model, device_dpi=device_dpi, 
                                device_vendor=device_vendor, device_version=device_version, 
                                device_language=device_language, threads_code=threads_code, 
                                threads_version=threads_version)
print(threads_user_agent)
```
## facebook user agent
generate facebook user agent
```python
from socialagent import socialagent

ua = socialagent()

# generate facebook user agent
facebook_user_agent = ua.facebook()
print(facebook_user_agent)

# generate facebook user agent with custom parameters
dalvik = True # default False
device = 'samsung' # default None -> random
device_model = 'SM-A105G' # default None -> random
device_version = '9' # default None -> random
device_armeabi = 'armeabi-v7a' # default None -> random
device_density = '{density=3.0,width=1080,height=2068}' # default None -> random
device_language = 'en_US' # default None -> random
device_operator = 'AIRTEL' # default None -> random
facebook_code = '521858775' # default None -> random
facebook_build = '332957647' # default None -> random
facebook_version = '345.0.0.34.118' # default None -> random
facebook_package = 'com.facebook.katana' # default None -> random

facebook_user_agent = ua.facebook(dalvik=dalvik, device=device, device_model=device_model, device_version=device_version, 
                                  device_armeabi=device_armeabi, device_density=device_density, 
                                  device_language=device_language, device_operator=device_operator, 
                                  facebook_code=facebook_code, facebook_build=facebook_build, 
                                  facebook_version=facebook_version, facebook_package=facebook_package)
print(facebook_user_agent)
```
## instagram user agent
generate instagram user agent
```python
from socialagent import socialagent

ua = socialagent()

# generate instagram user agent
instagram_user_agent = ua.instagram()
print(instagram_user_agent)

# generate instagram user agent with custom parameters
device = 'samsung' # default None -> random
device_model = 'SM-A105G' # default None -> random
device_dpi = '480dpi; 1080x2400' # default None -> random
device_vendor = 'qcom' # default None -> random
device_version = '9' # default None -> random
device_language = 'en_US' # default None -> random
instagram_code = '521858775' # default None -> random
instagram_version = '303.0.0.22.112' # default None -> random

instagram_user_agent = ua.instagram(device=device, device_model=device_model, device_dpi=device_dpi, 
                                    device_vendor=device_vendor, device_version=device_version, 
                                    device_language=device_language, instagram_code=instagram_code, 
                                    instagram_version=instagram_version)
print(instagram_user_agent)
```
