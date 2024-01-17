from pymongo import MongoClient
import pandas as pd
import numpy
import json


def connectmongodb():
    client = MongoClient('mongodb://admin:123456@localhost:27017/')
    # 指定数据库 
    global db
    db = client.woman_top_clothings 

def readmongodb(table_name):
    # # 连接mongoDB
    # # client = MongoClient('mongodb://admin:123456@localhost:27017/')
    # client = MongoClient('mongodb://admin:123456@10.176.200.11:27017/')
    # # 指定数据库 
    # db = client.woman_top_clothings 

    print("开始统计分析：" + table_name + "表*************************\n")
    # 指定表
    mycol = db[table_name]
    data = pd.DataFrame(list(mycol.find()))

    # 5表示物种属性：面料、开合方式、大码、衣领、场所
    # 6表示每个属性最多包含六种情况
    temp_data_list = numpy.zeros((5,6))

    # 统计面料
    temp1 = "Pol".lower(); temp2 = "Spandex".lower(); temp3 = "Cotton".lower(); temp4 = "Rayon".lower(); temp5 = "Viscose".lower(); temp6 = "Lace".lower()
    temp_data_list[0][0] = 0; temp_data_list[0][1] = 0; temp_data_list[0][2] = 0; temp_data_list[0][3] = 0; temp_data_list[0][4] = 0; temp_data_list[0][5] = 0
    for i in range(100):
        if temp1 in str(data['features'][i]).lower():
            temp_data_list[0][0] += 1
        if temp2 in str(data['features'][i]).lower():
            temp_data_list[0][1] += 1 
        if temp3 in str(data['features'][i]).lower():
            temp_data_list[0][2] += 1 
        if temp4 in str(data['features'][i]).lower():
            temp_data_list[0][3] += 1  
        if temp5 in str(data['features'][i]).lower():
            temp_data_list[0][4] += 1  
        if temp6 in str(data['features'][i]).lower():
            temp_data_list[0][5] += 1    

    # 统计开合方式closure
    temp1 = "Button".lower(); temp2 = "Pull".lower(); temp3 = "Zipper".lower(); temp4 = "Elastic".lower()
    temp_data_list[1][0] = 0; temp_data_list[1][1] = 0; temp_data_list[1][2] = 0; temp_data_list[1][3] = 0; temp_data_list[1][4] = 0
    for i in range(100):
        if temp1 in str(data['features'][i]).lower():
            temp_data_list[1][0] += 1 
        elif temp2 in str(data['features'][i]).lower():
            temp_data_list[1][1] += 1 
        elif temp3 in str(data['features'][i]).lower():
            temp_data_list[1][2] += 1 
        elif temp4 in str(data['features'][i]).lower():
            temp_data_list[1][3] += 1 
        elif "closure" in str(data['features'][i]).lower():
            temp_data_list[1][4] += 1

    # 统计plus size
    temp1 = "plus size".lower()
    temp_data_list[2][0] = 0
    for i in range(100): # 行号：0——99
        if temp1 in str(data['features'][i]).lower():
            temp_data_list[2][0] += 1 

    # 统计衣领collar/neck
    temp1 = "scoop".lower(); temp2 = "knit".lower(); temp3 = "self-fabric".lower(); temp4 = "ribbed".lower()
    temp_data_list[3][0] = 0; temp_data_list[3][1] = 0; temp_data_list[3][2] = 0; temp_data_list[3][3] = 0; temp_data_list[3][4] = 0; temp_data_list[3][5] = 0
    for i in range(100): # 行号：0——99
        if 'collar' in str(data['features'][i]).lower():
            if temp1 in str(data['features'][i]).lower():
                temp_data_list[3][0] += 1 
            elif temp2 in str(data['features'][i]).lower():
                temp_data_list[3][1] += 1 
            elif temp3 in str(data['features'][i]).lower():
                temp_data_list[3][2] += 1 
            elif temp4 in str(data['features'][i]).lower():
                temp_data_list[3][3] += 1 
            else:
                temp_data_list[3][5] += 1
        if 'neck' in str(data['features'][i]).lower():
            if 'v' in str(data['features'][i]).lower():
                temp_data_list[3][4] += 1
            else:
                temp_data_list[3][5] += 1
   
    # occasion 
    temp1 = "sport".lower(); temp2 = "work".lower(); temp3 = "daily".lower()
    temp_data_list[4][0] = 0; temp_data_list[4][1] = 0; temp_data_list[4][2] = 0
    for i in range(100): # 行号：0——99
        if temp1 in str(data['features'][i]).lower() or "exercise" in str(data['features'][i]).lower() or "travel" in str(data['features'][i]).lower():
            temp_data_list[4][0] += 1 
        if temp2 in str(data['features'][i]).lower() or "school" in str(data['features'][i]).lower() or "office" in str(data['features'][i]).lower():
            temp_data_list[4][1] += 1 
        if temp3 in str(data['features'][i]).lower() or "home" in str(data['features'][i]).lower():
            temp_data_list[4][2] += 1 

    return temp_data_list


