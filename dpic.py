import os
urls = [
    "https://img.hywly.com/a/1/17859/46.jpg",
    "https://img.hywly.com/a/1/24987/51.jpg",
    "https://img.hywly.com/a/1/29093/56.jpg",
    "https://img.hywly.com/a/1/24059/60.jpg",
    "https://img.hywly.com/a/1/5081/62.jpg",
    "https://mtl.xtpxw.com/images/img/9702/68.jpg",
    "https://img.hywly.com/a/1/22609/65.jpg",
    "https://img.hywly.com/a/1/24275/52.jpg",
    "https://img.hywly.com/a/1/1087/48.jpg",
    "https://img.hywly.com/a/1/24592/50.jpg",
    "https://img.hywly.com/a/1/26753/45.jpg",
    "https://img.hywly.com/a/1/2559/39.jpg",
    "https://img.hywly.com/a/1/25166/48.jpg",
    "https://img.hywly.com/a/1/25011/80.jpg",
    "https://img.hywly.com/a/1/27189/44.jpg",
    "https://img.hywly.com/a/1/24985/49.jpg",
    "https://img.hywly.com/a/1/24079/40.jpg",
    "https://img.gzhuibei.com/images/img/7896/43.jpg",
    "https://img.hywly.com/a/1/33732/50.jpg",
]

def download(url):
    p = url.split('/')
    nums = int(p[-1].split(".")[0])
    _id = p[-2]
    for index in range(1, nums + 1):
        url_d = url.replace(str(nums) + '.jpg', str(index) + '.jpg')
        os.system('curl ' + url_d + f'> ./pic/{_id}-{index}.jpg')

for u in urls:
    download(u)
