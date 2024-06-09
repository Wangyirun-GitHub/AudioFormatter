import os,shutil

Version=1.2
Developer="Peppa Wang"
Programname="AudioFormatter"
devdate="2024.5.30"

print("Welcome to use",Programname,"developed by",Developer,".")
print("Version:",Version,"    Date:",devdate)
print("Open Source Software:Copyright reserved.")
print("")

current=os.getcwd()
Inputpath=current+"\\Input"
Outputpath=current+"\\Output"
Temppath=current+"\\Temp"
parapath=current+"\\Parameters.txt"
mpegpath=current+"\\Environment"
ffmpegpath=current+"\\Environment\\ffmpeg.exe"
print("FFMPEG Path:",ffmpegpath)
os.system('path=%path%;'+ffmpegpath)
print("Input Folder Path:",Inputpath)
print("Output Folder Path:",Outputpath)

if os.path.exists(Inputpath)==0:
    os.mkdir(Inputpath)
if os.path.exists(Outputpath)==0:
    os.mkdir(Outputpath)
if os.path.exists(Temppath)==0:
    os.mkdir(Temppath)
if os.path.exists(mpegpath)==0:
    os.mkdir(mpegpath)
while os.path.isfile(ffmpegpath)==0:
    print("Please put'ffmpeg.exe'in",mpegpath,"folder!")
    os.system("pause")
while os.path.isfile(parapath)==0:
    print("Please put'Parameters.txt'in",current,"folder!")
    os.system("pause")
    
Inputdir=os.listdir(Inputpath)
Outputdir=os.listdir(Outputpath)
Tempdir=os.listdir(Temppath)
if len(Tempdir)!=0:
    for r in Tempdir:
        remove=Temppath+"\\"+r
        os.remove(remove)
while len(Inputdir)!=0:
    print("To prevent data loss,please empty files in the'Input'folder!")
    os.startfile(Inputpath)
    os.system("pause")
    Inputdir=os.listdir(Inputpath)
while len(Outputdir)!=0:
    print("To prevent data loss,please empty files in the'Output'folder!")
    os.startfile(Outputpath)
    os.system("pause")
    Outputdir=os.listdir(Outputpath)
print("All folders are ready.")
print("")

print("Please put pending files in the'Input'folder!")
os.startfile(Inputpath)
os.system("pause")

pendingmenu=os.listdir(Inputpath)
while len(pendingmenu)==0:
    print("Please put pending files in the'Input'folder!")
    os.startfile(Inputpath)
    os.system("pause")
    pendingmenu=os.listdir(Inputpath)

pendingnumber=len(pendingmenu)
print("Input Files:",pendingnumber,"files.")

data=["","","",""]
Parameters=open(parapath)
for i in range(0,4):
    data[i]=Parameters.readline()
    data[i]=data[i].strip('\n')
    data[i]=data[i].split("=")
list1=data[0]
list2=data[1]
list3=data[2]
list4=data[3]
samplingrate=list1[1]
channel=list2[1]
bitrate=list3[1]
outformat=list4[1]
Parameters.close()

serialnumber=list()
for i in range(0,pendingnumber):
    print("Please input the sequence number of the audio'",pendingmenu[i],"'.")
    s=input("")
    serialnumber.append(s)
    sourcename=Inputpath+"\\"+pendingmenu[i]
    splitname=os.path.splitext(sourcename)[-1]
    targetname=Temppath+"\\"+serialnumber[i]+splitname
    shutil.copy(sourcename,targetname)
print("Process scales:","Samplingrate=",samplingrate,"Hz,  Channel=",channel,"ch,  Bitrate=",bitrate,"bit/s.")
print("Output Format:",outformat)
print("Press Enter to start processing!")
wait=input("")
processmenu=os.listdir(Temppath)
processnumber=len(processmenu)        
for j in range(0,processnumber):
    print("Processing",pendingmenu[j],"and Output as",serialnumber[j]+outformat)
    inputname=Temppath+"\\"+processmenu[j]
    outputname=Outputpath+"\\"+serialnumber[j]+outformat
    print("Command:",ffmpegpath+" -i "+inputname+" -ac "+channel+" -ar "+samplingrate+" -ab "+bitrate+" -y "+outputname)
    os.system(ffmpegpath+" -i "+inputname+" -ac "+channel+" -ar "+samplingrate+" -ab "+bitrate+" -y "+outputname)
print("")
print("Done!")

resultnumber=len(os.listdir(Outputpath))
print("Output Files:",resultnumber,"files.")
os.startfile(Outputpath)

Tempdir=os.listdir(Temppath)
if len(Tempdir)!=0:
    for r in Tempdir:
        remove=Temppath+"\\"+r
        os.remove(remove)

print("Thank you for using",Programname,".")
os.system("pause")
