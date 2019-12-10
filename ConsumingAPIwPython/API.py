
import requests 

url = "http://127.0.0.1:5000/cars" 

response = requests.get(url) 

data = response.json() 

#output to console print (data) 





for car in data["cars"]:    

    print (car) 





import json 

#other code 

#save this to a file 

filename = 'cars.json' 

if filename:     

    # Writing JSON data     

     with open(filename, 'w') as f: 

        json.dump(data, f, indent=4) 



from xlwt import * 

#other code

# # write to excel file

w = Workbook()

ws = w.add_sheet('cars')

row = 0;

ws.write(row, 0, "reg") 

ws.write(row, 1, "make") 

ws.write(row, 2, "model") 

ws.write(row, 3, "price") row += 1

for car in data["cars"]: 

    ws.write(row, 0, car["reg"]) 

    ws.write(row, 1, car["make"]) 

    ws.write(row, 2, car["model"]) 

    ws.write(row, 3, car["price"]) row += 1 

    w.save('cars.xls')

 

 import requests import json 

 dataString = {'reg':'08 C 1234','make':'Ford','model':'Galaxy','pr ice':12324} url = 'http://127.0.0.1:5000/cars' 

 response = requests.post(url, json=dataString) 

 print (response.status_code)





 import requests import json 

 dataString = {'make':'Ford','model':'Kuga'} url = 'http://127.0.0.1:5000/cars/test' 

 response = requests.put(url, json=dataString) 

 print (response.status_code) print (response.text) 	

  

 import requests 

 url = 'http://127.0.0.1:5000/cars/08%20C%201234' response = requests.delete(url) print (response.status_code) print (response.text) 	

  

 import requests, json  

 #url = "https://api.github.com/users?since=100" 

 url = "https://api.github.com/users/andrewbeattycourseware/follow ers" 

 response = requests.get(url) data = response.json() #print(data) 

 #Get the file name for the new file to write 

 filename = 'githubusers.json' with open(filename, 'w') as f:     

    json.dump(data, f, indent=4) 

 
