from datetime import datetime

class file_operations:

    def database(self,name):
        with open('log.txt','r+') as f:
            myDataList = f.readlines()
            nameList = []
            
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
        
            if name not in nameList:
                now = datetime.now()
                time = now.strftime('%I:%M:%S:%p')
                date = now.strftime('%d-%B-%Y')
                f.writelines(f'{name}, {time}, {date}')
            f.close()


