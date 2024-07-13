import getopt
import os
import sys
try:
	import pyzstd
	import colorama
except:
	os.system('pip install pyzstd')
	os.system('pip install colorama')
	import pyzstd
	import colorama
	os.system("cls")
#--------------------------------------------
VMODCHECK = input("Skin -> Hero [1]; bEqual [2] :") 
chedovien = input("Frame Auto [1]; Handmade [2] :") 
deskins = input("Overlay Effects Skin S [y]; No [n] :") 
fixlag= input("Fix AssetRefs Yes [y]; No [n] :") 
fixlag1= input("Fix Born Yes [y]; No [n] :")
while True:
    def process_input_numbers(numbers):
        results = []

        for number in numbers:
            number_str = str(number)
            
            if len(number_str) == 5:
                results.append(number - 1)
            elif len(number_str) == 4:
                results.append(int(number_str[:-1] + "0" + number_str[-1]) - 1)
            else:
                print(f"Number {number} Is Invalid. Please Enter a 4 or 5 Digit Number ")
                return None
        
        return results

    # Nhập các số từ người dùng
    print("─"*30)
    input_numbers = input(''+"\033[1;30mSkin ID: ")
    numbers = [int(num) for num in input_numbers.split()]
    
    # Xử lý
    results = process_input_numbers(numbers)

    # In kết quả
    if results is not None:
        # Sử dụng str.join để kết hợp các số thành một chuỗi
        result_str = ' '.join(map(str, results))
    from colorama import init, Fore
    from os import listdir
    import os,zipfile,colorama,shutil,xml.dom.minidom,xml.sax,os,re,shutil,random,getopt,sys,pyzstd
    ZSTD_DICT=b'7\xa40\xec\xe7UC\x0bM\x10@\xae\xa6\xe9P\xaa\xffPL\x8d\xe1Tn)\xb7Dr\xbb\xecH\xaclT)(((((\xa0\xa2\xa0CU(G\x01\x18\x08r\x18\x11\x11\x9a]k\xd3\x8a:\x16\xa9\x89\xe8%\xc2\xde{\xef\xbd\xa5\x8e\xae\xdb2\xaa\x8ee\x99\x85a\xf0\xf9\xf1#\x9b\x02\x83\x05\x19\x0c\x08\x06\x05b\xa1`\x96\xc6\x81\xac}\x04D\xe4\xe1\xa4\xc3\x01\xe2`A\xc1\xe0`\xc1\xa0\xc0\xa0`0\x10\x08\x03\xc3\xc0@(\x10\x06\x80\xc2\xc2@ \x1c\n\x07D\x82\xf48\xe9\x96\x1b\x00\xd4\x0e\x11\x06\x1d\x8bA\x901\xc6\x18bH\x19\x00 \x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x08\x00\x00\x00mName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="skillCombineLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="skillCombineSrcId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSkillMark" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration14" eventType="HitTriggerDuration" guid="38f874e2-e64b-478d-be55-fc7453046e1c" enabled="true" refParamName="" useRefParam="false" r="0.183" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="8" guid="1b06b263-6aa9-4007-a2cb-116a920b9312" status="true"/>\n\t\t\t<Event eventName="HitTriggerDuration" time="0.200" lenid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack0" eventType="StopTrack" guid="8013dc81-a485-4567-bc08-9e0ec7d7cd99" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.017" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="4" guid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack1" eventType="StopTrack" guid="8633109d-53e5-4931-87b1-bf3472773aed" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.633" exe\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe8\xb0\xa6\xe8\xae\xa9"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe6\x94\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x87\xaa\xe6\x9d\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe9\x99\xa4\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="Buff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x81\xa2\xe5\xa4\x8dBuff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe5\xb0\x84\xe7\xa8\x8b"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="CheckSkillCombineConditionTick1" eventType="CheckSkillCombineConditionTick" guid="bc7f4540-c6d9-4813-88cb-990e1d8abf7f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.433" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentBuffId" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="skillCombineId" value="136001" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType"ame="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidMoveButRotate" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<int name="rotateSpeed" value="720" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t</Event>\r\n\t\t</Track>\r\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="4abae504-d3a2-4370-a0a8-255fde6c84d5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true" />\r\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="0.500" isDuration="true">\r\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<String name="clipName" value="Hit" refP/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00\xbb\x01\x00\x00J\x00\x00\x00\x17\x00\x00\x00Terms_Of_Service_Title\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x1c\x00\x00\x00\xc4\x90i\xe1\xbb\x81u kho\xe1\xba\xa3n d\xe1\xbb\x8bch v\xe1\xbb\xa5\x00=\x00\x00\x00\xe0\xb9\x80\xe0\xb8\x87\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\xad\xe0\xb8\x99\xe0\xb9\x84\xe0\xb8\x82\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb9\x83\xe0\xb8\xab\xe0\xb9\x89\xe0\xb8\x9a\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\x00\x11\x00\x00\x00\xec\x84\x9c\xeb\xb9\x84\xec\x8a\xa4 \xec\x95\xbd\xea\xb4\x80\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x12\x00\x00\x00Ketentuan Layanan\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe5\x88\xa9\xe7\x94\xa8\xe8\xa6\x8f\xe7\xb4\x84\x00g\x13\x00\x00K\x00\x00\x00\x16\x00\x00\x00Terms_Of_Service_Text\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\xe5\x85\xa7\xe5\xae\xb9\xe5\x85\xa7\xe5\xae\xb9\xe5\xbc\x89"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="collisionCheckDistanceOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="collisionCheckWidth" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInteruptOtherMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bProtectInteruptedByOtherMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsAreaLimitedToBeMoveDone" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="d7e3a6f9-943b-4dda-9650-7a88a29698f8" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.783" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnObjectDuration" time="0.233" length="0.300" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="parentId" ob\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00^KL\x00\x14\x00\x00\x000AF0A00F2605E9BB_##\x00\x00\x00\x14\x00\x00\x00349C21E70FD859FE_##\x00\x01\x00\x00\x00\x00\xe7.\x00\x00\x01\x00\x00\x00\x00\x04\x04\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00\x90\x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\n\x00\x00\x00}\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xa0\x00\x00\x00\x00\xbc\x96\x98J\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00`KL\x00\x14\x00\x00\x00B8FA881B79F41C0F_##\x00\x00\x00\x14\x00\x00\x0085F89A39568DD08B_##\x00\x01\x00\x00\x00\x00`KL\x00\x01\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00b\x00\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0f\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x01\x00\x00_KL\x00\x14\x00\x00\x004BF61216E72F555D_##\x00\x00\x00\x14\x00\x00\x00EA1631C678E20D11_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00starguardcard.png\x00\x04\x16\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x002\x00\x00\x00\xfa\x00\x00\x00d\x00\x00\x00d\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x80A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x01\x00\x00@\x85:\xe1\\\x12\x00\x00@\xeb<\r\xa5\x12\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00\x05^\x0c\x00\x14\x00\x00\x00DEC1050D07839DB7_##\x00\x00\x00\x14\x00\x00\x00F620F03B6DE88773_##\x00\x01\x00\x00\x00\x00\xfa\x97\x04\x00\x01\x00\x00\x00\x00\x04\n\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00 \x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\xa4\x04\x00\x00 \x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x00\x00\xd2B\x00\x00\x80?\x00\x00\x00\x00\x00\x00\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\x87\xb4\xe5\x91\xbd\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe7\xa6\x81\xe7\x94\xa8\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe8\x83\xbd\xe9\x87\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\xa4\xe7\x94\xb2\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb\xe5\xb8\xa6\xe6\xb3\x95\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2\xef\xbc\x88\xe7\xa6\x81\xe6\xad\xa2\xe4\xbd\xbf\xe7\x94\xa8\xef\xbc\x89"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x83\xbd\xe9\x87\x8f\xe5\x8d\xe7\xba\xbf\xe5\x8e\x8b\xe5\x8a\x9b\xef\xbc\x9b\\n\\n\xe2\x80\xa6\xe2\x80\xa6\\n\\n\xe4\xba\xba\xe7\xb1\xbb\xe7\x9a\x84\xe5\xbc\xba\xe8\x80\x85\xe4\xbb\xac\xe7\xbb\x93\xe6\x9d\x9f\xe4\xba\x86\xe5\x90\x84\xe8\x87\xaa\xe4\xb8\xba\xe6\x88\x98\xe7\x9a\x84\xe6\x97\xa5\xe5\xad\x90\xef\xbc\x8c\xe4\xbb\x96\xe4\xbb\xac\xe8\x81\x9a\xe9\x9b\x86\xe5\x9c\xa8\xe8\x90\xa8\xe5\xb0\xbc\xe7\x9a\x84\xe9\xba\xbe\xe4\xb8\x8b\xef\xbc\x8c\xe5\xb0\x86\xe4\xb8\x80\xe8\x82\xa1\xe8\x82\xa1\xe5\xbe\xae\xe5\xb0\x8f\xe7\x9a\x84\xe5\x8a\x9b\xe9\x87\x8f\xef\xbc\x8c\xe8\x81\x9a\xe5\x90\x88\xe6\x88\x90\xe6\x8e\xa8\xe5\x8a\xa8\xe5\x8e\x86\xe5\x8f\xb2\xe7\x9a\x84\xe6\xb4\xaa\xe6\xb5\x81\xe3\x80\x82\xe5\x9c\xa8\xe8\xbf\x99\xe8\x82\xa1\xe6\xb4\xaa\xe6\xb5\x81\xe9\x9d\xa2\xe5\x89\x8d\xef\xbc\x8c\xe5\xbc\xba\xe5\xa4\xa7\xe7\x9a\x84\xe6\x81\xb6\xe9\xad\x94\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x80\xe5\xae\x88\xe6\xb7\xb1\xe6\xb8\x8a\xef\xbc\x8c\xe7\x8b\x82\xe9\x87\x8e\xe7\x9a\x84\xe5\x85\xbd\xe7\xbe\xa4\xe5\xad\xa6\xe4\xbc\x9a\xe4\xba\x86\xe8\x87\xaa\xe6\x88\x91\xe6\x94\xb6\xe6\x95\x9b\xef\xbc\x8c\xe5\xb0\xb1\xe8\xbf\x9e\xe5\x9c\xa3\xe6\xae\xbf\xe7\x9a\x84\xe7\xa5\x9e\xe7\xa5\x87\xe4\xbb\xac\xe4\xb9\x9f\xe4\xb8\x8d\xe6\x95\xa2\xe7\x9b\xb4\xe6\x8e\xa0\xe9\x94\x8b\xe8\x8a\x92\xe3\x80\x82\xe4\xbd\x86\xe8\x90\xa8\xe5\xb0\xbc\xe5\xb9\xb6\xe6\xb2\xa1\xe6\x9c\x89\xe8\xa2\xab\xe8\x87\xaa\xe5\xb7\xb1\xe7\x9a\x84\xe4\xbc\x9f\xe5\xa4\xa7\xe5\x8a\x9f\xe7\xbb\xa9\xe5\x86\xb2\xe6\x98\x8f\xe5\xa4\xb4\xe8\x84\x91\xef\xbc\x8c\xe4\xbb\x96\xe6\x97\xb6\xe5\x88\xbb\xe4\xbf\x9d\xe6\x8c\x81\xe7\x9d\x80\xe8\xad\xa6\xe6\x83\x95\xef\xbc\x8c\xe5\x8f\xaa\xe8\xa6\x81\xe6\x88\x98\xe6\x96\x97\xe7\x9a\x84\xe5\x8f\xb7\xe8\xa7\x92\xe5\x90\xb9\xe5\x93\x8d\xef\xbc\x8c\xe4\xbb\x96\xe5\xb0\xb1\xe4\xbc\x9a\xe5\x86\x8d\xe6\xac\xa1\xe6\x8c\xba\xe5\x89\x91\xe8\x80\x8c\xe4\xb8\x8a\xe3\x80\x82\\n\\n\xe2\x80\x9c\xe5\x90\xbe\xe6\x89\xa7\xe5\x90\xbe\xe5\x89\x91\xef\xbc\x8c\xe6\x96\xa9\xe5\xb0\xbd\xe5\xa5\xb8\xe9\x82\xaa\xef\xbc\x81\xe2\x80\x9d\r\n0588A320CABA3789_## = \xe7\x81\xb5\xe7\x81\xb5\xe4\xb8\xba\xe4\xbb\x80\xe4\xb9\x88\xe6\x98\xaf\xe7\x88\x86\xe7\x82\xb8\xe5\xa4\xb4\xef\xbc\x9f\r\n0590EDDF3CC30F2A_## = \xe5\xb9\xb4\xe8\xbd\xbb\xe4\xba\xba\xef\xbc\x8c\xe4\xbd\xa0\xe7\x9a\x84\xe8\xaf\x9a\xe6\x84\x8f\xe6\x89\x93\xe5\x8a\xa8\xe4\xba\x86\xe6\x88\x91\\n\xe5\xa6\x82\xe6\x9e\x9c\xe4\xbd\xa0\xe4\xb8\x8d\xe4\xbb\x8b\xe6\x84\x8f\xe5\x92\x8c\xe6\x88\x91\xe4\xb8\x80\xe8\xb5\xb7\\n\xe8\xa1\x8c\xe4\xbe\xa0\xe6\xad\xa3\xe4\xb9\x89\xef\xbc\x8c\xe9\x99\xa4\xe6\x81\xb6\xe6\x89\xac\xe5\x96\x84\\n\xe5\x88\x9a\xe5\xa5\xbd\xe6\x88\x91\xe7\x8e\xb0\xe5\x9c\xa8\xe7\xbc\xba\xe4\xb8\x80\xe4\xb8\xaa\xe5\x8a\xa9\xe7\x90\x86\\n\xe4\xbb\x8a\xe5\x90\x8e\xe6\x88\x91\xe4\xbb\xac\xe5\xb0\xb1\xe6\x98\xaf\xe6\x97\xa0\xe6\x95\x8c\xe7\x9a\x84\xe9\x9c\xb9\xe9\x9b\xb3\xe7\xbb\x84\xe5\x90\x88\xef\xbc\x81\r\n0592D198A67E021F_## = <color=#ffd200>\xe8\xa7\xa3\xe9\x94\x81\xe6\x9d\xa1\xe4\xbb\xb6</color>\xef\xbc\x9a\xe4\xb8\x8e<color=#ffd200>{0}</color>\xe8\xbe\xbe\xe5\x88\xb0<color=#ffd200>\xe7\xbe\x81\xe7\xbb\x8a\xe9\x98\xb6\xe6\xae\xb52 \xe7\x9b\xb8\xe8\xaf\x86</color>\r\n05A181D7672725DC_## = \xe6\xb4\x9b\xe9\x87\x8c\xe6\x98\x82\r\n05A9BBD41D0A9179_## = \xe2\x80\x9c\xe4\xb9\x9d\xe5\xa4\xa9\xe4\xb9\x8b\xe4\xb8\x8a\xef\xbc\x8c\xe7\xa5\x9e\xe5\xba\xa7\xe4\xb9\x8b\xe6\x97\x81\xef\xbc\x8c\xe5\x85\xad\xe7\xbf\xbc\xe8\x88\x9e\xe5\x8a\xa8\xef\xbc\x8c\xe4\xbb\xa5\xe7\xbf\xb1\xe4\xbb\xa5\xe7\xbf\x94\xe3\x80\x82\xe2\x80\x9d\\n\\n\xe8\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x97\x8b\xe8\xbd\xac"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="materialParentActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyScaling" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableLayer"head145.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x15\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00:\x00\x00\x00\x0f\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x16\xf6\x99\x00\x0c\x00\x00\x00vp10042.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00X\x00\x00\x00\x0f\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x17\xf6\x99\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x18\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x01\x00\x00\x00\x00O\x00\x00\x00\x0f\x00\x00\x00\n\x00\x00\x00\xab\x9e\x98\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x19\xf6\x99\x00\x12\x00\x00\x00return_js_new.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1a\xf6\x99\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1b\xf6\x99\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1c\xf6\x99\x00\x0c\x00\x00\x00vp90007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1d\xf6\x99\x00\x0c\x00\x00\x00vp10106.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00>\x00\x00\x00\x0f\x00\x00\x00\x0f\x00\x00\x00\xac\x9e\x98\x00\x0c\x00\x00\x00vp90005.png\x00\x1e\xf6\x99\x00\x10\x00\x00\x00valorpass03.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1f\xf6\x99\x00\x0c\x00\x00\x00vp12007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00 \xf6\x99\x00\x0c\x00\x00\x00vp11029.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00!\xf6\x99\x00\r\x00\x00\x00vp120100.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00Q\x00\x00\x00\x0f\x00\x00\x00\x14\x00\x00\x00\xad\x9e\x98\x00\x0c\x00\x00\x00vp90007.png\x00#\xf6\x99\x00\x14\x00\x00\x00level20skin_big.png\x00\x01\x00\x00\x00\x00\x10\x00\x00\x00level20skin.png\x00;\x00\x00\x00\x0f\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\xe7\x8e\x84\xe7\xad\x96\xe8\xa2\xab\xe5\x8a\xa8\x00\x16\x00\x00\x00\xe5\x87\xbb\xe6\x9d\x80\xe6\x88\x96\xe5\x8a\xa9\xe6\x94\xbb\xe8\x8b\xb1\xe9\x9b\x84\x007\x00\x00\x00Prefab_Characters/Prefab_Hero/195_BaiLiXuanCe/skill/P2\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xbe\x00\x00\x00(<\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x19\x00\x00\x00\xe5\x8f\xb6\xe5\xa8\x9c\xe5\xad\xa6\xe4\xb9\xa0\xe5\xa4\xa7\xe6\x8b\x9b\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x004\x00\x00\x00Prefab_Characters/Prefab_Hero/154_HuaMuLan/skill/P1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xce\x00\x00\x00%\xd5\x01\x00\xd0\x07\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00[EX]\xe7\x99\xbd\xe8\xb5\xb7\xe8\xa2\xab\xe5\x8a\xa8\x00\x13\x00\x00\x00\xe5\x8f\x97\xe5\x87\xbb\xe6\x9c\x89\xe5\x87\xa0\xe7\x8e\x87\xe8\xbd\xac\x00:\x00\x00\x00Prefab_Characters/Prefab_Hero/120_BaiQi/skill/extend/exP1\x00\x02\x00\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\xbf\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\xe7\xba\xb3\xe5\x85\x8b\xe7\xbd\x97\xe6\x96\xaf\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/150_HanXin/skill/extend/exP2\x00\x08\x00\x00\x00\xa0\x0f\x00\x00\x14\x00\x00\x00\xf4\x01\x00\x00\x8c\x06\x17\x00\x98:\x00\x00\x0c\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x12\x01\x00\x00>A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x00\x00\x00\xef\xbc\x8810v10\xef\xbc\x89\xe7\x8c\xb4\xe5\xad\x90\xe6\xaf\x8f\xe6\xac\xa1\xe9\x87\x8a\xe6\x94\xbe\xe6\x8a\x80\xe8\x83\xbd\xe7\x9a\x84\xe6\x97\xb6\xe5\x80\x99\xe5\xb0\x86\xe4\xbc\x9a\xe8\x8e\xb7\xe5\xbe\x97\xe4\xb8\x80\xe4\xb8\xaa\xe6\x8a\xa4\xe7\x9b\xbe\xef\xbc\x8c\xe5\x8f\xaf\xe5\x8f\xa0\xe5\x8a\xa05\xe6\xac\xa1\x00\x12\x00\x00\x00\xe6\x82\x9f\xe7\xa9\xba[EX]\xe8\xa2\xab\xe5\x8a\xa81\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/167_WuKong/skill/extend/exP1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00e="" r="0.517" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CameraShakeDuration" time="2.000" length="2.000" isDuration="true">\n\t\t\t\t<bool name="useMainCamera" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="shakeRange" x="0.500" y="0.500" z="0.500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_self" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_target" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_enemy" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_allies" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useAccumOffset" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cosDecay" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="cosDecayFactor" v\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00M\x00\x00\x00\x1f\xb2\x01\x00%\x00\x00\x00Play_SunShangXiang_VO_TiaoXin_Skin13\x00i+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00J\x00\x00\x00)\xb2\x01\x00"\x00\x00\x00Play_sunshangxiang_tiaoxin_Skin14\x00j+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00\x85\xb5\x01\x00\x18\x00\x00\x00Play_GongShuBan_TiaoXin\x00\xc0+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\x99\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin2\x00\xc2+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xb7\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin5\x00\xc5+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xc1\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin6\x00\xc6+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00m\xb9\x01\x00\x18\x00\x00\x00Play_ZhuangZhou_TiaoXin\x00$,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00=\x00\x00\x00U\xbd\x01\x00\x15\x00\x00\x00Play_LiuShan_TiaoXin\x00\x88,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00?\x00\x00\x00=\xc1\x01\x00\x17\x00\x00\x00Play_GaoJianLi_TiaoXin\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00Q\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin2\x00\xee,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00[\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin3\x00\xef,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00<\x00\x00\x00%\xc5\x01\x00\x14\x00\x00\x00Play_JingKe_TiaoXin\x00P-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00M\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin4\x00T-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00W\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin5\x00U-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00C\x00\x00\x00o\xc6\x01\x00\x1b\x00\x00\x00Plname="bInverse" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupActorType" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupRadius" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterInTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="teamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="diffTeamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="monsterTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="soldierTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetBehaviourModeTick0" eventType="SetBehaviourModeTick" guid="53e062a5-ebd1-4b49-83fe-4b2026e48ae4" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.283" exe\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bChargingEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="chargingDistance" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="distance" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bResetMoveDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="minSpeed" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="12000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groundOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreHeight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="acceleration"v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/skill1_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_organ/tower/skill1_bullet_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/makeDamage2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00*\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc3\x00\x00\x00\x02\x00\x00\x00r\x00\x00\x00\x06\x00\x00\x00v1`\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String2\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/A1E2\x04\x00\x00\x00\x04\x00er/New_BlueTower/skill/New_BlueTower_makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00L\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe5\x00\x00\x00\x02\x00\x00\x00\x94\x00\x00\x00\x06\x00\x00\x00v1\x82\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringT\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_BlueTower/skill/New_BlueTower_A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75001\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xad\x03\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x1d\x03\x00\x00\x03\x00\x00\x00\x07\x01\x00\x01\x00\x00\x00\x00\x00\r\x00\x00\x00\xe5\xa4\xa7\xe7\xa5\x9e\xe5\x85\xb3\xe5\x8d\xa1\x00\x15\x00\x00\x00Tutorial_BGod_Design\x00\x17\x00\x00\x00ART_5V5_01_High_Artist\x00\x0c\x00\x00\x00PVP_5V5_Nav\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00~\x02\x00\x00z\x02\x00\x00{\x02\x00\x00\x7f\x02\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00t\x02\x00\x00w\x02\x00\x00x\x02\x00\x00\x80\x02\x00\x00\x81\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x02\x00\x00\x007\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x08\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x00\x00pvp_5_small\x00\r\x00\x00\x00pvp_5_detail\x00\n\x00\x00\x00pvp_5_big\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xdd\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x02\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00Play_PVP_Music\x00\x0f\x00\x00\x00Stop_PVP_Music\x00\x01\x00\x00\x00\x00\n\x00\x00\x00Music_PVP\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90_\x01\x00\x95_\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x02\x00\x00e\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x10\x00\x00\x00\xe5\x8f\xac\xe5\x94\xa4\xe5\xb8\x88\xe6\x88\x98\xe5\x9c\xba\x00\x15\x00\x00\x00PVE_1_1_logic_Design\x00\x18\x00\x00\x00ART_PJGC_02_High_Artist\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00Img_Story\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x03\x00\x00\x00\xf3\x03\x00\x00\xf4\x03\x00\x00\xf5\x03\x00\x00Q\xc3\x00\x00\x00\x00\x00\x00f\x00\x00\x00\x05M\x04\x00\x00\x05\xb1\x04\x00\x00\x05\x15\x05\x00\x00\x05{\x05\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\t\x00\x00\x00\r\x00\x00\x00F\x05\x00\x00\xe7\x06\x00\x00\x88\x08\x00\x00\x9e\t\x00\x00\x84\x03\x00\x00\x9a\x04\x00\x00\xb0\x05\x00\x00i\x06\x00\x00\x00\x08\x00\x00\x00PVE_1_3\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa*\x00\x00\x00\x00\x00\x00\xc9\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00o\x00\x00\x00y\x00\x00\x00\x83\x00\x00\x00\x8d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 N\x00\x00\x00\x00\x00\x00\x0ee\x00\x01\x00\x00\x00\x00E\x00\x00\x00f\x82\x17\x00\x19\x00\x00\x00Play_Yena_VOX_Come_Skin7\x00/<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00@\x00\x00\x00\xba\xa6\x17\x00\x14\x00\x00\x00Play_LuoBin_VO_Come\x00\x8c<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00D\x00\x00\x00\xca\xcd\x17\x00\x18\x00\x00\x00Play_ZhangLiang_VO_Come\x00\xf0<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00\xf6\xce\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin3\x00\xf3<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00Z\xcf\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin4\x00\xf4<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00A\x00\x00\x00\xda\xf4\x17\x00\x15\x00\x00\x00Play_BuZhiHuoWu_Show\x00T=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\x06\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin3\x00W=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00j\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin4\x00X=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\xce\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin5\x00Y=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x002\xf7\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin6\x00Z=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00)\x00\x00\x00\xea\x1b\x18\x00\x01\x00\x00\x00\x00\xb8=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00)\x00\x00\x00\nj\x18\x00\x01\x00\x00\x00\x00\x80>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00*\xb8\x18\x00\x16\x00\x00\x00Play_Nakelulu_VO_Come\x00H?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00V\xb9\x18\x00\x1c\x00\x00\x00Play_Nakelulu_VO_Come_Skin3\x00K?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00:\xdf\x18\x00\x1c\x00\x00\x00Play_163_JuYouJing_VOX_Come\x00\xac?\x00\x01\x00\x00\x00\x00\x00?\x00\x00\x00Prefab_Skill_Effects/Level_Effects/AutoChess_Effects/ChessDrop\x00\x00\x00\x80?\x01\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00MSES\x07\x00\x00\x00\x17\x00\x00\x00\x0f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005d388e873657b33c203ea1a6adbbd555\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x001131\x00\x02\x00\x00\x00P\x00\x13\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x001132\x00\x02\x00\x00\x00B\x00\x12\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00901\x00\x02\x00\x00\x00C\x00\x12\x00\x00\x00\x04\x00\x00\x00\x04\x00\x00\x00902\x00\x02\x00\x00\x00D\x00\x13\x00\x00\x00\x05\x00\x00\x00\x05\x00\x00\x001130\x00\x02\x00\x00\x00E\x00\x13\x00\x00\x00\x06\x00\x00\x00\x05\x00\x00\x001133\x00\x02\x00\x00\x00F\x00\x13\x00\x00\x00\x07\x00\x00\x00\x05\x00\x00\x001134\x00\x02\x00\x00\x00G\x00\x13\x00\x00\x00\x08\x00\x00\x00\x05\x00\x00\x001135\x00\x02\x00\x00\x00H\x00\x13\x00\x00\x00\t\x00\x00\x00\x05\x00\x00\x001136\x00\x02\x00\x00\x00I\x00\x13\x00\x00\x00\n\x00\x00\x00\x05\x00\x00\x001137\x00\x02\x00\x00\x00J\x00\x13\x00\x00\x00\x0b\x00\x00\x00\x05\x00\x00\x001138\x00\x02\x00\x00\x00K\x00\x13\x00\x00\x00\x0c\x00\x00\x00\x05\x00\x00\x001139\x00\x02\x00\x00\x00L\x00\x13\x00\x00\x00\r\x00\x00\x00\x05\x00\x00\x001180\x00\x02\x00\x00\x00M\x00\x13\x00\x00\x00\x0e\x00\x00\x00\x05\x00\x00\x001181\x00\x02\x00\x00\x00N\x00\x13\x00\x00\x00\x0f\x00\x00\x00\x05\x00\x00\x001183\x00\x02\x00\x00\x00O\x00MSES\x07\x00\x00\x00\x82\x01\x00\x00a\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e7c2b766e9bca08f64db4f0b283f3ce4\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xd6\x00\x00\x00i\x00\x00\x00\x14\x00\x00\x0096C81CC5CA834D6C_##\x00\x1f\x00\x00\x00WrapperAI/Hero/HeroAutoChessAI\x00\xa0(\x00\x00\x00\x00\x00\x00LO\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00\x02\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00$\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Born\x00\x01\x00\x00\x00\x00)\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Dead_Born\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x00\x00\x00j\x00\x00\x00\x14\x00\x00\x000D17FEB38CC06\x00\x00\x00\x04\x00\x00\x00&\x01\x00\x00\x12\x00\x00\x00iCollisionSize&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00x9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V500\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00z9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/542_Tachi/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/542_Tachi/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xab%\xb5\xdc\x86\x1c\x00\x00\x86\x1c\x00\x00/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81^\x00\x00\x00Prefab_Hero/542_Tachi/542_Tachi_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xdb\x00\x00\x001\x1d\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00121_MiYue/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00121_MiYue/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00121_MiYue/skill/AutoChess/PK\x03\x04RefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAlwaysLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="b1stTickParentRot" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHideWhenDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreWhenHideModel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUse3DUICamerang name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRefreshVision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidTargetOutOfNavmeshConvexHull" va\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x06\x05\x00\x00\x04\x00\x00\x00\x1e\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb7\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00F\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdf\x00\x00\x00\x02\x00\x00\x00\x8e\x00\x00\x00\x06\x00\x00\x00v1|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00M\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe6\x00\x00\x00\x02\x00\x00\x00\x95\x00\x00\x00\x06\x00\x00\x00v1\x83\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringU\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack02_spell01\x04\x00\x00P\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x004EEC4F2E66D84324_##\x00\x14\x00\x00\x0022CA5E1185A20996_##\x00\n\x00\x00\x0011084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa2\x00\x00\x00\\R\x00\x00\x02\x00\x01\x01=\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/kill/Kill_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x009C5DF28AAE7D3EE2_##\x00\x14\x00\x00\x00D24D8A620C89E63A_##\x00\n\x00\x00\x0021084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa6\x00\x00\x00ly\x00\x00\x03\x00\x01\x01A\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00849FC2788990326B_##\x00\x14\x00\x00\x00E94BDB26D3AF7FEB_##\x00\n\x00\x00\x0031084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa5\x00\x00\x00M+\x00\x00\x01\x00\x01\x01@\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/returncity/return_5V5_01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00ACA13FE146E55BC7_##\x00\x14\x00\x00\x00F3CFA939C7E48289_##\x00\n\x00\x00\x0011085.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc9\x00\x00\x00*\xa0\x00\x00\x04\x00\x01\x011\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_houyi_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x009DF7DA730FC32408_##\x00\x14\x00\x00\x00559A118E1D79C256_##\x00\n\x00\x00\x0041002.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc7\x00\x00\x00+\xa0\x00\x00\x04\x00\x01\x01/\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_jin_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x0084D3846A3B38B40D_##\x00\x14\x00\x00\x00D3B4AFBD692854AB_##\x00\n\x00\x00\x0041003.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc8\x00\x00\x00,\xa0\x00\x00\x04\x00\x01\x010\x00\x00\x00Prefngle name="randRotEnd" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="7d755f67-9943-4d08-b439-ce9215f3a028" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.417" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnBulletTick" time="0.200" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetPosActorId" objectName="None" id="-1" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="referenceObjectId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="ActionName" value="prefab_characters/prefab_hero/190_zhugeliang/skill/AutoChess/aca1b1" refvalue="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpecialBuffEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bActionCtrlObjs" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleTeamNotSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="syncAnimationName" value="" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="MoveBulletDuration0" eventType="MoveBulletDuration" guid="a4b4420f-87ae-4a8f-8c74-f5b800394aec" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.367" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="MoveBulletDuration" time="0.000" length="0.533" isDpeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50002\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50000\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xe4\x01\x00\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00L\x01\x00\x00\x01\x00\x00\x00D\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdd\x00\x00\x00\x02\x00\x00\x00\x8c\x00\x00\x00\x06\x00\x00\x00v1z\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/Common_Effects/EF_PVP_M_11DefenseTower_Blue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00)\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x8d\x02\x00\x00\x02\x00\x00\x00B\x01\x00\x00t name="\xe5\xa2\x9e\xe5\x8a\xa0\xe9\x87\x91\xe9\x92\xb1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\x8b\xb1\xe9\x9b\x84\xe7\x94\x9f\xe5\x91\xbd\xe6\x97\xb6\xe9\x95\xbf"/>\n\t\t\t\t\t<uint name="\xe7\xa6\xbb\xe5\xbc\x80\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85\xe4\xb8\x80\xe5\xae\x9a\xe8\x8c\x83\xe5\x9b\xb4\xe5\x90\x8e\xe6\xb8\x85\xe9\x99\xa4BUFF"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90"/>\n\t\t\t\t\t<uint name="\xe9\x99\xa4\xe7\x9b\xae\xe6\xa0\x87\xe5\xa4\x96\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe9\x80\x9f\xe6\x8a\xb5\xe6\x8a\x97"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa3\xe9\x99\xa4\xe5\x87\x8f\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\xad\xbb\xe4\xba\xa1"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe6\xb6\x88\xe8\x80\x97\xe5\x89\x8a\xe5\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\xb6\xb3\xe7\x90\x83\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe5\xa5\x89\xe7\x8c\xae"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe8\xa7\x92\xe8\x89\xb2\xe9\x87\x8d\xe7\x94\x9f"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe8\x8e\xb7\xe5\x8f\x96\xe5\x89\x8a\xe5\x87\x8f\xe6\xaf\x94\xe4\xbe\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5\xe9\x98\xb2\xe5\xbe\xa1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe4\xba\x92\xe7\x9b\xb8\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xb8\xbb\xe4\xba\xba\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe5\x8c\x96\xe7\xbb\x99\xe5\xae\xa0\xe7\x89\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x81\x90\xe6\x83\xa7\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe5\x8d\x95\xe6\xac\xa1\xe4\xbc\xa4\xe5\xae\xb3\xe4\xb8\x8a\xe4\xb8\x8b\xe9\x99\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8a\x80\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\xad"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe8\x80\x97\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc\xe6\x8a\xb5\xe6\x8c\xa1\xe4\xbc\xa4\xe5refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTargetBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTotalHitCount" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEdgeCheck" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bExtraBuff" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_1" value="505100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_2" value="505120" refPSetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetAttackDirDuration" time="0.000" length="0.050" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration0" eventType="ForbidAbilityDuration" guid="70d891be-ca4c-4c49-af6f-53ed54d35f4b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.283" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.200" isD name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x80\x92\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe7\x90\x83\xe6\xa7\xbd\xe4\xbd\x8d"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xb9\xe6\x8d\xae\xe6\x8a\xa4\xe7\x94\xb2\xe5\x80\xbc\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xbc\xe6\x8c\xa1\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\xa4\xa7\xe8\xa7\x86\xe9\x87\x8e\xe5\x8d\x8a\xe5\xbe\x84"/>\n\t\t\t\t\t<uint name="\xe5\x8d\x95\xe4\xb8\xaa\xe6\x8a\x80\xe8\x83\xbd\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\xbc\xb9"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe5\xa4\x8d\xe6\xb4\xbb\xe6\x97\xb6\xe9\x97\xb4"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\xa7\x92\xe8\x89\xb2\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\xa7\xbd\xe4\xbd\x8d\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe9\x95\xbf\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe6\x8d\xa2"/>\n\t\t\t\t\t<uint name="\xe7\xb1\xbb\xe5\x9e\x8b\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xae\xad\xe8\xaf\xab\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe9\x94\x90\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\x87\xbb\xe6\x99\xae\xe6\x94\xbb\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe5\x8f\x97\xe5\x88\xb0\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe9\x80\xa0\xe6\x88\x90\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x83\x8c\xe5\x90\x8e\xe6\x94\xbb\xe5\x87\xbb\xe6\x9a\xb4\xe5\x87\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87\xe8\xbd\xac\xe5\x8c\x96\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3 name="excuteMoveCmd" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="immediaRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayMSES\x07\x00\x00\x00\x08\x00\x00\x00\x10\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000ed9c5e8c7fd9b42e102b09260202589\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00`\xea\x00\x00\x04\x00\x00\x00a\xea\x00\x00\x04\x00\x00\x00b\xea\x00\x00\x04\x00\x00\x00c\xea\x00\x00\x04\x00\x00\x00d\xea\x00\x00\x04\x00\x00\x00e\xea\x00\x00\x04\x00\x00\x00f\xea\x00\x00\x04\x00\x00\x00g\xea\x00\x00\x04\x00\x00\x00h\xea\x00\x00\x04\x00\x00\x00i\xea\x00\x00\x04\x00\x00\x00j\xea\x00\x00\x04\x00\x00\x00k\xea\x00\x00\x04\x00\x00\x00l\xea\x00\x00\x04\x00\x00\x00m\xea\x00\x00\x04\x00\x00\x00n\xea\x00\x00\x04\x00\x00\x00o\xea\x00\x00MSES\x07\x00\x00\x00\xb6\x00\x00\x00\x00\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0024e234988d548d1822de209cfbd17add\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00|\x01\x00\x00\xe9\x03\x00\x00\x05\x00\x00\x00Body\x00\x05\x00\x00\x00Hair\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_512.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_512_Mask.bytes\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_256.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_256_Mask.bytes\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00x\x01\x00\x00\xea\x03\x00\x00\x05\x00\x00\x00Body\x00\x01\x00\x00\x00\x00O\x00\x00\x00ChParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSpecifiedDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="specifiedDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReachDestStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bStopOnNavEdge" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDelayLeave" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="randomRotateRange" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepRelateDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOptimizeLanding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontFallInWall" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration1" eventType="HitTriggerDuration" guid="ed80eb7a-cbd8-4b36-a5da-860e3ab6f453" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.383" exeProSmall" type="int" value="5000" />\r\n    <par name="c_HideContinueSelfHP_ConSmall" type="int" value="7000" />\r\n  </pars>\r\n  <node class="SelectorLoop" version="1" id="0">\r\n    <node class="WithPrecondition" version="1" id="40">\r\n      <node class="Action" version="1" id="42">\r\n        <property Method="Self.NucleusDrive::Logic::ActorBaseAgent::IsDeadState()" />\r\n        <property PreconditionFailResult="BT_FAILURE" />\r\n        <property ResultOption="BT_INVALID" />\r\n      </node>\r\n      <node class="Sequence" version="1" id="51">\r\n        <node class="Action" version="1" id="25">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SetCurrCombatDecision(Idle,32)" />\r\n          <property PreconditionFailResult="BT_FAILURE" />\r\n          <property ResultOption="BT_INVALID" />\r\n        </node>\r\n        <node class="Action" version="1" id="41">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SwitchMicroTree(&quot;WrapperAI/Hierarchical/MicroAIs/HeroMicroIdelAI&quot;,true)" />\r\n="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceClearSkillIndicator" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="a74d46ba-4213-46ba-a7ec-e1f30bd87c8a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.917" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.400" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReturnCacheWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill1"!\x00E/\x07\xb9T\x0e\x00\x00T\x0e\x00\x00\x1d\x00\x00\x00156_ZhangLiang/skill/A4B1.xml\xef\xbb\xbf<?xml version="1.0" encoding="utf-8"?>\r\n<Project>\r\n  <TemplateObjectList>\r\n    <TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" />\r\n    <TemplateObject objectName="target" id="1" isTemp="false" />\r\n    <TemplateObject objectName="bullet" id="2" isTemp="true" />\r\n  </TemplateObjectList>\r\n  <RefParamList>\r\n    <uint name="156a4b1" value="0" refParamName="" useRefParam="false" />\r\n  </RefParamList>\r\n  <Action tag="" length="5.000" loop="false">\r\n    <Track trackName="SpawnLiteObjDuration0" eventType="SpawnLiteObjDuration" guid="a108b9de-b380-464d-ad3f-97838128e929" enabled="true" refParamName="" useRefParam="false" r="0.417" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="SpawnLiteObjDuration" time="0.000" length="3.000" isDuration="true">\r\n        <String name="OutputLiteBulletName" value="156a4b1" refParamName="" useRefParam="false" />\r\n        <uint name="ConfigID" valisDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x80\xe8\x83\xbdCD"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe7.String\x0f\x00\x00\x00\x05\x00\x00\x00VSpell3\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\t\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xa2\x00\x00\x00\x02\x00\x00\x00Q\x00\x00\x00\x06\x00\x00\x00v1?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x11\x00\x00\x00\x05\x00\x00\x00VSpell3_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\x1c\x00\x00\x00\xe0\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0055da304ff85c361e25965639354f5378\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00%w\x00\x00rRepeatedly" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="overrideCDValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="triggerRatio" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xa0\x04\xec\x038=\x00\x008=\x00\x00\x1a\x00\x00\x00107_Zhaoyun/skill/A1E1.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="0.500" loop="false">\n\t\t<Track trackName="FilterTargetType6" eventType="FilterTargetType" guid="20f64bb4-0d0e-40ed-91b4-7ee34475407e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.083" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="FilterTargetType" timetem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/M1A2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00:\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x82\x00\x00\x00\x06\x00\x00\x00v1p\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/PassiveResource/JungleHeal\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00;\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x83\x00\x00\x00\x06\x00\x00\x00v1q\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/PassiveResource/JungleHealB1\x04\x00\x00\x00\x04\x00cts/hero_skill_effects/199_li/li_attack01_spll01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe0\x00\x00\x00\x02\x00\x00\x00\x8f\x00\x00\x00\x06\x00\x00\x00v1}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/Li_attack_spell02_trail\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00B\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdb\x00\x00\x00\x02\x00\x00\x00\x8a\x00\x00\x00\x06\x00\x00\x00v1x\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03b\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xda\x00\x00\x00\x02\x00\x00\x00\x89\x00\x00\x00\x06\x00\x00\x00v1w\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringI\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03\x04\x00\x00\x00\x04\x00em.StringN\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/999_ChessPlayer/99940_ChessPlayer_Show2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00~\x01\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\x1b\x01\x00\x00\x02\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00\xb3\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00W\x00\x00\x00\x01\x00\x00\x00O\x00\x00\x00\t\x00\x00\x00Scale:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.3\x04\x00\x00\x00\x04\x00\x00\x00i\x00\x00\x00!\x00\x00\x00bShadowCameraFollowLobbyActor<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x19\x00\x00\x00runAnimationBaseSpeed;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\r\x00\x00\x00\x05\x00\x00\x00V0.86\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V3000\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0e\x00\x00\x00LobbyScale8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00alue="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID" value="11601" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseCombo" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID1Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkillLevel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="11600" ref\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00(#\x00\x00L\x1d\x00\x00p\x17\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x02\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x10\'\x00\x00c\x00\x00\x00X\x00\x00\x00\x08\x00\x00\x00\x03\x00\r\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\xb9\xb3\xe5\x88\x86\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x88\x13\x00\x00\x01\x03\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x10\'\x00\x00{\x00\x00\x00Y\x00\x00\x00\x08\x00\x00\x00\x04\x00%\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\x86\x85\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x02\x00\x02\x00\x10\'\x00\x00p\x17\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00p\x17\x00\x00\x00\x10\'\x00\x00x\x00\x00\x00Z\x00\x00\x00\x08\x00\x00\x00\x05\x00"\x00\x00\x00\xe9\x98\xb5\xe8\x90\xa5\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x8a\xa9\xe6\x94\xbb\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00Prefab_Hero/510_Liliana/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xe9a\x8a\x18W5\x00\x00W5\x00\x003\x00\x00\x00Prefab_Hero/510_Liliana/510_Liliana_actorinfo.bytesW5\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x035\x00\x00\x0e\x00\x00\x00Y\x00\x00\x00\r\x00\x00\x00ActorName@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x12\x00\x00\x00\x05\x00\x00\x00V\xe8\x8e\x89\xe8\x8e\x89\xe5\xae\x89\x04\x00\x00\x00\x04\x00\x00\x00\xeb\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa3\x01\x00\x00\x03\x00\x00\x00\x89\x00\x00\x00\x0b\x00\x00\x00Elementr\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/510_Liliana/5101_Liliana_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x89\x00\x00\x00Param="false"/>\n\t\t\t\t<int name="iDelayDisappearTime" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\xad\xbb\xe4\xba\xa1\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb6\xe4\xbb\x96\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe6\x88\x98\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe6\x96\x97\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe9\x9d\x9e\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bExcludeSpecialActor"TPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00J\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe3\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x06\x00\x00\x00v1\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/Prefab_Soldier/New_Truck/skill/monster_atk_bullet_noaoe\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00=\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x85\x00\x00\x00\x06\x00\x00\x00v1s\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringE\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00C\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdc\x00\x00\x00\x02\x00\x00\x00\x8b\x00\x00\x00\x06\x00\x00\x00v1y\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9a\x01\x00\x00\x0c\x00\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/common_effects/allhero_jiaxue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V4\x04\x00\x00\x00\x04\x00\x00\x00>\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x86\x00\x00\x00\x06\x00\x00\x00v1t\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringF\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/526_Summoner/5261_Summoner_LOD1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00<\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x84\x00\x00\x00\x06\x00\x00\x00v1r\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Birth1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe1\x00\x00\x00\x02\x00\x00\x00\x90\x00\x00\x00\x06\x00\x00\x00v1~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Summoner_pet_death\x04\x00\x00ram="false"/>\n\t\t\t\t<bool name="bFilterSameCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlySelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyHostHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRevive" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="attackType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x89\x80\xe6\x9c\x89\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x91\xe6\x88\x98\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x9c\xe7\xa8\x8b\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bSelectJob" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="jobType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="N/A"/>\n\t\t\t\t\t<uint name="\xe5\x9d\xa6\xe5\x85\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe5\xa3\xab"/>\n\t\t\t\t\t<uint name="\xe5\x88\xba\xe5\xae\xa2"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe5\xb8\x88"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x84\xe6\x89\x8b"/>\n\t\t\t\t\t<uint name="\xe8\xbe\x85\xe5\x8a\xa9"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterGrouped" val1_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x17\x00\x00\x00ArtLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa8\x01\x00\x00\x03\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow1\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow2\x04\x00\x00\x00\x04\x00\x00\x00\x88\x00\x00\x00\x0b\x00\x00\x00Elementq\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamerao\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Cam\x04\x00\x00\x00\x04\x00\x00\x00\x0e\x18\x00\x00\x0e\x00\x00\x00SkinPrefabG\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr2\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement[]\x04\x00\x00\x00\xb1\x17\x00\x00\x03\x00\x00\x00\xc2\x07\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00j\x07\x00\x00\x06\x00\x00\x00\xe9\x01\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x9d\x01\x00\x00\x03\x00\x00\x00\x87\x00\x00\x00\x0b\x00\x00\x00Elementp\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x000986.wem\x007\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00+\x00\x00\x00Sound/Android/Chinese(Taiwan)/97838123.wem\x008\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/987101814.wem\x008\x00\x00\x00\xe4\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/994406221.wem\x008\x00\x00\x00\xe5\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995073947.wem\x008\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995257090.wem\x00$\x00\x00\x00\xe7\x00\x00\x00\x04\x00\x00\x00\x18\x00\x00\x00AssetBundle/Show/BG/*.*\x00E\x00\x00\x00\xe8\x00\x00\x00\x01\x00\x00\x009\x00\x00\x00AssetBundle/Show/Hero/133_DiRenJie_show_base.assetbundle\x00A\x00\x00\x00\xe9\x00\x00\x00\x03\x00\x00\x005\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_DiRenJie_Show.bnk\x00+\x00\x00\x00\xea\x00\x00\x00\x05\x00\x00\x00\x1f\x00\x00\x00AssetBundle/Modules/Soccer/*.*\x00-\x00\x00\x00\xeb\x00\x00\x00\x05\x00\x00\x00!\x00\x00\x00AssetBundle/Modules/FiveCamp/*.*\x00/\x00\x00\x00\xec\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_Zhaoyun_SFX.bnk\x00>\x00\x00\x00\xed\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_Zhaoyun_VO.bnk\x00/\x00\x00\x00\xee\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_XiangYu_SFX.bnk\x00>\x00\x00\x00\xef\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_XiangYu_VO.bnk\x003\x00\x00\x00\xf0\x00\x00\x00\x03\x00\x00\x00\'\x00\x00\x00Sound/Android/Hero_WangZhaoJun_SFX.bnk\x00B\x00\x00\x00\xf1\x00\x00\x00\x03\x00\x00\x006\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_WangZhaoJun_VO.bnk\x00?\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x003\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_LiuShan_SFX.bnk\x00>\x00\x00\x00\xf3\x00\x00\x00\x03\x00\x00\x00useRefParam="false"/>\n\t\t\t\t<String name="endClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayEndClipName" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTriggerTick0" eventType="ChangeSkillTriggerTick" guid="7e6b69c3-4a8c-40e5-bbc7-971898233929" enabled="true" useRefParam="false" refParamName="" r="0.800" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ChangeSkillTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="effectTime" e="\xe4\xb8\x8d\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="interuptAutoAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="a66c0c5d-659b-4258-b6f7-6630f5046041" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.117" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="taMSES\x07\x00\x00\x00}\x00\x00\x00f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e0a70c7ddff5db1861c7359c802ff1eb\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00y\x00\x00\x00\x01\x00\x00\x00\x01\x01\x14\x00\x00\x00BB2CD71CABB8E0D8_##\x00=\x00\x00\x00UGUI/Particle/UI_MapCircle_effect/UI_MapCircle_effect_Yellow\x00\x14\x00\x00\x008574E33444BD2708_##\x00\x01\x00y\x00\x00\x00\x02\x00\x00\x00\x01\x01\x14\x00\x00\x00033F49AD5A74\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00K\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe4\x00\x00\x00\x02\x00\x00\x00\x93\x00\x00\x00\x06\x00\x00\x00v1\x81\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringS\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xab\x02\x00\x00\x02\x00\x00\x00Q\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xea\x00\x00\x00\x02\x00\x00\x00\x99\x00\x00\x00\x06\x00\x00\x00v1\x87\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringY\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/chusheng_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x01\x00\x00\x0b\x00\x00\x00uncInstant0" eventType="SkillFuncInstant" guid="8d09eb2f-50ed-4358-a741-27ca7e1a94dd" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.667" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillFuncInstant" time="0.000" isDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration12" eventType="ForbidAbilityDuration" guid="ae7adc4b-a73f-4229-a4f1-dd860c67f460" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.117" b="0tion" x="0" y="0" z="1500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHeroEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseIndicatorDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="targetdir" useRefParam="true"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" vaorceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetCollisionTick" time="0.180" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="type" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="BOX"/>\n\t\t\t\t\t<uint name="SPHERE"/>\n\t\t\t\t\t<uint name="CYLINDERSECTOR"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bIsBlockMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderLine" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockJungleMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="blockCampType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x95\x8c\xe5\xaf\xb9\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe8\x87\xaa\xe5\xb7\xb1\xe9\x98\xb5\xe8\x90\xa5"22C6_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00e2\x00\x00f2\x00\x00g2\x00\x00h2\x00\x00i2\x00\x00j2\x00\x00k2\x00\x00l2\x00\x00m2\x00\x00n2\x00\x00\xe88\x01\x00\x02\x00\x00\x00x\x05\x00\x00\x14\x05\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\x1e\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\xe2\x04\x00\x00x\x05\x00\x00\x14\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\x05\x00\x00\x00\x97\x04\x00\x00\x82\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00E7CA65090D658757_##\x00\x0e\x00\x00\x00GongBenWuZang\x00\x01\x14\x00\x00\x00C2F5E48F7D5C72F0_##\x00\x07\x00\x00\x00301300\x00L\x00\x00\x00Prefab_Characters/Prefab_Hero/130_GongBenWuZang/130_GongBenWuZang_actorinfo\x00\x01\x00\x00\x00\x01X\x1b\x00\x00\xd7\r\x00\x00=\x00\x00\x00\xaaG\x00\x00\xaa\x00\x00\x00\x00\x00\x00\x00\x89\x00\x00\x00P\x00\x00\x00\xd8\x0e\x00\x00\xc0\xc6-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00\xc0\xc6-\x00(\x17\x02\x00\x00\x00\x00\x00`[\x03\x00X\x0f\x02\x00\xd32\x00\x00\x00\x00\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xd22\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xdc2\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xe62\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x90_\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x06\x00\x00\x00\x08\x00\x00\x00\x06\x00\x00\x00\x02\x03\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x14\x00\x00\x004744E357C306D3C2_##\x00\x01\x11\x00\x00\x00\x19\x00\x00\x00WrapperAI/Hero/HeroLowAI\x00\x1c\x00\x00\x00WrapperAI/Hero/HeroSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmNormalAI\x00"\x00\x00\x00WrapperAI/Hero/HeroFiveCampSimple\x00\x02\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00BB3239B9CC0563BF_##\x00\x02\x00\x00\x00\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00200065368D0DBAAB_##\x00\x19\x00\x00\x00Play_bobao_gongbenwuzang\x00\x01\x00\x00\x002\x00\x00\x00Prefab_Characters/Prefab_Hero/commonresource/Born\x007\x00\x00\x00PrZ\xf9\xd8O\xb7F\x1bLuaS\x01\x19\x93\r\n\x1a\n\x04\x04\x08\x08xV\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(w@\x01<@Assets/Prefabs/Lua/AOV/MagicLab/MagicLabRewardItemView.lua\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x14\x00\x00\x00\x03\x00@\x00N@\x00\x00\x83\x80@\x00\x93\xc0@\x01\x04\x80\x80\x01C\x00A\x00\x8e@\x01\x00D\x80\x00\x01\x8c\x00\x00\x00\x07\x80\x00\x83\x8c@\x00\x00\x07\x80\x80\x83\x8c\x80\x00\x00\x07\x80\x00\x84\x8c\xc0\x00\x00\x07\x80\x80\x84\x8c\x00\x01\x00\x07\x80\x00\x85\x0b\x00\x00\x01\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06Class\x04\x17MagicLabRewardItemView\x04\x02N\x04\x0bCUILuaView\x04\x08require\x04\x19AOV.MagicLab.MagicLabSys\x04\x0edocumentation\x04\rOnViewInited\x04\x08Refresh\x04\nSetCDNPic\x04\nItemClick\x01\x00\x00\x00\x01\x00\x05\x00\x00\x00\x00\x06\x00\x00\x00\r\x00\x00\x00\x01\x00\x02\x17\x00\x00\x00\x0b\x00\x80\x00C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S@\xc1\x00\x07@\x00\x80C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc1\x00\x07@\x00\x83C@@\x00S@\xc2\x00\x07@\x00\x84C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc2\x00\x07@\x00\x85\x0b\x00\x80\x00\x0c\x00\x00\x00\x04\x0cListElement\x04\x03CS\x04\x07Assets\x04\x08Scripts\x04\x03UI\x04\x15CUIListElementScript\x04\x07CDNpic\x04\x10CDNPicComponent\x04\x08BoxText\x04\x06Text2\x04\x0bClickEvent\x04\x0fCUIEventScript\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x01\x00\x00\x00\x05self\x00\x00\x00\x00\x17\x00\x00\x00\x01\x00\x00\x00\x05_ENV\x00\x0f\x00\x00\x00\x17\x00\x00\x00\x01\x00\x05\r\x00\x00\x00\x07@@\x80S\x80@\x00\x8c\x00\x00\x00G\x80\x80\x81S\x00A\x00l@\xc1\x00\xc3\x80A\x00\x03\xc1A\x00\x13\x01B\x02\xc4\x00\x00\x01D\x80\x00\x00G\x80\xc2\x84\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06BoxID\x13\xff\xff\xff\xff\xff\xff\xff\xff\x04\x0bClickEvent\x04\x08onClick\x04\x0cListElement\x04\rGetComponent\x04\x07typeof\x04\x02N\x04\x0fCUIEventScript\x04\x08enabled\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x00\x00\x02\x04\x00\x00\x00\x05\x00\x00\x00,\x00@\x00\x04@\x00\x01\x0b\x00\x80\x00\x01\x00\x00\x00\x04\nItemClick\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05self\r\x00\x00\x00\x10\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x14\x00\x00\x00\x16\x00\x00\x00\x16\x00\x00\x00name="_TargetPos" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="6c8555eb-3d65-40dc-b96b-22085a7b349f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.MSES\x07\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f36f7a0cf63b751b43487af3ac37a561\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00HB\x00\x00\xc8B\x14\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0A\x00\x00HB\x14\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00 A\x00\x00\xf0A\x14\x00\x00\x00\x14\x00\x00\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0@\x00\x00 A\x14\x00\x00\x002\x00\x00\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\xa0@\x14\x00\x00\x00d\x00\x00\x00\xf4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x14\x00\x00\x00\xf4\x01\x00\x00\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x14\x00\x00\x00\xe8\x03\x00\x00\x88\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\xd7\xa3=\x14\x00\x00\x00\x88\x13\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xccL=MSES\x07\x00\x00\x00^\x00\x00\x00\x06\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ea39319bc554c025c5f107f401c732b8\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00L\x00\x00\x00e\x00\x00\x00\x14\x00\x00\x00C235D3F892E815B5_##\x00\x14\x00\x00\x006E67E299EE10381A_##\x00\n\x00\x00\x00touxiang1\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00f\x00\x00\x00\x14\x00\x00\x008BD1A0FD4DFCA919_##\x00\x14\x00\x00\x005696820E83B5B08F_##\x00\n\x00\x00\x00touxiang2\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00g\x00\x00\x00\x14\x00\x00\x007B989B6E5EDFA305_##\x00\x14\x00\x00\x00498F4E0296"" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDeadControlHero" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCurrentTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMoveDirection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Angle" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBigMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyMe" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="bulletID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCantAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType1" valu\x00\x00\x00\x04\x00\x00\x00\x91\x00\x00\x00\x0b\x00\x00\x00Elementz\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_LOD3\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x0b\x00\x00\x00Element{\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringM\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_Show1\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00]\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0f\x00\x00\x00SavedSkinId7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00CrossFadeTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.3\x04\x00\x00\x00\x04\x00\x00\x00#\x04\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\xc0\x03\x00\x00\x02\x00\x00\x00\xda\x01\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00~\x01\x00\x00\x02\x00\x00\x00)\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00I\x00\x00\x00\x05\x00\x00\x00x8\x00\x00\x00\x03 r="0.100" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack5" eventType="StopTrack" guid="b3cfc329-c442-4487-ab73-1d5ffcf3a8d7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.133" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="2" guid="d1939f1f-84aa-46f2-9322-abcc2231ad1a" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x120X\xbc\xa5S\x00\x00\xa5S\x00\x00#\x00\x00\x00196_Elsu/skill/AfterLastEvent="true">\n\t\t\t<Event eventName="HitTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="hitTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInheritRefParams" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="triggerId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bulletHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="victimId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="lastHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSkillCombineChoose" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="1841001" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" val\t<Vector3i name="offsetDir" x="0" y="0" z="0" refParamName="_TargetDir" useRefParam="true"/>\n\t\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="distance" value="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="18000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="gravity" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAdjustSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="1e0b1d40-f329-4718-b4d0-d5c0caaaa1e4" enabled="true" lod="0" useRefParam="false" refParamName="" r="1.000" g="0.233" b="me="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="9d243092-f160-4189-a9da-f132595032c9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.650" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="1.267" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="clipName" value="Atk1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontReplaceSameAnim" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="subLayer" .Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00I\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe2\x00\x00\x00\x02\x00\x00\x00\x91\x00\x00\x00\x06\x00\x00\x00v1\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acA1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00O\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x97\x00\x00\x00\x06\x00\x00\x00v1\x85\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringW\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acmakeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9b\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x10\x01\x00\x00\x01\x00\x00\x00\x08\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa1\x00\x00\x00\x02\x00\x00\x00P\x00\x00\x00\x06\x00\x00\x00v1>\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x10\x00\x00\x00\x05\x00\x00\x00V6710002\x04\x00\x00\x00\x04\x004_##\x00>\x00\x00\x00\x1e\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002B5B6A1F7A9007E5_##\x00?\x00\x00\x00$\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00EE2974C205C472E7_##\x00\x01\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002521BBD3EE0BDF80_##\x00<\x00\x00\x00\x06\x00\x00\x00\x01\x00\x00\x00\x01<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":68}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00BDB77D73EF3CDFB6_##\x00\x03\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00898A75C147D555B3_##\x00\x06\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00FA3AF0603BDD9365_##\x00\x07\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x0051ED5D030B64764D_##\x00\n\x00\x00\x00\t\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00C50583CB6167E4E5_##\x00\x0b\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd8\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x004721F4D35F33FCA5_##\x00\x0c\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x00<\x00\x00\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00HF\xa6,D\x0e\x00\x00D\x0e\x00\x00+\x00\x00\x00177_ChengJiSiHan/skill/AutoChess/acA1E3.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList/>\n\t<Action tag="" length="0.300" loop="false">\n\t\t<Track trackName="SkillFuncDuratio-9322-abcc2231ad1a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.833" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticle" time="0.000" length="1.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet1" id="3" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<uint name="RefLiteBulletID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/174_yuji/yuji_attack01_spell02" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="dontShowIfNoBindPoint" valtem.Int32]\x04\x00\x00\x00\xeb\x00\x00\x00\x02\x00\x00\x00\x9a\x00\x00\x00\x06\x00\x00\x00v1\x88\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringZ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huijidi_dead\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00S\x0e\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xbb\r\x00\x00\x0b\x00\x00\x00\x1f\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb8\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x06\x00\x00\x00v28\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0b\x00\x00\x00\x05\x00\x00\x00V10\x04\x00\x00\x00\x04\x00\x00\x00@\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd9\x00\x00\x00\x02\x00\x00\x00\x88\x00\x00\x00\x06\x00\x00\x00v1v\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/109_daji/daji_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V3\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneSkillSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplaceHPBarImmuneSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCallBoss" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidExtraBtnSlot1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="43618e12-f288-4877-9d44-4cb1ef89f0a2" enabled="true" useRefParam="false" refParamName="" r="0.467" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.333" isDur1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/536_Ninja/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/544_Painter/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xc5z\x03\xef/\x0c\x00\x00/\x0c\x00\x003\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81`\x00\x00\x00Prefab_Hero/544_Painter/544_Painter_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xe1\x00\x00\x00\xe0\x0c\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00Prefab_Hero/148_JiangZiYa/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00h-\x11\x99U\x1f\x00\x00U\x1f\x00\x007\x00\x00\x00Prefab_Hero/148_JiangZiYa/148_JiangZiYa_actorinfo.bytesU\x1f\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x01\x1f\x00\x00\x0f\x00\x00\x00]\x00\x00\x00\r\x00\x00\x00ActorNameD\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x16\x00\x00\x00\x05\x00\x00\x00V148_JiangZiYa\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xaf\x01\x00\x00\x03\x00\x00\x00\x8d\x00\x00\x00\x0b\x00\x00\x00Elementv\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplayWhenChangeMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTrailProtect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepChildScale" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/HeroStun\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x008\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x80\x00\x00\x00\x06\x00\x00\x00v1n\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String@\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x004\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcd\x00\x00\x00\x02\x00\x00\x00|\x00\x00\x00\x06\x00\x00\x00v1j\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xbc\x07\x00\x00\x0e\x00\x00\x00animationsw\x00\t\t<String name="SpecialActionName" value="prefab_characters/prefab_hero/115_gaojianli/skill/a1b2" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDeadRemove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmeExcute" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeEternal" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletTypeId" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletUpperLimit" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpawnBounceBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="bulletSkillType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\xbb\x98\xe8\xae\xa4\xe7\xb1\xbb\xe5\x9e\x8b_0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x81\xe8\xae\xb8\xe7\x89\xb9\xe6\xae\x8a\xe6\x89\x93\xe6\x96\xad_1"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDestroyedBySpecialBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTrigger\t\t\t\t<bool name="forbidFilterSkill4" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill5" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill6" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill7" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill8" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill10" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill11" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSummonerSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterMapSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterEquipActiveSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterActiveSame="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRealTimeSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOpenSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBlockObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkin" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRecordObjPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="recordTargeID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TrackObject name="trackId" id="-1" guid="00000000-0000-0000-0000-000000000000" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetCollisionTick0" eventType="SetCollisionTick" guid="dcd824ef-bb03-4fc8-bf5c-a64a29c3c0\t<int name="ExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Rotation" value="160" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="HeightGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="RotationGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</EMSES\x07\x00\x00\x00\x1c\x00\x00\x00\x0e\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009b0dbb76c4f9d3da6c78991155e5e1c2\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x05\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x07\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00\x02\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0b\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0c\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\r\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0e\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x91\xb0\x00\x00\x08\x00\x00\x00RargetSkillCombine_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_3" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBullet" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="BulletActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/extend/exs2b1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeImmeExcute" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTriggerObj" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceUseTriggerObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerMode" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBounceBullete"/>\n\t\t\t\t<int name="triggerInterval" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorInterval" value="30" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterFriend" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterMonter" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterChest" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEye" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMyself" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" \xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x85\xe9\x80\x9f\xe5\xa4\x8d\xe6\xb4\xbb"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe7\x90\x83\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\xa9\xb1\xe6\x95\xa3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x85\x8d\xe7\x96\xab\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe8\x8e\xb7\xe5\x8f\x96\xe8\xa7\x86\xe9\x87\x8e\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\xba\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9f\xa7\xe6\x80\xa7\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x86\xb7\xe5\x8d\xb4\xe7\xbc\xa9\xe5\x87\x8f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x97\xe6\x9a\xb4\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9d\xa1\xe4\xbb\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5RVO"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe6\x9d\xa1\xe4\xbb\xb6\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9b\xb4\xe6\x8d\xa2\xe8\xa1\x80\xe6\x9d\xa1\xe9\xa3\x8e\xe6\xa0\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\xbb\x8f\xe9\xaa\x8c\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xbb\x8f\xe9\xaa\x8c\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x97\xe6\x8e\xa7\xe9\xa2\x9d\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"<int name="level3Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level4Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level5Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level6Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOtherSkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillUseCacheTick0" eventType="SkillUseCacheTick" guid="53c33571-7838-484f-9f06-7b93d4bc28e0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.217" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillUseCacheTick" time="0.350" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="e8a22af8-4078-4313-893b-f729c0f328ed" enabled="false" useRalse"/>\n\t\t\t\t<bool name="bUseRealScaling" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseHeroLocalForward" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRandomRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="randRotBegin" x="0.ramName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="612800" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckCondition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOvertimeCD" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSendEvent" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="attackTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="level0Id" valuname="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x89\x80\xe6\x9c\x89\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bVaildBlockForSelfTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVaildBlockForEnemyTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Pos" x="0" y="0" z="-1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Size" x="2000" y="10000" z="3000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="PosList" refParamName="" useRefParam="false" type="Vector3i"/>\n\t\t\t\t<int name="Radius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorRadius" value="1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Height" value="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Degree" value="160" refP\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/commonresource/Dead_Born\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x003\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcc\x00\x00\x00\x02\x00\x00\x00{\x00\x00\x00\x06\x00\x00\x00v1i\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String;\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x000\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc9\x00\x00\x00\x02\x00\x00\x00x\x00\x00\x00\x06\x00\x00\x00v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/A1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x002\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcb\x00\x00\x00\x02\x00\x00\x00z\x00\x00\x00\x06\x00\x00\x00v1h\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String:\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/\x00h\x00\x00\x00\x01\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V2200\x04\x00\x00\x00\x04\x00\x00\x00g\x00\x00\x00\x0b\x00\x00\x00HudTypeP\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.HudCompType\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00n\x00\x00\x00\x11\x00\x00\x00collisionTypeQ\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum1\x00\x00\x00\x08\x00\x00\x00TypeNucleusDrive.Share.CollisionShapeType\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00$\x01\x00\x00\x14\x00\x00\x00iCollisionCenter&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00x7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V200\x04\x00\x00\x00\x04\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00z7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1600\x04\x00\x00\x00\x04\x00\x00\x00v\x00\x00\x00\x12\x00\x00\x00BtResourcePathX\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String*\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Soldier/BTSoldierNormal\x04\x00\x00\x00\x04\x00\x00\x00\x8d\x00\x00\x00\x0f\x00\x00\x00deadAgePathramName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType2" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBeControledActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyAttackerPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyDeadOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCanntAttackOrgan" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorCount" value="32" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="SelectMode" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x9a\x8f\xe6\x9c\xba\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe8\xa1\x80\xe9\x87\x8f\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x89\xe7\x9c\xbc\xe7\x9a\x84\xe8\xa7\x84\xe5\x88\x99\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="CollideMaxCount" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" am="false" />\r\n        <bool name="bExtraBuff" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bOverrideParam" value="false" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam1" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam4" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam5" value="0" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId2" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="StopTrack1" eventType="StopTrack" guid="4ce273d3-51d6-4fe0-8fbe-1ff46fefa576" enabl guid="884649fb-eee1-4f09-8e8c-136817834eb9" enabled="true" useRefParam="false" refParamName="" r="0.900" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetBehaviourModeTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delayStopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="deadControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0="SkillInputCacheDuration" time="0.233" length="0.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCacheSkillReCalcLock" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkMoveAbortCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDure"/>\n\t\t\t\t<int name="animatorOverrideLayer" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLoop" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseFadeOutTime" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="fadeOutTime" value="0.200" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="startTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="endTime" value="99999.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeed" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alwaysAnimate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepOldSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCanNotBeCulled" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="beginClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayBeginCliTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/fireta_hurt_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00825732d46fb1b030cdac35cc22c3f23d\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\x07\x00\x00\x00\x14\x00\x00\x00A409CCAC72376898_##\x00\x1c\x00\x00\x00\x1e\x00\x00\x00\x14\x00\x00\x000629BC043F5D2625_##\x00\x1c\x00\x00\x00d\x00\x00\x00\x14\x00\x00\x007D56267D87A29EDD_##\x00\x1c\x00\x00\x00m\x01\x00\x00\x14\x00\x00\x00DFB6F47F471FD135_##\x00\x13\x0f\x00\x00\x08\x00\x00\x00ROOTC\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom.\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSet\x04\x00\x00\x00\xc0\x0e\x00\x00\x01\x00\x00\x00\xb8\x0e\x00\x00\x0e\x00\x00\x00baseSubsetF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSubset\x04\x00\x00\x00\\\x0e\x00\x00\x04\x00\x00\x00l\x05\x00\x00\x0b\x00\x00\x00actionsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xe2\x04\x00\x00\x04\x00\x00\x005\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xce\x00\x00\x00\x02\x00\x00\x00}\x00\x00\x00\x06\x00\x00\x00v1k\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String=\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/Soldier1/skill/M1A1\x04\x00\x00\x00\x04\x00>\n\t\t\t\t<bool name="bTargetPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="targetPosition" x="0" y="0" z="0" refParamName="" useRefParam="true"/>\n\t\t\t\t<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveCollision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="recreateExisting" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="superTranslation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyTranslation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="translation" x="-600" y="1400" z="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableTag" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" va\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="c41c436a-6fd5-4207-a69b-f3ffebeadf55" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.583" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDonotAttackToMesh" valuSoundTick7" eventType="PlayHeroSoundTick" guid="a23129b2-cb41-44f8-93ff-cf6c2ceaf519" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="sourceId" objectName="None" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="eventName" value="Play_Meilin_Wanou_Skill_Hit_1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="use1P3PSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSkinSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="extraSkinId" refParamName="" useRefParam="false" type="uint"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xffZ\x87\xc0\xeaa\x00\x00\xeaa\x00\x00*\x00\x00\x00Prefab_Monster/137_SiMaYi_Pet/skill/A2.xml<?xLLY\x04\x00\x00\x00\x04\x00\x00\x00,\x00\x00\x00\x0b\x00\x00\x00Element\x15\x00\x00\x00\x01\x00\x00\x00\r\x00\x00\x00\x08\x00\x00\x00NULLY\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00A\x06\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe9\x05\x00\x00\x05\x00\x00\x00\x01\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb5\x01\x00\x00\x03\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x07\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb8\x01\x00\x00\x03\x00\x00\x00\x90\x00\x00\x00\x0b\x00\x00\x00Elementy\x00\x00\x00\x03\x00\x00\x00\t\t<bool name="abortFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterDamage" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMoveRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delaySkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="protectAbortLevel" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe4\xbf\x9d\xe6\x8a\xa4"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="ImmuneNegative" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" valu\n        <int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_1" value="523000" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID1Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID2Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID3Probability" value="0" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSight" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSkillLevel" value="false" refParamName="" useRefParam="false" />\r\n        <Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\r\n          <uint name="\xe6\x99\xae\xe6\x94\xbb" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd1" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd2" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd3" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd4" />\r\n \x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x0f\x03\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00w\x02\x00\x00\x02\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Bullet\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x006\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcf\x00\x00\x00\x02\x00\x00\x00~\x00\x00\x00\x06\x00\x00\x00v1l\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String>\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Hit\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\xbe\x00\x00\x00:\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00189d89e27401dc8d9af987c9418892f7\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xab\x00\x00\x00\x02\x00\x00\x00\x00\n\x00\x00\x005v5\xe5\x8c\xb9\xe9\x85\x8d\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00Param="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="ReplacementUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x89\xe6\xb0\xb4\xe5\x8a\xa0\xe9\x80\x9f\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="ReplacementSubUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe8\x90\xbd\xe5\x9c\xb0\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bNoDynamicLod" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMeshResouce" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAllowEmptyEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true"/>\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.500" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceForbidding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkillAndHideBtn" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill3" valame="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="refSkillLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="compareOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterMajorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMinorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSoldier" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterOtherMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAddEffectCount" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="f1307d98-07[System.String,System.Int32]\x04\x00\x00\x00\xf2\x00\x00\x00\x02\x00\x00\x00\xa1\x00\x00\x00\x06\x00\x00\x00v1\x8f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Stringa\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_RedTower_High/skill/New_RedTower_High_A1E1_Slow\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75013\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xb4\x04\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00$\x04\x00\x00\x04\x00\x00\x00\x07\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa0\x00\x00\x00\x02\x00\x00\x00O\x00\x00\x00\x06\x00\x00\x00v1=\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0f\x00\x00\x00\x05\x00\x00\x00V750130\x04\x00\x00\x00\x04\x00\x00<TemplateObject name="VirtualAttachBulletId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseAttachBulletShape" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/502_astrid/astrid_natk01_hurt01" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="lifeTime" value="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="bindPointName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="bindRotOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x05\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\x9e\x00\x00\x00\x02\x00\x00\x00M\x00\x00\x00\x06\x00\x00\x00v1;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\r\x00\x00\x00\x05\x00\x00\x00VAtk2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00508_Zhadanren/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00508_Zhadanren/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x00\x00\x00508_Zhadanren/skill/extend/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x11\xe7\x15!\x06x\x00\x00\x06x\x00\x00#\x00\x00\x00508_Zhadanren/skill/extend/exA4.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t\t<TemplateObject objectName="bullet" id="2" isTemp="true"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="targetdir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Tram="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillCDTriggerTick0" eventType="SkillCDTriggerTick" guid="ed9f0f3d-9931-4fb8-a5fa-b455c6cbe800" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillCDTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSlotType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80'
    ZSTD_LEVEL = 17
    iconvaneovmacdinh=b'\t\x03\x00\x00\xff3\x00\x00\x85\x00\x00\x00\x14\x00\x00\x00F9B9135D9DECEB62_##\x00\x0b\x00\x00\x00\x14\x00\x00\x0075939F64822D8D0D_##\x00\x08\x00\x00\x003013311\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00Share_13311.jpg\x00\x10\x00\x00\x00Share_13311.jpg\x00\x10\x00\x00\x00Share_13311.jpg\x00\n\x00\x00\x0013311.jpg\x00\x05\x00\x00\x00\x10\x00\x00\x00Skin_Icon_Model\x00\x14\x00\x00\x00D1188909BCF1A796_##\x00\x10\x00\x00\x00Skin_Icon_Skill\x00\x14\x00\x00\x008771C9DA02F4FEA6_##\x00\x16\x00\x00\x00Skin_Icon_SoundEffect\x00\x14\x00\x00\x008D69A8C30826E8D2_##\x00\x13\x00\x00\x00Skin_Icon_Dialogue\x00\x14\x00\x00\x006740D42BD5B8DAF3_##\x00\x15\x00\x00\x00Skin_Icon_Atmosphere\x00\x14\x00\x00\x002231A8E028E42D2D_##\x00\x15\x00\x00\x00Skin_Icon_BackToTown\x00\x14\x00\x00\x00D74BB3893108A06A_##\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00%\x00\x00\x00BG_Commons_01/BG_Commons_01_Platform\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x01x\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x003013311.jpg\x00\x10\x00\x00\x003013311head.jpg\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00'
    iconvaneovbat5=b'%\x03\x00\x00\xff3\x00\x00\x85\x00\x00\x00\x14\x00\x00\x00F9B9135D9DECEB62_##\x00\x0b\x00\x00\x00\x14\x00\x00\x0075939F64822D8D0D_##\x00\n\x00\x00\x003013311_2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00Share_13311_2.jpg\x00\x12\x00\x00\x00Share_13311_2.jpg\x00\x12\x00\x00\x00Share_13311_2.jpg\x00\x0c\x00\x00\x0013311_2.jpg\x00\x05\x00\x00\x00\x10\x00\x00\x00Skin_Icon_Model\x00\x14\x00\x00\x00D1188909BCF1A796_##\x00\x10\x00\x00\x00Skin_Icon_Skill\x00\x14\x00\x00\x008771C9DA02F4FEA6_##\x00\x16\x00\x00\x00Skin_Icon_SoundEffect\x00\x14\x00\x00\x008D69A8C30826E8D2_##\x00\x13\x00\x00\x00Skin_Icon_Dialogue\x00\x14\x00\x00\x006740D42BD5B8DAF3_##\x00\x15\x00\x00\x00Skin_Icon_Atmosphere\x00\x14\x00\x00\x002231A8E028E42D2D_##\x00\x15\x00\x00\x00Skin_Icon_BackToTown\x00\x14\x00\x00\x00D74BB3893108A06A_##\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x003\x00\x00\x00BG_DiRenJie_13312_T3/BG_yinyingzhishou_01_platform\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x01x\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x003013311_2.jpg\x00\x12\x00\x00\x003013311head_2.jpg\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00'
    iconngokhongeovmacdinh=b'R\x03\x00\x00CA\x00\x00\xa7\x00\x00\x00\x14\x00\x00\x00EBC0C74462FF4B6A_##\x00\x07\x00\x00\x00\x14\x00\x00\x00DDB8BB646733B67E_##\x00\x07\x00\x00\x00301677\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00Share_16707.jpg\x00\x10\x00\x00\x00Share_16707.jpg\x00\x10\x00\x00\x00Share_16707.jpg\x00\n\x00\x00\x0016707.jpg\x00\x08\x00\x00\x00\x10\x00\x00\x00Skin_Icon_Model\x00\x14\x00\x00\x008407CA15068FFAAA_##\x00\x14\x00\x00\x00Skin_Icon_Animation\x00\x14\x00\x00\x00C35E60871AB1288B_##\x00\x15\x00\x00\x00Skin_Icon_Atmosphere\x00\x14\x00\x00\x007CD9214682BAB4D9_##\x00\x15\x00\x00\x00Skin_Icon_BackToTown\x00\x14\x00\x00\x0030F7AD035D47227A_##\x00\x10\x00\x00\x00Skin_Icon_Skill\x00\x14\x00\x00\x00B64FCE08AE9DDFE5_##\x00\x16\x00\x00\x00Skin_Icon_SoundEffect\x00\x14\x00\x00\x0051BF047372097407_##\x00\x13\x00\x00\x00Skin_Icon_Dialogue\x00\x14\x00\x00\x00E51142379BF893FC_##\x00\x14\x00\x00\x00Skin_Icon_HeadFrame\x00\x14\x00\x00\x00B68080AD661210A0_##\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00%\x00\x00\x00BG_Commons_01/BG_Commons_01_Platform\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x01N\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00301677.jpg\x00\x0f\x00\x00\x00301677head.jpg\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00'
    iconngokhongeovbat5=b'h\x03\x00\x00CA\x00\x00\xa7\x00\x00\x00\x14\x00\x00\x00EBC0C74462FF4B6A_##\x00\x07\x00\x00\x00\x14\x00\x00\x00DDB8BB646733B67E_##\x00\t\x00\x00\x00301677_2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00Share_16707_2.jpg\x00\x12\x00\x00\x00Share_16707_2.jpg\x00\x12\x00\x00\x00Share_16707_2.jpg\x00\x0c\x00\x00\x0016707_2.jpg\x00\x08\x00\x00\x00\x10\x00\x00\x00Skin_Icon_Model\x00\x14\x00\x00\x008407CA15068FFAAA_##\x00\x14\x00\x00\x00Skin_Icon_Animation\x00\x14\x00\x00\x00C35E60871AB1288B_##\x00\x15\x00\x00\x00Skin_Icon_Atmosphere\x00\x14\x00\x00\x007CD9214682BAB4D9_##\x00\x15\x00\x00\x00Skin_Icon_BackToTown\x00\x14\x00\x00\x0030F7AD035D47227A_##\x00\x10\x00\x00\x00Skin_Icon_Skill\x00\x14\x00\x00\x00B64FCE08AE9DDFE5_##\x00\x16\x00\x00\x00Skin_Icon_SoundEffect\x00\x14\x00\x00\x0051BF047372097407_##\x00\x13\x00\x00\x00Skin_Icon_Dialogue\x00\x14\x00\x00\x00E51142379BF893FC_##\x00\x14\x00\x00\x00Skin_Icon_HeadFrame\x00\x14\x00\x00\x00B68080AD661210A0_##\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00-\x00\x00\x00BG_wukongjuexing2/BG_wukongjuexing2_Platform\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x01N\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\x00301677_2.jpg\x00\x11\x00\x00\x00301677_2head.jpg\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00'
    bacvaneovmacdinh=b'\t\x01\x00\x00\xff3\x00\x00\x85\x00\x00\x00\x14\x00\x00\x00D898FD6DC80FD88F_##\x00\x0b\x00\x00\x00\x14\x00\x00\x0062C20D284D202339_##\x00\x14\x00\x00\x00105E41477A829A72_##\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\n\x00\x00\x0013311.png\x00\x00\x00\x01\x00\x00\x00\x00\x00\xc7\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9f\x86\x01\x00\x00\xf7\x07\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x0020220902000000\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x87\x01\x00\x01\x01\x00\x00\x06,\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00'
    bacvaneovbat5=b'\x11\x01\x00\x00\xff3\x00\x00\x85\x00\x00\x00\x14\x00\x00\x00D898FD6DC80FD88F_##\x00\x0b\x00\x00\x00\x14\x00\x00\x0062C20D284D202339_##\x00\x14\x00\x00\x00105E41477A829A72_##\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00Awake_Label_5.png\x00\x00\x00\x01\x00\x00\x00\x00\x00\xc7\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9f\x86\x01\x00\x00\xf7\x07\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x0020220902000000\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x87\x01\x00\x01\x01\x00\x00\x06,\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00'
    bacngokhongeovmacdinh=b"\x11\x01\x00\x00CA\x00\x00\xa7\x00\x00\x00\x14\x00\x00\x000B0B75B334002849_##\x00\x07\x00\x00\x00\x14\x00\x00\x006B7679BBD5264133_##\x00\x14\x00\x00\x00942E74C2AD28AE4C_##\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00Awake_Label_1.png\x00\x01\x00\x01\x00\x00\x00\x00\x01\xc7\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x90_\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x0020210318060000\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xab'\x00\x00\x01\x01\x00\x00\x06:\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00"
    bacngokhongeovbat5=b"\x11\x01\x00\x00CA\x00\x00\xa7\x00\x00\x00\x14\x00\x00\x000B0B75B334002849_##\x00\x07\x00\x00\x00\x14\x00\x00\x006B7679BBD5264133_##\x00\x14\x00\x00\x00942E74C2AD28AE4C_##\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00Awake_Label_5.png\x00\x01\x00\x01\x00\x00\x00\x00\x01\xc7\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x90_\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x0020210318060000\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xab'\x00\x00\x01\x01\x00\x00\x06:\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00"
    ngoaihinhvaneov=b'/\x0c\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xd7\x0b\x00\x00\n\x00\x00\x00\x16\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xca\x01\x00\x00\x03\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x1c\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xcd\x01\x00\x00\x03\x00\x00\x00\x97\x00\x00\x00\x0b\x00\x00\x00Element\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show1\x04\x00\x00\x00\x04\x00\x00\x00\x97\x00\x00\x00\x0b\x00\x00\x00Element\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x97\x00\x00\x00\x0b\x00\x00\x00Element\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show3\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa5\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.5\x04\x00\x00\x00\x04\x00\x00\x00b\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.9\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x004\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.07000029\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.539993\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-3.739998\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xff\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.002750125\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00yB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.009888734\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V0.9999473\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
    ngoaihinhvaneovvang=b'J\x0c\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\r\x0c\x00\x00\n\x00\x00\x00\x16\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xca\x01\x00\x00\x03\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x007\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x01\x00\x00\x03\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa5\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.5\x04\x00\x00\x00\x04\x00\x00\x00b\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.9\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x004\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.07000029\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.539993\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-3.739998\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xff\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.002750125\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00yB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.009888734\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V0.9999473\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
    ngoaihinhvaneovdo= b'J\x0c\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\r\x0c\x00\x00\n\x00\x00\x00\x16\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xca\x01\x00\x00\x03\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00Element\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x007\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x01\x00\x00\x03\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\xa0\x00\x00\x00\x0b\x00\x00\x00Element\x89\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Component/13312_DiRenJie_AW5_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa5\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.5\x04\x00\x00\x00\x04\x00\x00\x00b\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.9\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x004\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.07000029\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.539993\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-3.739998\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xff\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.002750125\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00yB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V0.009888734\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V0.9999473\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
    ngoaihinhkhieov=b'B\x10\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xea\x0f\x00\x00\x0e\x00\x00\x00\x10\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc4\x01\x00\x00\x03\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x16\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc7\x01\x00\x00\x03\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show1\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show3\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\xa2\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_wukong/Awaken/1678_sunwukong_03_Cam\x04\x00\x00\x00\x04\x00\x00\x00\xa3\x00\x00\x00\x19\x00\x00\x00ArtSkinLobbyShowMovie~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/167_wukong/Awaken/1678_sunwukong_03_Movie\x04\x00\x00\x00\x04\x00\x00\x00Y\x00\x00\x00\x11\x00\x00\x00useNewMecanim<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x0f\x00\x00\x00bUnityLight<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00a\x00\x00\x00\x19\x00\x00\x00bUseCodeAnimComponent<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00f\x00\x00\x00\x08\x00\x00\x00MSAAR\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum2\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.EAntiAliasing\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00$\x03\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xd2\x02\x00\x00\x05\x00\x00\x00\x8e\x00\x00\x00\x0b\x00\x00\x00Elementw\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringI\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x0b\x00\x00\x00Element|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint_Idle\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x0b\x00\x00\x00Element|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint_Loop\x04\x00\x00\x00\x04\x00\x00\x00\x92\x00\x00\x00\x0b\x00\x00\x00Element{\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringM\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_WuKong/wukong_Sprint_Run\x04\x00\x00\x00\x04\x00\x00\x00\x84\x00\x00\x00\x0b\x00\x00\x00Elementm\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/Dance_Effects/167/dance_03_texiao\x04\x00\x00\x00\x04\x00\x00\x00\x86\x03\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x00.\x03\x00\x00\x04\x00\x00\x00B\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xfc\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00\x05\x00\x00\x00xB\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x14\x00\x00\x00\x05\x00\x00\x00V-0.05998039\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x05\x00\x00\x00y?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x11\x00\x00\x00\x05\x00\x00\x00V1.389713\x04\x00\x00\x00\x04\x00\x00\x00Q\x00\x00\x00\x05\x00\x00\x00z@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x12\x00\x00\x00\x05\x00\x00\x00V-2.490662\x04\x00\x00\x00\x04\x00\x00\x00B\x01\x00\x00\r\x00\x00\x00Direction4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xf9\x00\x00\x00\x03\x00\x00\x00T\x00\x00\x00\x05\x00\x00\x00xC\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x15\x00\x00\x00\x05\x00\x00\x00V1.831149E-07\x04\x00\x00\x00\x04\x00\x00\x00T\x00\x00\x00\x05\x00\x00\x00yC\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x15\x00\x00\x00\x05\x00\x00\x00V-8.35189E-09\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x05\x00\x00\x00z8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00P\x00\x00\x00\x0c\x00\x00\x00Duration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\r\x00\x00\x00CameraFOV9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0b\x00\x00\x00\x05\x00\x00\x00V17\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
    bienvengokonhocty=b'\r\n\t<Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="2b767094-bee5-4ffd-807c-e2759b06b84e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="103b0d01-3a4a-4124-93cd-2f4f36565344">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="rotationY" value="180" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="b9729512-4050-459e-9644-dc609c2a3a1f" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="f7df0085-7f43-4a62-8d4c-1318238ba3ce">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="parentResourceName" value="born_back_reborn/huijidi_01" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/component_effects/16707/16707_5/huijidi_01" refParamName="" useRefParam="true"/>\r\n        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="28dbc769-e471-407e-8108-9012ecf910d8" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="6057cb60-5062-42e9-a6cd-09c8e9e7eb05">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/component_effects/16707/16707_5/huicheng_tongyong_01" refParamName="" useRefParam="true"/>\r\n        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="b9729512-4050-459e-9644-dc609c2a3a1f" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="f7df0085-7f43-4a62-8d4c-1318238ba3ce">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="parentResourceName" value="born_back_reborn/huijidi_01" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/16707/16707_5/huijidi_01" refParamName="" useRefParam="true"/>\r\n        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="28dbc769-e471-407e-8108-9012ecf910d8" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="6057cb60-5062-42e9-a6cd-09c8e9e7eb05">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/16707/16707_5/huicheng_tongyong_01" refParamName="" useRefParam="true"/>\r\n        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
    bienvevanxathan=b'\r\n    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="cd9fc83b-cec9-4414-b884-00fe7c6c8e82" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t  <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="8a15b50f-d8c7-4479-a6fb-ab20aa6aefae">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="rotationY" value="198" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="efb4fcc6-58ae-4313-be89-4c39a7a42798" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t  <Event eventName="SetObjectDirectionTick" time="7.000" isDuration="false" guid="b72c4e01-16b7-4c8b-9b0b-b0ef3ffa571b">\r\n        <TemplateObject name="targetId" id="3" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick" eventType="TriggerParticleTick" guid="b9729512-4050-459e-9644-dc609c2a3a1f" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t  <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="f7df0085-7f43-4a62-8d4c-1318238ba3ce">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Component_Effects/13311/13311_5/huijidi_01" refParamName="" useRefParam="true" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticleTick" eventType="TriggerParticle" guid="28dbc769-e471-407e-8108-9012ecf910d8" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t  <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="6057cb60-5062-42e9-a6cd-09c8e9e7eb05">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Component_Effects/13311/13311_5/huicheng_tongyong_01" refParamName="" useRefParam="true" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="Home" eventType="PlayAnimDuration" guid="664523ad-bc5e-4796-94a7-003b758fb8c4" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="PlayAnimDuration" time="0.000" length="7.000" isDuration="true" guid="ff3c2242-829b-4cfd-aaad-8e70a5e03ba2">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="clipName" value="13311/Awaken/Home" refParamName="" useRefParam="false" />\r\n        <int name="layer" value="2" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="Gohome" eventType="PlayAnimDuration" guid="972d1382-031a-4c10-8eeb-d10b3fc76f47" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t  <Event eventName="PlayAnimDuration" time="7.000" length="1.500" isDuration="true" guid="620b137f-72fa-4602-a653-72ae85944d33">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="clipName" value="13311/Awaken/Gohome" refParamName="" useRefParam="false" />\r\n        <int name="layer" value="2" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
    CODEBIENVE=b'\r\n\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="b9729512-4050-459e-9644-dc609c2a3a1f" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/huijidi_01" refParamName="" useRefParam="true"/>\r\n     </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="28dbc769-e471-407e-8108-9012ecf910d8" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/huicheng_tongyong_01" refParamName="" useRefParam="true"/>\r\n        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
    projack=b'      </Event>\r\n    </Track>\r\n    <Track trackName="HitTriggerTick0" eventType="HitTriggerTick" guid="3fcc5b3f-3a9c-495c-bddd-5e3b03e5c01b" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">'
    CODECHECKBIENVE = b''
    checkHasteE1=b'\r\n    <Track trackName="CheckHeroIdTick1" eventType="CheckSkinIdTick" guid="Cre" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkinIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skinId" value="ID_Hero" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
    checkHasteE1_leave=b'\r\n    <Track trackName="CheckHeroIdTick1" eventType="CheckHeroIdTick" guid="Cre" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="heroId" value="ID_Hero" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
    gtHasteE1bv=b'\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="412ea073-5944-46e4-ae5e-3037e855fda7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="5.000" isDuration="true">\r\n        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
    CODEBVYENA = b'\r\n\t<Track trackName="SetObjectDirectionTick2" eventType="SetObjectDirectionTick" guid="62996a6c-a8d4-42f6-90aa-6ee10271d08e" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="cc68e0b3-a496-4fc2-8128-6f215a965229">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <int name="rotationY" value="180" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="ChangeHDHeightDuration3" eventType="ChangeHDHeightDuration" guid="3965e0e3-dd4b-44b8-ba36-682488d46550" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="ChangeHDHeightDuration" time="0.000" length="7.000" isDuration="true" guid="32824200-4e8e-4101-8d7d-be0ea0c313d1">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <int name="heightChange" value="700" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="216618f0-8c39-4789-903b-08ddecb68b45" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="PlayAnimDuration" time="0.000" length="7.000" isDuration="true" guid="96fa9d23-90bd-480b-af17-a12d8c342396">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="clipName" value="Home2" refParamName="" useRefParam="false" />\r        <int name="layer" value="3" refParamName="" useRefParam="false" />\r        <bool name="bLoop" value="true" refParamName="" useRefParam="false" />\r        <float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false" />\r        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="PlayAnimDuration2" eventType="PlayAnimDuration" guid="201bd792-c933-43a0-a590-bec4367a2710" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="PlayAnimDuration" time="7.000" length="1.500" isDuration="true" guid="621e77cb-3dfc-40e3-8082-3e8603e3f7e2">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="clipName" value="Gohome2" refParamName="" useRefParam="false" />\r        <int name="layer" value="3" refParamName="" useRefParam="false" />\r        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\xb6\xe5\xa8\x9cT2\xe7\x8e\xaf\xe5\x88\x83" eventType="TriggerParticleTick" guid="372cea2b-4677-4587-a037-9c13affdb97d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="007b4fc2-b841-493b-a390-91fde34a7624">\r        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/huijidi_01_r" refParamName="strReturnCityFall" useRefParam="false" />\r        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <bool name="bUseHeroLocalForward" value="true" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementSubUsage" value="1" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\xb6\xe5\xa8\x9cT2\xe7\x8e\xaf\xe5\x88\x83" eventType="TriggerParticle" guid="3b9eb49a-febc-4403-827d-1dc93e40bf8b" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="fba560da-156f-42fd-a4a0-b2d002e20c8b">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/huicheng_tongyong_01_r" refParamName="strReturnCityEffectPath" useRefParam="false" />\r        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <bool name="bEnableOptCull" value="false" refParamName="" useRefParam="false" />\r        <bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r        <bool name="bApplySpecialEffect" value="true" refParamName="" useRefParam="false" />\r        <bool name="bOnlySetAlpha" value="true" refParamName="" useRefParam="false" />\r        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe7\x8e\xaf\xe5\x88\x83\xe5\x8f\x8c\xe5\x89\x91buff" eventType="TriggerParticle" guid="b4915550-8c39-430e-a71c-71fbf46dfaa4" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticle" time="0.000" length="8.367" isDuration="true" guid="2f0136b1-53ec-45e3-b28b-ba244e737c6f">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/Huicheng_ personality_01 _r" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\xb6\xe5\xa8\x9cT2\xe7\x8e\xaf\xe5\x88\x83" eventType="TriggerParticleTick" guid="136fd4b7-a92f-4ba8-a3d6-d7c2fc6fbfe3" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="60a991c3-3bf1-4db0-b833-6f5fe406473b">\r        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="born_back_reborn/huijidi_01_b" refParamName="strReturnCityFall" useRefParam="false" />\r        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <bool name="bUseHeroLocalForward" value="true" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementSubUsage" value="1" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\xb6\xe5\xa8\x9cT2\xe7\x8e\xaf\xe5\x88\x83" eventType="TriggerParticle" guid="ca420146-9732-4190-9790-c214efc6e549" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="37743f3e-8508-41df-9c61-5b44988c3889">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_01_b" refParamName="strReturnCityEffectPath" useRefParam="false" />\r        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <bool name="bEnableOptCull" value="false" refParamName="" useRefParam="false" />\r        <bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r        <bool name="bApplySpecialEffect" value="true" refParamName="" useRefParam="false" />\r        <bool name="bOnlySetAlpha" value="true" refParamName="" useRefParam="false" />\r        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\x8c\xe5\x88\x83\xe5\x8f\x8c\xe5\x89\x91buff" eventType="TriggerParticle" guid="48412d98-0d6e-4772-bfca-fb58c57d741b" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticle" time="0.000" length="8.367" isDuration="true" guid="3fff9929-dfc8-403b-9e63-510f08c4930a">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="prefab_skill_effects/Huicheng_ personality_01" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe5\x8f\xb6\xe5\xa8\x9cT2\xe7\x8e\xaf\xe5\x88\x83" eventType="TriggerParticleTick" guid="ac18c450-19ac-42e1-8167-c194b96ba645" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="10bf2901-d739-46b0-a6bb-cbf8634011cc">\r        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <String name="resourceName" value="born_back_reborn/huijidi_01_b" refParamName="strReturnCityFall" useRefParam="false" />\r        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />\r        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r        <bool name="bUseHeroLocalForward" value="true" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r        <Enum name="ReplacementSubUsage" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>'
    CODEBVYENA1 = b'\r\n\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="b9729512-4050-459e-9644-dc609c2a3a1f" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Condition id="co1" guid="54bef446-7cce-4539-97a8-9a0cbd37563d" status="true" />\r      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false">\r        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\r        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huijidi_01" refParamName="" useRefParam="true"/>\r        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false"/>\r     </Event>\r    </Track>\r    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="28dbc769-e471-407e-8108-9012ecf910d8" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Condition id="co1" guid="54bef446-7cce-4539-97a8-9a0cbd37563d" status="true" />\r      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true">\r        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <String name="parentResourceName" value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_01" refParamName="" useRefParam="false"/>\r        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huicheng_tongyong_01" refParamName="" useRefParam="true"/>\r        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>\r      </Event>\r    </Track>\r\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="b9729512-4050-459e-9644-dc609c2a3a1f" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Condition id="cod2" guid="b588953f-80b3-4084-a5e2-6840b43b171c" status="true" />\r      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false">\r        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\r        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\r        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huijidi_01_r" refParamName="" useRefParam="true"/>\r        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false"/>\r     </Event>\r    </Track>\r    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="28dbc769-e471-407e-8108-9012ecf910d8" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Condition id="cod2" guid="b588953f-80b3-4084-a5e2-6840b43b171c" status="true" />\r      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true">\r        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <String name="parentResourceName" value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_01" refParamName="" useRefParam="false"/>\r        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huicheng_tongyong_01_r" refParamName="" useRefParam="true"/>\r        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
    GIATOC='13210,10611,11113,11604,13011,15004,16307,19007,50108,50112,54402,54004,13111,13112,13202,16606,19502,50605,53002,13311,13015,52011,15710'
    GIATOCEDIT='11607,14111,15009,16707'
    gtHasteE1 = gtHasteE1bv
    gtHasteE1_leave = gtHasteE1bv
    AABBCC = 'HSM'
    ngoaihinhxanhveres = b'9\t\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe1\x08\x00\x00\x0b\x00\x00\x00\x10\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc4\x01\x00\x00\x03\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x16\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc7\x01\x00\x00\x03\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_2_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCameram\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/5208_Veres_Cam\x04\x00\x00\x00\x04\x00\x00\x00Z\x00\x00\x00\x16\x00\x00\x00CamInterpolateTime8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V7\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.1\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\\\x00\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
    ngoaihinhdoveres = b'9\t\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe1\x08\x00\x00\x0b\x00\x00\x00\x10\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc4\x01\x00\x00\x03\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x94\x00\x00\x00\x0b\x00\x00\x00Element}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x16\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xc7\x01\x00\x00\x03\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x0b\x00\x00\x00Element~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/Component/5208_Veres_RT_3_Show2\x04\x00\x00\x00\x04\x00\x00\x00E\x01\x00\x00\x1b\x00\x00\x00ArtSkinLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x93\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCameram\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/520_Veres/5208_Veres_Cam\x04\x00\x00\x00\x04\x00\x00\x00Z\x00\x00\x00\x16\x00\x00\x00CamInterpolateTime8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V7\x04\x00\x00\x00\x04\x00\x00\x00^\x00\x00\x00\x18\x00\x00\x00Cam02InterpolateTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.1\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x1c\x00\x00\x00Cam02InterpolateDuration8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00\\\x00\x00\x00\n\x00\x00\x00LookAtF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CameraLookAt\x04\x00\x00\x00\x04\x00\x00\x00m\x00\x00\x00\x0f\x00\x00\x00LightConfigR\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom=\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.PrepareBattleLightConfig\x04\x00\x00\x00\x04\x00\x00\x00'
    hasteE1cechbv = 65
    hasteE1_leavecechbv=64

    def giai(a):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
        except getopt.GetoptError:
            sys.exit(1)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                sys.exit()
        
        if not args:
            args = a
            anti=b''
            input_blob = None
            with open(args, "rb") as f:
                input_blob = f.read()
            if opts:
                opt, arg = opts[0]
            else:
                pos = input_blob.find(b"\x28\xb5\x2f\xfd")
                if pos != -1:
                   opt = "-d"
                   input_blob = input_blob[pos:]
                else:
                    opt = "-c"
            zstd_mode = None
            try:
                if opt in ("-c", "--compress"):
                    zstd_mode = "compress"
                    output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                    output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                    output_blob[0:0] = b"\x22\x4a\x00\xef"
                    new=random.randbytes(0)
                    anti+=new
                elif opt in ("-d", "--decompress"):
                    input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]
                    zstd_mode = "decompress"
                    output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

                output_path = args
                with open(output_path, "wb") as output_file:
                    output_file.write(output_blob)
                with open(output_path, "ab") as output_file:
                        output_file.write(anti)
                file_path = a
                test = os.path.isdir(file_path)
                file_stat = os.stat(file_path)
                new_atime = new_mtime = new_ctime = 4299999999
                os.utime(file_path, times=(new_atime, new_mtime))
                updated_stat = os.stat(file_path)
            except pyzstd.ZstdError:
                pass
        return
    def ArtSkinLobbyIdleShowLOD(data4):
        a=camSkin.find(b'\x00ArtSkinLobbyIdleShowLOD')-7
        a10=camSkin.find(b'\x00ArtSkinLobbyIdleShowLOD')-3
        a3=camSkin[a:a+8]
        a4=a3[4:]
        a2=camSkin[a:a+4]
        vitri=int.from_bytes(a2,byteorder='little')
        ne=camSkin[vitri:]
        vitri2=int.from_bytes(a4,byteorder='little')
        a5=camSkin[a:a+vitri]
        a25=camSkin[a10:a10+vitri2]
        a22=camSkin[a10:a10+vitri2].replace(b'\x00ArtSkinLobbyIdleShowLOD',b'\x00ArtLobbyIdleShowLOD')
        a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
        code=a5.replace(a25,a13)
        data4=len(code).to_bytes(4,byteorder='little')+code[4:]+ne
        return data4
    def ArtPrefabLODnew(data):
        a=ab.find(b'\x00ArtPrefabLOD')-7
        a2=ab[a:a+4]
        a3=ab[a:a+5]
        a4=a3[4:5]#so 10
        vitri=int.from_bytes(a2,byteorder='little')
        data=ab[a:a+vitri]
        return data
    def ArtPrefabLODExnew(data4):
        a=ab.find(b'\x00ArtPrefabLODEx')-7
        a2=ab[a:a+4]
        a3=ab[a:a+5]
        a4=a3[4:5]#so 10
        vitri=int.from_bytes(a2,byteorder='little')
        data4=ab[a:a+vitri]
        return data4
    def ArtSkinPrefabLODnew(data3):
        a=ab.find(b'\x00ArtSkinPrefabLOD')-7
        a10=ab.find(b'\x00ArtSkinPrefabLOD')-3
        a3=ab[a:a+8]
        a4=a3[4:]
        a2=ab[a:a+4]
        vitri=int.from_bytes(a2,byteorder='little')
        vitri2=int.from_bytes(a4,byteorder='little')
        a5=ab[a:a+vitri]
        a25=ab[a10:a10+vitri2]
        a22=ab[a10:a10+vitri2].replace(b'\x00ArtSkinPrefabLOD',b'\x00ArtPrefabLOD')
        a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
        code=a5.replace(a25,a13)
        data3=len(code).to_bytes(2,byteorder='little')+code[2:]
        return data3 
    def ArtSkinPrefabLODExnew(data2):
        a=ab.find(b'\x00ArtSkinPrefabLODEx')-7
        a10=ab.find(b'\x00ArtSkinPrefabLODEx')-3
        a3=ab[a:a+8]
        a4=a3[4:]
        a2=ab[a:a+4]
        vitri=int.from_bytes(a2,byteorder='little')
        vitri2=int.from_bytes(a4,byteorder='little')
        a5=ab[a:a+vitri]
        a25=ab[a10:a10+vitri2]
        a22=ab[a10:a10+vitri2].replace(b'\x00ArtSkinPrefabLODEx',b'\x00ArtPrefabLODEx')
        a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
        code=a5.replace(a25,a13)
        data2=len(code).to_bytes(4,byteorder='little')+code[4:]
        return data2
    def bienve(data):#Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/
        teninfo23=NAME_HERO.encode()
        IDBV=IDCHECK[:3].encode()
        IDBV1=IDCHECK.encode()
        codenew1=codenew.replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
        codenew3=codenew1.replace(b'Name_Hero',teninfo23)
        data=codenew3.replace(b'ID_Skin',IDBV1)
        return data
    def bienve1(data):#Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/
        teninfo23=NAME_HERO.encode()
        IDBV=IDCHECK[:3].encode()
        IDBV1=IDCHECK.encode()
        codenew1=codenew.replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
        data=codenew1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/',b'prefab_skill_effects/component_effects/16707/16707_5/')
        return data
    def bienvecheck(data):
        teninfobv1=NAME_HERO[4:].encode()
        teninfo23=NAME_HERO.encode()
        IDBV=IDCHECK[:3].encode()
        if IDCHECK == "15412":
            CODECHECKBIENVE = b'      </Event>\r\n    </Track>\r\n    <Track trackName="CheckHeroIdTick0" eventType="CheckHeroIdTick" guid="Cre" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r        <int name="heroId" value="ID_Hero" refParamName="" useRefParam="false"/>\r      </Event>\r    </Track>\r    <Track trackName="\xe6\xa3\x80\xe6\xb5\x8b\xe5\x8f\x8c\xe5\x88\x83buff" eventType="CheckSkillCombineConditionTick" guid="54bef446-7cce-4539-97a8-9a0cbd37563d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="37a8c180-8551-4dc1-870e-46049f6e392b">\r        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\r        <int name="skillCombineId" value="154999" refParamName="" useRefParam="false" />\r        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false" />\r        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r      </Event>\r    </Track>\r    <Track trackName="\xe6\xa3\x80\xe6\xb5\x8b\xe7\x8e\xaf\xe5\x88\x83buff" eventType="CheckSkillCombineConditionTick" guid="b588953f-80b3-4084-a5e2-6840b43b171c" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="bb954fcc-b78f-406a-bfb8-12c1bb2e3359">\r        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r        <int name="skillCombineId" value="254999" refParamName="" useRefParam="false" />\r        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false" />\r        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="HitTriggerTick0" eventType="HitTriggerTick" guid="3fcc5b3f-3a9c-495c-bddd-5e3b03e5c01b" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">'
        else:
            CODECHECKBIENVE=b'      </Event>\r\n    </Track>\r\n    <Track trackName="CheckHeroIdTick0" eventType="CheckHeroIdTick" guid="Cre" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="heroId" value="ID_Hero" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="HitTriggerTick0" eventType="HitTriggerTick" guid="3fcc5b3f-3a9c-495c-bddd-5e3b03e5c01b" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">'

        codenew=CODECHECKBIENVE.replace(b'value="ID_Hero',b'value="'+IDBV)
        data=codenew.replace(b'guid="Cre',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
        return data
    def hasteE1(data):
        teninfo23=NAME_HERO.encode()
        IDBV=IDCHECK[:3].encode()
        IDBV1=IDCHECK.encode()
        codenew1=codenew.replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
        codenew3=codenew1.replace(b'Name_Hero',teninfo23)
        data=codenew3.replace(b'ID_Skin',IDBV1)
        return data 
    def hasteE1check(data):
        teninfobv1=NAME_HERO[4:].encode()
        teninfo23=NAME_HERO.encode()
        IDBV=IDCHECK[:3].encode()
        IDBV=IDBV+b'00'
        codenew=data.replace(b'value="ID_Hero',b'value="'+IDBV)
        data=codenew.replace(b'guid="Cre',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
        return data
    def hasteE1_leave(data):
        teninfo23=NAME_HERO.encode()
        IDBV=IDCHECK[:3].encode()
        IDBV1=IDCHECK.encode()
        codenew1=codenew.replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
        codenew3=codenew1.replace(b'Name_Hero',teninfo23)
        data=codenew3.replace(b'ID_Skin',IDBV1)
        return data 
    def hasteE1check_leave(data):
        teninfobv1=NAME_HERO[4:].encode()
        teninfo23=NAME_HERO.encode()
        IDBV=IDCHECK[:3].encode()
        codenew=data.replace(b'value="ID_Hero',b'value="'+IDBV)
        data=codenew.replace(b'guid="Cre',b'guid="'+AABBCC.encode('utf-8') + b'_'+teninfo23)
        return data
    def count_tracks_above_action_name(filename, action_name):
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        count = 0
        for line in lines:
            if action_name in line:
                break
            if 'trackName' in line:
                count += 1
        return count
    IDD = result_str
    IDMODSKIN=IDD.split()
    IDMODSKIN1=IDD.split()
    print(IDMODSKIN1)
    print("─"*30)
    DANHSACH = IDD.split()
    with open ('Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes', 'rb') as f:
        a=f.read()
    if b'"J\x00' in a:
        giai('Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes')
    map1='Resources/1.55.1/Languages/VN_Garena_VN/languageMap.txt'
    map2='Resources/1.55.1/Languages/VN_Garena_VN/languageMap_Newbie.txt'
    map3='Resources/1.55.1/Languages/VN_Garena_VN/languageMap_WorldConcept.txt'
    map4='Resources/1.55.1/Languages/VN_Garena_VN/languageMap_Xls.txt'
    map5='Resources/1.55.1/Languages/VN_Garena_VN/lanMapIncremental.txt'
    FILES_MAP = [map1, map2, map3, map4, map5]
    for mapp in FILES_MAP:
        with open (mapp, 'rb') as f:
            a=f.read()
        if b'"J\x00' in a:
            giai(mapp)
    TENSKIN =[]
    for mapp in FILES_MAP:
        for i in DANHSACH:

            with open(mapp,'rb') as f: rpl=f.read()
            with open('Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes','rb') as f: RPL=f.read()
            i = int(i)
            IDFIND=RPL.find(i.to_bytes(4,'little')+int(str(i)[:3]).to_bytes(4,'little'))
            if IDFIND != -1:
                VT=RPL[IDFIND+12:IDFIND+31]
                VT1=rpl.find(VT)
                VT2=rpl.find(b'\r',VT1)
                VTR=rpl[VT1:VT2]
                VT=RPL[IDFIND+40:IDFIND+59]
                VT1=rpl.find(VT)
                VT2=rpl.find(b'\r',VT1)
                VTR_SKIN=rpl[VT1:VT2]
                A = VTR[22:]
                B = VTR_SKIN[22:]
                #aaaa=(' '.join(all_characters))
                sanitized_input = ((A + b' ' +B).decode())
                sanitized_input = ''.join(char for char in sanitized_input if char not in ['/', '\\', ':', '*', '?', '"', '<', '>', '|'])
                TENSKIN.append(sanitized_input)
    #print(TENSKIN)
    aaabbbcccnnn = ''
    for sanitized_input in TENSKIN:
        if sanitized_input == ' ':
            continue
            print("Skin Does Not Exist")
            
        if '[ex]' in sanitized_input:
            print("Skin Does Not Exist")
            continue
            
        else:
            print(sanitized_input)
            aaabbbcccnnn = sanitized_input
            sanitized_input = sanitized_input+"HSM"

            with open('skin.txt', 'a', encoding='utf-8') as file:

                file.write('Mod Skin '+aaabbbcccnnn+'\n')
                file.write(aaabbbcccnnn+'\n')
    sanitized_input = aaabbbcccnnn +"HSM"
    giai('Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes')
    print('─'*30)
    if len(DANHSACH) > 1:
        sanitized_input = input('Enter Skin Pack Name: ')
    #===================================================================================================================
    base_path = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/"
    directories = ["Actor", "Shop", "Sound", "Skill", "Character", "Motion", "Global"]
    for directory in directories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)
        
    #===================================================================================================================
    file_actor = "Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes"
    file_actor_mod = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Actor/heroSkin.bytes"
    shutil.copy(file_actor, file_actor_mod)
    giai(file_actor_mod)

    file_shop = "Resources/1.55.1/Databin/Client/Shop/HeroSkinShop.bytes"
    file_shop_mod = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Shop/HeroSkinShop.bytes"
    shutil.copy(file_shop, file_shop_mod)
    giai(file_shop_mod)

    file_sound1 = "Resources/1.55.1/Databin/Client/Sound/BattleBank.bytes"
    file_sound_mod1 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/BattleBank.bytes"
    shutil.copy(file_sound1, file_sound_mod1)
    giai(file_sound_mod1)

    file_sound2 = "Resources/1.55.1/Databin/Client/Sound/ChatSound.bytes"
    file_sound_mod2 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/ChatSound.bytes"
    shutil.copy(file_sound2, file_sound_mod2)
    giai(file_sound_mod2)

    file_sound3 = "Resources/1.55.1/Databin/Client/Sound/HeroSound.bytes"
    file_sound_mod3 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/HeroSound.bytes"
    shutil.copy(file_sound3, file_sound_mod3)
    giai(file_sound_mod3)

    file_sound4 = "Resources/1.55.1/Databin/Client/Sound/LobbyBank.bytes"
    file_sound_mod4 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/LobbyBank.bytes"
    shutil.copy(file_sound4, file_sound_mod4)
    giai(file_sound_mod4)
    
    file_sound5 = "Resources/1.55.1/Databin/Client/Sound/LobbySound.bytes"
    file_sound_mod5 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound/LobbySound.bytes"
    shutil.copy(file_sound5, file_sound_mod5)
    giai(file_sound_mod5)

    Sound_Files = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Sound"

    file_skill1 = "Resources/1.55.1/Databin/Client/Skill/liteBulletCfg.bytes"
    file_mod_skill1 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Skill/liteBulletCfg.bytes"
    shutil.copy(file_skill1, file_mod_skill1)
    giai(file_mod_skill1)

    file_skill2 = "Resources/1.55.1/Databin/Client/Skill/skillmark.bytes"
    file_mod_skill2 = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Skill/skillmark.bytes"
    shutil.copy(file_skill2, file_mod_skill2)
    giai(file_mod_skill2)

    file_Character = "Resources/1.55.1/Databin/Client/Character/ResCharacterComponent.bytes"
    file_mod_Character = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Character/ResCharacterComponent.bytes"
    shutil.copy(file_Character, file_mod_Character)
    giai(file_mod_Character)

    file_Modtion = "Resources/1.55.1/Databin/Client/Motion/ResSkinMotionBaseCfg.bytes"
    file_mod_Modtion = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Motion/ResSkinMotionBaseCfg.bytes"
    shutil.copy(file_Modtion, file_mod_Modtion)
    giai(file_mod_Modtion)

    file_vien = "Resources/1.55.1/Databin/Client/Global/HeadImage.bytes"
    file_mod_vien = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Global/HeadImage.bytes"
    shutil.copy(file_vien, file_mod_vien)
    giai(file_mod_vien)

    with zipfile.ZipFile('Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes') as f:
        f.extractall(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/')
        giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Back.xml')
        f.close()

    file_name = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Back.xml'
    action_name = '<String name="actionName" value="Back"'
    track_count = count_tracks_above_action_name(file_name, action_name)
    track_count = track_count - 1
    k1bv=track_count
    track_count1 = k1bv+1
    
    giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1.xml')
    file_name = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1.xml'
    action_name = '</Project>'
    track_count = count_tracks_above_action_name(file_name, action_name)
    hasteE1cechbv = track_count
    giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1.xml')

    giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1_leave.xml')
    file_name = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1_leave.xml'
    action_name = '</Project>'
    track_count = count_tracks_above_action_name(file_name, action_name)
    hasteE1_leavecechbv = track_count
    giai(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1_leave.xml')
    
    os.makedirs(f"{sanitized_input}/files/Resources/1.55.1/AssetRefs/Hero/")
    
    #===================================================ICON_BAC================================================================

    for IDMODSKIN in IDMODSKIN:
        SKINEOV = ''
        if IDMODSKIN == '13311':
            SKINEOV = "r"
        if IDMODSKIN == '16707':
            SKINEOV = "b"
        if IDMODSKIN == '15412':
            SKINEOV = "y"
        nhap_id = IDMODSKIN
        file_actor = file_actor_mod
        file_shop = file_shop_mod
        IDCHECK = IDMODSKIN
        IDSOUND_S = IDMODSKIN
        phukien = ''
        phukienv = ''

        if IDCHECK == '52007':
            phukien1 = '3'#input("1/xanh ; 2/do ; 3/no: ")
            if phukien1 == "1":
               phukien = 'xanh'
            if phukien1 == "2":
               phukien = 'do'
        if IDCHECK == '13311':
            phukien1v = '3'#input("1/vang ; 2/do ; 3/no: ")
            if phukien1v == "1":
               phukienv = 'vangv'
            if phukien1v == "2":
               phukienv = 'dov'
        if IDSOUND_S[3:4] == '0':
            IDSOUND_S=IDSOUND_S[:3]+IDSOUND_S[4:]
        IDSOUND1=IDSOUND_S[3:]
        IDSOUND12=IDSOUND1.encode()
        IDSOUND = b"_Skin" + IDSOUND12
        HPCAO=b'\r\n    <!-- '+AABBCC.encode('utf-8') +b' -->'

        IDINFO=int(IDMODSKIN)+1
        IDINFO=str(IDINFO)
        if str(IDINFO)[3:4] == '0':
            IDINFO=IDINFO[:3]+IDINFO[4:]
        IDINFO=str(IDINFO)
        if IDCHECK not in ["10611", "13211", "13212"]:
            def tim_id(data, chuoi_thay_the):
                id_tim = b'\x00\x00' + int(data).to_bytes(4, 'little')
                
                vi_tri_truoc = chuoi_thay_the.find(id_tim) - 2
                
                vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+4]
                vi_tri_tim = int.from_bytes(vi_tri, 'little')
                if vi_tri_tim > 100:
                    return True
                else:
                    return False

            tat_ca_id = []
            with open(file_actor, 'rb') as f:
                chuoi_thay_the = f.read()

            if nhap_id == '16707':
                chuoi_thay_the = chuoi_thay_the.replace(iconngokhongeovmacdinh, iconngokhongeovbat5)
            elif nhap_id == '13311':
                chuoi_thay_the = chuoi_thay_the.replace(iconvaneovmacdinh, iconvaneovbat5)

            for i in range(int(nhap_id[:3] + '00'), int(nhap_id[:3] + '99')):
                if i != int(nhap_id):
                    kiem_tra_id = tim_id(i, chuoi_thay_the)
                    if kiem_tra_id:
                        tat_ca_id.append(str(i))

            id_skin_moi = list(set(tat_ca_id))

            vi_tri_id_tim_kiem = b'\x00\x00' + int(nhap_id).to_bytes(4, 'little')
            vi_tri_truoc = chuoi_thay_the.find(vi_tri_id_tim_kiem) - 2
            vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+4]
            vi_tri_tim = int.from_bytes(vi_tri, 'little')
            vi_tri_mod = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+vi_tri_tim+4]

            for i in id_skin_moi:
                ll = i
                vi_tri_mod1 = vi_tri_mod
                vi_tri_id_tim_kiem = b'\x00\x00' + int(i).to_bytes(4, 'little')
                vi_tri_truoc = chuoi_thay_the.find(vi_tri_id_tim_kiem) - 2
                vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+4]
                vi_tri_tim = int.from_bytes(vi_tri, 'little')
                vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+vi_tri_tim+4]

                if i[3:] == '00':
                    if vi_tri_mod1[64:65] == b'\x07':
                        i = nhap_id[:3] + nhap_id[4:]
                        vi_tri_mod1 = vi_tri_mod1[:68] + vi_tri_mod1[68:73] + b'0' + vi_tri_mod1[74:]
                        vi_tri_mod1 = vi_tri_mod1[:4] + int(ll).to_bytes(4, 'little') + vi_tri_mod1[8:]
                        vi_tri_mod1 = vi_tri_mod1[:36] + b'\x00' + vi_tri_mod1[37:]
                    else:
                        vi_tri_mod1 = vi_tri_mod1[:68] + vi_tri_mod1[68:73] + b'0' + vi_tri_mod1[75:]
                        vi_tri_mod1 = (len(vi_tri_mod1[:64] + b'\x07' + vi_tri_mod1[65:]) - 4).to_bytes(4, 'little') + vi_tri_mod1[4:64] + b'\x07' + vi_tri_mod1[65:]
                        vi_tri_mod1 = vi_tri_mod1[:4] + int(ll).to_bytes(4, 'little') + vi_tri_mod1[8:]
                        vi_tri_mod1 = vi_tri_mod1[:36] + int(ll[3:]).to_bytes(1, 'little') + vi_tri_mod1[37:]
                else:
                    vi_tri_mod1 = vi_tri_mod1[:36] + int(i[3:]).to_bytes(1, 'little') + vi_tri_mod1[37:]
                    vi_tri_mod1 = vi_tri_mod1[:4] + int(ll).to_bytes(4, 'little') + vi_tri_mod1[8:]

                chuoi_thay_the = chuoi_thay_the.replace(vi_tri, vi_tri_mod1).replace(b'\x07\x00\x00\x00301330_2', b'\x07\x00\x00\x00301330').replace(b'\x07\x00\x00\x003016702', b'\x07\x00\x00\x00301670').replace(b'$\x03\x00\x00\xf43', b'"\x03\x00\x00\xf43').replace(b'g\x03\x00\x00<A', b'f\x03\x00\x00<A').replace(b'73F8D70E20CB6B44_##\x00\x00\x00\x00\x00\x14\x00\x00\x00C748BCA5990E9431_##\x00\x07\x00\x00\x00301330', b'73F8D70E20CB6B44_##\x00\x00\x00\x00\x00\x14\x00\x00\x00C748BCA5990E9431_##\x00\x07\x00\x00\x00301320')  # 13311and16707

            with open(file_actor, 'wb') as f:
                f.write(chuoi_thay_the)
            dieukienmod = vi_tri_mod1
            tat_ca_id_skin = []
            with open(file_shop, 'rb') as f:
                chuoi_thay_the = f.read()

            if nhap_id == '16707':
                chuoi_thay_the = chuoi_thay_the.replace(bacngokhongeovmacdinh, bacngokhongeovbat5)
            elif nhap_id == '13311':
                chuoi_thay_the = chuoi_thay_the.replace(bacvaneovmacdinh, bacvaneovbat5)

            for id_tim in range(int(nhap_id[:3] + '00'), int(nhap_id[:3] + '99')):
                if str(id_tim) == nhap_id:
                    continue
                vi_tri_id_tim_kiem = id_tim.to_bytes(4, 'little') + int(nhap_id[:3]).to_bytes(2, 'little') + b'\x00\x00\x14'
                if chuoi_thay_the.find(vi_tri_id_tim_kiem) != -1:
                    tat_ca_id_skin.append(vi_tri_id_tim_kiem)

            if chuoi_thay_the.find(int(nhap_id).to_bytes(4, 'little') + int(nhap_id[:3]).to_bytes(2, 'little') + b'\x00\x00\x14') != -1:
                vi_tri_id_tim_kiem = int(nhap_id).to_bytes(4, 'little') + int(nhap_id[:3]).to_bytes(2, 'little') + b'\x00\x00\x14'
                vi_tri_truoc = chuoi_thay_the.find(vi_tri_id_tim_kiem) - 4
                vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+4]
                vi_tri_tim = int.from_bytes(vi_tri, 'little')
                ma_skin_mod = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+vi_tri_tim+4]
                for id1 in tat_ca_id_skin:
                    vi_tri_truoc = chuoi_thay_the.find(id1) - 4
                    vi_tri = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+4]
                    vi_tri_tim = int.from_bytes(vi_tri, 'little')
                    ma_skin_mod1 = chuoi_thay_the[vi_tri_truoc:vi_tri_truoc+vi_tri_tim+4]
                    ma_rpl = ma_skin_mod[:4] + id1[:4] + ma_skin_mod[8:]
                    chuoi_thay_the = chuoi_thay_the.replace(ma_skin_mod1, ma_rpl)

            with open(file_shop, 'wb') as f:
                f.write(chuoi_thay_the)
        if IDCHECK in ["10611", "13211", "13212"]:
            
            
            ID = IDCHECK
            Show = 'n'
            IDB = int(ID).to_bytes(4, byteorder="little")
            IDH = int(ID[0:3]).to_bytes(4, byteorder="little")
            Files = [file_actor, file_shop]
            print('')
            for File in Files:
                All = []
                Skin = ""
                file = open(File, "rb")
                Code = file.read()
                Find= -10
                while True:
                    Find = Code.find(b"\x00\x00"+IDH, Find+10)
                    if Find == -1: break
                    elif str(int.from_bytes(Code[Find-2:Find], byteorder="little"))[0:3] == ID[0:3]:
                        VT2 = int.from_bytes(Code[Find-6:Find-4], byteorder="little")
                        Code2 = Code[Find-6:Find-6+VT2]
                        All.append(Code2)
                        if Code2.find(IDB) != -1: Skin=Code2
                if Skin == "":
                    print("\n \033[1;31m The Id Couldn't Be Found In " + File + " file!")
                    IDNew = input("\n\033[1;36m  Enter An Alternate Skin ID: ")
                    IDK = int(IDNew).to_bytes(4, byteorder="little")
                    IDH2 = int(IDNew[0:3]).to_bytes(4, byteorder="little")
                    Find = Code.find(IDK+IDH2)
                    Sum = int.from_bytes(Code[Find-4:Find-2], byteorder="little")
                    Skin = Code[Find-4:Find-4+Sum]
                for Id in All:
                    Cache = Skin.replace(Skin[4:6], Id[4:6], 1)
                    Cache = Cache.replace(Cache[35:44], Id[35:40]+Cache[40:44],1)
                    if Show == "y":
                        if Id == Skin:
                            Cache = Cache.replace(Skin[35:44], b"\x00" * 5 + b"\x14" + b"\x00" *3, 1)
                        if Id == All[0]:
                            Cache = Cache.replace(Id[35:44], Skin[35:44], 1)
                    Hero = hex(int(ID[0:3]))[2:]
                    if len(Hero) == 3: Hero = Hero[1:3] + "0" + Hero[0]
                    else: Hero+="00"
                    Hero += "0000"
                    Hero = bytes.fromhex(Hero)
                    Cache = Cache.replace(Cache[8:12],Hero,1)
                    if File == Files[0]:
                        if Id == All[0]:
                            ID30 = b"\x07\x00\x00\x0030" + bytes(ID[0:3] + "0", "utf8") + b"\x00"
                            XYZ = Cache[64]
                            ID0 = Cache[64: 68 + XYZ]
                            Cache = Cache.replace(ID0, ID30, 1)
                            VT = Id.find(b"Hero_")
                            NumHero = Id[VT - 4]
                            Hero = Id[VT - 4: VT + NumHero]
                            Cache = Cache.replace(b"jpg\x00\x01\x00\x00\x00\x00", b"jpg\x00" + Hero)
                            Full = Cache.count(Hero)
                            if Full > 1:
                                Cache = Cache.replace(b"jpg\x00" + Hero, b"jpg\x00\x01\x00\x00\x00\x00", Full - 1)
                            EndTheCode = hex(len(Cache))
                            if len(EndTheCode) == 5:
                                EndTheCode = EndTheCode[3:5] + "0" + EndTheCode[2:3]
                            else:
                                EndTheCode = EndTheCode[4:6] + EndTheCode[2:4]
                            EndTheCode = bytes.fromhex(EndTheCode)
                            Cache = Cache.replace(Cache[0:2], EndTheCode, 1)
                    Code = Code.replace(Id, Cache, 1)
                    dieukienmod1=[]
                    dieukienmod1.append(Cache)
                    for dieukienmod2 in dieukienmod1:
                        if b"Hero" in dieukienmod2:
                             dieukienmod = dieukienmod2
                    #print(Cache)
                file = open(File, "wb")
                W = file.write(Code)



                file.close()
                

        #======================================================AM_THANH_DATABIN=============================================================
        if b"Skin_Icon_SoundEffect" in dieukienmod or b"Skin_Icon_Dialogue" in dieukienmod:
            skin_id_input = IDMODSKIN
            sound_directory = Sound_Files
            sound_files = os.listdir(sound_directory)

            all_skin_ids = []
            for i in range(21):
                if i < 10:
                    i = "0" + str(i)
                all_skin_ids.append(b"\x00" + int(skin_id_input[0:3] + str(i)).to_bytes(4, byteorder="little"))

            initial_skin_id = all_skin_ids[0]
            selected_skin_id = all_skin_ids[int(skin_id_input[3:])]

            all_skin_ids.remove(selected_skin_id)
            all_skin_ids.remove(initial_skin_id)

            for sound_file_name in sound_files:
                with open(os.path.join(sound_directory, sound_file_name), "rb") as sound_file:
                    sound_data = sound_file.read()

                if skin_id_input == "13311":
                    if sound_file_name == 'BattleBank.bytes':
                        sound_data = sound_data.replace(b'\x9dO\x14', b'\xff3\x00').replace(b'\x9eO\x14', b'\xff3\x00').replace(b'\x9fO\x14', b'\xff3\x00').replace(b'\xa0O\x14', b'\xff3\x00')
                    if sound_file_name == 'ChatSound.bytes':
                        sound_data = sound_data.replace(b'\x9fO\x14', b'\xff3\x00')
                    if sound_file_name == 'HeroSound.bytes':
                        sound_data = sound_data.replace(b'\x9fO\x14', b'\xff3\x00').replace(b'\xa0O\x14', b'\xff3\x00')
                    if sound_file_name == 'LobbyBank.bytes':
                        sound_data = sound_data.replace(b'\xa0O\x14', b'\xff3\x00')
                    if sound_file_name == 'LobbySound.bytes':
                        sound_data = sound_data.replace(b'\xa0O\x14', b'\xff3\x00')

                if skin_id_input == "16707":
                    if sound_file_name == 'BattleBank.bytes':
                        sound_data = sound_data.replace(b'/~\x19', b'CA\x00').replace(b'0~\x19', b'CA\x00').replace(b'1~\x19', b'CA\x00')
                    if sound_file_name == 'ChatSound.bytes':
                        sound_data = sound_data.replace(b'0~\x19', b'CA\x00')
                    if sound_file_name == 'HeroSound.bytes':
                        sound_data = sound_data.replace(b'0~\x19', b'CA\x00').replace(b'1~\x19', b'CA\x00')
                    if sound_file_name == 'LobbyBank.bytes':
                        sound_data = sound_data.replace(b'0~\x19', b'CA\x00')
                    if sound_file_name == 'LobbySound.bytes':
                        sound_data = sound_data.replace(b'0~\x19', b'CA\x00')

                if sound_file_name != "CoupleSound.bytes":
                    for skin_id in all_skin_ids:
                        skin_id += b"\x00" * 8
                        sound_data = sound_data.replace(skin_id, b"\x0000" + b"\x00" * 10)
                else:
                    for skin_id in all_skin_ids:
                        skin_id += b"\x02\x00\x00\x00\x01"
                        sound_data = sound_data.replace(skin_id, b"\x0000\x00\x00\x02\x00\x00\x00\x01")

                if sound_data.find(selected_skin_id) != -1:
                    if sound_file_name != "CoupleSound.bytes":
                        sound_data = sound_data.replace(initial_skin_id + b"\x00" * 8, b"\x0000" + b"\x00" * 10)
                        sound_data = sound_data.replace(selected_skin_id + b"\x00" * 8, initial_skin_id + b"\x00" * 8)
                    else:
                        sound_data = sound_data.replace(initial_skin_id + b"\x02\x00\x00\x00\x01", b"\x0000\x00\x00\x02\x00\x00\x00\x01")
                        sound_data = sound_data.replace(selected_skin_id + b"\x02\x00\x00\x00\01", initial_skin_id + b"\x02\x00\x00\x00\x01")

                with open(os.path.join(sound_directory, sound_file_name), "wb") as sound_file:
                    sound_file.write(sound_data)
            
        #=======================================================Skill_Databin============================================================
        initial_modification_time1 = os.path.getmtime(file_mod_skill1)
        initial_modification_time2 = os.path.getmtime(file_mod_skill2)

        if b"Skin_Icon_Skill" in dieukienmod or b"Skin_Icon_BackToTown" in dieukienmod:

            file_paths = [file_mod_skill1, file_mod_skill2]


            matching_files = []
            user_id = IDMODSKIN
            user_id_bytes = bytes(f"fects/{user_id[0:3]}_", "utf8")
            for file in file_paths:
                if user_id_bytes in open(file, "rb").read():
                    matching_files.append(file)
            for file in matching_files:
                if user_id == '13311':
                    with open(file, "rb") as f:
                        code_content = f.read()
                        code_content = code_content.replace(b"prefab_skill_effects/hero_skill_effects/133_direnjie/",
                                                              b"prefab_skill_effects/component_effects/13311/13311_5/")
                    with open(file, "wb") as f:
                        f.write(code_content)
                    break
                modified_codes = []
                buffer_codes = []
                with open(file, "rb") as f:
                    begin_content = f.read(140)
                    while True:
                        data_length = f.read(2)
                        if data_length == b"":
                             break
                        section_length = data_length[0] + data_length[1] * 256 + 2
                        code_section = data_length + f.read(section_length)
                        if user_id_bytes in code_section:
                             modified_codes.append(code_section)
                for code_section in modified_codes:
                    start_index = code_section.find(user_id_bytes) + 6
                    end_index = code_section.find(b"/", start_index) + 1
                    hero_name = code_section[start_index:end_index]
                    code_section = code_section.replace(b"Prefab_Skill_Effects/Hero_Skill_Effects",
                                                          b"prefab_skill_effects/hero_skill_effects")
                    code_section = code_section.replace(b"hero_skill_effects/" + hero_name,
                                                          b"hero_skill_effects/" + hero_name + bytes(user_id + "/", "utf"))
                    offset = code_section.find(b"prefab_skill_effects") - 4
                    length_change = bytes.fromhex(hex(code_section[offset] + len(user_id) + 1)[2:]) + b"\x00" * 3
                    code_section = code_section.replace(code_section[offset:offset + 4], length_change)
                    target_length = hex(len(code_section) - 4)[2:]
                    if len(target_length) == 3:
                        target_length = target_length[1:3] + "0" + target_length[0]
                    elif len(target_length) == 2:
                        target_length += "00"
                    target_length = bytes.fromhex(target_length)
                    code_section = code_section.replace(code_section[0:2], target_length, 1)
                    buffer_codes.append(code_section)
                modified_content = open(file, "rb").read()
                for index in range(len(modified_codes)):
                    modified_content = modified_content.replace(modified_codes[index], buffer_codes[index], 1)
                with open(file, "wb") as f:
                    f.write(modified_content)

        final_modification_time1 = os.path.getmtime(file_mod_skill1)
        final_modification_time2 = os.path.getmtime(file_mod_skill2)
        if len(IDMODSKIN1) == 1:
            if initial_modification_time1 == final_modification_time1:
                os.remove(file_mod_skill1)
            if initial_modification_time2 == final_modification_time2:
                os.remove(file_mod_skill2)
            elif initial_modification_time1 != final_modification_time1 or initial_modification_time2 != final_modification_time2:
                print('')
                
 







        #=====================================================Phu_Kien==============================================================
        initial_modification_time3 = os.path.getmtime(file_mod_Character)

        if IDCHECK not in ["13008", "52007"]:
            file_name = file_mod_Character
            with open(file_name, 'rb') as file:
                file_content = file.read()

            user_input = IDMODSKIN

            found_patterns = []
            Code = file_content

            for i in range(10500, 20000):
                if Code.find(i.to_bytes(4, 'little')) != -1:
                    found_patterns.append(str(i))

            for i in range(50100, 54899):
                if Code.find(i.to_bytes(4, 'little')) != -1:
                    found_patterns.append(str(i))

            relevant_patterns = [pattern for pattern in found_patterns if user_input[:3] in pattern[:3]]

            if relevant_patterns:
                first_pattern = relevant_patterns[0]
                count = 0
                total = 0
                num_relevant_patterns = len(relevant_patterns)
                
                for pattern in relevant_patterns:
                    count += file_content.count(int(pattern).to_bytes(4, 'little'))

                start_position = file_content.find(int(first_pattern).to_bytes(4, 'little')) - 155
                start_pattern = file_content[start_position:start_position+4]
                start_pattern_value = int.from_bytes(start_pattern, 'little')
                start_pattern = file_content[start_position:start_position+start_pattern_value+4]
                full_code = b''
                la = b'\x00'
                
                while True:
                    dem = b''
                    start_pattern = file_content[start_position:start_position+4]
                    start_pattern_value = int.from_bytes(start_pattern, 'little')
                    start_pattern = file_content[start_position:start_position+start_pattern_value+4]
                    remaining_code = file_content[start_pattern_value+4:]
                    file_content = remaining_code

                    for pattern in relevant_patterns:
                        if start_pattern.find(int(pattern).to_bytes(4, 'little')) == -1:
                            dem += la

                    if len(dem) == num_relevant_patterns:
                        break

                    full_code += start_pattern

                full_code = Code.replace(full_code, b'')

                with open(file_name, 'wb') as file:
                    file.write(full_code)
        final_modification_time3 = os.path.getmtime(file_mod_Character)
        if len(IDMODSKIN1) == 1:

            if initial_modification_time3 == final_modification_time3:
                os.remove(file_mod_Character)
        else:
            print('')

        #========================================================DIEU_NHAY===========================================================
        file_path = file_mod_Modtion
        skin_id = IDMODSKIN
        all_ids = []

        for i in range(21):
            if i < 10:
                all_ids.append(skin_id[0:3] + "0" + str(i))
            else:
                all_ids.append(skin_id[0:3] + str(i))

        all_patterns = []

        for id in all_ids:
            hex_id = hex(int(id))[2:]
            all_patterns.append(bytes.fromhex(f"{hex_id[2:4]}{hex_id[0:2]}0000"))

        with open(file_path, "rb") as file:
            file_start = file.read(140)
            all_codes = []
            
            while True:
                segment_length = file.read(2)
                if segment_length == b"":
                    file.close()
                    break
                segment_length_value = segment_length[0] + segment_length[1] * 256 + 2
                code = segment_length + file.read(segment_length_value)
                if all_patterns[all_ids.index(skin_id)] in code:
                    all_codes.append(code)
                elif all_patterns[0] in code:
                    all_codes.append(code)

        dance_codes = []
        dance_codes_database = []
        dance_codes_mod = []

        for code in all_codes:
            if code[0:2] in b"6\x00S\x00":
                dance_codes_database.append(code)
            else:
                dance_codes.append(code)
                dance_codes_mod.append(code)

        dance_selection = 0

        if len(dance_codes_database) > 1:
            dance_selection = int(1)-1

        if len(dance_codes_database) > 0:
            selected_dance_code = dance_codes_database[dance_selection]
            dance_mod_id = selected_dance_code[21:25]
            for code in dance_codes:
                index = dance_codes.index(code)
                for pattern in all_patterns:
                    position = code.find(pattern)
                    if position != -1:
                        code_to_replace = code[position + 4:position + 8]
                        code = code.replace(code_to_replace, dance_mod_id, 1)
                    else:
                        break
                dance_codes[index] = code
        else:
            for code in dance_codes:
                index = dance_codes.index(code)
                position_ref = code.find(all_patterns[all_ids.index(skin_id)])
                dance_mod_id = code[position_ref + 4:position_ref + 8]
                for pattern in all_patterns:
                    position = code.find(pattern)
                    if position != -1:
                        code_to_replace = code[position + 4:position + 8]
                        code = code.replace(code_to_replace, dance_mod_id, 1)
                    else:
                        break
                dance_codes[index] = code

        with open(file_path, "rb") as file:
            content = file.read()
            file.close()

        for i in range(len(dance_codes_mod)):
            content = content.replace(dance_codes_mod[i], dance_codes[i], 1)

        if len(dance_codes) + len(dance_codes_database) == 0:
            for pattern in all_patterns:
                content = content.replace(pattern, b"00\x00\x00", 1)

        with open(file_path, "wb") as file:
            file.write(content)

        #===================================================VIEN================================================================
        if len(IDMODSKIN1) == 1:
            if b'Skin_Icon_HeadFrame' in dieukienmod:
                
                if chedovien == '1':
                    data = dieukienmod
                    target = b'\x00\x00\x10\x00\x00\x00Share_'+IDCHECK.encode()+b'.jpg'
                    index = data.find(target) - 2
                    two_bytes_before = data[index:index+2]
                    print("Frame: ", two_bytes_before)
                if chedovien == '2':
                    idvien=input('Frame Need Mod: ')
                    two_bytes_before=bytes.fromhex(str(idvien))
                if two_bytes_before != b'\x00\x00':
                    if chedovien in ['1', '2']:

                        inp=file_mod_vien
                        with open(inp,'rb') as f:
                            ab=f.read()
                        a=two_bytes_before
                        i=ab.find(a)-4
                        vt=ab[i:i+4]
                        vtr=int.from_bytes(vt,byteorder='little')
                        vt1=ab[i:i+vtr]
                        id2='6500'
                        a1=bytes.fromhex(str(id2))
                        f.close()
                        i1=ab.find(a1)-4
                        vt11=ab[i1:i1+4]
                        vtr1=int.from_bytes(vt11,byteorder='little')
                        vt2=ab[i1:i1+vtr1]
                        vt1=vt1.replace(a,a1)
                        vt11=ab.replace(vt2,vt1)
                        with open(inp,'wb') as go:
                            go.write(vt11)
                else:
                    print('Frame Not Found (Please Enter Manually)')
        #===================================================Skill_Ages================================================================
        CODE_BV_HERO = b''

        def modify_skill_data(data, new_id, effect_name_lowercase, effect_name):
            if deskins == "y":
                modified_data = data.read().replace(string1, string1 + new_id).replace(string3, string3 + new_id).replace(string2, string2 + new_id).replace(string4, string4 + new_id).replace(b"""tyEffect" value="true""", b"""tyEffect" value="false""").replace(string5, string5 + new_id).replace(string7, string7 + new_id).replace(b'\r\n        <String name="clipName"', b'\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="clipName"').replace(b'\r\n        <String name="resourceName" value="', b'\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="').replace(b'\r\n        <String name="clipName"', b'\r\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>\r\n        <String name="clipName"').replace(b'\r\n        <String name="resourceName" value="', b'\r\n        <bool name="bUseTargetSkinEffect" value="true" refParamName="" useRefParam="false"/>\r\n        <String name="resourceName" value="')
                modified_data = modified_data.replace(SKIN_EFFECT_ID, IDMODSKIN)
                data = modified_data.replace(SKIN_EFFECT_ID, IDMODSKIN)
            if deskins == "n":
                modified_data = data.read().replace(string1, string1 + new_id).replace(string3, string3 + new_id).replace(string2, string2 + new_id).replace(string4, string4 + new_id).replace(b"""tyEffect" value="true""", b"""tyEffect" value="false""").replace(string5, string5 + new_id).replace(string7, string7 + new_id).replace(b'\r\n        <String name="clipName"', b'\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="clipName"').replace(b'\r\n        <String name="resourceName" value="', b'\r\n        <int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="')
                modified_data = modified_data.replace(SKIN_EFFECT_ID, IDMODSKIN)
                data = modified_data.replace(SKIN_EFFECT_ID, IDMODSKIN)
            return data

        Files_Directory_Path = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod/'
        with zipfile.ZipFile('Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/Actor_'+f'{IDMODSKIN[:3]}'+'_Actions.pkg.bytes') as File_Zip:
            File_Zip.extractall(Files_Directory_Path)
            File_Zip.close()
        HERO_NAME_LIST = os.listdir(Files_Directory_Path)
        for HERO_NAME_ITEM in HERO_NAME_LIST:
            NAME_HERO = HERO_NAME_ITEM
        if b"Skin_Icon_Skill" in dieukienmod or b"Skin_Icon_BackToTown" in dieukienmod or IDCHECK == "53702":

            new_folder_path = Files_Directory_Path
            new_files_list = os.listdir(new_folder_path)
            NAME_HERO = new_files_list
            effect_name = NAME_HERO
            for new_file_item in new_files_list:
                effect_name = new_file_item
            for name1 in NAME_HERO:
                NAME_HERO = name1
            directory_path = Files_Directory_Path + f'{NAME_HERO}' + '/skill/'
            file_name = effect_name
            effect_name_db = file_name[4:]
            effect_info = effect_name_db.capitalize()
            file_name = file_name.replace(effect_name_db, effect_info)
            new_effect_name = file_name.encode()
            effect_name = effect_name.encode()
            effect_name_lowercase = effect_name.lower()
            effect_name_lowercase = bytes(effect_name_lowercase)
            new_id = IDMODSKIN
            IDMODSKIN = IDMODSKIN.encode()
            new_id_with_slash = IDMODSKIN + b"/"
            files_in_directory = os.listdir(directory_path)
            string1 = b"hero_skill_effects/" + effect_name_lowercase + b"/"
            string2 = b"hero_skill_effects/" + effect_name + b"/"
            string3 = b"Hero_Skill_Effects/" + effect_name_lowercase + b"/"
            string4 = b"Hero_Skill_Effects/" + effect_name + b"/"
            string5 = b"hero_skill_effects/" + new_effect_name + b"/"
            string7 = b"Hero_Skill_Effects/" + new_effect_name + b"/"
            string_new = b"hero_skill_effects/" + effect_name_lowercase + b"/"
            SKIN_EFFECT_ID = IDMODSKIN + b"/" + IDMODSKIN
            New_Files = files_in_directory
            MKBV=b''
            Born = AABBCC + '_' + NAME_HERO
            Born1 = NAME_HERO
            Born2 = f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Born.xml'


                
                

            for file_item in New_Files:
                file_path = Files_Directory_Path + f'{NAME_HERO}' + '/' + 'skill/' + file_item
                giai(file_path)
                if file_item.find('Back') != -1:
                    if IDCHECK+'_Back.xml' == file_item:
                        with open(Files_Directory_Path + f'{NAME_HERO}' + '/' + 'skill/' + file_item,'rb') as f: CODE_BV_HERO=f.readlines()
                        MKBV=b'\x36'
                    continue
            for file_item in New_Files:
                file_path = Files_Directory_Path + f'{NAME_HERO}' + '/' + 'skill/' + file_item
                if IDCHECK not in ["13210"]:
                    with open(file_path, 'rb') as file:
                        modified_data = modify_skill_data(file, new_id_with_slash, effect_name_lowercase, effect_name)
                    with open(file_path, 'wb') as file:
                        file.write(modified_data)
                #with open(file_path, 'rb') as f:
                    #lines = [line.replace(b'enabled="true"', b'enabled="false"') if b'CameraShakeDuration' in line else line for line in f]
                #with open(file_path, 'wb') as f:
                    #f.writelines(lines)
                if IDCHECK == '10611':
                    if file_item == 'U1B1.xml':
                        with open(file_path, 'rb') as f:
                            rpl = f.read().replace(b'<Condition id="10" guid="2e5f463f-105d-4143-b786-e59ea8b34fa2" status="true" />', b'\r\n    <!-- '+AABBCC.encode('utf-8') +b' -->')
                            f.close()
                        with open(file_path, 'wb') as f:
                            f.write(rpl)
                    if file_item == 'A3.xml':
                        with open(file_path, 'rb') as f:
                            rpl = f.read().replace(b'<String name="clipName" value="Atk3"', b'<String name="clipName" value="Atk1"')
                            f.close()
                        with open(file_path, 'wb') as f:
                            f.write(rpl)
                if IDCHECK == '15412':
                    if file_item == 'P12E2.xml':
                        with open(file_path, 'rb') as f:
                            rpl = f.read().replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/15413_HuaMuLan_Red', b'Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15413_HuaMuLan_Red')
                            f.close()
                        with open(file_path, 'wb') as f:
                            f.write(rpl)
                if IDCHECK =='11107':
                    with open(file_path, 'rb') as f:
                        if file_item != 'Death.xml': 
                            rpl = f.read().replace(b'<String name="clipName" value="',b'<String name="clipName" value="11107/')
                    with open(file_path, 'wb') as f:
                        f.write(rpl)
                if IDCHECK =='15704':
                    with open(file_path, 'rb') as f:
                        if file_item != 'Death.xml': 
                            rpl = f.read().replace(b'<String name="clipName" value="',b'<String name="clipName" value="15704/')
                        
                    with open(file_path, 'wb') as f:
                        f.write(rpl)
                if IDCHECK =='10603':
                    with open(file_path, 'rb') as f:
                        if file_item != 'Death.xml': 
                            rpl = f.read().replace(b'<String name="clipName" value="',b'<String name="clipName" value="10603/')
                    with open(file_path, 'wb') as f:
                        f.write(rpl)
                if IDCHECK =='52007':
                    if phukien == "do":
                        with open(file_path, 'rb') as f:
                            rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/520_Veres/52007/',b'prefab_skill_effects/component_effects/52007/5200402/')
                        with open(file_path, 'wb') as f:
                            f.write(rpl)
                    if phukien == "xanh":
                        with open(file_path, 'rb') as f:
                            rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/520_Veres/52007/',b'prefab_skill_effects/component_effects/52007/5200401/')
                        with open(file_path, 'wb') as f:
                            f.write(rpl)
                if IDCHECK =='14111':
                    if file_item != 'S1.xml': 
                        with open(file_path, 'rb') as f:
                            
                               rpl = f.read().replace(b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />', b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <<<bool name="bEqual" value="false" refParamName="" useRefParam="false" />>>\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />').replace(b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />', b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />').replace(b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <<<bool name="bEqual" value="false" refParamName="" useRefParam="false" />>>\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />', b'\r\n        <int name="skinId" value="14111" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />')
                            
                        with open(file_path, 'wb') as f:
                            f.write(rpl)
                    SSS = ["A1.xml", "A2.xml", "Death.xml", "A4.xml", "S1.xml"]
                    if file_item in SSS:
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/141_diaochan/',b'prefab_skill_effects/hero_skill_effects/141_diaochan/14111/')
                        with open(file_path,'wb') as f: f.write(rpl)
                            
                    if file_item == 'S1.xml':
                        with open(file_path, 'rb') as f:
                            rpl = f.read().replace(b'guid="960a9e3c-6ad4-4438-aa64-54970f974b72" enabled="true"', b'guid="960a9e3c-6ad4-4438-aa64-54970f974b72" enabled="false"').replace(b'guid="d6b86049-520f-4922-9aad-3dfda1b6e89b" enabled="true"', b'guid="d6b86049-520f-4922-9aad-3dfda1b6e89b" enabled="false"').replace(b'\r\n    <Track trackName="NOBUFF" eventType="CheckSkillCombineConditionTick" guid="e175b61f-fe87-4276-8c6c-56b5e54e0740" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="true" />', b'\r\n    <Track trackName="NOBUFF" eventType="CheckSkillCombineConditionTick" guid="e175b61f-fe87-4276-8c6c-56b5e54e0740" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">').replace(b'\r\n      <Condition id="16" guid="1b81f7e8-2c40-45bb-bc8c-c09e4f809817" status="true" />\r\n      <Condition id="15" guid="e175b61f-fe87-4276-8c6c-56b5e54e0740" status="true" />', b'\r\n      <Condition id="15" guid="e175b61f-fe87-4276-8c6c-56b5e54e0740" status="true" />').replace(b'\r\n      <Condition id="15" guid="e175b61f-fe87-4276-8c6c-56b5e54e0740" status="true" />\r\n      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="true" />', b'\r\n      <Condition id="15" guid="e175b61f-fe87-4276-8c6c-56b5e54e0740" status="true" />').replace(b'\r\n      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="true" />\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="fcff2124-c9e2-4380-a74b-13b666d35d71">', b'\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="fcff2124-c9e2-4380-a74b-13b666d35d71">').replace(b'\r\n      <Condition id="21" guid="4e58afb2-d042-4375-8e74-4dfb7f062efe" status="true" />\r\n      <Condition id="20" guid="c26bb31c-a046-42ee-bc75-0857b87baea5" status="true" />', b'\r\n      <Condition id="20" guid="c26bb31c-a046-42ee-bc75-0857b87baea5" status="true" />').replace(b'      </Event>\r\n    </Track>\r\n    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="ec27549a-f5de-4f44-a084-6e733b00f3cc" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="23" guid="0bbb2edb-0717-4137-9771-3c0ed1c0ff0a" status="false" />\r\n      <Condition id="20" guid="c26bb31c-a046-42ee-bc75-0857b87baea5" status="true" />\r\n      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="true" />\r\n      <Event eventName="SpawnBulletTick" time="0.133" isDuration="false" guid="1d185159-f388-45bd-80c5-015c5f38670f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b12" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="0b29bfee-ffd4-4168-b83d-beb6a123d493" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="23" guid="0bbb2edb-0717-4137-9771-3c0ed1c0ff0a" status="false" />\r\n      <Condition id="20" guid="c26bb31c-a046-42ee-bc75-0857b87baea5" status="true" />\r\n      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="true" />\r\n      <Event eventName="SpawnBulletTick" time="0.133" isDuration="false" guid="02b4f73c-2d40-48b4-8eb1-383506c304ee">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b22" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>', b'      </Event>\r\n    </Track>\r\n    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="ec27549a-f5de-4f44-a084-6e733b00f3cc" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="23" guid="0bbb2edb-0717-4137-9771-3c0ed1c0ff0a" status="false" />\r\n      <Condition id="20" guid="c26bb31c-a046-42ee-bc75-0857b87baea5" status="true" />\r\n      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="true" />\r\n      <Event eventName="SpawnBulletTick" time="0.133" isDuration="false" guid="1d185159-f388-45bd-80c5-015c5f38670f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b12" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="0b29bfee-ffd4-4168-b83d-beb6a123d493" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="23" guid="0bbb2edb-0717-4137-9771-3c0ed1c0ff0a" status="false" />\r\n      <Condition id="20" guid="c26bb31c-a046-42ee-bc75-0857b87baea5" status="true" />\r\n      <Condition id="8" guid="fd20a444-1b70-42c0-94a6-4783d23ab256" status="true" />\r\n      <Event eventName="SpawnBulletTick" time="0.133" isDuration="false" guid="02b4f73c-2d40-48b4-8eb1-383506c304ee">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b22" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="ec27549a-f5de-4f44-a084-6e733b00f3cc" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="20" guid="c26bb31c-a046-42ee-bc75-0857b87baea5" status="true" />\r\n      <Condition id="7" guid="2a6ab8c3-3cba-4002-95c5-b9f3cfa702ef" status="true" />\r\n      <Event eventName="SpawnBulletTick" time="0.133" isDuration="false" guid="1d185159-f388-45bd-80c5-015c5f38670f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b12" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="0b29bfee-ffd4-4168-b83d-beb6a123d493" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="20" guid="c26bb31c-a046-42ee-bc75-0857b87baea5" status="true" />\r\n      <Condition id="7" guid="2a6ab8c3-3cba-4002-95c5-b9f3cfa702ef" status="true" />\r\n      <Event eventName="SpawnBulletTick" time="0.133" isDuration="false" guid="02b4f73c-2d40-48b4-8eb1-383506c304ee">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/s1b22" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>')
                            f.close()
                        with open(file_path, 'wb') as f:
                            f.write(rpl)
                            
                            
                            
                if IDCHECK =='13011':
                    if file_item == ( '13011_Back.xml'):
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'  <Action tag="" length="9.000" loop="false">\r\n    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="2b767094-bee5-4ffd-807c-e2759b06b84e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="SetObjectDirectionTick" time="0.000" isDuration="false" guid="0b9090b0-a50f-4a21-a836-d5fee4adaf3e">\r\n        <TemplateObject name="targetId" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="rotationY" value="175" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="SetObjectDirectionTick0" eventType="SetObjectDirectionTick" guid="b781bec7-a0a4-47ea-b14f-22a5487ab7f6" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="SetObjectDirectionTick" time="7.000" isDuration="false" guid="d53624dd-ba5b-44a9-87e4-3636c5dc4ec1">\r\n        <TemplateObject name="targetId" id="0" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="rotationY" value="30" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>',b'  <Action tag="" length="1.000" loop="false">\r\n    <Track trackName="CheckSkinIdTick1" eventType="CheckSkinIdTick" guid="46c0a671-a81f-4cce-9362-3cf8512a40cd" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkinIdTick" time="0.000" isDuration="false" guid="2353be74-4ba4-4485-876c-a3de9c859e36">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skinId" value="13011" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="f7cc90e1-0903-43fb-91ec-7fa8e0998295" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="0" guid="46c0a671-a81f-4cce-9362-3cf8512a40cd" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.000" isDuration="true" guid="f720cf9e-c348-4163-a5e5-c13004eafd10">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/130_gongbenwuzang/13011/gongbenwuzang_attack01_spell01_2" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.500" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="bUseRealScaling" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="bOnlyFollowPos" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="b1stTickParentRot" value="true" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>')
                        with open(file_path, 'wb') as f:
                             f.write(rpl)
                    if file_item == ( 'UCS.xml'):
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'  <Action tag="" length="0.600" loop="false">\r\n    <Track trackName="CameraShakeDuration0" eventType="CameraShakeDuration" guid="20c9a92f-6c8b-4320-bec5-eb48f5e4b418" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CameraShakeDuration" time="0.000" length="0.600" isDuration="true" guid="54e19b05-d68f-4c09-90dd-4ad5d3422cae">\r\n        <bool name="useMainCamera" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="filter_self" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="canBeCover" value="false" refParamName="" useRefParam="false" />\r\n        <Vector3 name="shakeRange" x="0.200" y="0.400" z="0.200" refParamName="" useRefParam="false" />\r\n        <bool name="bUseCustomCurveMode" value="true" refParamName="" useRefParam="false" />\r\n        <String name="curvesPath" value="Prefab_Skill_Assets/CameraShakeCurves/nor04" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>',b'  <Action tag="" length="1.000" loop="false">\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="f7cc90e1-0903-43fb-91ec-7fa8e0998295" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.000" isDuration="true" guid="f720cf9e-c348-4163-a5e5-c13004eafd10">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/130_gongbenwuzang/13011/gongbenwuzang_attack01_spell01_1" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.500" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="bUseRealScaling" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="bOnlyFollowPos" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="b1stTickParentRot" value="true" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>')
                        with open(file_path, 'wb') as f:
                             f.write(rpl)
                    #if file_item == ( 'UFX.xml'):
                        #with open(file_path, 'rb') as f: rpl = f.read().replace(b'  </Action>\r\n</Project>',b'    <Track trackName="CameraShakeDuration0" eventType="CameraShakeDuration" guid="20c9a92f-6c8b-4320-bec5-eb48f5e4b418" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CameraShakeDuration" time="0.533" length="0.600" isDuration="true" guid="54e19b05-d68f-4c09-90dd-4ad5d3422cae">\r\n        <bool name="useMainCamera" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="filter_self" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="canBeCover" value="false" refParamName="" useRefParam="false" />\r\n        <Vector3 name="shakeRange" x="0.200" y="0.400" z="0.200" refParamName="" useRefParam="false" />\r\n        <bool name="bUseCustomCurveMode" value="true" refParamName="" useRefParam="false" />\r\n        <String name="curvesPath" value="Prefab_Skill_Assets/CameraShakeCurves/nor04" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>')
                        #with open(file_path, 'wb') as f:

                             f.write(rpl)
                    if file_item in ["S2.xml", "S21.xml", "S22.xml"]:
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'"PlayAnimDuration" guid="9d243092-f160-4189-a9da-f132595032c9" enabled="true"',b'"PlayAnimDuration" guid="9d243092-f160-4189-a9da-f132595032c9" enabled="false"').replace(b'        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="false" refParamName="" useRefParam="false" />', b'').replace(b'        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />', b'        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />').replace(b'        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="false" refParamName="" useRefParam="false" />', b'     <bool name="bEqual" value="false" refParamName="" useRefParam="false" />').replace(b'        <bool name="useNegateValue" value="false" refParamName="" useRefParam="false" />\r\n        <Array name="skinIdArray" refParamName="" useRefParam="false" type="int" />\r\n      </Event>\r\n    </Track>', b'      </Event>\r\n    </Track>')
                        with open(file_path, 'wb') as f:
                             f.write(rpl)
                    if file_item == ( 'S2.xml'):
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'    <Track trackName="13011_22" eventType="PlayAnimDuration" guid="346663c5-53c1-4f57-9196-8ea5aec7bafb" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="5" guid="1d2453a9-f234-4489-90f4-dde12f642d17" status="true" />',b'    <Track trackName="13011_22" eventType="PlayAnimDuration" guid="346663c5-53c1-4f57-9196-8ea5aec7bafb" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">').replace(b'    <Track trackName="ChangeSpringDuration5" eventType="ChangeSpringDuration" guid="fc54f26a-3264-4759-b526-2609b8aa6fc0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="5" guid="1d2453a9-f234-4489-90f4-dde12f642d17" status="true" />', b'    <Track trackName="ChangeSpringDuration5" eventType="ChangeSpringDuration" guid="fc54f26a-3264-4759-b526-2609b8aa6fc0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">')
                        with open(file_path, 'wb') as f:
                             f.write(rpl)
                    if file_item == ( 'S21.xml'):
                        ABCD = []
                        with open(file_path, 'rb') as file:
                            xml_bytes = file.read()#.decode('utf-8')
                            start_phrase = b'<Track trackName="'
                            end_phrase = b'</Track>' 
                            start_index = xml_bytes.find(start_phrase)
                            end_index = xml_bytes.find(end_phrase, start_index)
                            while start_index != -1 and end_index != -1:
                                track_text = xml_bytes[start_index:end_index + len(end_phrase)]
                                start_index = xml_bytes.find(start_phrase, end_index)
                                end_index = xml_bytes.find(end_phrase, start_index)
                                if b'a07302eb-cb3b-4146-9996-d018f92247aa' in track_text:
                                    ABCD.append(track_text)
                                    #print(track_text)
                                    #track_text = track_text.encode()
                        for track_text in ABCD:
                            with open(file_path, 'rb') as file:
                                xml_bytes = file.read()
                            modified_data =b'    <Track trackName="\xe5\xa4\xa7\xe9\x83\xa8\xe5\x88\x86\xe7\x9a\xae\xe8\x82\xa4\xe7\x9a\x84\xe7\x89\xb9\xe6\x95\x88\xe5\xad\x90\xe5\xbc\xb91" eventType="SpawnBulletTick" guid="7255b095-38a9-420b-96c1-0fc359ef272d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="6" guid="6b3a8d20-c4c6-4d17-83e1-b60201720bb2" status="true" />\r\n      <Event eventName="SpawnBulletTick" time="0.000" isDuration="false" guid="0fe84e6b-f4b9-491b-a802-c85858c85dd3">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/130_gongbenwuzang/skill/UCS" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>'
                            modified_data1 = xml_bytes.replace(track_text, modified_data)
                            with open(file_path, 'wb') as file:
                                file.write(modified_data1)
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'    <Track trackName="13011_22" eventType="PlayAnimDuration" guid="346663c5-53c1-4f57-9196-8ea5aec7bafb" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="5" guid="753f3471-d461-40e5-b0d9-9305c2d4615d" status="true" />',b'    <Track trackName="13011_22" eventType="PlayAnimDuration" guid="346663c5-53c1-4f57-9196-8ea5aec7bafb" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">').replace(b'prefab_skill_effects/hero_skill_effects/130_gongbenwuzang/13011/GongBenWuZang_attack01_spell01_2', b'HSM').replace(b'    <Track trackName="ChangeSpringDuration6" eventType="ChangeSpringDuration" guid="6d7eb5bc-f19e-4c58-ac74-9ef746b58e86" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="5" guid="753f3471-d461-40e5-b0d9-9305c2d4615d" status="true" />', b'    <Track trackName="ChangeSpringDuration6" eventType="ChangeSpringDuration" guid="6d7eb5bc-f19e-4c58-ac74-9ef746b58e86" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">')
                        with open(file_path, 'wb') as f:
                             f.write(rpl)
                    if file_item == ( 'S22.xml'):
                        ABCD = []
                        with open(file_path, 'rb') as file:
                            xml_bytes = file.read()#.decode('utf-8')
                            start_phrase = b'<Track trackName="'
                            end_phrase = b'</Track>' 
                            start_index = xml_bytes.find(start_phrase)
                            end_index = xml_bytes.find(end_phrase, start_index)
                            while start_index != -1 and end_index != -1:
                                track_text = xml_bytes[start_index:end_index + len(end_phrase)]
                                start_index = xml_bytes.find(start_phrase, end_index)
                                end_index = xml_bytes.find(end_phrase, start_index)
                                if b'a07302eb-cb3b-4146-9996-d018f92247aa' in track_text:
                                    ABCD.append(track_text)
                                    #print(track_text)
                                    #track_text = track_text.encode()
                        for track_text in ABCD:
                            if b'guid="6d1d27e2-efcc-4365-a0a0-c650d4ca16ef"' in track_text:
                                continue
                            with open(file_path, 'rb') as file:
                                xml_bytes = file.read()
                            modified_data = b'    <Track trackName="\xe5\xa4\xa7\xe9\x83\xa8\xe5\x88\x86\xe7\x9a\xae\xe8\x82\xa4\xe7\x9a\x84\xe7\x89\xb9\xe6\x95\x88\xe5\xad\x90\xe5\xbc\xb92" eventType="SpawnBulletTick" guid="7255b095-38a9-420b-96c1-0fc359ef272d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="6" guid="8d5e99b6-7c14-4d52-930f-cf8653835641" status="true" />\r\n      <Event eventName="SpawnBulletTick" time="0.000" isDuration="false" guid="0fe84e6b-f4b9-491b-a802-c85858c85dd3">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="ActionName" value="prefab_characters/prefab_hero/130_gongbenwuzang/skill/13011_back" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>'              
                            modified_data1 = xml_bytes.replace(track_text, modified_data)
                            with open(file_path, 'wb') as file:
                                file.write(modified_data1)
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'    <Track trackName="13011_22" eventType="PlayAnimDuration" guid="346663c5-53c1-4f57-9196-8ea5aec7bafb" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="5" guid="cea185dc-6db5-47e8-9a5f-fbf0f2aabacb" status="true" />',b'    <Track trackName="13011_22" eventType="PlayAnimDuration" guid="346663c5-53c1-4f57-9196-8ea5aec7bafb" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">').replace(b'    <Track trackName="ChangeSpringDuration7" eventType="ChangeSpringDuration" guid="4e903727-596c-4844-9b0c-c882335080b9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="5" guid="cea185dc-6db5-47e8-9a5f-fbf0f2aabacb" status="true" />', b'    <Track trackName="ChangeSpringDuration7" eventType="ChangeSpringDuration" guid="4e903727-596c-4844-9b0c-c882335080b9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">')
                        with open(file_path, 'wb') as f:
                             f.write(rpl)
                    if file_item == ( 'S2B1.xml'):
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'      </Event>\r\n    </Track>\r\n    <Track trackName="AutoY" eventType="HitTriggerTick" guid="9749148c-8e56-47f6-89e8-70c4ed334ef0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="62578072-d0be-44f1-bf0d-d8c1de538873">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="130006" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>',b'      </Event>\r\n    </Track>').replace(b'  <Action tag="" length="2.000" loop="false">', b'  <Action tag="" length="2.000" loop="false">\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="39adb49e-b73a-4b00-ab89-1cc90a2f6860" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.000" isDuration="true" guid="879c7677-a1d1-4da3-a387-a65149b7d0b7">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/130_gongbenwuzang/13011/gongbenwuzang_attack01_spell01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.500" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="bUseRealScaling" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="bOnlyFollowPos" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="b1stTickParentRot" value="true" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>')
                        with open(file_path, 'wb') as f:
                             f.write(rpl)
                    if file_item == ('U1.xml'):
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'"SpawnBulletTick" guid="7255b095-38a9-420b-96c1-0fc359ef272d" enabled="true"',b'"SpawnBulletTick" guid="7255b095-38a9-420b-96c1-0fc359ef272d" enabled="false"')
                        with open(file_path, 'wb') as f:
                             f.write(rpl)

                             
                if IDCHECK[:3] =='524':
                    if file_item == 'A1E9.xml':
                        with open(file_path, 'rb') as f:
                             rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/524_Capheny/'+IDCHECK.encode()+b'/Atk1_FireRange',b'prefab_skill_effects/hero_skill_effects/524_Capheny/Atk1_FireRange')
                             f.close()
                        with open(file_path, 'wb') as f:
                             f.write(rpl)
                if IDCHECK[:3] =='537':
                    if file_item == 'S12.xml':
                        with open(file_path, 'rb') as f:
                             rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1_S',b'prefab_skill_effects/hero_skill_effects/537_Trip/Trip_attack_spell01_1_S')
                             f.close()
                        with open(file_path, 'wb') as f:
                             f.write(rpl)

                if IDCHECK =='11119':
                    if file_item =='A1B1.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false" />', b'<String name="prefabName" value="prefab_skill_effects/hero_skill_effects/111_sunshangxiang/11119/sunshangxiang_fly_01b" refParamName="" useRefParam="false" />\r\n        <Vector3i name="translation" x="0" y="750" z="0" refParamName="" useRefParam="false" />')
                        with open(file_path,'wb') as f: f.write(rpl)
                    if file_item == 'A2B1.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false" />',b'<String name="prefabName" value="prefab_skill_effects/hero_skill_effects/111_sunshangxiang/11119/sunshangxiang_fly_01b" refParamName="" useRefParam="false" />\r\n        <Vector3i name="translation" x="0" y="700" z="0" refParamName="" useRefParam="false" />')
                        with open(file_path,'wb') as f: f.write(rpl)
                             
                             
                if IDCHECK[:3] =='544':
                    if file_item =='U1E0.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'Bone_Whisk03',b'Bone_Weapon01')
                        with open(file_path,'wb') as f: f.write(rpl)
                    if file_item == 'A4B1.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/544_Painter/'+IDCHECK.encode()+b'/Painter_Atk4_blue',b'prefab_skill_effects/hero_skill_effects/544_Painter/Painter_Atk4_blue').replace(b'prefab_skill_effects/hero_skill_effects/544_Painter/'+IDCHECK.encode()+b'/Painter_Atk4_red',b'prefab_skill_effects/hero_skill_effects/544_Painter/Painter_Atk4_red')
                        with open(file_path,'wb') as f: f.write(rpl)
                if IDCHECK == '13112':
                    if file_item =='P1E5.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'Bone_Blade',b'Bip001 Prop1').replace(b'Bone_Weapon01',b'Bip001 Prop1')
                        with open(file_path,'wb') as f: f.write(rpl)
                if IDCHECK == '13111':
                    if file_item =='P1E5.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'Bone_Blade',b'Bone_Weapon01').replace(b'Bip001 Prop1',b'Bone_Weapon01')
                        with open(file_path,'wb') as f: f.write(rpl)
                if IDCHECK == '13116':
                    if file_item =='P1E5.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'Bone_Blade',b'Bip001 Prop1').replace(b'Bone_Weapon01',b'Bip001 Prop1')
                        with open(file_path,'wb') as f: f.write(rpl)
                if IDCHECK == '13311':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/133_direnjie/13311/',b'prefab_skill_effects/component_effects/13311/13311_5/').replace(b'"Play_DiRenJie_Attack_1"', b'"Play_DiRenJie_Attack_1_Skin11_AW2"').replace(b'"Play_DiRenJie_Voice_Short"', b'"Play_DiRenJie_Voice_Short_Skin11_AW3"').replace(b'"Play_DiRenJie_Attack_Hit_1"', b'"Play_DiRenJie_Attack_Hit_1_Skin11_AW2"').replace(b'"Play_DiRenJie_Skill_A"', b'"Play_DiRenJie_Skill_A_Skin11_AW2"').replace(b'"Play_DiRenJie_Voice_Anger"', b'"Play_DiRenJie_Voice_Anger_Skin11_AW3"').replace(b'"Play_DiRenJie_Skill_A_Hit"', b'"Play_DiRenJie_Skill_A_Hit_Skin11_AW2"').replace(b'"Play_DiRenJie_Attack_Hit_2"', b'"Play_DiRenJie_Attack_Hit_2_Skin11_AW2"').replace(b'"Play_DiRenJie_Skill_B"', b'"Play_DiRenJie_Skill_B_Skin11_AW2"').replace(b'"Play_DiRenJie_Skill_B_Hit"', b'"Play_DiRenJie_Skill_B_Hit_Skin11_AW2"').replace(b'"Play_DiRenJie_Card_Red"', b'"Play_DiRenJie_Card_Red_Skin11_AW2"').replace(b'"Play_DiRenJie_Card_Blue"', b'"Play_DiRenJie_Card_Blue_Skin11_AW2"').replace(b'"Play_DiRenJie_Card_Yellow"', b'"Play_DiRenJie_Card_Yellow_Skin11_AW2"').replace(b'"Play_DiRenJie_Voice_Dead"', b'"Play_DiRenJie_Voice_Dead_Skin11_AW3"').replace(b'"Play_DiRenJie_Voice_Skill_B"', b'"Play_DiRenJie_Voice_Skill_B_Skin11_AW3"').replace(b'"Play_DiRenJie_Skill_C"', b'"Play_DiRenJie_Skill_C_Skin11_AW2"').replace(b'"Play_DiRenJie_Voice_Skill_C"', b'"Play_DiRenJie_Voice_Skill_C_Skin11_AW3"').replace(b'"Play_DiRenJie_Skill_C_Hit"', b'"Play_DiRenJie_Skill_C_Hit_Skin11_AW2"')
                        with open(file_path,'wb') as f: f.write(rpl)
                if IDCHECK =='13311':
                    if "U1" in file_item:
                        if phukienv == "vangv":
                            with open(file_path, 'rb') as f:
                                rpl = f.read().replace(b'prefab_skill_effects/component_effects/13311/13311_5/',b'prefab_skill_effects/component_effects/13311/1331101/')
                            with open(file_path, 'wb') as f:
                                f.write(rpl)
                        if phukienv == "dov":
                            with open(file_path, 'rb') as f:
                                rpl = f.read().replace(b'prefab_skill_effects/component_effects/13311/13311_5/',b'prefab_skill_effects/component_effects/13311/1331102/')
                            with open(file_path, 'wb') as f:
                                f.write(rpl)
                if IDCHECK == '16707':
                    with open(file_path, 'rb') as f: rpl = f.read().replace(b'prefab_skill_effects/hero_skill_effects/167_wukong/16707/',b'prefab_skill_effects/component_effects/16707/16707_5/').replace(b'"Play_Back_WuKong"', b'"Play_Back_WuKong_Skin7_AW3"').replace(b'"Play_WuKong_Attack_1"', b'"Play_WuKong_Attack_1_Skin7_AW3"').replace(b'"Play_WuKong_VO_Short"', b'"Play_WuKong_VO_Short_Skin7_AW4"').replace(b'"Play_WuKong_Attack_Hit_1"', b'"Play_WuKong_Attack_Hit_1_Skin7_AW3"').replace(b'"Play_WuKong_Attack_2"', b'"Play_WuKong_Attack_2_Skin7_AW3"').replace(b'"Play_WuKong_VO_Anger"', b'"Play_WuKong_VO_Anger_Skin7_AW4"').replace(b'"Play_WuKong_Skill_Passive_Hit1"', b'"Play_WuKong_Skill_Passive_Hit1_Skin7_AW3"').replace(b'"Play_WuKong_Skill_Passive_Hit2"', b'"Play_WuKong_Skill_Passive_Hit2_Skin7_AW3"').replace(b'"Play_WuKong_Skill_Passive_Hit3"', b'"Play_WuKong_Skill_Passive_Hit3_Skin7_AW3"').replace(b'"Play_WuKong_Skill_B_2"', b'"Play_WuKong_Skill_B_2_Skin7_AW3"').replace(b'"Play_WuKong_Skill_B_Hit"', b'"Play_WuKong_Skill_B_Hit_Skin7_AW3"').replace(b'"Play_WuKong_VO_Dead"', b'"Play_WuKong_VO_Dead_Skin7_AW4"').replace(b'"Play_WuKong_Skill_A_2"', b'"Play_WuKong_Skill_A_2_Skin7_AW3"').replace(b'"Play_WuKong_Skill_A_Hit"', b'"Play_WuKong_Skill_A_Hit_Skin7_AW3"').replace(b'"Play_WuKong_Skill_A_1"', b'"Play_WuKong_Skill_A_1_Skin7_AW3"').replace(b'"Play_WuKong_VO_Skill_A"', b'"Play_WuKong_VO_Skill_A_Skin7_AW4"').replace(b'"Play_WuKong_Skill_A_Run"', b'"Play_WuKong_Skill_A_Run_Skin7_AW3"').replace(b'"Stop_WuKong_Skill_A_Run"', b'"Stop_WuKong_Skill_A_Run_Skin7_AW3"').replace(b'"Play_WuKong_Skill_B_1"', b'"Play_WuKong_Skill_B_1_Skin7_AW3"').replace(b'"Play_WuKong_VO_Skill_B"', b'"Play_WuKong_VO_Skill_B_Skin7_AW4"').replace(b'"Play_WuKong_Skill_C"', b'"Play_WuKong_Skill_C_Skin7_AW3"').replace(b'"Play_WuKong_VO_Skill_C"', b'"Play_WuKong_VO_Skill_C_Skin7_AW4"').replace(b'"Play_WuKong_Skill_C_01"', b'"Play_WuKong_Skill_C_01_Skin7_AW3"').replace(b'"Play_WuKong_Skill_C_02"', b'"Play_WuKong_Skill_C_02_Skin7_AW3"').replace(b'"Play_WuKong_Skill_C_Hit"', b'"Play_WuKong_Skill_C_Hit_Skin7_AW3"')
                    with open(file_path,'wb') as f: f.write(rpl)
                    if file_item =='U1B0.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'<String name="resourceName" value="prefab_skill_effects/component_effects/16707/16707_5/wukong_attack_spell03" refParamName="" useRefParam="false" />', b'<String name="resourceName" value="prefab_skill_effects/component_effects/16707/16707_5/wukong_attack_spell03_1" refParamName="" useRefParam="false" />\r\n         <String name="resourceName2" value="prefab_skill_effects/component_effects/16707/16707_5/wukong_attack_spell03_1" refParamName="" useRefParam="false" />')
                        with open(file_path,'wb') as f: f.write(rpl)
                if IDCHECK == '13609':
                    if file_item =='U1B1.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03" refParamName="" useRefParam="false" />', b'        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_1" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_2" refParamName="" useRefParam="false" />').replace(b'        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_e" refParamName="" useRefParam="false" />', b'        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_e" refParamName="" useRefParam="false" />\r\n        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_1_e" refParamName="" useRefParam="false" />\r\n        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/136_wuzetian/13609/wuzetian_attack_spell03_2_e" refParamName="" useRefParam="false" />')
                        with open(file_path,'wb') as f: f.write(rpl)
                    if file_item =='S1B1.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'<Vector3 name="scaling" x="1.300" y="1.000" z="1.000" refParamName="" useRefParam="false" />', b'<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false" />')
                        with open(file_path,'wb') as f: f.write(rpl)
                if IDCHECK == '13210':
                    if file_item =='S1E1.xml':
                        with open(file_path, 'rb') as f: rpl = f.read().replace(b'\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_hurt_01" refParamName="" useRefParam="false" />', b'\r\n        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/132_MaKeBoLuo/13210/Makeboluo_spell01_hurt_01" refParamName="" useRefParam="false" />\r        <String name="resourceName2" value="Prefab_Skill_Effects/Hero_Skill_Effects/132_MaKeBoLuo/13210/Makeboluo_spell01_hurt_02" refParamName="" useRefParam="false" />\r        <String name="resourceName3" value="Prefab_Skill_Effects/Hero_Skill_Effects/132_MaKeBoLuo/13210/Makeboluo_spell01_hurt_03" refParamName="" useRefParam="false" />')
                        with open(file_path,'wb') as f: f.write(rpl)
                if IDCHECK == '13210':
                    def checkskin(a,ID):
                        pz=a.split(b'</Track>')
                        b=[]
                        for code in pz:
                            if b'CheckSkinIdTick' in code and b'<int name="skinId" value="'+ID in code and b'bEqual" value="f' not in code:
                                a=a.replace(code,code.replace(b'CheckSkinIdTick',b'CheckHeroIdTick').replace(b'<int name="skinId" value="'+ID,b'<int name="heroId" value="'+ID[:3]))
                            if b'CheckSkinIdTick' in code and b'<int name="skinId" value="'+ID in code and b'bEqual" value="f' in code:
                                condition=code[code.find(b'guid="'):code.find(b'" enabled="',code.find(b'guid="'))]
                                b.append(condition)
                        p=a.find(b'<Track trackName="')
                        while p!=-1:
                            p2=a.find(b'</Track>',p)
                            code=a[p:p2]
                            for z in b:
                                if z in code :
                                    a=a.replace(code,code.replace(b'" enabled="true"',b'" enabled="false"'))
                            p=a.find(b'<Track trackName="',p2)
                        return a
                    def fix_condition(a):
                        p=a.find(b'<Condition id="')
                        while p!=-1:
                            p2=a.find(b'" guid="',p)
                            condition=a[p:a.find(b'" status="',p)]
                            ID=a[p2:a.find(b'" status="',p2)]
                            check=a[p+15:a.find(b'"',p+15)]
                            if len(ID)>10:
                                pz=a.split(b'</Track>')
                                for i in range(len(pz)):
                                    if ID in pz[i] and condition not in pz[i]:
                                        if check.decode()!=str(i):
                                            a=a.replace(condition,b'<Condition id="'+str(i).encode('utf-8')+ID)
                            p=a.find(b'<Condition id="',p2)
                        return a
                    with open(file_path,'rb') as f:
                        a=f.read()
                        if file_item in['S1B0.xml','S11B0.xml','S12B0.xml']:
                            a=a.replace(b'hero_skill_effects/132_makeboluo/',b'hero_skill_effects/132_makeboluo/HSM/')
                            a=a.replace(b'  </Action>',b'    <Track trackName="1" eventType="CheckSkillCombineConditionTick" guid="Mod_By_HSM_Mod_132111" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="b0dbc04b-5f6d-4610-a37b-b5240f304825">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132111" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="2" eventType="CheckSkillCombineConditionTick" guid="Mod_By_HSM_Mod_132112" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="fb9ffe1e-fc80-463c-aa04-7e4749711ab8">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132112" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="3" eventType="CheckSkillCombineConditionTick" guid="Mod_By_HSM_Mod_132113" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="6786a65e-f11b-484a-a0ae-613c7521f69e">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineId" value="132113" refParamName="" useRefParam="false" />\r\n        <Enum name="checkOPType" value="3" refParamName="" useRefParam="false" />\r\n        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132111" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_spell01_attack_01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132111" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_spell01_attack_01_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132112" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_spell01_attack_02" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132112" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_spell01_attack_02_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132113" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_spell01_attack_03" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132113" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_spell01_attack_03_1'+b'  </Action>')
                            a=a.replace(b'  </Action>',b'" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132111" status="false" />\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132112" status="false" />\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132113" status="false" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_spell01_attack_01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="91aaf49d-c92c-4481-9957-e3b0448f1479" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132111" status="false" />\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132112" status="false" />\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132113" status="false" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="1.400" isDuration="true" guid="51311a35-66be-4940-9a41-431050e09e2b">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_spell01_attack_01_1" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="f92f38f7-c71a-4ea3-abfc-c8e4eb5b3865" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132111" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="9b862449-dea5-4cee-b1f0-8b1b3724ca8f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_03" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba2 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="c7107416-30e0-4ee8-83fa-5f97bb948faf" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132112" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="4a8d55af-a3b6-4c1a-b7b9-830ea761ccf9">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_01" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba3 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="bca0dd8d-b83a-49da-982c-6cadaef3966a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132113" status="true" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="129a0664-39ba-43af-9d93-43c6b7d64878">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_02" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1 \xe9\x9f\xb3\xe6\x95\x88" eventType="PlayHeroSoundTick" guid="f92f38f7-c71a-4ea3-abfc-c8e4eb5b3865" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132111" status="false" />\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132112" status="false" />\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132113" status="false" />\r\n      <Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false" guid="9b862449-dea5-4cee-b1f0-8b1b3724ca8f">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="sourceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="eventName" value="Play_13210_Hayate_SkillA_03" refParamName="" useRefParam="false" />\r\n        <bool name="useSkinSwitch" value="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="T2\xe9\x9a\x8f\xe6\x9c\xba1" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132111" status="false" />\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132112" status="false" />\r\n      <Condition id="HSM" guid="Mod_By_HSM_Mod_132113" status="false" />\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132111" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'+b'  </Action>')
                            a=fix_condition(a)
                        elif file_item =='A1.xml':
                            a=a.replace(b'  </Action>',b'    <Track trackName="HSM" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132111" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132113" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132112" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'+b'  </Action>')
                        elif file_item =='A2.xml':
                            a=a.replace(b'  </Action>',b'    <Track trackName="HSM" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132112" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132111" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132113" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'+b'  </Action>')
                        elif file_item =='A3.xml':
                            a=a.replace(b'  </Action>',b'    <Track trackName="HSM" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132113" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132111" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="RemoveBuffTick0" eventType="RemoveBuffTick" guid="3de6a2a7-e28c-4002-b42c-5fa3bdc98217" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="RemoveBuffTick" time="0.000" isDuration="false" guid="13b2f181-602e-4ada-b268-cc5399b4d39d">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="buffId" value="132112" refParamName="" useRefParam="false" />\r\n        <int name="BuffLayer" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'+b'  </Action>')
                        elif file_item =='S1B1.xml':
                            a=a.replace(b'  </Action>',b'    <Track trackName="HSM" eventType="HitTriggerTick" guid="810de6b2-8b68-4614-8762-84bbafe2e77a" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="2a780e78-eb27-468a-aee5-3567a6e0debf" status="true" />\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="06468bb9-532f-4c15-819f-4ea3434f2a47">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132111" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="HSM" eventType="HitTriggerTick" guid="8593531d-6223-4e88-8100-271908335727" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="5" guid="c8ec3b75-100a-4421-a2a4-cc36f4c7fbcc" status="true" />\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="e9ad175b-19a2-4349-bbe2-9943b68b27d2">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132112" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="HSM" eventType="HitTriggerTick" guid="1d752369-b04e-4751-9c2e-bf07c90d34dd" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="7" guid="ef1cbc7a-93c8-41d8-ba2d-5d2fe605b325" status="true" />\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="5f9271af-ec05-4d4f-af1e-70941661041c">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="132113" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle6" eventType="TriggerParticle" guid="536a47d0-fdc5-441e-b382-53866c442844" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="3" guid="c83eb09d-73c4-461b-938f-f73070abc892" status="false" />\r\n      <Condition id="5" guid="c83eb09d-73c4-461b-938f-f73070abc892" status="false" />\r\n      <Condition id="7" guid="c83eb09d-73c4-461b-938f-f73070abc892" status="false" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="0.700" isDuration="true" guid="38ee198d-1e31-45e7-857a-06c00d811da8">\r\n        <TemplateObject name="targetId" id="2" objectName="bullet" isTemp="true" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/Makeboluo_spell01_bullet_01" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'+b'  </Action>')
                            a=a.replace(b'        <bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />\r\n',b'')
                        elif file_item =='S1E1.xml':
                            pass
                        elif file_item=='S1B0.xml':
                            pass
                        else:
                            a=checkskin(a,b'13210')
                        a=a.replace(b'hero_skill_effects/132_makeboluo/',b'hero_skill_effects/132_makeboluo/13210/')
                        with open(file_path,'wb') as f:f.write(a)
            if fixlag1 == 'y':
                path=directory_path
                ID_Born=IDCHECK
                ID_Born=ID_Born[0:3]
                Path1=Born2
                giai(Born2)
                path11=list(os.listdir(path))
                for file1 in path11:
                    if file1.endswith("Back.xml"): path11.remove(file1)
                    if file1.endswith("Born.xml"): path11.remove(file1)
                    if file1.endswith("Haste.xml"): path11.remove(file1)
                    if os.path.isdir(os.path.join(path, file1)): path11.remove(file1)
                Code=[]
                for file1 in path11:
                    if 'Back' in file1 or 'Born' in file1 or 'Haste'in file1:
                        continue
                    try:
                        with open(os.path.join(path, file1)) as F: R=F.read()
                        if "resourceName" in R:
                            R=R.splitlines()
                            for i in R:
                                if "resourceName" in i:
                                    i=i.replace("resourceName2", "resourceName")
                                    i=i.replace("resourceName3", "resourceName")
                                    if ID_Born in i:
                                        try: Code.index(i)
                                        except: Code.append(i)
                    except: None

                CheckHero=f'    <Track trackName="{Born1}" eventType="CheckHeroIdTick" guid="{Born}" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false" guid="04f92912-4114-4768-97c1-f7668183b5d2">\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\n        <int name="heroId" value="IDSKIN" refParamName="" useRefParam="false" />\n      </Event>\n    </Track>\n'

                TG=f'    <Track trackName="{Born1}" eventType="TriggerParticleTick" guid="b9729512-4050-459e-9644-dc609c2a3a1f" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n      <Condition id="NUM" guid="{Born}" status="true" />\n      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="d7cba7f7-6ca6-4a4d-9540-9d4a634dc68cd">\n        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\n\n      </Event>\n    </Track>\n'

                kh='    <Track trackName="SetBehaviourModeTick0'
                with open(Path1) as F: Read=F.read()
                Read=Read.replace(kh, CheckHero+kh, 1)
                NUM=Read.count("heroId\" value=")
                Read=Read.replace("IDSKIN", ID_Born)
                for code in Code:
                    New=TG.replace("\n\n", "\n"+code+"\n")
                    Read=Read.replace("  </Action>", New+"  </Action>")
                Read=Read.replace("NUM", str(NUM))
                with open(Path1, "w") as F: F.write(Read)
                giai(Born2)
        #==================================================Auto_Check_Ages=================================================================
            IDNODMODCHECK = ['14111', '13210', '16707', '13011']
            if IDCHECK not in IDNODMODCHECK:
                    ABCD=[]
                    files_list = os.listdir(directory_path)
                    for filename in files_list:
                        if filename in ['A1B1.xml', 'A2B1.xml', 'A1b2.xml', 'A2b2.xml'] and IDCHECK == "11119":
                            continue
                        elif filename == 'P1E5.xml' and IDCHECK[:3] == '131':
                            continue
                        elif filename != 'S1B1.xml' and IDCHECK == '13609':
                            continue
                        elif filename != 'U1E1.xml' and IDCHECK == '10611':
                            continue
                        file_path = os.path.join(directory_path, filename)
                        if VMODCHECK == "1":
                            with open(file_path, 'rb') as file:
                                xml_bytes = file.read()#.decode('utf-8')
                                start_phrase = b'<Track trackName="'
                                end_phrase = b'</Track>' 
                                start_index = xml_bytes.find(start_phrase)
                                end_index = xml_bytes.find(end_phrase, start_index)
                                while start_index != -1 and end_index != -1:
                                    track_text = xml_bytes[start_index:end_index + len(end_phrase)]
                                    start_index = xml_bytes.find(start_phrase, end_index)
                                    end_index = xml_bytes.find(end_phrase, start_index)
                                    if b'"skinId" value="' + IDCHECK.encode() + b'"' in track_text:
                                        ABCD.append(track_text)
                                        #print(track_text)
                                        #track_text = track_text.encode()
                            for track_text in ABCD:
                                with open(file_path, 'rb') as file:
                                    xml_bytes = file.read()
                                modified_data = (
                                    track_text
                                    .replace(b"CheckSkinIdTick", b"CheckHeroIdTick")
                                    .replace(b"CheckSkinIdVirtualTick", b"CheckHeroIdTick")
                                    .replace(
                                        b'"skinId" value="' + IDCHECK.encode() + b'"',
                                        b'"heroId" value="' + IDCHECK[:3].encode() + b'"'
                                    )
                                )                                        
                                modified_data1 = xml_bytes.replace(track_text, modified_data)
                                with open(file_path, 'wb') as file:
                                    file.write(modified_data1)
                        if VMODCHECK == "2":
                            with open(file_path, 'rb') as file:
                                xml_bytes = file.read()#.decode('utf-8')
                                start_phrase = b'<Track trackName="'
                                end_phrase = b'</Track>' 
                                start_index = xml_bytes.find(start_phrase)
                                end_index = xml_bytes.find(end_phrase, start_index)
                                while start_index != -1 and end_index != -1:
                                    track_text = xml_bytes[start_index:end_index + len(end_phrase)]
                                    start_index = xml_bytes.find(start_phrase, end_index)
                                    end_index = xml_bytes.find(end_phrase, start_index)
                                    if b'"skinId" value="' + IDCHECK.encode() + b'"' in track_text:
                                        ABCD.append(track_text)
                                        #print(track_text)
                                        #track_text = track_text.encode()
                            for track_text in ABCD:
                                if b'<bool name="bEqual" value="false" refParamName="" useRefParam="false" />' in track_text:
                                    with open(file_path, 'rb') as file:
                                        xml_bytes = file.read()
                                    modified_data = (
                                        track_text
                                        .replace(b'<int name="skinId" value="' + IDCHECK.encode() + b'" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />',b'        <int name="skinId" value="' + IDCHECK.encode() + b'" refParamName="" useRefParam="false" />')
                                        .replace(b"CheckSkinIdVirtualTick", b"CheckSkinIdTick")
                                    )                                        
                                    modified_data1 = xml_bytes.replace(track_text, modified_data)
                                    with open(file_path, 'wb') as file:
                                        file.write(modified_data1)
                                if b'<bool name="bEqual" value="false" refParamName="" useRefParam="false" />' not in track_text:
                                    with open(file_path, 'rb') as file:
                                        xml_bytes = file.read()
                                    modified_data = (
                                        track_text
                                        .replace(b'        <int name="skinId" value="' + IDCHECK.encode() + b'" refParamName="" useRefParam="false" />', b'<int name="skinId" value="' + IDCHECK.encode() + b'" refParamName="" useRefParam="false" />\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />')
                                        .replace(b"CheckSkinIdVirtualTick", b"CheckSkinIdTick")
                                    )                                        
                                    modified_data1 = xml_bytes.replace(track_text, modified_data)
                                    with open(file_path, 'wb') as file:
                                        file.write(modified_data1)

            for file_item in New_Files:
                file_path = Files_Directory_Path + f'{NAME_HERO}' + '/' + 'skill/' + file_item
                giai(file_path)
            
            
        #===============================================Sound_Ages====================================================================
        if b"Skin_Icon_SoundEffect" in dieukienmod or b"Skin_Icon_Dialogue" in dieukienmod:
            if IDCHECK not in ["13311", "16707"]:
                directory_path = Files_Directory_Path + f'{NAME_HERO}' + '/skill/'

                o=directory_path
                ID=(IDSOUND)
                File=os.listdir(o)
                for file in File:
                    giai(o+file)
                    with open(o+file,'rb') as f:rpl=f.readlines()
                    with open(o+file,'rb') as f:Rpl=f.read()
                    Code=[]
                    for i in rpl:
                        if i.find(b'<String name="eventName" value="') != -1:
                            Code.append(i[40:i.find(b'" refParamName="" useRefParam="false" />')])
                    for i in Code:
                        a = b'<String name="eventName" value="' + i + b'" refParamName="" useRefParam="false" />'
                        if Code==[]: pass
                        else:
                            Rpl=Rpl.replace(a,b'<String name="eventName" value="' + i + IDSOUND + b'" refParamName="" useRefParam="false" />')
                    with open(o+file,'wb') as f:f.write(Rpl)

                    giai(o+file)
                
        #=========================================================NGOAI_HINH==========================================================
        INFO_MOD = f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/'
        with zipfile.ZipFile('Resources/1.55.1/Prefab_Characters/Actor_'+f'{IDINFO[:3]}'+'_Infos.pkg.bytes') as f:
            f.extractall(INFO_MOD)
            f.close()
        
        đuongan=INFO_MOD+'Prefab_Hero/'+f'{NAME_HERO}'+'/'
        newpath=đuongan+'/'+NAME_HERO+'_actorinfo.bytes'
        giai(newpath)
        def skincanmod(data):
            trc1=r.find(timtrc,r.find(b'SkinPrefabG'))
            vt1=r.find(b'JTCom0',trc1-300)
            a1=r[vt1-31:]
            a3=vt1 - 31
            skin1=a1[:4]
            skin2=int.from_bytes(skin1,byteorder='little')
            data=r[a3:a3+skin2]
            #open('kb','wb').write(data)
            return data
        op = newpath


        trc=IDINFO
        with open(op,'rb') as f:
            r=f.read()
            r1=r
            timtrc = trc.encode()
            f.close()
        #skin
        mkcam=b''
        teninfobv1=NAME_HERO
        if IDCHECK == '14111':
            teninfobv1='141_DiaoChan'
        tenefec2=teninfobv1.encode()
        tenefec=teninfobv1.lower().encode()
        newteneffec=tenefec[4:].capitalize()
        newteneffec=tenefec[:4]+newteneffec
        str1 = b"hero_skill_effects/" + tenefec2 + b"/"
        str2 = b"hero_skill_effects/" + tenefec + b"/"
        str3 = b"Hero_Skill_Effects/" + tenefec2 + b"/"
        str4 = b"Hero_Skill_Effects/" + tenefec + b"/"
        str5 = b"hero_skill_effects/" + newteneffec + b"/"
        str7 = b"Hero_Skill_Effects/" + newteneffec + b"/"
        IDskineffecđbt=IDCHECK.encode()+b"/"+IDCHECK.encode()
        idnew=IDCHECK.encode()+b"/"
        mkcam =b''
        new1=b''
        new1+=skincanmod(r)
        if IDCHECK == '13311':
            if phukienv == "vangv":
                new1=ngoaihinhvaneovvang
                print('vanpkvang')
            if phukienv == "dov":
                new1=ngoaihinhvaneovdo
            if phukienv == '':
                new1=ngoaihinhvaneov
        if IDCHECK == '16707':
            new1=ngoaihinhkhieov
        if IDCHECK == '52007':
            if phukien == "do":
                new1=ngoaihinhdoveres
            if phukien == "xanh":
                new1=ngoaihinhxanhveres
        IDskineffecđbt=IDCHECK.encode()+b"/"+IDCHECK.encode()
        idnew=IDCHECK.encode()+b'/'
        ID1=IDCHECK.encode()
        if new1.find(b'prefab_skill_effects/hero_skill_effects/')!= -1:#rpl = f.read().replace(str1,str1+ idnew).replace(str3,str3 + idnew).replace(str2,str2 + idnew).replace(str4,str4 + idnew).replace(b"""tyEffect" value="true""",b"""tyEffect" value="false""").replace(str5,str5+ idnew).replace(str6,str6 + idnew).replace(str7,str7 + idnew).replace(str8,str8 + idnew)
            FIND=new1.find(b'PreloadAnimatorEffects')-8
            VT1=new1[FIND:FIND+4]
            VTR=int.from_bytes(VT1,byteorder='little')
            VTM=new1[FIND:FIND+VTR]
            VTM9=VTM
            VTM=(VTR+12).to_bytes(4,byteorder='little')+VTM[4:]
            ELe=VTM.find(b'Element')-8
            ELe1=VTM.find(b'Element')-16
            VTRCM=VTM[:ELe-8] #vt đầu PreloadAnimatorEffects
            DAU=VTM[ELe:ELe+4]
            VTR=int.from_bytes(DAU,byteorder='little')
            VTM1=VTM[ELe:ELe+VTR]#chuẩn
            VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
            VTCUOI=VTM[ELe:]#owr cuoois
            VTCUOI1=VTM[ELe1:ELe1+8] #đếm full eleme
            tinh=VTM.count(b'Element')
            VTM=VTCUOI
            KB=0
            CODEFULL=b''
            for i in range(tinh):
                    ELe=VTM.find(b'Element')-8
                    DAU=VTM[ELe:ELe+4]
                    VTR=int.from_bytes(DAU,byteorder='little')
                    VTM1=VTM[ELe:ELe+VTR]#chuẩn
                    if VTM1.find(b'Vprefab_skill_effects/hero_skill_effects/') == -1:
                        CODEFULL+=VTM1
                        break
                    VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
                    VTCUOI=VTM[VTR:]
                    ELe1=VTM.find(b'Element')+7
                    DAU1=VTM[ELe1:ELe1+4]
                    VTR=int.from_bytes(DAU1,byteorder='little')
                    VTM2=VTM[ELe1:ELe1+VTR]#đếm r
                    VTM2=(VTR+6).to_bytes(4,byteorder='little')+VTM2[4:]
                    newvt=VTM1.find(b'Vprefab_skill_effects/')-8
                    MOI=VTM1[newvt:newvt+4]
                    VTR=int.from_bytes(MOI,byteorder='little')
                    VTR3=VTM1[newvt:newvt+VTR]
                    VTM3=(VTR+6).to_bytes(4,byteorder='little')+VTR3[4:]
                    CODE=VTM1[:15]+VTM2[:46]+VTM3+b'\x04\x00\x00\x00\x04\x00\x00\x00'
                    VTM=VTCUOI
                    CODEFULL+=CODE
            CODEFULL=CODEFULL.replace(str1,str1+ idnew).replace(str2,str2 + idnew)#.to_bytes(4,byteorder='little')
            CODEFULL=len(VTRCM+VTCUOI1+CODEFULL).to_bytes(4,byteorder='little')+VTRCM[4:]+(len(VTCUOI1+CODEFULL)).to_bytes(4,byteorder='little')+VTCUOI1[4:]+CODEFULL
            new1=new1.replace(VTM9,CODEFULL)
            new1=len(new1).to_bytes(4,byteorder='little')+new1[4:]
            mkcam = b'\x05'#\x05
        if new1.find(b'Prefab_Skill_Effects/Hero_Skill_Effects/')!= -1:#rpl = f.read().replace(str1,str1+ idnew).replace(str3,str3 + idnew).replace(str2,str2 + idnew).replace(str4,str4 + idnew).replace(b"""tyEffect" value="true""",b"""tyEffect" value="false""").replace(str5,str5+ idnew).replace(str6,str6 + idnew).replace(str7,str7 + idnew).replace(str8,str8 + idnew)
            FIND=new1.find(b'PreloadAnimatorEffects')-8
            VT1=new1[FIND:FIND+4]
            VTR=int.from_bytes(VT1,byteorder='little')
            VTM=new1[FIND:FIND+VTR]
            VTM9=VTM
            VTM=(VTR+12).to_bytes(4,byteorder='little')+VTM[4:]
            ELe=VTM.find(b'Element')-8
            ELe1=VTM.find(b'Element')-16
            VTRCM=VTM[:ELe-8] #vt đầu PreloadAnimatorEffects
            DAU=VTM[ELe:ELe+4]
            VTR=int.from_bytes(DAU,byteorder='little')
            VTM1=VTM[ELe:ELe+VTR]#chuẩn
            VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
            VTCUOI=VTM[ELe:]#owr cuoois
            VTCUOI1=VTM[ELe1:ELe1+8] #đếm full eleme
            tinh=VTM.count(b'Element')
            VTM=VTCUOI
            KB=0
            CODEFULL=b''
            for i in range(tinh):
                    ELe=VTM.find(b'Element')-8
                    DAU=VTM[ELe:ELe+4]
                    VTR=int.from_bytes(DAU,byteorder='little')
                    VTM1=VTM[ELe:ELe+VTR]#chuẩn
                    if VTM1.find(b'VPrefab_Skill_Effects/Hero_Skill_Effects/') == -1:
                        CODEFULL+=VTM1
                        break
                    VTM1=(VTR+6).to_bytes(4,byteorder='little')+VTM1[4:]
                    VTCUOI=VTM[VTR:]
                    ELe1=VTM.find(b'Element')+7
                    DAU1=VTM[ELe1:ELe1+4]
                    VTR=int.from_bytes(DAU1,byteorder='little')
                    VTM2=VTM[ELe1:ELe1+VTR]#đếm r
                    VTM2=(VTR+6).to_bytes(4,byteorder='little')+VTM2[4:]
                    newvt=VTM1.find(b'VPrefab_Skill_Effects/')-8
                    MOI=VTM1[newvt:newvt+4]
                    VTR=int.from_bytes(MOI,byteorder='little')
                    VTR3=VTM1[newvt:newvt+VTR]
                    VTM3=(VTR+6).to_bytes(4,byteorder='little')+VTR3[4:]
                    CODE=VTM1[:15]+VTM2[:46]+VTM3+b'\x04\x00\x00\x00\x04\x00\x00\x00'
                    VTM=VTCUOI
                    CODEFULL+=CODE
            CODEFULL=CODEFULL.replace(str3,str3 + idnew).replace(str4,str4 + idnew)#.to_bytes(4,byteorder='little')
            CODEFULL=len(VTRCM+VTCUOI1+CODEFULL).to_bytes(4,byteorder='little')+VTRCM[4:]+(len(VTCUOI1+CODEFULL)).to_bytes(4,byteorder='little')+VTCUOI1[4:]+CODEFULL
            new1=new1.replace(VTM9,CODEFULL)
            new1=len(new1).to_bytes(4,byteorder='little')+new1[4:]
            mkcam = b'\x05'#\x05
        skinmoi=new1
        skinprefag=r.find(b'SkinPrefabG')-8
        tinhskinpre=r[skinprefag:skinprefag+4]
        tinhskinpre1=int.from_bytes(tinhskinpre,byteorder='little')
        tinhskinpre2=r[skinprefag:skinprefag+tinhskinpre1] #
        JTCom0 = tinhskinpre2.count(b"JTCom0")
        beginskin=tinhskinpre2[:101]
        CodeSkinNew=beginskin+new1*JTCom0 #
        tinhCodeSkinNew1=CodeSkinNew[:93]
        tinhCodeSkinNew=CodeSkinNew[93:]
        Elenmen=len(tinhCodeSkinNew).to_bytes(4,byteorder='little')+tinhCodeSkinNew[4:]
        SkinPrefag1=tinhCodeSkinNew1+Elenmen
        SkinPrefag=len(SkinPrefag1).to_bytes(4,byteorder='little')+SkinPrefag1[4:]
        codeskinnew=r1.replace(tinhskinpre2,SkinPrefag)

        def ArtSkinPrefabLOD(data3):
            a=skinmoi.find(b'\x00ArtSkinPrefabLOD')-7
            a10=skinmoi.find(b'\x00ArtSkinPrefabLOD')-3
            a3=skinmoi[a:a+8]
            a4=a3[4:]
            a2=skinmoi[a:a+4]
            vitri=int.from_bytes(a2,byteorder='little')
            vitri2=int.from_bytes(a4,byteorder='little')
            a5=skinmoi[a:a+vitri]
            a25=skinmoi[a10:a10+vitri2]
            a22=skinmoi[a10:a10+vitri2].replace(b'\x00ArtSkinPrefabLOD',b'\x00ArtPrefabLOD')
            a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
            code=a5.replace(a25,a13)
            data3=len(code).to_bytes(4,byteorder='little')+code[4:]
            return data3 
        def ArtSkinLobbyShowLOD(data4):
            a=skinmoi.find(b'\x00ArtSkinLobbyShowLOD')-7
            a10=skinmoi.find(b'\x00ArtSkinLobbyShowLOD')-3
            a3=skinmoi[a:a+8]
            a4=a3[4:]
            a2=skinmoi[a:a+4]
            vitri=int.from_bytes(a2,byteorder='little')
            vitri2=int.from_bytes(a4,byteorder='little')
            a5=skinmoi[a:a+vitri]
            a25=skinmoi[a10:a10+vitri2]
            a22=skinmoi[a10:a10+vitri2].replace(b'\x00ArtSkinLobbyShowLOD',b'\x00ArtLobbyShowLOD')
            a13=len(a22).to_bytes(4,byteorder='little')+a22[4:]
            code=a5.replace(a25,a13)
            data4=len(code).to_bytes(4,byteorder='little')+code[4:]
            return data4
        #codeskinmd
        SkinMD=r[:skinprefag]

        #skinmd Art
        Art=SkinMD.find(b'ArtPrefabLOD')-8
        tinhskinpre=SkinMD[Art:Art+4]
        tinhskinpre1=int.from_bytes(tinhskinpre,byteorder='little')
        tinhskinpre2=SkinMD[Art:Art+tinhskinpre1] #
        #skinmd ArtLobbyShowLOD
        ArtLobby=SkinMD.find(b'ArtLobbyShowLOD')-8
        tinhArtLobby=SkinMD[ArtLobby:ArtLobby+4]
        tinhArtLobby1=int.from_bytes(tinhArtLobby,byteorder='little')
        tinhArtLobby2=SkinMD[ArtLobby:ArtLobby+tinhArtLobby1] #
        ArtSkinPrefab=b''
        ArtSkinPrefab+=ArtSkinPrefabLOD(skinmoi)
        CodeNewMD=SkinMD.replace(tinhskinpre2,ArtSkinPrefab)
        ArtSkinLobby=b''
        ArtSkinLobby+=ArtSkinLobbyShowLOD(skinmoi)
        CodeNewMD=CodeNewMD.replace(tinhArtLobby2,ArtSkinLobby)
        ArtLobbyIdle=CodeNewMD.find(b'ArtLobbyIdleShowLOD0')-8
        cammd=CodeNewMD[ArtLobbyIdle:999999]
        ArtLobbyIdleSkin=skinmoi.find(b'ArtSkinLobbyIdleShowLOD')-8
        camSkin=skinmoi[ArtLobbyIdleSkin:999999]
        camSkin=ArtSkinLobbyIdleShowLOD(camSkin)
        if mkcam == b'\x05':
            camSkin=camSkin.replace(CODEFULL,b'')
        CodeNewMD=CodeNewMD.replace(cammd,camSkin)
        CodeFull=codeskinnew.replace(SkinMD,CodeNewMD)
        RootDtrc=CodeFull[:84]
        RootDsau=CodeFull[84:]
        RootD1=RootDsau[8:12]
        VTR=int.from_bytes(RootD1,byteorder='little')#ArtPrefabLOD
        m=RootDsau.find(b'ArtPrefabLOD')-8
        CRE=b'c\x00\x00\x00\r\x00\x00\x00ActorNameJ\x00\x00\x00\x03\x00\x00\x00\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1c\x00\x00\x00\x05\x00\x00\x00VFilesModBy_HSM\x04\x00\x00\x00\x04\x00\x00\x00'
        if IDCHECK == '54402':
            RootDsau=RootDsau[:VTR+8]+CRE+RootDsau[m:] 
        tinhRootDsau=len(RootDsau).to_bytes(4,byteorder='little')+RootDsau[4:]
        tinhRootDtrc=RootDtrc+tinhRootDsau
        CodeDayDu=len(tinhRootDtrc).to_bytes(4,byteorder='little')+tinhRootDtrc[4:]
        CodeDayDu=CodeDayDu.replace(b"Light<",b"00000<")
        tinhcam=CodeDayDu[:89]
        with open(op,'wb')as f: f.write(CodeDayDu)
        o=open(op,'rb')
        h=o.read(92)
        k=0
        while True:
            r1=o.read(4)
            if r1==b'':
                break
            KB=r1.hex()
            KB=KB[6:8]+KB[4:6]+KB[2:4]+KB[0:2]
            KB=int(KB,16)
            O=r1+o.read(KB-4)
            k+=1
        o.close()
        k=k.to_bytes(1,byteorder='little')
        tinhcam1=CodeDayDu[:88]+k
        CodeDayDu=CodeDayDu.replace(tinhcam,tinhcam1)
        with open(op,'wb')as f: f.write(CodeDayDu)
        giai(newpath)


        if IDCHECK[:3] == '196':
            giai(f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/Prefab_Hero/196_Elsu/196_Elsu_trap_actorinfo.bytes')
            init()
            while True:
                Path = (f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/Prefab_Hero/196_Elsu/196_Elsu_trap_actorinfo.bytes')
                try:
                    break
                except:
                    os.system("clear")
            IDSKINELSU = IDCHECK
            Light = "n"
            HD = "n"
            if len(IDSKINELSU) in (4,5):
                for FilePath in Path:
                    path = Path + "/" + FilePath
                    try:
                        file = open(path, "rb")
                        notfile = file.read(4)
                        file.close()
                        if notfile != b"PK\x03\x04":
                             
                             file = open(path, "rb")
                             Begin = file.read(92)
                             MD = []
                             MDD = []
                             
                             while True:
                                 SL = file.read(4)
                                 SL0 = SL.hex()
                                 SL0 = SL0[6:8]+SL0[4:6]+SL0[2:4]+SL0[0:2]
                                 SL0 = int(SL0,16)
                                 CodeZ = SL+file.read(SL0-4)
                                 Find = CodeZ.find(b"SkinPrefabG")
                                 if Find == -1:
                                     MD.append(CodeZ)
                                 else:
                                     SkinPrefabG = CodeZ
                                     break

                             while True:
                                 SL = file.read(4)
                                 if SL == b"":
                                     break
                                 SL0 = SL.hex()
                                 SL0 = SL0[6:8]+SL0[4:6]+SL0[2:4]+SL0[0:2]
                                 SL0 = int(SL0,16)
                                 CodeZ = SL+file.read(SL0-4)
                                 MDD.append(CodeZ)
                    
                             file.close()
                             
                             AllSkin = []
                             filez = open(".Cache","wb+")
                             Write = filez.write(SkinPrefabG)
                             filez.close()
                             filez = open(".Cache","rb")
                             BeginSkin = filez.read(101)
                             
                             while True:
                                 SL = filez.read(4)
                                 if SL == b"":
                                     break
                                 SL0 = SL.hex()
                                 SL0 = SL0[6:8]+SL0[4:6]+SL0[2:4]+SL0[0:2]
                                 SL0 = int(SL0,16)
                                 CodeZ = SL+filez.read(SL0-4)
                                 AllSkin.append(CodeZ)

                             filez.close()
                
                             for JTC in AllSkin:
                                 tryFind = JTC.find(bytes(IDSKINELSU,"utf8"))
                                 if tryFind != -1:
                                     ModSkin = JTC
                                     break
                             if tryFind == -1:
                                 break                
                             filex = open(".Cache2","wb+")
                             Writein = filex.write(JTC)
                             filex.close()
                             filex = open(".Cache2","rb")
                             BeginSkinJTC = filex.read(96)
                             
                             SkinJTC = []
                             while True:
                                 SL = filex.read(4)
                                 if SL == b"":
                                     break
                                 SL0 = SL.hex()
                                 SL0 = SL0[6:8]+SL0[4:6]+SL0[2:4]+SL0[0:2]
                                 SL0 = int(SL0,16)
                                 CodeZ = SL+filex.read(SL0-4)
                                 SkinJTC.append(CodeZ)
                             KB = []
                             MD_S = MD + MDD

                             for i in range(len(SkinJTC)):
                                 DK = 0
                                 for k in range(len(MD_S)):
                                     if SkinJTC[i][8:25] == MD_S[k][8:25]:
                                         MD_S[k] = SkinJTC[i]
                                         DK = 1
                                         break
                                 if DK == 0:
                                     KB.append(SkinJTC[i])
                                     
                             TT = []
                             for Name in KB:
                                 if Name.find(b"_LOD") != -1:
                                     TT.append(Name)
                                     KB.remove(Name)
                             
                             for NameZ in KB:
                                 if NameZ.find(b"LODEx0") != -1:
                                     TT.append(NameZ)
                                     KB.remove(NameZ)

                             for Name in KB:
                                 if Name.find(b"_Show1\x04") != -1:
                                     TT.append(Name)
                                     KB.remove(Name)		
                             
                             for NameZ in KB:
                                 if NameZ.find(b"LobbyIdle") != -1:
                                     TT.append(NameZ)
                                     KB.remove(NameZ)
                             
                             Eff_C = None
                             for Effects in KB:
                                 if b"PreloadAnimatorEffects" in Effects and b"ffects/" in Effects:
                                     Eff_C = Effects
                                     break
                                 
                             if Eff_C != None:
                                 Find = -7
                                 while True:
                                     Find = Eff_C.find(b"Element",Find+7)
                                     if Find == -1:
                                         break
                                     GT = Eff_C[Find-8]
                                     CodeC = Eff_C[Find-8:Find-8+GT]
                                     CodeCC = CodeC
                                     FIDSKINELSU = CodeC.find(bytes(IDSKINELSU[0:3]+"_", "utf"))
                                     FEIDSKINELSU = CodeC.find(b"/", FIDSKINELSU)
                                     NameHero = CodeC[FIDSKINELSU:FEIDSKINELSU]
                                     if len(IDSKINELSU) == 4:
                                         IDSKINELSUE = IDSKINELSU[0:3]+"0"+str(int(IDSKINELSU[3])-1)
                                     if len(IDSKINELSU) == 5:
                                         IDSKINELSUE = IDSKINELSU[0:3]+str(int(IDSKINELSU[3:5])-1)
                                     CodeC = CodeC.replace(NameHero, NameHero+b"/"+bytes(IDSKINELSUE,"utf"))
                                     GTS = bytes.fromhex(hex(GT+6)[2:4])
                                     CodeC = CodeC.replace(CodeC[0:1],GTS,1)
                                     GT2X = CodeC[0:15]+bytes.fromhex(hex(CodeC[15]+6)[2:4])+CodeC[16:]
                                     CodeC = CodeC.replace(CodeC[0:],GT2X,1)
                                     GTC = CodeC[55:61]+bytes.fromhex(hex(CodeC[61]+6)[2:4])
                                     CodeC = CodeC.replace(CodeC[55:62],GTC,1)
                                     Eff_C = Eff_C.replace(CodeCC,CodeC,1)
                                     
                                 TSL = int(Eff_C.count(b"ffects/")/2)*6
                                 GTBD = hex(Eff_C[0] + Eff_C[1]*256 + TSL)
                                 GTBD = bytes.fromhex(GTBD[3:5]+"0"+GTBD[2])
                                 Eff_C = Eff_C.replace(Eff_C[0:2],GTBD,1)
                                 GTT2 = hex(Eff_C[82] + Eff_C[83]*256 + TSL)
                                 GTT2 = bytes.fromhex(GTT2[3:5]+"0"+GTT2[2])
                                 Eff_C = Eff_C.replace(Eff_C[82:84],GTT2,1)
                                     
                                 KB.remove(Effects)                
                                 
                                 ModSkin = ModSkin.replace(Effects, Eff_C)

                                 GT1 = str(hex(ModSkin[0]+ModSkin[1]*256+TSL))[2:6]
                                 if len(GT1) == 3:
                                     GT1 = bytes.fromhex(GT1[1:3]+"0"+GT1[0])
                                 if len(GT1) == 4:
                                     GT1 = bytes.fromhex(GT1[2:4]+GT1[0:2])
                                 ModSkin = ModSkin.replace(ModSkin[0:2],GT1,1)
                                                 
                                 GT5 = hex(ModSkin[88]+ModSkin[89]*256+TSL)
                                 if len(GT5) == 5:
                                     GT5 = bytes.fromhex(GT5[3:5]+"0"+GT5[2])
                                 if len(GT5) == 6:
                                     GT5 = bytes.fromhex(GT5[4:6]+GT5[2:4])
                                 GT5 += b"\x00"*2
                                 ModSkin = ModSkin.replace(ModSkin[88:92],GT5,1)
                                         
                
                             for NR in range(len(TT)):
                                 Cache = TT[NR]
                                 Cache = Cache.replace(b"Skin",b"")
                                 NC = len(Cache)
                                 NC = str(hex(NC))
                                 if len(NC) == 4:
                                     NC = NC[2:4]+"000000"
                                     NC = bytes.fromhex(NC)
                                 else:
                                     NC = NC[3:5] + "0" + NC[2] + "0000"
                                     NC = bytes.fromhex(NC)
                                 Cache = Cache.replace(Cache[0:4],NC)
                                 NCK = int(Cache[4]) - 4
                                 NCK = str(hex(NCK))
                                 NCK = NCK[2:4]+"000000"
                                 NCK = bytes.fromhex(NCK)
                                 Cache = Cache.replace(Cache[4:8],NCK,1)
                                 TT[NR] = Cache
                                 
                                 
                             for i in range(len(TT)):
                                 for k in range(len(MD_S)):
                                     if TT[i][8:25] == MD_S[k][8:25]:
                                         MD_S[k] = TT[i]
                                         break
                             
                             JTCom0 = SkinPrefabG.count(b"JTCom0")
                             SkinPrefab = BeginSkin + ModSkin*JTCom0
                             Cache = SkinPrefab
                             NC = len(Cache)
                             NC0 = NC - 93
                             NC = str(hex(NC))
                             if len(NC) == 6:
                                 NC = NC[4:6] + NC[2:4] + "0000"
                             if len(NC) == 7:
                                 NC = NC[5:7] + NC[3:5] + "0" + NC[2] + "00"
                             NC = bytes.fromhex(NC)
                             Cache = Cache.replace(Cache[0:4],NC)
                             SkinPrefab = Cache
                             NCS = SkinPrefabG[93:97]
                             NC0 = str(hex(NC0))
                             NC0 = NC0[4:6] + NC0[2:4] + "0000"
                             NC0 = bytes.fromhex(NC0)
                             Cache = Cache.replace(NCS,NC0,1)
                             SkinPrefab = Cache

                             NCX = len(KB)
                             EndEvent = Begin
                             for A in range(len(MD)):
                                 EndEvent += MD_S[A]
                             for B in KB:
                                 EndEvent += B
                             EndEvent += SkinPrefab
                             for C in range(len(MDD)):
                                 EndEvent += MD_S[C+len(MD)]
                             
                             if IDSKINELSU == "5443":
                                 EndEvent = EndEvent.replace(MD[1],b"",1)
                                 NCX -= 1
                                 
                             NCZ = len(EndEvent)
                             NCZ0 = NCZ - 84
                             NCZ = hex(NCZ)
                             if len(NCZ) == 6:
                                 NCZ = NCZ[4:6]+NCZ[2:4]+"0000"
                             if len(NCZ) == 7:
                                 NCZ = NCZ[5:7]+NCZ[3:5]+"0"+NCZ[2]+"00"
                             NCZ = bytes.fromhex(NCZ)
                             EndEvent = EndEvent.replace(EndEvent[0:4],NCZ,1)
                             
                             NCV = EndEvent[84:88]
                             NCZ0 = hex(NCZ0)
                             if len(NCZ0) == 6:
                                 NCZ0 = NCZ0[4:6]+NCZ0[2:4]+"0000"
                             if len(NCZ0) == 7:
                                 NCZ0 = NCZ0[5:7]+NCZ0[3:5]+"0"+NCZ0[2]+"00"
                             NCZ0 = bytes.fromhex(NCZ0)
                             EndEvent = EndEvent.replace(EndEvent[0:4],NCZ,1)
                             EndEvent= EndEvent.replace(NCV, NCZ0, 1)
                             
                             XXX = EndEvent[88:92]
                             NCO = int(EndEvent[88])+NCX
                             NCO = hex(NCO)
                             NCO = NCO[2:4] + "000000"
                             NCO = bytes.fromhex(NCO)
                             EndEvent = EndEvent.replace(XXX,NCO,1)
                             
                             if Light == "y":
                                 EndEvent = EndEvent.replace(b"Light<",b"00000<")
                             
                             if HD == "y":
                                 EndEvent = EndEvent.replace(b"_LOD2",b"_LOD1")
                                 EndEvent = EndEvent.replace(b"_LOD3",b"_LOD1")
                             
                             File = open(path,"wb")
                             WriteEnd = File.write(EndEvent)
                             File.close()
                             
                             os.remove(".Cache").remove(".Cache2")
                        else:
                             pass
                             file = file.close()
                    except:
                        pass
            giai(f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/Prefab_Hero/196_Elsu/196_Elsu_trap_actorinfo.bytes')
            
        
        #=========================================================BIEN_VE==========================================================
        if b"Skin_Icon_BackToTown" in dieukienmod or b"Skin_Icon_Animation" in dieukienmod:
            RPL = CODE_BV_HERO
            cod = CODEBIENVE
            đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Back.xml'
            for ibv in range(1,2):
                if SKINEOV in ('r','b','y') :
                    break
                with open (đuongan,'rb') as f : 
                    bv = f.read()
                    f.close()
                for kkbv in range(0,2):
                    k1bv=k1bv+kkbv
                    if '15412' in IDMODSKIN1:
                        if IDMODSKIN1.index(IDCHECK) == IDMODSKIN1.index('15412') + 1:
                            k1bv = k1bv+1

                ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
                s1bv=str(k1bv).encode()
                ab=ab.replace(b'coid',s1bv).replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+NAME_HERO.encode())
                if MKBV == b'\x36':
                    dem1=0
                    for i in RPL:
                        if i.find(b'<Action tag=""') !=-1:
                            break
                        dem1+=1
                    VT=RPL[dem1+1:]#dem]
                    VTR=b''.join(VT)
                    VT1=VTR.count(b'<Condition id="')
                    for i in range(VT1):
                        dem1=0
                        for i1 in VT:
                            if i1.find(b'<Condition id="') != -1 :
                                break
                            dem1+=1
                        VTR=VTR.replace(i1,b'')
                    VTR=VTR.replace(b'  </Action>\r\n</Project>',b'')
                    VTR+=b'  </Action>\r\n</Project>'
                    codenew=cod.replace(b'  </Action>\r\n</Project>',VTR)
                    codenew=codenew.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
                else:
                    cod=HPCAO+cod
                    codenew=cod.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
                aa=b''
                aa+=bienve(codenew)
                aabv=b''
                aabv+=bienvecheck(codenew)
                CodeFullBV=aa
                ##printaa)
                #codenew=bv.replace(projack,codenew)
                codenew=bv.replace(projack,aabv)
                codenew=codenew.replace(b'\r\n  </Action>\r\n</Project>',CodeFullBV).replace(b'Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huicheng_tongyong', b'').replace(b'Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huijidi', b'').replace(b'strReturnCityFall', b'').replace(b'strReturnCityEffectPath', b'')
                with open (đuongan,'wb') as f : f.write(codenew)
            if SKINEOV == 'b' :
                with open (đuongan,'rb') as f : 
                    bv = f.read()
                    f.close()
                for kkbv in range(0,2):
                    k1bv=k1bv+kkbv
                ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
                s1bv=str(k1bv).encode()
                ab=ab.replace(b'coid',s1bv).replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+NAME_HERO.encode())
                cod=bienvengokonhocty
                codenew=cod.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
                aabv=b''
                aabv+=bienvecheck(codenew)
                codenew=bv.replace(projack,aabv).replace(b'\r\n  </Action>\r\n</Project>',codenew).replace(b'Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huicheng_tongyong', b'').replace(b'Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huijidi', b'').replace(b'strReturnCityFall', b'').replace(b'strReturnCityEffectPath', b'')
                with open (đuongan,'wb') as f : f.write(codenew)

            if SKINEOV == 'r' :
                with open (đuongan,'rb') as f : 
                    bv = f.read()
                    f.close()
                for kkbv in range(0,2):
                    k1bv=k1bv+kkbv
                ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
                s1bv=str(k1bv).encode()
                ab=ab.replace(b'coid',s1bv).replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+NAME_HERO.encode())
                cod=bienvevanxathan
                codenew=cod.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
                aabv=b''
                aabv+=bienvecheck(codenew)
                codenew=bv.replace(projack,aabv).replace(b'\r\n  </Action>\r\n</Project>',codenew).replace(b'Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huicheng_tongyong', b'').replace(b'Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huijidi', b'').replace(b'strReturnCityFall', b'').replace(b'strReturnCityEffectPath', b'')
                with open (đuongan,'wb') as f : f.write(codenew)
            if SKINEOV == 'y' :
                with open (đuongan,'rb') as f : 
                    bv = f.read()
                    f.close()
                for kkbv in range(0,2):
                    k1bv=k1bv+kkbv
                    k1bv1=k1bv+1
                    k1bv2=k1bv1+1
                ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
                s1bv=str(k1bv).encode()
                s1bv1=str(k1bv1).encode()
                s1bv2=str(k1bv2).encode()
                ab=ab.replace(b'coid',s1bv).replace(b'guid="tentuong',b'guid="'+AABBCC.encode('utf-8') + b'_'+NAME_HERO.encode())
                cod=CODEBVYENA
                codenew111=CODEBVYENA1.replace(b'co1', s1bv1).replace(b'cod2', s1bv2)
                codenew=cod.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
                codenew = codenew + codenew111
                aabv=b''
                aabv+=bienvecheck(codenew)
                codenew=bv.replace(projack,aabv).replace(b'\r\n  </Action>\r\n</Project>',codenew).replace(b'Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huicheng_tongyong', b'').replace(b'Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huijidi', b'').replace(b'strReturnCityFall', b'').replace(b'strReturnCityEffectPath', b'')
                with open (đuongan,'wb') as f : f.write(codenew)
            
        #=========================================================GIA_TOC==========================================================

        if IDCHECK in GIATOCEDIT:
            if IDCHECK =='15009':
                gtHasteE1=gtHasteE1.replace(b'JiaSu_tongyong_01',b'T2_Spint').replace(b'\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'JiaSu_tongyong_01',b'T2_Spint').replace(b'\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />',b'')
            if IDCHECK =='14111':
                gtHasteE1=gtHasteE1.replace(b'JiaSu_tongyong_01',b'14111_luoer_Sprint').replace(b'\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'JiaSu_tongyong_01',b'14111_luoer_Sprint').replace(b'\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />',b'')
            if IDCHECK =='11607':
                gtHasteE1=gtHasteE1.replace(b'JiaSu_tongyong_01',b'jingke_sprint_01')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'JiaSu_tongyong_01',b'jingke_sprint_01')
                #T2_Spint
            đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1.xml'
            giai(đuongan)
            with open(đuongan,'rb') as f: a234123=f.read()
            f.close()
            ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
            s1bv=str(hasteE1cechbv).encode()
            ab=ab.replace(b'coid',s1bv)
            codenew=gtHasteE1.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
            aa=b''
            aa+=hasteE1(codenew)
            aabv=b''
            aabv+=hasteE1check(checkHasteE1)
            CodeFullBV=aa
            codenew=a234123.replace(b'\r\n  </Action>\r\n</Project>',aabv)
            codenew=codenew.replace(b'\r\n  </Action>\r\n</Project>',CodeFullBV)
            with open (đuongan,'wb') as f : f.write(codenew)
            giai(đuongan)
            đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1_leave.xml'
            giai(đuongan)
            with open(đuongan,'rb') as f: a234123=f.read()
            f.close()
            ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
            s1bv=str(hasteE1_leavecechbv).encode()
            ab=ab.replace(b'coid',s1bv)
            codenew=gtHasteE1_leave.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
            aa=b''
            aa+=hasteE1_leave(codenew)
            aabv=b''
            aabv+=hasteE1check(checkHasteE1)
            CodeFullBV=aa
            codenew=a234123.replace(b'\r\n  </Action>\r\n</Project>',aabv)
            codenew=codenew.replace(b'\r\n  </Action>\r\n</Project>',CodeFullBV)
            with open (đuongan,'wb') as f : f.write(codenew)
            hasteE1_leavecechbv+=2
            hasteE1cechbv+=2
            giai(đuongan)

        if IDCHECK in GIATOC:
            if IDCHECK =='54004':
                gtHasteE1=gtHasteE1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_97_heike').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_97_heike').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
            if IDCHECK =='13311':
                gtHasteE1=gtHasteE1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_122_gushiji').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_122_gushiji').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
            if IDCHECK =='13112':
                gtHasteE1=gtHasteE1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_111_shanyi_01').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_111_shanyi_01').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
            if IDCHECK =='54402':
                gtHasteE1=gtHasteE1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_109_tanzhilang_1').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_109_tanzhilang_1').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
            if IDCHECK =='13202':
                gtHasteE1=gtHasteE1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_61_moon').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_61_moon').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
            if IDCHECK =='16606':
                gtHasteE1=gtHasteE1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_61_moon').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_61_moon').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
            if IDCHECK =='19502':
                gtHasteE1=gtHasteE1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_61_moon').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_61_moon').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
            if IDCHECK =='50605':
                gtHasteE1=gtHasteE1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_61_moon').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_61_moon').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
            if IDCHECK =='53002':
                gtHasteE1=gtHasteE1.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_61_moon').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
                gtHasteE1_leave=gtHasteE1_leave.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/Name_Hero/ID_Skin/JiaSu_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_61_moon').replace(b'\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false"/>',b'')
            đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1.xml'
            giai(đuongan)
            with open(đuongan,'rb') as f: a234123=f.read()
            f.close()
            ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
            s1bv=str(hasteE1cechbv).encode()
            ab=ab.replace(b'coid',s1bv)
            codenew=gtHasteE1.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
            aa=b''
            aa+=hasteE1(codenew)
            aabv=b''
            aabv+=hasteE1check_leave(checkHasteE1_leave)
            CodeFullBV=aa
            codenew=a234123.replace(b'\r\n  </Action>\r\n</Project>',aabv)
            codenew=codenew.replace(b'\r\n  </Action>\r\n</Project>',CodeFullBV)
            with open (đuongan,'wb') as f : f.write(codenew)
            giai(đuongan)

            đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/HasteE1_leave.xml'
            giai(đuongan)
            with open(đuongan,'rb') as f: a234123=f.read()
            f.close()
            ab=b'\r\n      <Condition id="coid" guid="tentuong" status="true"/>'
            s1bv=str(hasteE1_leavecechbv).encode()
            ab=ab.replace(b'coid',s1bv)
            codenew=gtHasteE1_leave.replace(b'stopAfterLastEvent="true">',b'stopAfterLastEvent="true">'+ab)
            aa=b''
            aa+=hasteE1_leave(codenew)
            aabv=b''
            aabv+=hasteE1check_leave(checkHasteE1_leave)
            CodeFullBV=aa
            codenew=a234123.replace(b'\r\n  </Action>\r\n</Project>',aabv)
            codenew=codenew.replace(b'\r\n  </Action>\r\n</Project>',CodeFullBV)
            with open (đuongan,'wb') as f : f.write(codenew)
            hasteE1_leavecechbv+=2
            hasteE1cechbv+=2
            giai(đuongan)
        #=========================================================HIEU_UNG_VE_THAN==========================================================
        if IDCHECK in ("50108","14111","11107","15009"):
            organSkin = "Resources/1.55.1/Databin/Client/Actor/organSkin.bytes"
            organSkin_mod = f"{sanitized_input}/files/Resources/1.55.1/Databin/Client/Actor/organSkin.bytes"
            shutil.copy(organSkin, organSkin_mod)
            giai(organSkin_mod)
            print('')

        if IDCHECK in ("50108","14111","11107","15009"):
            ID = IDCHECK
            file = open(organSkin_mod, "rb")
            IDN = str(hex(int(ID)))
            IDN = IDN[4:6] + IDN[2:4]
            IDN = bytes.fromhex(IDN)
            ALL_ID = []
            MD = int(ID[0:3] + "00")
            for IDNew in range(21):
                ALL_ID.append(str(MD))
                MD += 1
            ALL_ID.remove(ID)
            for x in range(20):
                IDK = str(hex(int(ALL_ID[x])))
                IDK = IDK[4:6] + IDK[2:4]
                IDK = bytes.fromhex(IDK)
                ALL_ID[x] = IDK
            Begin = file.read(140)
            Read = b"\x00"
            All = []
            while Read != b"":
                Read = file.read(36)
                if Read.find(IDN) != -1:
                    All.append(Read)
                try:
                    Max = Read[4] + (Read[5]*256)
                    Max0 = str(hex(Max))
                    if len(Max0) == 4:
                        Max0 = Max0[2:4] + "00"
                    if len(Max0) == 5:
                        Max0 = Max0[3:5] + "0" + Max0[2]
                    if len(Max0) == 6:
                        Max0 = Max0[4:6] + Max0[2:4]
                    Max0 = bytes.fromhex(Max0)
                except:
                    None
            file.close()
            file = open(organSkin_mod, "ab+")
            Read0 = file.read()
            for i in range(len(ALL_ID)):
                for j in range(len(All)):
                    CT = All[j]
                    if CT.find(IDN) != -1:
                        CT = CT.replace(IDN,ALL_ID[i])
                    else:
                        CT = CT.replace(ALL_ID[i-1],ALL_ID[i])
                    CTN = str(hex(Max0[0]+(Max0[1]*256)+1))
                    if len(CTN) == 4:
                        CTN = CTN[2:4]
                    if len(CTN) == 5:
                        CTN = CTN[3:5] + "0" + CTN[2]
                    if len(CTN) == 6:
                        CTN = CTN[4:6] + CTN[2:4]
                    CTN = bytes.fromhex(CTN)
                    OZ = b" \x00\x00\x00"
                    if len(CTN) == 1:
                        CT = CT.replace(OZ+CT[4:6],OZ+CTN+b"\x00",1)
                    if len(CTN) == 2:
                        CT = CT.replace(OZ+CT[4:6],OZ+CTN,1)
                    All[j] = CT
                    XXX = file.write(CT)
                    Max0 = CT[4:6]
            file.close()
            file = open(organSkin_mod, "rb")
            Read = file.read()
            Read = Read.replace(Begin[12:14],Max0,1)
            file.close()
            file = open(organSkin_mod, "wb")
            Z = file.write(Read)
            file.close()
            giai(organSkin_mod)
            #print("Hiệu Ứng Vệ Thần")
        #=========================================================HABUANAK==========================================================
        if IDCHECK == "15009":
            đuongan1=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/PassiveResource/BlueBuff.xml'
            đuongan2=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/PassiveResource/RedBuff_Slow.xml'
            giai(đuongan1)
            giai(đuongan2)
            with open (đuongan1, 'rb') as f:
                noidung = f.read()
                noidung = noidung.replace(b"CheckSkinIdVirtualTick", b"CheckHeroIdTick").replace(b'"skinId" value="15009"', b'"heroId" value="150"')
            with open (đuongan1,'wb') as f : f.write(noidung)
            with open (đuongan2, 'rb') as f:
                noidung = f.read()
                noidung = noidung.replace(b"CheckSkinIdVirtualTick", b"CheckHeroIdTick").replace(b'"skinId" value="15009"', b'"heroId" value="150"')
            with open (đuongan2,'wb') as f : f.write(noidung)
            giai(đuongan1)
            giai(đuongan2)
            print('')
        if IDCHECK == "":
            with zipfile.ZipFile('Resources/1.55.1/Ages/Prefab_Characters/Prefab_Organ_Age.pkg.bytes') as f:
                f.extractall(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/mod2/')
                TRU1 = (f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/mod2/Prefab_Organ/Crystal/New_BlueCrystal/Skill/')
                TRU2 = (f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/mod2/Prefab_Organ/Crystal/New_RedCrystal/Skill/')
                TRU3 = (f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/mod2/Prefab_Organ/Tower/New_BlueTower/Skill/')
                TRU4 = (f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/mod2/Prefab_Organ/Tower/New_BlueTower_High/Skill/')
                TRU5 = (f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/mod2/Prefab_Organ/Tower/New_RedTower/Skill/')
                TRU6 = (f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/mod2/Prefab_Organ/Tower/New_RedTower_High/Skill/')
                f.close()
            folder_path1 = [TRU1, TRU2, TRU3, TRU4, TRU5, TRU6]
            for folder_path in folder_path1:
                for filename in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, filename)
                    giai(file_path)
                    print(file_path)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            content = file.readlines()

                        with open(file_path, 'w', encoding='utf-8') as file:
                            for line in content:
                                if '<String name="prefabName"' in line:
                                    parts = line.split('/')
                                    if len(parts) >= 5:
                                        parts[4] = '1/' + parts[4]
                                        line = '/'.join(parts)
                                elif '<String name="resourceName"' in line:
                                    parts = line.split('/')
                                    if len(parts) >= 3:
                                        parts[2] = '1/' + parts[2]
                                        line = '/'.join(parts)
                                file.write(line)
                    except UnicodeDecodeError:
                        print(f"Files Encryptes JG: {file_path}")
                        continue
            #print("HIEUUNGTRU" + "*"*30 +"BETA")
            
            
            
            
            
            
        #=========================================================FIXLAG==========================================================
        if fixlag == 'y':
            if '11107' in IDCHECK or '15704' in IDCHECK:
                if b"Skin_Icon_Skill" in dieukienmod or IDCHECK == "53702":
                    shutil.copy(f'Resources/1.55.1/AssetRefs/Hero/{IDCHECK[:3]}_AssetRef.bytes', f'{sanitized_input}/files/Resources/1.55.1/AssetRefs/Hero/{IDCHECK[:3]}_AssetRef.bytes')
                    
                    Path=f'{sanitized_input}/files/Resources/1.55.1/AssetRefs/Hero/{IDCHECK[:3]}_AssetRef.bytes'
                    giai(Path)
                    id=IDCHECK
                    if IDCHECK == "13311":
                        with open(Path,'rb') as f:rpl=f.read()
                        CODETONG = rpl.replace(b"prefab_skill_effects/hero_skill_effects/133_direnjie/", b"prefab_skill_effects/component_effects/13311/13311_5/")
                        with open(Path,'wb') as f:f.write(CODETONG)
                        print('')
                    elif IDCHECK == "16707":
                        with open(Path,'rb') as f:rpl=f.read();f.close()
                        CACHE=[]
                        VTR=rpl[rpl.find(b'particlesInFirstLayer')-8:rpl.find(b'particlesInFirstLayer')-4];VTC=rpl[rpl.find(b'particlesInFirstLayer')-8:rpl.find(b'animationsw')-8]
                        DAU1=rpl[:rpl.find(b'particlesInFirstLayer')-8]
                        VTF=b''
                        if rpl.find(b'skinSubset') != -1:
                            VTF=rpl[rpl.find(b'skinSubset')-8:]
                            CUOI1=rpl[rpl.find(b'animationsw')-8:rpl.find(b'skinSubset')-8]
                        else:
                            CUOI1=rpl[rpl.find(b'animationsw')-8:]
                        while True:
                            if VTC == b'': break
                            CACHE.append(VTC[:int.from_bytes((VTC[:4]),'little')])
                            VTC=VTC[int.from_bytes((VTC[:4]),'little'):]
                        CODETONG=b''
                        for i in CACHE:
                            VT=i.find(b'Element')-8
                            VTDAU=i[VT-8:VT]
                            DAU=i[:VT-8]
                            VTD=i[VT:]
                            CODE=b''
                            for ig in range(i.count(b'Element')):
                                VTC=VTD[:int.from_bytes((VTD[:4]),'little')]
                                VT=VTC[103:111]
                                VT1=VTC[111:121]
                                VT2=VTC[121:167]
                                Cuoi=VTC[int.from_bytes(VTC[167:171],'little')+167:]
                                VTT=VTC[167:int.from_bytes(VTC[167:171],'little')+167]
                                if VTT.find(id[:3].encode())!= -1:
                                    IDEOV = "16707_5"
                                    RPL=VTT[4:].replace(b"hero_skill_effects/167_wukong/",b"component_effects/16707/16707_5/").replace(b"Hero_Skill_Effects/167_wukong/",b"component_effects/16707/16707_5/");RPL=RPL.replace(IDEOV.encode()+b'/'+IDEOV.encode(),IDEOV.encode())
                                else:RPL=VTT[4:]
                                RPL=len(b'\x0b\x00\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+b'\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi
                                CODE+=RPL
                                VTD=VTD[int.from_bytes((VTD[:4]),'little'):]
                            CODE=len(DAU+len(CODE+VTDAU).to_bytes(4,'little')+VTDAU[4:]+CODE).to_bytes(4,'little')+DAU[4:]+len(CODE+VTDAU).to_bytes(4,'little')+VTDAU[4:]+CODE;CODETONG+=CODE
                        if id in('15704','11107'):
                            VTP=CUOI1[:149]
                            CUOI=CUOI1[149:]
                            ELEMENT=[]
                            while True:
                                VT=CUOI[:4]
                                if CUOI==b'': break
                                ELEMENT.append(CUOI[:int.from_bytes(VT,'little')])
                                CUOI=CUOI[int.from_bytes(VT,'little'):]
                            CUOI1=b''
                            for VTC in ELEMENT:
                                VT=VTC[103:111]
                                VT1=VTC[111:121]
                                VT2=VTC[121:167]
                                Cuoi=VTC[int.from_bytes(VTC[167:171],'little')+167:]
                                VTT=VTC[167:int.from_bytes(VTC[167:171],'little')+167]
                                RPL=VTT[4:]
                                RPL=RPL[:5]+id.encode()+b'/'+RPL[5:]
                                RPL=len(b'\x0b\x00\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+b'\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi
                                CUOI1+=RPL
                            CUOI1=VTP[:141]+(len(CUOI1)+8).to_bytes(4,'little')+VTP[145:]+CUOI1
                        CODETONG=len(DAU1[:83]+len((DAU1[83:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF)).to_bytes(4,'little')+DAU1[87:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF).to_bytes(4,'little')+DAU1[4:83]+len((DAU1[83:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF)).to_bytes(4,'little')+DAU1[87:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF
                        #with open('kb1.bytes','wb') as f:f.write(CODETONG)
                        with open(Path,'wb') as f:f.write(CODETONG)



                    if IDCHECK == "52007":
                        if phukien == "do" or "xanh":
                            with open(Path,'rb') as f:rpl=f.read();f.close()
                            CACHE=[]
                            VTR=rpl[rpl.find(b'particlesInFirstLayer')-8:rpl.find(b'particlesInFirstLayer')-4];VTC=rpl[rpl.find(b'particlesInFirstLayer')-8:rpl.find(b'animationsw')-8]
                            DAU1=rpl[:rpl.find(b'particlesInFirstLayer')-8]
                            VTF=b''
                            if rpl.find(b'skinSubset') != -1:
                                VTF=rpl[rpl.find(b'skinSubset')-8:]
                                CUOI1=rpl[rpl.find(b'animationsw')-8:rpl.find(b'skinSubset')-8]
                            else:
                                CUOI1=rpl[rpl.find(b'animationsw')-8:]
                            while True:
                                if VTC == b'': break
                                CACHE.append(VTC[:int.from_bytes((VTC[:4]),'little')])
                                VTC=VTC[int.from_bytes((VTC[:4]),'little'):]
                            CODETONG=b''
                            for i in CACHE:
                                VT=i.find(b'Element')-8
                                VTDAU=i[VT-8:VT]
                                DAU=i[:VT-8]
                                VTD=i[VT:]
                                CODE=b''
                                for ig in range(i.count(b'Element')):
                                    VTC=VTD[:int.from_bytes((VTD[:4]),'little')]
                                    VT=VTC[103:111]
                                    VT1=VTC[111:121]
                                    VT2=VTC[121:167]
                                    Cuoi=VTC[int.from_bytes(VTC[167:171],'little')+167:]
                                    VTT=VTC[167:int.from_bytes(VTC[167:171],'little')+167]
                                    if VTT.find(id[:3].encode())!= -1:
                                        if phukien == "do":
                                            PHUKHIENDO = "5200402"
                                            RPL=VTT[4:].replace(b"hero_skill_effects/520_Veres/",b"component_effects/52007/5200402/").replace(b"hero_skill_effects/520_Veres/",b"component_effects/52007/5200402/");RPL=RPL.replace(PHUKHIENDO.encode()+b'/'+PHUKHIENDO.encode(),PHUKHIENDO.encode())
                                        if phukien == "xanh":
                                            PHUKHIENDO = "5200401"
                                            RPL=VTT[4:].replace(b"hero_skill_effects/520_Veres/",b"component_effects/52007/5200401/").replace(b"hero_skill_effects/520_Veres/",b"component_effects/52007/5200401/");RPL=RPL.replace(PHUKHIENDO.encode()+b'/'+PHUKHIENDO.encode(),PHUKHIENDO.encode())

                                    else:RPL=VTT[4:]
                                    RPL=len(b'\x0b\x00\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+b'\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi
                                    CODE+=RPL
                                    VTD=VTD[int.from_bytes((VTD[:4]),'little'):]
                                CODE=len(DAU+len(CODE+VTDAU).to_bytes(4,'little')+VTDAU[4:]+CODE).to_bytes(4,'little')+DAU[4:]+len(CODE+VTDAU).to_bytes(4,'little')+VTDAU[4:]+CODE;CODETONG+=CODE
                            if id in('15704','11107'):
                                VTP=CUOI1[:149]
                                CUOI=CUOI1[149:]
                                ELEMENT=[]
                                while True:
                                    VT=CUOI[:4]
                                    if CUOI==b'': break
                                    ELEMENT.append(CUOI[:int.from_bytes(VT,'little')])
                                    CUOI=CUOI[int.from_bytes(VT,'little'):]
                                CUOI1=b''
                                for VTC in ELEMENT:
                                    VT=VTC[103:111]
                                    VT1=VTC[111:121]
                                    VT2=VTC[121:167]
                                    Cuoi=VTC[int.from_bytes(VTC[167:171],'little')+167:]
                                    VTT=VTC[167:int.from_bytes(VTC[167:171],'little')+167]
                                    RPL=VTT[4:]
                                    RPL=RPL[:5]+id.encode()+b'/'+RPL[5:]
                                    RPL=len(b'\x0b\x00\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+b'\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi
                                    CUOI1+=RPL
                                CUOI1=VTP[:141]+(len(CUOI1)+8).to_bytes(4,'little')+VTP[145:]+CUOI1
                            CODETONG=len(DAU1[:83]+len((DAU1[83:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF)).to_bytes(4,'little')+DAU1[87:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF).to_bytes(4,'little')+DAU1[4:83]+len((DAU1[83:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF)).to_bytes(4,'little')+DAU1[87:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF
                            #with open('kb1.bytes','wb') as f:f.write(CODETONG)
                            with open(Path,'wb') as f:f.write(CODETONG)
                            







                    else:
                        with open(Path,'rb') as f:rpl=f.read();f.close()
                        CACHE=[]
                        VTR=rpl[rpl.find(b'particlesInFirstLayer')-8:rpl.find(b'particlesInFirstLayer')-4];VTC=rpl[rpl.find(b'particlesInFirstLayer')-8:rpl.find(b'animationsw')-8]
                        DAU1=rpl[:rpl.find(b'particlesInFirstLayer')-8]
                        VTF=b''
                        if rpl.find(b'skinSubset') != -1:
                            VTF=rpl[rpl.find(b'skinSubset')-8:]
                            CUOI1=rpl[rpl.find(b'animationsw')-8:rpl.find(b'skinSubset')-8]
                        else:
                            CUOI1=rpl[rpl.find(b'animationsw')-8:]
                        while True:
                            if VTC == b'': break
                            CACHE.append(VTC[:int.from_bytes((VTC[:4]),'little')])
                            VTC=VTC[int.from_bytes((VTC[:4]),'little'):]
                        CODETONG=b''
                        for i in CACHE:
                            VT=i.find(b'Element')-8
                            VTDAU=i[VT-8:VT]
                            DAU=i[:VT-8]
                            VTD=i[VT:]
                            CODE=b''
                            for ig in range(i.count(b'Element')):
                                VTC=VTD[:int.from_bytes((VTD[:4]),'little')]
                                VT=VTC[103:111]
                                VT1=VTC[111:121]
                                VT2=VTC[121:167]
                                Cuoi=VTC[int.from_bytes(VTC[167:171],'little')+167:]
                                VTT=VTC[167:int.from_bytes(VTC[167:171],'little')+167]
                                if VTT.find(id[:3].encode())!= -1:
                                    RPL=VTT[4:].replace(b"hero_skill_effects/"+(VTT[(VTT.find(b'/',VTT.find(id[:3].encode())-1))+1:(VTT.find(b'/',VTT.find(id[:3].encode())))]),b"hero_skill_effects/"+(VTT[(VTT.find(b'/',VTT.find(id[:3].encode())-1))+1:(VTT.find(b'/',VTT.find(id[:3].encode())))])+b'/'+id.encode()).replace(b"Hero_Skill_Effects/"+(VTT[(VTT.find(b'/',VTT.find(id[:3].encode())-1))+1:(VTT.find(b'/',VTT.find(id[:3].encode())))]),b"Hero_Skill_Effects/"+(VTT[(VTT.find(b'/',VTT.find(id[:3].encode())-1))+1:(VTT.find(b'/',VTT.find(id[:3].encode())))])+b'/'+id.encode());RPL=RPL.replace(id.encode()+b'/'+id.encode(),id.encode())
                                else:RPL=VTT[4:]
                                RPL=len(b'\x0b\x00\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+b'\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi
                                CODE+=RPL
                                VTD=VTD[int.from_bytes((VTD[:4]),'little'):]
                            CODE=len(DAU+len(CODE+VTDAU).to_bytes(4,'little')+VTDAU[4:]+CODE).to_bytes(4,'little')+DAU[4:]+len(CODE+VTDAU).to_bytes(4,'little')+VTDAU[4:]+CODE;CODETONG+=CODE
                        if id in('15704','11107'):
                            VTP=CUOI1[:149]
                            CUOI=CUOI1[149:]
                            ELEMENT=[]
                            while True:
                                VT=CUOI[:4]
                                if CUOI==b'': break
                                ELEMENT.append(CUOI[:int.from_bytes(VT,'little')])
                                CUOI=CUOI[int.from_bytes(VT,'little'):]
                            CUOI1=b''
                            for VTC in ELEMENT:
                                VT=VTC[103:111]
                                VT1=VTC[111:121]
                                VT2=VTC[121:167]
                                Cuoi=VTC[int.from_bytes(VTC[167:171],'little')+167:]
                                VTT=VTC[167:int.from_bytes(VTC[167:171],'little')+167]
                                RPL=VTT[4:]
                                RPL=RPL[:5]+id.encode()+b'/'+RPL[5:]
                                RPL=len(b'\x0b\x00\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+b'\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00'+len(VT+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi).to_bytes(4,'little')+VT[4:]+(len(VT1+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL)+8).to_bytes(4,'little')+VT1[4:]+len(VT2+(len(RPL)+4).to_bytes(4,'little')+RPL).to_bytes(4,'little')+VT2[4:]+(len(RPL)+4).to_bytes(4,'little')+RPL+Cuoi
                                CUOI1+=RPL
                            CUOI1=VTP[:141]+(len(CUOI1)+8).to_bytes(4,'little')+VTP[145:]+CUOI1
                        CODETONG=len(DAU1[:83]+len((DAU1[83:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF)).to_bytes(4,'little')+DAU1[87:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF).to_bytes(4,'little')+DAU1[4:83]+len((DAU1[83:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF)).to_bytes(4,'little')+DAU1[87:91]+(len(DAU1[91:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[95:183]+len(DAU1[183:]+CODETONG+CUOI1).to_bytes(4,'little')+DAU1[187:]+CODETONG+CUOI1)+VTF
                        #with open('kb1.bytes','wb') as f:f.write(CODETONG)
                        with open(Path,'wb') as f:f.write(CODETONG)
                        giai(Path)
                        print('─'*30)
            
            
            
        try:
            a=shutil.make_archive(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/Actor_'+f'{IDCHECK[:3]}'+'_Actions.pkg.bytes','zip',f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod/')
            os.rename(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/Actor_'+f'{IDCHECK[:3]}'+'_Actions.pkg.bytes.zip',f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/Actor_'+f'{IDCHECK[:3]}'+'_Actions.pkg.bytes')
            shutil.rmtree(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod/')
        except Exception as e:
            print(e)
            
        try:
            a=shutil.make_archive(f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/Actor_'+f'{IDCHECK[:3]}'+'_Infos.pkg.bytes','zip',f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/')
            os.rename(f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/Actor_'+f'{IDCHECK[:3]}'+'_Infos.pkg.bytes.zip',f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/Actor_'+f'{IDCHECK[:3]}'+'_Infos.pkg.bytes')
            shutil.rmtree(f'{sanitized_input}/files/Resources/1.55.1/Prefab_Characters/mod/')
        except Exception as e:
            print(e)
    đuongan=f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/commonresource/Back.xml'
    giai(đuongan)
    try:
        a=shutil.make_archive(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes','zip',f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/')
        os.rename(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes.zip',f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes')
        shutil.rmtree(f'{sanitized_input}/files/Resources/1.55.1/Ages/Prefab_Characters/Prefab_Hero/mod1/')
    except Exception as e:
        print(e)
    else:
        pass
    giai(file_actor_mod)
    giai(file_shop_mod)
    giai(file_sound_mod1)
    giai(file_sound_mod2)
    giai(file_sound_mod3)
    giai(file_sound_mod4)
    giai(file_sound_mod5)
    giai(file_mod_Modtion)
    if len(IDMODSKIN1) == 1:
        if initial_modification_time1 != final_modification_time1:
            giai(file_mod_skill1)
        if initial_modification_time2 != final_modification_time2:
            giai(file_mod_skill2)
        if initial_modification_time3 != final_modification_time3:
            giai(file_mod_Character)
    else:
        giai(file_mod_skill1)
        giai(file_mod_skill2)
        giai(file_mod_Character)



