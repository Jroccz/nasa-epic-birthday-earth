import requests

def retrieve_epic_photos(api_key, date):
    endpoint_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
    params = {"api_key": api_key}

    response = requests.get(endpoint_url, params=params)

    if response.status_code == 200:
        data = response.json()
        photo = data[0]
        return photo
    else:
        print(f"Data not received. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
  birthday = input("What is your birthday? (YYYY-MM-DD): ")
photos = retrieve_epic_photos("RMW9pB6c6BR8mjhJ6wwCbWBq8FccJwGp96jHbmwh"
, "2019-02-10")
new_date=birthday.replace("-","/")
base = "https://epic.gsfc.nasa.gov/archive/natural"
print(f"{base}/{new_date}/png/{photos['image']}.png")
if photos:
        print(f"Photos on this date: {len(photos)}")
        print()
else:
        print("No photos for this date.")
