import csv,datetime as dt,time
with open('rows_300.csv','w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['№','Секунда','Микросекунда'])
    for line in range(300):
        writer.writerow([line+1,dt.datetime.now().second,dt.datetime.now().microsecond])
        time.sleep(0.01)