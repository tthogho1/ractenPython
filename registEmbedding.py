import requests
import dotenv
import os
from  component.upload import travelSearch
import time

# .envの読み込み
dotenv.load_dotenv()

GET_ARAEA_URL = os.environ['GET_AREA_CLASS']
API = os.environ['RAKUTEN_API']

URL = f"{GET_ARAEA_URL}?applicationId={API}&format=json"   
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    l_classes = data["areaClasses"]["largeClasses"]
    for l_class in l_classes:
        l_class = l_class["largeClass"]
        m_classes = l_class[1]["middleClasses"]
        
        for m_class in m_classes:
            m_class = m_class["middleClass"]
            s_classes = m_class[1]["smallClasses"]
            
            for s_class in s_classes:
                s_class = s_class["smallClass"]
                #
                # wait 2 second
                time.sleep(2)
                travelSearch(l_class[0]["largeClassCode"]
                            ,m_class[0]["middleClassCode"]
                            ,s_class[0]["smallClassCode"])
                                
                if len(s_class) < 2 or s_class[1] is None:
                    continue

    # print(data["areaClasses"]["largeClasses"])
    print("リクエスト成功")
else:
    print(f"リクエスト失敗: {response.status_code}")