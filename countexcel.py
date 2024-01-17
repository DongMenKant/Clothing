from numpy import short
import pandas as pd #导入pandas库

#导入excel数据
excel_file_root = "G:\\Desktop\\"
excel_files = ("blouses_result.xlsx", "polos_result.xlsx", "t_shirts_result.xlsx", "tanks_result.xlsx", "tunics_result.xlsx", "vests_result.xlsx", "total_result.xlsx")

for num in range(6):
    excel_file = excel_file_root + excel_files[num]
    data = pd.read_excel(excel_file)     
    print(excel_files[num] + "**********************")
    # 统计面料
    temp1 = "Pol".lower(); temp2 = "Spandex".lower(); temp3 = "Cotton".lower(); temp4 = "Rayon".lower(); temp4 = "Viscose".lower(); temp5 = "Lace".lower()
    polyester = 0; spandex = 0; cotton = 0; rayon = 0; viscose = 0; lace = 0
    for i in range(0,100): # 行号：0——99
        k = 0 
        for j in range(1, 13): # 列名：1——12
            if temp1 in str(data[j][i]).lower():
                polyester += 1
                k += 1
            if temp2 in str(data[j][i]).lower():
                spandex += 1 
                k += 1
            if temp3 in str(data[j][i]).lower():
                cotton += 1 
                k += 1
            if temp4 in str(data[j][i]).lower():
                rayon += 1  
                k += 1
            if temp4 in str(data[j][i]).lower():
                viscose += 1  
                k += 1
            if temp5 in str(data[j][i]).lower():
                lace += 1  
                k += 1
            if k > 0:
                break
    print("面料：""\npolyester =" + str(polyester) + "\nspandex =" + str(spandex) + "\ncotton =" + str(cotton) + " rayon =" + str(rayon)+ " viscose =" + str(viscose))

    # 统计开合方式closure
    temp1 = "Button".lower(); temp2 = "Pull".lower(); temp3 = "Zipper".lower(); temp4 = "Elastic".lower()
    button = 0; pull = 0; zipper = 0; elastic = 0; other = 0
    for i in range(0,100): # 行号：0——99
        k = 0 
        for j in range(1, 13): # 列名：1——12
            if temp1 in str(data[j][i]).lower():
                button += 1 
                k += 1
            elif temp2 in str(data[j][i]).lower():
                pull += 1 
                k += 1
            elif temp3 in str(data[j][i]).lower():
                zipper += 1 
                k += 1
            elif temp4 in str(data[j][i]).lower():
                elastic += 1 
                k += 1
            elif "closure" in str(data[j][i]).lower():
                other += 1
                k += 1
            if k > 0:
                break
    print("开合方式:""\nbutton =" + str(button) + "\npull =" + str(pull) + "\nzipper =" + str(zipper) + " elastic =" + str(elastic) + " other =" + str(other))

    # 统计plus size
    temp1 = "plus size".lower()
    plus_size = 0
    for i in range(0,100): # 行号：0——99
        k = 0 
        for j in range(1, 13): # 列名：1——12
            if temp1 in str(data[j][i]).lower():
                plus_size += 1 
                k += 1
            if k > 0:
                break
    print("大码\nplus size:" + str(plus_size))

    # 统计衣领collar/neck
    temp1 = "scoop".lower(); temp2 = "knit".lower(); temp3 = "self-fabric".lower(); temp4 = "ribbed".lower(); temp5 = ""
    scoop = 0; knit = 0; self_fabric = 0; ribbed = 0; v_neck = 0; other = 0
    for i in range(0,100): # 行号：0——99
        k = 0 
        for j in range(1, 13): # 列名：1——12
            if 'collar' in str(data[j][i]).lower():
                if temp1 in str(data[j][i]).lower():
                    scoop += 1 
                    k += 1
                elif temp2 in str(data[j][i]).lower():
                    knit += 1 
                    k += 1
                elif temp3 in str(data[j][i]).lower():
                    self_fabric += 1 
                    k += 1
                elif temp4 in str(data[j][i]).lower():
                    ribbed += 1 
                    k += 1 
                else:
                    other += 1
                    k += 1 
            if 'neck' in str(data[j][i]).lower():
                if 'v' in str(data[j][i]).lower():
                    v_neck += 1
                    k += 1
                else:
                    other += 1
                    k += 1
            if k > 0:
                break   
    print("衣领:""\nscoop =" + str(scoop) + "\nknit =" + str(knit) + "\nself_fabric =" + str(self_fabric) + " ribbed =" + str(ribbed) + " v-neck =" + str(v_neck)+ " other =" + str(other))

    # occasion 
    temp1 = "sport".lower(); temp2 = "work".lower(); temp3 = "daily".lower()
    sport = 0; work = 0; daily = 0
    for i in range(0,100): # 行号：0——99
        k = 0 
        for j in range(1, 13): # 列名：1——12
            if temp1 in str(data[j][i]).lower() or "exercise" in str(data[j][i]).lower() or "travel" in str(data[j][i]).lower():
                sport += 1 
                k += 1
            if temp2 in str(data[j][i]).lower() or "school" in str(data[j][i]).lower() or "office" in str(data[j][i]).lower():
                work += 1 
                k += 1
            if temp3 in str(data[j][i]).lower() or "home" in str(data[j][i]).lower():
                daily += 1 
                k += 1
            if k > 0:
                break
    print("场所:""\nsport =" + str(sport) + "\nwork =" + str(work) + "\ndaily =" + str(daily))


