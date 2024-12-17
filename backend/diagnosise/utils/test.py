from ai_request import ai_request


ai_request = ai_request('Тошнота, рвота, острые боли в животе')
disease_category = ai_request['disease_category']
description = ai_request['description']

print(disease_category)
print(description)