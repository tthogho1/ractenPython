import requests
import dotenv
import os
import sys
from component.lib import get_assistant


# .envの読み込み
dotenv.load_dotenv()

TRAVEL_SEARCH_URL = os.environ['TRAVEL_SEARCH_API']
API = os.environ['RAKUTEN_API']


def createTextFile(info):
    text = f"hotelName：{info["hotelName"]}\n"
    text += f"hotlInfo：{info["hotelSpecial"]}\n" 
    text += f"useReview：{info["userReview"]}\n"
    text += f"access：{info['access']}\n"
    text += f"address：{info['address1']}{info['address2']}\n" 
    
    return text


def travelSearch(largeClassCode, middleClassCode, smallClassCode):
    URL = f"{TRAVEL_SEARCH_URL}?applicationId={API}&format=json&largeClassCode={largeClassCode}"
    URL += f"&middleClassCode={middleClassCode}&smallClassCode={smallClassCode}"
    
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        hotelinfomations = data["hotels"]
        for hotel in hotelinfomations:
            info = hotel["hotel"][0]["hotelBasicInfo"]
            text = createTextFile(info)

            with open(f"{info['hotelNo']}.txt", "w", encoding="utf-8") as f:
                f.write(text)
            
            # try:
            #     # upload file to pinecone assistant
            #     assistant = get_assistant()
            #     response = assistant.upload_file(
            #         file_path=f"{info['hotelNo']}.txt",
            #         timeout=None,
            #     )
                
            #     if response.status_code == 200:
            #         print(response.json())
            #         # delete file
            #         os.remove(f"{info['hotelNo']}.txt")
            #     else:
            #         print(response.status_code)
            # except Exception as e:
            #     print(f"error occureds: {e}", file=sys.stderr)
    else:
        print(response.status_code)    
