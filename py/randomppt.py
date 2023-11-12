import os
import random
import time
import sys




workmode = sys.argv[1]
#print(workmode)

com = "taskkill /f /t /im "
to_ppt = "PPTService.exe"
pa_ppt = '\"D:\\Program Files (x86)\\Seewo\\PPTService\\Main\\PPTService.exe\"'
to_esc = 'esc.exe'
t = '\"D:\\seewo\\py\\'     #文件夹路径（含开头“）
pptfolder = 'ppsx'  #定义PPSX文件存放位置（子目录）
notefolder = 'note'  #定义NOTE文件存放位置（子目录）
remixfolder = 'remix'  #定义REMIX文件存放位置（子目录）
to_vol = 'SetVol.exe'

here = os.path.dirname(__file__)
#file_path = os.path.join(here, pptfolder)	#相对路径转换

os.chdir(sys.path[0])
entries = os.listdir(pptfolder)
playing_ppsx = random.choice(entries)
playing_path = os.path.join(here, pptfolder, playing_ppsx)

os.chdir(sys.path[0])
entries = os.listdir(notefolder)
note_path = os.path.join(here, notefolder, random.choice(entries) )

remix_path = os.path.join(here, remixfolder, workmode)
entries = os.listdir(remix_path)
remix_path = os.path.join(here, remixfolder, workmode, random.choice(entries) )


#entries = os.listdir(file_path)  



b = os.system(com + to_ppt)	#杀ppt小助手后台

os.chdir(sys.path[0])
os.system("volumeplus.exe") #自动音量

os.chdir(sys.path[0])
y = os.system(to_vol + " 100")	#音量调到100%
print(note_path)

os.chdir(sys.path[0])
s = "mpv.exe " + note_path + " --load-osd-console=no --force-window=no --no-taskbar-progress"
a=os.system(s)
"""

time.sleep(4)

os.chdir(sys.path[0])
s = "mpv.exe " + remix_path + " --load-osd-console=no --force-window=no --no-taskbar-progress"
print(s)

time.sleep(1)

a=os.system(s)

#   旧版抽取    ####
#r = random.randint(1, n)
#rr = str(r)
#pat = r'cd "C:\Program Files\Microsoft Office\root\Office16\"'
#str = "上课了_"


s = "start POWERPNT" + ' ' + '/S ' + playing_path

#os.system(pat)

a=os.system(s)

time.sleep(random.randint(21, 24))

os.chdir(sys.path[0])
os.system("esc.exe")    #自动退出

time.sleep(2)  #重启小助手

a = os.system(pa_ppt)

"""

#print(s)
#"D:\Program Files (x86)\Seewo\PPTService\Main\PPTService.exe"星河辰海
#读取文件参考https://zhuanlan.zhihu.com/p/56909212
#从list中随机抽取元素的方法https://blog.csdn.net/HappyRocking/article/details/84314313
#相对路径转换 https://www.zhihu.com/question/466490632?utm_id=0
#	https://www.zhihu.com/question/313379182
"""
.\mpv.exe --load-osd-console=no --force-window=no --no-taskbar-progress "D:\seewo\py\候课时间到_云希_轻松_成年人口吻.mp3",
"""