def readmongodb_time(table_name):
    # client = MongoClient('mongodb://admin:123456@10.176.200.11:27017/')
    # # 指定数据库 
    # db = client.woman_top_clothings 

    print("开始统计分析：" + table_name + "表*************************\n")
    # 指定表
    mycol = db[table_name]
    data = pd.DataFrame(list(mycol.find()))

    # 10表示物种属性：100表示100个时间段
    # 4表示物种属性：面料、开合方式、衣领、场所
    # 6表示每个属性最多包含六种情况
    temp_data_list = numpy.zeros((100,4,6))
    # 统计面料
    temp1 = "Pol".lower(); temp2 = "Spandex".lower(); temp3 = "Cotton".lower(); temp4 = "Rayon".lower(); temp5 = "Viscose".lower(); temp6 = "Lace".lower()
    # temp_data_list[0][0] = 0; temp_data_list[0][1] = 0; temp_data_list[0][2] = 0; temp_data_list[0][3] = 0; temp_data_list[0][4] = 0; temp_data_list[0][5] = 0
    i = 0; time =-1
    while i<len(data):   
        if '#1' == str(data['topid'][i]): # 每个时间段开始
            time += 1   
        if temp1 in str(data['features'][i]).lower():
            temp_data_list[time][0][0] += 1
        if temp2 in str(data['features'][i]).lower():
            temp_data_list[time][0][1] += 1 
        if temp3 in str(data['features'][i]).lower():
            temp_data_list[time][0][2] += 1 
        if temp4 in str(data['features'][i]).lower():
            temp_data_list[time][0][3] += 1  
        if temp5 in str(data['features'][i]).lower():
            temp_data_list[time][0][4] += 1  
        if temp6 in str(data['features'][i]).lower():
            temp_data_list[time][0][5] += 1   
        i +=1
    

    # 统计开合方式closure
    temp1 = "Button".lower(); temp2 = "Pull".lower(); temp3 = "Zipper".lower(); temp4 = "Elastic".lower()
    # temp_data_list[1][0] = 0; temp_data_list[1][1] = 0; temp_data_list[1][2] = 0; temp_data_list[1][3] = 0; temp_data_list[1][4] = 0
    i = 0; time =-1
    while i<len(data):   
        if '#1' == str(data['topid'][i]): # 每个时间段开始
            time += 1   
        if temp1 in str(data['features'][i]).lower():
            temp_data_list[time][1][0] += 1
        elif temp2 in str(data['features'][i]).lower():
            temp_data_list[time][1][1] += 1 
        elif temp3 in str(data['features'][i]).lower():
            temp_data_list[time][1][2] += 1 
        elif temp4 in str(data['features'][i]).lower():
            temp_data_list[time][1][3] += 1    
        elif "closure" in str(data['features'][i]).lower():
            temp_data_list[time][1][4] += 1 
        i +=1

    # # 统计plus size
    # temp1 = "plus size".lower()
    # # temp_data_list[2][0] = 0
    # i = 0; time =-1
    # while i<len(data):   
    #     if '#1' == str(data['topid'][i]): # 每个时间段开始
    #         time += 1   
    #     if temp1 in str(data['features'][i]).lower():
    #         temp_data_list[time][2][0] += 1
    #     i +=1

    # 统计衣领collar/neck
    temp1 = "scoop".lower(); temp2 = "knit".lower(); temp3 = "self-fabric".lower(); temp4 = "ribbed".lower()
    # temp_data_list[3][0] = 0; temp_data_list[3][1] = 0; temp_data_list[3][2] = 0; temp_data_list[3][3] = 0; temp_data_list[3][4] = 0; temp_data_list[3][5] = 0
    i = 0; time =-1
    while i<len(data):   
        if '#1' == str(data['topid'][i]): # 每个时间段开始
            time += 1      
        if 'collar' in str(data['features'][i]).lower():
            if temp1 in str(data['features'][i]).lower():
                temp_data_list[time][2][0] += 1 
            elif temp2 in str(data['features'][i]).lower():
                temp_data_list[time][2][1] += 1 
            elif temp3 in str(data['features'][i]).lower():
                temp_data_list[time][2][2] += 1 
            elif temp4 in str(data['features'][i]).lower():
                temp_data_list[time][2][3] += 1 
            else:
                temp_data_list[time][2][5] += 1
        if 'neck' in str(data['features'][i]).lower():
            if 'v' in str(data['features'][i]).lower():
                temp_data_list[time][2][4] += 1
            else:
                temp_data_list[time][2][5] += 1
        i +=1

    # occasion 
    temp1 = "sport".lower(); temp2 = "work".lower(); temp3 = "daily".lower()
    # temp_data_list[4][0] = 0; temp_data_list[4][1] = 0; temp_data_list[4][2] = 0
    i = 0; time =-1
    while i<len(data):   
        if '#1' == str(data['topid'][i]): # 每个时间段开始
            time += 1   
        if temp1 in str(data['features'][i]).lower():
            temp_data_list[time][3][0] += 1
        if temp2 in str(data['features'][i]).lower():
            temp_data_list[time][3][1] += 1 
        if temp3 in str(data['features'][i]).lower():
            temp_data_list[time][3][2] += 1 
        i +=1
    return temp_data_list


