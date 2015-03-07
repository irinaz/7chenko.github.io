__author__ = 'misha'

import json

#assumes your json is in a string my_json
with open("sla-node-28741.json", "r") as myfile:
    my_json = myfile.read()

json_dict = json.loads(my_json)

#where f is a file object like

f = open("csv.csv", "w")

#json_dict is a dictionary of dictionaries representing your json where you can get objects and values like this;

for node in json_dict["nodes"]:
    #print node["node"]["field_event_time"]
#    for obj in key:
    f.write(node["node"]["field_event_time"] + "," + node["node"]["field_event_time"] + "," +
            node["node"]["field_event_type"] + "\n")

