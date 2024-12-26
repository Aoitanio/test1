import os
import requests

# 画像のURL
image_url = "https://drive.google.com/uc?id=1zhQu9PbAPhGRAmTdOvy1uOwXEdDHiuOP"

# 保存先ディレクトリとファイル名
save_directory = "public"
file_name = "dr-logo.png"
save_path = os.path.join(save_directory, file_name)

# ディレクトリが存在しない場合は作成
os.makedirs(save_directory, exist_ok=True)

# 画像をダウンロードして保存
response = requests.get(image_url)
if response.status_code == 200:
    with open(save_path, "wb") as file:
        file.write(response.content)
    print(f"画像を {save_path} に保存しました。")
else:
    print(f"画像のダウンロードに失敗しました。ステータスコード: {response.status_code}")
