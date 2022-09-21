# Write a python program to get the key of lowest value from the dictionary.


sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
} 

low=sample_dict['C']
key_of_lowest_value=""
for key in sample_dict:
    if(low>sample_dict[key]):
        low=sample_dict[key]
        key_of_lowest_value=key
    
print(key_of_lowest_value)