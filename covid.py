import requests
import json

req = requests.get('https://api.covid19india.org/state_district_wise.json')
data = json.loads(req.text)
state_names = """1) Andaman and Nicobar Islands\t\t\t\t11) Gujarat\t\t\t21) Meghalaya\t\t\t31) Telangana
2) Andhra Pradesh\t\t\t\t\t12) Himachal Pradesh\t\t22) Manipur\t\t\t32) Tamil Nadu
3) Arunachal Pradesh\t\t\t\t\t13) Haryana\t\t\t23) Madhya Pradesh\t\t33) Tripura
4) Assam\t\t\t\t\t\t14) Jharkhand\t\t\t24) Mizoram\t\t\t34) Uttar Pradesh
5) Bihar\t\t\t\t\t\t15) Jammu and Kashmir\t\t25) Nagaland\t\t\t35) Uttarakhand
6) Chandigarh\t\t\t\t\t\t16) Karnataka\t\t\t26) Odisha\t\t\t36) West Bengal
7) Chhattisgarh\t\t\t\t\t\t17) Kerala\t\t\t27) Punjab
8) Delhi\t\t\t\t\t\t18) Ladakh\t\t\t28) Puducherry
9) Dadra and Nagar Haveli and Daman and Diu\t\t19) Lakshadweep\t\t\t29) Rajasthan
10) Goa\t\t\t\t\t\t\t20) Maharashtra\t\t\t30) Sikkim 
"""


values = {
	"state" : None,
	"district" : None
}

def getMaxspacetab(ch):
	return len(ch)//4

def distict_data():
	dis = list(data[values["state"]]["districtData"].keys())[3:]
	res = ['', '', '', '', '', '' ,'', '', '', '']
	tab_count = getMaxspacetab(max(dis , key=lambda x:len(x)))
	try :
		for ind in range(0, len(dis), 10):
			for x in range(10):
				res[x] =  res[x] + str(ind+x) + ') ' +dis[ind+x] + '\t'*tab_count
	except IndexError:
		return '\n'.join(res)

def printFun():
	if not values["state"]:
		print(state_names)
		values["state"] = list(data.keys())[int(input("\nEnter the State Number : "))]

	if not values["district"]:
		print(distict_data())
		values["district"] = list(data[values["state"]]["districtData"].keys())[int(input("\nEnter the District Number : "))]

printFun()
for key, values in data[values["state"]]["districtData"][values["district"]].items():
	if values == "": continue
	print(key , " : " , values)