def readmongodb_style(table_name):
    # client = MongoClient('mongodb://admin:123456@10.176.200.11:27017/')
    # # 指定数据库 
    # db = client.woman_top_clothings 


    print("开始统计分析：" + table_name + "表*************************\n")
    # 指定表
    mycol = db[table_name]
    data = pd.DataFrame(list(mycol.find()))
    data_max = max(numpy.array(data['boho']).tolist())
    if data_max < max(numpy.array(data['camo']).tolist()):
        data_max = max(numpy.array(data['camo']).tolist())
    if data_max < max(numpy.array(data['chinese_national']).tolist()):
        data_max = max(numpy.array(data['chinese_national']).tolist())
    if data_max < max(numpy.array(data['college']).tolist()):
        data_max = max(numpy.array(data['college']).tolist())
    if data_max < max(numpy.array(data['hip_hop']).tolist()):
        data_max = max(numpy.array(data['hip_hop']).tolist())
    if data_max < max(numpy.array(data['palace']).tolist()):
        data_max = max(numpy.array(data['palace']).tolist())
    if data_max < max(numpy.array(data['professional']).tolist()):
        data_max = max(numpy.array(data['professional']).tolist())
    if data_max < max(numpy.array(data['small_fragrance']).tolist()):
        data_max = max(numpy.array(data['small_fragrance']).tolist())
    if data_max < max(numpy.array(data['sports']).tolist()):
        data_max = max(numpy.array(data['sports']).tolist())
    return data, data_max

def computer_max(json_name, num):
    with open("json/" + json_name + ".json", 'r') as load_f:
        data = json.load(load_f)
    return max(data[num])