excel_file = excel_file_root + excel_files[6]
data = pd.read_excel(excel_file)  
print(excel_files[6] + "**********************")
# 统计面料
temp1 = "Pol".lower(); temp2 = "Spandex".lower(); temp3 = "Cotton".lower(); temp4 = "Rayon".lower(); temp4 = "Viscose".lower(); temp5 = "Lace".lower()
polyester = 0; spandex = 0; cotton = 0; rayon = 0; viscose = 0; lace = 0
for i in range(0,600): # 行号：0——599
    k = 0 
    for j in range(1, 13): # 列名：1——12
        if temp1 in str(data[j][i]).lower():
            polyester += 1
            k += 1
        if temp2 in str(data[j][i]).lower():
            spandex += 1 
            k += 1
        if temp3 in str(data[j][i]).lower():
            cotton += 1 
            k += 1
        if temp4 in str(data[j][i]).lower():
            rayon += 1  
            k += 1
        if temp4 in str(data[j][i]).lower():
            viscose += 1  
            k += 1
        if temp5 in str(data[j][i]).lower():
            lace += 1  
            k += 1
        if k > 0:
            break
print("面料：""\npolyester =" + str(polyester) + "\nspandex =" + str(spandex) + "\ncotton =" + str(cotton) + " rayon =" + str(rayon)+ " viscose =" + str(viscose))

# 统计开合方式closure
temp1 = "Button".lower(); temp2 = "Pull".lower(); temp3 = "Zipper".lower(); temp4 = "Elastic".lower()
button = 0; pull = 0; zipper = 0; elastic = 0; other = 0
for i in range(0,600): # 行号：0——599
    k = 0 
    for j in range(1, 13): # 列名：1——12
        if temp1 in str(data[j][i]).lower():
            button += 1 
            k += 1
        elif temp2 in str(data[j][i]).lower():
            pull += 1 
            k += 1
        elif temp3 in str(data[j][i]).lower():
            zipper += 1 
            k += 1
        elif temp4 in str(data[j][i]).lower():
            elastic += 1 
            k += 1
        elif "closure" in str(data[j][i]).lower():
            other += 1
            k += 1
        if k > 0:
            break
print("开合方式:""\nbutton =" + str(button) + "\npull =" + str(pull) + "\nzipper =" + str(zipper) + " elastic =" + str(elastic) + " other =" + str(other))

# 统计plus size
temp1 = "plus size".lower()
plus_size = 0
for i in range(0,600): # 行号：0——599
    k = 0 
    for j in range(1, 13): # 列名：1——12
        if temp1 in str(data[j][i]).lower():
            plus_size += 1 
            k += 1
        if k > 0:
            break
print("大码\nplus size:" + str(plus_size))

# 统计衣领collar/neck
temp1 = "scoop".lower(); temp2 = "knit".lower(); temp3 = "self-fabric".lower(); temp4 = "ribbed".lower(); temp5 = ""
scoop = 0; knit = 0; self_fabric = 0; ribbed = 0; v_neck = 0; other = 0
for i in range(0,600): # 行号：0——599
    k = 0 
    for j in range(1, 13): # 列名：1——12
        if 'collar' in str(data[j][i]).lower():
            if temp1 in str(data[j][i]).lower():
                scoop += 1 
                k += 1
            elif temp2 in str(data[j][i]).lower():
                knit += 1 
                k += 1
            elif temp3 in str(data[j][i]).lower():
                self_fabric += 1 
                k += 1
            elif temp4 in str(data[j][i]).lower():
                ribbed += 1 
                k += 1 
            else:
                other += 1
                k += 1 
        if 'neck' in str(data[j][i]).lower():
            if 'v' in str(data[j][i]).lower():
                v_neck += 1
                k += 1
            else:
                other += 1
                k += 1
        if k > 0:
            break   
print("衣领:""\nscoop =" + str(scoop) + "\nknit =" + str(knit) + "\nself_fabric =" + str(self_fabric) + " ribbed =" + str(ribbed) + " v-neck =" + str(v_neck)+ " other =" + str(other))


# occasion 
temp1 = "sport".lower(); temp2 = "work".lower(); temp3 = "daily".lower()
sport = 0; work = 0; daily = 0
for i in range(0,600): # 行号：0——599
    k = 0 
    for j in range(1, 13): # 列名：1——12
        if temp1 in str(data[j][i]).lower() or "exercise" in str(data[j][i]).lower() or "travel" in str(data[j][i]).lower():
            sport += 1 
            k += 1
        if temp2 in str(data[j][i]).lower() or "school" in str(data[j][i]).lower() or "office" in str(data[j][i]).lower():
            work += 1 
            k += 1
        if temp3 in str(data[j][i]).lower() or "home" in str(data[j][i]).lower():
            daily += 1 
            k += 1
        if k > 0:
            break
print("场所:""\nsport =" + str(sport) + "\nwork =" + str(work) + "\ndaily =" + str(daily))



