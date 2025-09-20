python -c "
import csv, requests

API_KEY = 'AIzaSyBB93pQFssH3DTGXfROEojYCJARPOzQj04'
CHANNEL_ID = 'UCib793mnUOhWymCh2VJKplQ'

base_url = 'https://www.googleapis.com/youtube/v3'
videos = []

# 1) pegar uploads playlist id
res = requests.get(f'{base_url}/channels', params={'part':'contentDetails','id':CHANNEL_ID,'key':API_KEY}).json()
uploads_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# 2) percorrer playlist e coletar IDs
page_token = ''
while True:
    pl = requests.get(f'{base_url}/playlistItems', params={'part':'contentDetails','playlistId':uploads_id,'maxResults':50,'pageToken':page_token,'key':API_KEY}).json()
    ids = [item['contentDetails']['videoId'] for item in pl.get('items',[])]
    if not ids: break

    # 3) buscar metadados detalhados de cada vídeo
    vd = requests.get(f'{base_url}/videos', params={'part':'snippet,contentDetails,statistics','id':','.join(ids),'key':API_KEY}).json()
    videos.extend(vd.get('items',[]))

    page_token = pl.get('nextPageToken')
    if not page_token: break

# 4) salvar em CSV
with open('videos.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    header = ['videoId','title','publishedAt','description','duration','viewCount','likeCount','commentCount']
    writer.writerow(header)
    for v in videos:
        s, c, stats = v['snippet'], v['contentDetails'], v['statistics']
        writer.writerow([
            v['id'],
            s.get('title',''),
            s.get('publishedAt',''),
            s.get('description','').replace('\n',' '),
            c.get('duration',''),
            stats.get('viewCount',''),
            stats.get('likeCount',''),
            stats.get('commentCount','')
        ])
print('Salvo em videos.csv com', len(videos), 'vídeos')
"
