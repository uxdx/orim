listvideo=[
    {'Img_channel': 'https://yt3.ggpht.com/gp_3wsQU5QbA-mqVBNG8CSpgm3G0r3xcGKPYDT7zlq8gWgWFdIK6nFcnNHLL5ug-e1SeeGIEfg=s88-c-k-c0x00ffffff-no-rj', 'category': 'Music', 'channelId': 'UC4mOLela441MNvGJNy6h8bg', 'channel_name': 'YENA - Topic', 'channelurl': 'https://www.youtube.com/channel/UC4mOLela441MNvGJNy6h8bg', 'thumbnail': 'https://i.ytimg.com/vi/2KSWVz2tDEI/hqdefault.jpg', 'title': 'SMILEY (Feat. BIBI)', 'uploadDate': '2022-01-17 18:04:29', 'url': 'https://www.youtube.com/embed/2KSWVz2tDEI', 'videoId': '2KSWVz2tDEI'},
    {'Img_channel': 'https://yt3.ggpht.com/Ni7vBUKLu3y6g6zscGpcHPfoWfoCFbCn2fuZ241oIg5VITQdXMmbK1JZI9-WxyzqR0J2VG1q=s88-c-k-c0x00ffffff-no-rj', 'category': 'Music', 'channelId': 'UCKjRJx4JecfT9f8gmhIP72Q', 'channel_name': 'Coogie - Topic', 'channelurl': 'https://www.youtube.com/channel/UCKjRJx4JecfT9f8gmhIP72Q', 'thumbnail': 'https://i.ytimg.com/vi/LKUXc1uwA2Y/hqdefault.jpg', 'title': "Good Night (Feat. BE'O) (Good Night (Feat. BE'O))", 'uploadDate': '2022-01-24 18:23:37', 'url': 'https://www.youtube.com/embed/LKUXc1uwA2Y', 'videoId': 'LKUXc1uwA2Y'},
    {'Img_channel': 'https://yt3.ggpht.com/jv3r-jNHhG2jktdZcbxgdOUqdX6Yu-AbrpS6kYpYAeoAc0nZyMB5x7jjdjoDzxmHo2Q0LZQC=s88-c-k-c0x00ffffff-no-rj', 'category': 'Music', 'channelId': 'UC_pwIXKXNm5KGhdEVzmY60A', 'channel_name': 'Stone Music Entertainment', 'channelurl': 'https://www.youtube.com/channel/UC_pwIXKXNm5KGhdEVzmY60A', 'thumbnail': 'https://i.ytimg.com/vi/MR8ZIKmYjk8/hqdefault.jpg', 'title': '마마돌 (M.M.D) - 우아힙 (WooAh HIP) Performance Video', 'uploadDate': '2022-01-28 22:30:04', 'url': 'https://www.youtube.com/embed/MR8ZIKmYjk8', 'videoId': 'MR8ZIKmYjk8'},
    {'Img_channel': 'https://yt3.ggpht.com/kTbsA-GpVIqjs-OojhdXtAMoGCVa29hZWU_adcE_q1TfJBiEiwilQtH4k1FKai_1N_cZqjYas1E=s88-c-k-c0x00ffffff-no-rj', 'category': 'Music', 'channelId': 'UCwzCuKxyMY_sT7hr1E8G1XA', 'channel_name': 'TAEYEON - Topic', 'channelurl': 'https://www.youtube.com/channel/UCwzCuKxyMY_sT7hr1E8G1XA', 'thumbnail': 'https://i.ytimg.com/vi/O6zHTk0U4fU/hqdefault.jpg', 'title': "Can't Control Myself", 'uploadDate': '2022-01-17 18:07:44', 'url': 'https://www.youtube.com/embed/O6zHTk0U4fU', 'videoId': 'O6zHTk0U4fU'},
    {'Img_channel': 'https://yt3.ggpht.com/0QC8CSPYAxIwS56N2QLYrc-zjmQv-KC9PSN_BGH5Q7uG98T6NhEeiuOk8bHt7_QTwK4YuZPbCA=s88-c-k-c0x00ffffff-no-rj', 'category': 'Music', 'channelId': 'UC3M9MRdZz-WWtAQos94_h6w', 'channel_name': 'fromis_9 - Topic', 'channelurl': 'https://www.youtube.com/channel/UC3M9MRdZz-WWtAQos94_h6w', 'thumbnail': 'https://i.ytimg.com/vi/QT60l6MSoz8/hqdefault.jpg', 'title': 'DM', 'uploadDate': '2022-01-17 18:47:21', 'url': 'https://www.youtube.com/embed/QT60l6MSoz8', 'videoId': 'QT60l6MSoz8'},
    {'Img_channel': 'https://yt3.ggpht.com/3r_KXtEy4-B04RiH7aqsHr_gLz4UD4AOgBt7WrtIx5VTgu-E9AKlcQmjL-jXjIV_wWwt-DNl8Rw=s88-c-k-c0x00ffffff-no-rj', 'category': 'Music', 'channelId': 'UCfXj9asBtiIIVlbp0wXWXdQ', 'channel_name': 'ASH ISLAND - Topic', 'channelurl': 'https://www.youtube.com/channel/UCfXj9asBtiIIVlbp0wXWXdQ', 'thumbnail': 'https://i.ytimg.com/vi/qlFiAtpk-iw/hqdefault.jpg', 'title': 'Because', 'uploadDate': '2022-01-25 18:04:19', 'url': 'https://www.youtube.com/embed/qlFiAtpk-iw', 'videoId': 'qlFiAtpk-iw'}]
a=dict()
j=0
for i in listvideo:
    a[i['uploadDate']]=j
    j+=1

b=sorted(a.items(),reverse=False)


print(a)
print(b)

c=[]
for i in b:
    c.append(i[1])

print(c)

d=[]
for i in c:
    d.append(listvideo[i])


for i in d:
    print(i['uploadDate'])