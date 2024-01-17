from pymongo import MongoClient
import pandas as pd
import numpy
# 连接mongoDB
# client = MongoClient('mongodb://admin:123456@localhost:27017/')
client = MongoClient('mongodb://admin:123456@10.176.200.11:27017/')
# 指定数据库 
db = client.woman_top_clothings 

# 指定表
table = ("blouses", "polos", "t_shirts", "tanks", "tunics", "vests")

# 5表示物种属性：面料、开合方式、大码、衣领、场所
# 6表示每个属性最多包含六种情况
blouses_data_list = numpy.zeros((5,6))
polos_data_list = numpy.zeros((5,6))
t_shirts_data_list = numpy.zeros((5,6))
tanks_data_list = numpy.zeros((5,6))
tunics_data_list = numpy.zeros((5,6))
vests_data_list = numpy.zeros((5,6))
total_data_list = numpy.zeros((5,6))


total_polyester = 0; total_spandex = 0; total_cotton = 0; total_rayon = 0; total_viscose = 0; total_lace = 0
total_button = 0; total_pull = 0; total_zipper = 0; total_elastic = 0; total_closure_other = 0
total_plus_size = 0
total_scoop = 0; total_knit = 0; total_self_fabric = 0; total_ribbed = 0; total_v_neck = 0; total_collar_other = 0
total_sport = 0; total_work = 0; total_daily = 0


for j in range(len(table)):
    print("开始统计分析：" + table[j] + "表*************************\n")
    mycol = db[table[j]]
    data = pd.DataFrame(list(mycol.find()))
    # 统计面料
    temp1 = "Pol".lower(); temp2 = "Spandex".lower(); temp3 = "Cotton".lower(); temp4 = "Rayon".lower(); temp4 = "Viscose".lower(); temp5 = "Lace".lower()
    polyester = 0; spandex = 0; cotton = 0; rayon = 0; viscose = 0; lace = 0
    for i in range(100):
        if temp1 in str(data['features'][i]).lower():
            polyester += 1
        if temp2 in str(data['features'][i]).lower():
            spandex += 1 
        if temp3 in str(data['features'][i]).lower():
            cotton += 1 
        if temp4 in str(data['features'][i]).lower():
            rayon += 1  
        if temp4 in str(data['features'][i]).lower():
            viscose += 1  
        if temp5 in str(data['features'][i]).lower():
            lace += 1  
    print("面料：""\npolyester =" + str(polyester) + "\nspandex =" + str(spandex) + "\ncotton =" + str(cotton) + " rayon =" + str(rayon)+ " viscose =" + str(viscose) + " lace =" + str(lace))
    total_polyester += polyester; total_spandex += spandex; total_cotton += cotton; total_rayon += rayon; total_viscose += viscose; total_lace += lace

    # 统计开合方式closure
    temp1 = "Button".lower(); temp2 = "Pull".lower(); temp3 = "Zipper".lower(); temp4 = "Elastic".lower()
    button = 0; pull = 0; zipper = 0; elastic = 0; closure_other = 0
    for i in range(100):
        if temp1 in str(data['features'][i]).lower():
            button += 1 
        elif temp2 in str(data['features'][i]).lower():
            pull += 1 
        elif temp3 in str(data['features'][i]).lower():
            zipper += 1 
        elif temp4 in str(data['features'][i]).lower():
            elastic += 1 
        elif "closure" in str(data['features'][i]).lower():
            closure_other += 1
    print("开合方式:""\nbutton =" + str(button) + "\npull =" + str(pull) + "\nzipper =" + str(zipper) + " elastic =" + str(elastic) + " other =" + str(closure_other))
    total_button += button; total_pull += pull; total_zipper += zipper; total_elastic += elastic; total_closure_other += closure_other

    # 统计plus size
    temp1 = "plus size".lower()
    plus_size = 0
    for i in range(100): # 行号：0——99
        if temp1 in str(data['features'][i]).lower():
            plus_size += 1 
    print("大码\nplus size:" + str(plus_size))
    total_plus_size += plus_size

    # 统计衣领collar/neck
    temp1 = "scoop".lower(); temp2 = "knit".lower(); temp3 = "self-fabric".lower(); temp4 = "ribbed".lower(); temp5 = ""
    scoop = 0; knit = 0; self_fabric = 0; ribbed = 0; v_neck = 0; collar_other = 0
    for i in range(100): # 行号：0——99
        if 'collar' in str(data['features'][i]).lower():
            if temp1 in str(data['features'][i]).lower():
                scoop += 1 
            elif temp2 in str(data['features'][i]).lower():
                knit += 1 
            elif temp3 in str(data['features'][i]).lower():
                self_fabric += 1 
            elif temp4 in str(data['features'][i]).lower():
                ribbed += 1 
            else:
                collar_other += 1
        if 'neck' in str(data['features'][i]).lower():
            if 'v' in str(data['features'][i]).lower():
                v_neck += 1
            else:
                collar_other += 1
    print("衣领:""\nscoop =" + str(scoop) + "\nknit =" + str(knit) + "\nself_fabric =" + str(self_fabric) + " ribbed =" + str(ribbed) + " v-neck =" + str(v_neck)+ " other =" + str(collar_other))
    total_scoop += scoop; total_knit += knit; total_self_fabric += self_fabric; total_ribbed += ribbed; total_v_neck += v_neck; total_collar_other += collar_other

    # occasion 
    temp1 = "sport".lower(); temp2 = "work".lower(); temp3 = "daily".lower()
    sport = 0; work = 0; daily = 0
    for i in range(100): # 行号：0——99
        if temp1 in str(data['features'][i]).lower() or "exercise" in str(data['features'][i]).lower() or "travel" in str(data['features'][i]).lower():
            sport += 1 
        if temp2 in str(data['features'][i]).lower() or "school" in str(data['features'][i]).lower() or "office" in str(data['features'][i]).lower():
            work += 1 
        if temp3 in str(data['features'][i]).lower() or "home" in str(data['features'][i]).lower():
            daily += 1 
    print("场所:""\nsport =" + str(sport) + "\nwork =" + str(work) + "\ndaily =" + str(daily))
    total_sport += sport; total_work += work; total_daily += daily



print("Total:***************")
print("面料：""\npolyester =" + str(total_polyester) + "\nspandex =" + str(total_spandex) + "\ncotton =" + str(total_cotton) + " rayon =" + str(total_rayon) + " viscose =" + str(total_viscose) + " lace =" + str(total_lace))
print("开合方式:""\nbutton =" + str(total_button) + "\npull =" + str(total_pull) + "\nzipper =" + str(total_zipper) + " elastic =" + str(total_elastic) + " other =" + str(total_closure_other))
print("大码\nplus size:" + str(total_plus_size))
print("衣领:""\nscoop =" + str(total_scoop) + "\nknit =" + str(total_knit) + "\nself_fabric =" + str(total_self_fabric) + " ribbed =" + str(total_ribbed) + " v-neck =" + str(total_v_neck)+ " other =" + str(total_collar_other))
print("场所:""\nsport =" + str(total_sport) + "\nwork =" + str(total_work) + "\ndaily =" + str(total_daily))

