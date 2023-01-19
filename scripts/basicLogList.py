

basiclogs = []

lithologicLogs = ['Porosity Log','Density Log']

# add a list on the empty list
def addLogs(list,iterable):
    list.extend(iterable)
    return list


# add a log on the end of the list: append
def appendLog(list,e):
    list.append(e)
    return list

# insert a log on the begining of the list: insert
def insertlog(list,pos, log):
    list.insert(pos,log)
    return list

def run():
    print(addLogs(basiclogs,lithologicLogs))
    print(appendLog(basiclogs,'Sonic'))
    print(insertlog(basiclogs,0,'Gamma Ray'))

if __name__ == "__main__":
    run()