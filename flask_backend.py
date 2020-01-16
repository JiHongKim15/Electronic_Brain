from random import *
import pymysql
import json
import re


Destination = ''
attribute = ''

# mysql 접속
conn = pymysql.connect(host='45.119.146.152', port=1024, user='trivle', password='Trivle_96', db='trivle',
                       use_unicode=True, charset='utf8')


# 장바구니db  가져오기
def Sum():
    cur = conn.cursor()
    sql = 'SELECT * from //장바구니db name//;'
    cur.execute(sql)  # 쿼리 수행
    conn.commit()

    rows = cur.fetchall()  # 결과 가져옴(데이터타입: 튜플)

    


    # sum 초기화
    reset_sql = "Truncate table //장바구니db name//"
    cur.execute(reset_sql)  # 쿼리 수행
    conn.commit()

    # 장바구니 초기화


# 장바구니에 목록 추가
def  Plus_List(item):
    cur = conn.cursor()
    
    # 장바구니 db 가져옴
    sql = 'SELECT * from //장바구니db name//;'
    cur.execute(sql)  # 쿼리 수행
    rows = cur.fetchall()  # 결과 가져옴(데이터타입: 튜플)

    # 장바구니 db 이용하여 추가
    # 라면 / 가격 형태




# ------------------------------------------------------------------------------
def Set_Location(parameters):
    print('Set_List: parameters')
    print('Set:' + parameters['DestinationForSet']['value'])

    recently(parameters['DestinationForSet']['value'])

    cur = conn.cursor()
    sql = 'SELECT * from location;'
    cur.execute(sql)  # 쿼리 수행
    rows = cur.fetchall()  # 결과 가져옴(데이터타입: 튜플)

    for i in rows:
        for j in i:
            if (j == parameters['DestinationForSet']['value']):
                hello = {
                    'Destination1': '존재'}  # 하는 리스트예요. 듣기를 원하시면 ' + parameters['DestinationForSet']['value'] + ' 리스트 들려줘라고 말씀해주세요'}
                return hello

    # 존재하는 리스트 return


# ------------------------------------------------------------------------------
def Delete_List(parameters):
    print('parameters')
    print(parameters)

    Destination = parameters['DestinationForDelete']['value']  # 여행지

    cursor = conn.cursor()
    tsql = "Truncate table RECENT"
    cursor.execute(tsql)  # 쿼리 수행
    conn.commit()

    # print(Destination)
    # query 결과물 받아서 return
    check = "SHOW TABLES LIKE '" + Destination + "';"
    cursor.execute(check)
    res = cursor.fetchall()
    if len(res) == 0:
        result = '존재하지 않는 여행지에요.'
    else:
        sql = 'DROP TABLE ' + Destination + ';'
        cursor.execute(sql)  # 쿼리 수행
        conn.commit()

        delsql = "Delete from trivle.location where place = '" + Destination + "';"
        print(delsql)
        cursor.execute(delsql)
        conn.commit()
        result = Destination + ' 여행 리스트를 삭제할게요.'

    print('@@')
    print(result)
    hello = {'DONE': result}
    return hello


# ------------------------------------------------------------------------------
def Listen_DTN_YES(parameters):  # location table에서 DestinationForListen이 존재하는지 확인
    print('parameters')
    print(parameters)

    # parameters에서 필요한 인자 추출
    Destination = parameters['DestinationForListen']['value']  # 여행지
    print('Destination: ', Destination)

    # query 결과물 받아서 return
    cursor = conn.cursor()
    sql = "SELECT EXISTS (SELECT * FROM location WHERE place = '" + Destination + "');"
    print(sql)
    cursor.execute(sql)  # 쿼리 수행
    rows = cursor.fetchone()  # 결과 가져옴(데이터타입: 튜플)
    print(rows[0])

    if (rows[0] == 1):
        hello = {'is_exist': 'exist'}
        recently(Destination)

    else:
        hello = {'is_exist': 'not_exist'}

    return hello


# ------------------------------------------------------------------------------
def Listen_DTN_NO(parameters):  # recent table에서 Destination이 존재하는지 확인
    print('parameters')
    print(parameters)

    # query 결과물 받아서 return
    cursor = conn.cursor()
    sql = 'SELECT R FROM RECENT;'
    cursor.execute(sql)  # 쿼리 수행
    rows = cursor.fetchone()  # 결과 가져옴(데이터타입: 튜플)
    print(rows)

    if (rows[0] != ''):
        hello = {'exist_recent': str(rows[0])}

    else:
        hello = {'exist_recent': 'not_exist'}

    return hello

# ---------------------------------------------------------------------------------
def Crawling(item):
    
# ------------------------------------------------------------------------------