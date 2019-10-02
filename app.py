from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return "นางสาว ธนัชญา วิสุทธิแพทย์ เลขที่ 14 ชั้น ม.4/7"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['originalDetectintentRequest'][payload]['data']['replyToken']
    userText = decoded['queryResult']['intent']['displyName']
    #sendtext(user,userText)
    if (userText == 'hello') :
        sendText(user,'เออออหว่ะ')
    elif (userText == 'ไปล่ะ') :
        sendText(user,'ไปไหนก็ไปไป๊')
    else :
        sendText(user,'ว่าไงนะะ')
    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
