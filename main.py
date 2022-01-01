import requests
import time
import threading
import json

with open('tokens.json','r') as f:
    tokens = json.load(f)
with open('data/board.json','r') as f:
    tasks = json.load(f)


token_time = {k: 0 for k in tokens}
dict_t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
          'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
server = 'https://www.luogu.com.cn/paintboard'
boardaddr = server + '/board'
paintaddr = server + '/paint'
refer = 'https://www.luogu.com.cn/paintboard'
cd = 30

# 获取坐标(x,y)上的颜色
def getBoardColor(x, y):
    try:
        return color[x][y]
    except IndexError:
        print("Error,",x,y,color)
# 在(x,y)上用color和token绘画
def paint(x, y, color, token, refer):
    data = {'x': x, 'y': y, 'color': color}
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36','Referer': refer,'content-type':'application/x-www-form-urlencoded'}
    print(requests.post(paintaddr + "?token=" + token, data=data, headers=head).text,x,y,token)

# 更新绘板颜色数据
def boardUpdate():
    global color
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Referer': refer, 'content-type': 'application/x-www-form-urlencoded'}
    color = requests.get(boardaddr,headers=head).text.split('\n')

# 获取一个已经冷却的账号
def getToken():
    while True:
        for k, v in token_time.items():
            if time.time() - v > cd:
                return k

if __name__ == "__main__":
    boardUpdate()
    upd = threading.Thread(target=boardUpdate()) # 创建并开启子线程用于实时更新绘板数据
    upd.start()
    while True:
        for x in tasks: # 循环遍历并绘画
            if getBoardColor(x[0], x[1]) != dict_t[x[2]]:
                t = getToken()
                threading.Thread(target=paint,args=(x[0], x[1], x[2], t, refer),daemon=True).start()
                token_time[t] = time.time()
                time.sleep(0.3)