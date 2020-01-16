from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)


# mysql 접속
conn = pymysql.connect(host='45.119.146.152', port=1024, user='trivle', password='Trivle_96', db='trivle',
                       use_unicode=True, charset='utf8')


# IP address of NodeMCU
address = 'http://192.168.0.6'

response_dict = {"response": {
"outputSpeech": {
"text": "",
"type": "PlainText"
},
"shouldEndSession": True
},
"sessionAttributes": {},
"version": "1.0"
}


@app.route('/', methods=['POST'])
def index():
    print(type(request.data))
    print(type(request.json))

    request_json = request.json
    intent = get_intent_from_request(request_json)

    result = ''
    
    #장보기
    #item은 dialogflow에서 목록을 받아와서 검색
    if intent == '//장보기intent//':
        result = Shopping(item)
    #합계
    elif intent == '//합계intent':
        result = Sum()
    elif intent == '//목록보기':
        result = View_List()
    else:
        result = handle_fallback_intent()

    response_dict['response']['outputSpeech']['text'] = result

    return jsonify(json.dumps(response_dict))

#장보기 main
def Shopping(item):
    namelist = Name_Crawling()
    pricelist = Price_Crawling()
    Plus_List()

    return ""


# 장바구니db 가져오기
def Sum():
    cur = conn.cursor()
    sql = 'SELECT * from //장바구니db name//;'
    cur.execute(sql)  # 쿼리 수행
    conn.commit()

    rows = cur.fetchall()  # 결과 가져옴(데이터타입: 튜플)

    sum = 0
    for i in rows:
        for j in i:
            # 가격을 가져와서 +   
            sum += j.가격
    # 장바구니 초기화

    reset_sql = "Truncate table //장바구니db name//"
    cur.execute(reset_sql)  # 쿼리 수행
    conn.commit()
    return ""


# 장바구니에 목록 추가
def  Plus_List(item):
    cur = conn.cursor()
    
    # 장바구니 db 가져옴
    sql = 'SELECT * from //장바구니db name//;'
    cur.execute(sql)  # 쿼리 수행
    rows = cur.fetchall()  # 결과 가져옴(데이터타입: 튜플)

    # 장바구니 db 이용하여 추가
    # 라면 / 가격 형태

    return intent

# 리스트 보기
def View_List():
    cur = conn.cursor()
    
    # 장바구니 db 가져옴
    sql = 'SELECT * from //장바구니db name//;'
    cur.execute(sql)  # 쿼리 수행
    rows = cur.fetchall()  # 결과 가져옴(데이터타입: 튜플)

    viewlist[] = {}

    cnt = 1
    for i in rows:
        for j in i:
            # view list
            # 1. [품목/가격]
            # 2. [품목/가격]
            # 3. [품목/가격]
            # 위와 같은 형태로 viewlist 생성하여 출력
            viewlist.append(cnt + ". " + j.품목 + "/" + j.가격 + "\n") #품목
          
    return viewlist

# 크롤링
def Name_Crawling():
    # 코드를 채워주세욤
    return namelist

def Price_Crawling():
    
    return pricelist

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)