import csv
import requests
import itertools

API_KEY = "AIzaSyBB93pQFssH3DTGXfROEojYCJARPOzQj04"
CHANNEL_ID = "UCQimGgtBQmF4zxOdnARWFpg"
BASE = "https://www.googleapis.com/youtube/v3"

def fetch_all_videos(api_key, channel_id):
    # 1) playlist de uploads
    upl = requests.get(f"{BASE}/channels", params={
        "part": "contentDetails",
        "id": channel_id,
        "key": api_key
    }).json()
    uploads_id = upl["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    videos = []
    page_token = ""
    while True:
        pl = requests.get(f"{BASE}/playlistItems", params={
            "part": "contentDetails",
            "playlistId": uploads_id,
            "maxResults": 50,
            "pageToken": page_token,
            "key": api_key
        }).json()

        ids = [i["contentDetails"]["videoId"] for i in pl.get("items", [])]
        if not ids:
            break

        vd = requests.get(f"{BASE}/videos", params={
            "part": "snippet,contentDetails,statistics,status,topicDetails",
            "id": ",".join(ids),
            "key": api_key
        }).json()
        videos.extend(vd.get("items", []))

        page_token = pl.get("nextPageToken")
        if not page_token:
            break

    return videos

def save_csv(videos, filename="videos.csv"):
    # descobrir todas as chaves possíveis
    nested = set()
    for v in videos:
        for sec in ("snippet","contentDetails","statistics","status","topicDetails"):
            if sec in v:
                for k in v[sec]:
                    nested.add(f"{sec}.{k}")
    all_keys = ["id"] + sorted(nested)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(all_keys)
        for v in videos:
            row = [v.get("id", "")]
            for k in all_keys[1:]:
                sec, key = k.split(".", 1)
                row.append(v.get(sec, {}).get(key, ""))
            writer.writerow(row)

if __name__ == "__main__":
    vids = fetch_all_videos(API_KEY, CHANNEL_ID)
    save_csv(vids)
    print(f"✅ Salvo {len(vids)} vídeos em videos.csv")
