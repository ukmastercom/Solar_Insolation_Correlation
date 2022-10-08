#will convert csv to required format
from pandas import *
import csv
def convert_dates():
    
    # reading CSV file
    data_0 = read_csv("save_data_0.csv")
    dat = data_0['date'].tolist()
    dat_y = []
    dat_m=[]
    dat_d=[]
    for i in range (0,len(dat)):
        x=str(dat[i])
        dat_y.append(int(x[0:4]))
        dat_m.append(int(x[4:6]))
        dat_d.append(int(x[6:8]))
    val_0 = data_0['value'].tolist()
    data_1 = read_csv("save_data_1.csv")
    val_1 = data_1['value'].tolist()
    data_2 = read_csv("save_data_2.csv")
    val_2 = data_2['value'].tolist()
    data_3 = read_csv("save_data_3.csv")
    val_3 = data_3['value'].tolist()
    data_4 = read_csv("save_data_4.csv")
    val_4 = data_4['value'].tolist()
    data_5 = read_csv("save_data_5.csv")
    val_5 = data_5['value'].tolist()
    data_6 = read_csv("save_data_6.csv")
    val_6 = data_6['value'].tolist()
    data_7 = read_csv("save_data_7.csv")
    val_7 = data_7['value'].tolist()
    data_8 = read_csv("save_data_8.csv")
    val_8 = data_8['value'].tolist()
    data_9 = read_csv("save_data_9.csv")
    val_9 = data_9['value'].tolist()
    data_10 = read_csv("save_data_10.csv")
    val_10 = data_10['value'].tolist()
    data_11 = read_csv("save_data_11.csv")
    val_11 = data_11['value'].tolist()
    data_12 = read_csv("save_data_12.csv")
    val_12 = data_12['value'].tolist()
    data_13 = read_csv("save_data_13.csv")
    val_13 = data_13['value'].tolist()
    data_14 = read_csv("save_data_14.csv")
    val_14 = data_14['value'].tolist()
    data_15 = read_csv("save_data_15.csv")
    val_15 = data_15['value'].tolist()
    data_16 = read_csv("save_data_16.csv")
    val_16 = data_16['value'].tolist()
    data_17 = read_csv("save_data_17.csv")
    val_17 = data_17['value'].tolist()
    data_18 = read_csv("save_data_18.csv")
    val_18 = data_18['value'].tolist()
    header=['year','month','date','v0','v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11','v12','v13','v14','v15','v16','v17','v18']
    row = zip()
    with open("final_save_dates.csv", 'w',newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(zip(dat_y,dat_m,dat_d,val_0,val_1,val_2,val_3,val_4,val_5,val_6,val_7,val_8,val_9,val_10,val_11,val_12,val_13,val_14,val_15,val_16,val_17,val_18) )
