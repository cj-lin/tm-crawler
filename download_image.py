import pandas
import requests

for _, row in (
    pandas.read_csv("officers.csv")
    .query('img != "http://seo.docs.com.tw/blue/images/photo.jpg"')
    .iterrows()
):
    img_data = requests.get(row["img"]).content
    position_e = row["position_e"].replace(" ", "-")
    with open(f'images/{row["page"]}_{position_e}.jpg', "wb") as handler:
        handler.write(img_data)
