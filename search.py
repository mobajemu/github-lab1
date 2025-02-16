import json

def search_json(json_data, search_string):
    results = []
    for item in json_data:  # iterate over each item in the JSON data
        if search_string in item.values(): # check if the search string is present in the values of the item
            results.append(item) # if found, add the item to the results list
    return results