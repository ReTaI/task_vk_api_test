import vk
import glob
session=vk.Session(access_token="your_token")
api=vk.API(session, v=5.95)
allfiles=glob.glob('*.txt')
for k in range (len(allfiles)):
    file=open(allfiles[k],"r")
    i=0
    links=[]
    file.read(15)
    for line in file:
        file.read(15)
        links.insert(i,line)
        i=i+1
    file.close()
    file=open(allfiles[k],"w")

    result=api.users.get(user_ids=links)
    for i in range(len(result)):
        file.write(str(result[i]['id'])+'\n')
file.close()
