import requests
import json


with open(filename, 'r') as infile:
    chicken = json.loads(infile.read())


headers = {'Content-Type': 'application/json'}
chicken_dic = {}

def get_recipe():
    match_list=chicken["matches"]
    i=0
    for matches in match_list:
        print ("match" , i+1 , "is:")
        search_url = 'http://api.yummly.com/v1/api/recipe/' + match_list[i]["id"] + '?_app_id=4884cd95&_app_key=da496643eba26f82c06429b0dd386eed'
        api_url = search_url
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            recipe_info = json.loads(response.content.decode('utf-8'))
            chicken_dic[i]=recipe_info
            chicken_dic[i]["ingredients"]=chicken["matches"][i]["ingredients"]
            print (chicken["matches"][i]["ingredients"])
            i += 1
        with open(keywords, 'w') as outfile:
            json.dump(chicken_dic, outfile)





get_recipe()
