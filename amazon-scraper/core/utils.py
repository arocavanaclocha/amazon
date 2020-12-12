import json

def give_format(file_name):
  results = []
  with open(file_name, 'r') as json_file:
    for line in json_file:
      results.append(line)


  with open(file_name, 'w+') as json_file:
    json_file.write("[")
    for i in range(len(results)):
      json_file.write(results[i])
      if(i<len(results)-1):  
        json_file.write(",")
    json_file.write("]")

