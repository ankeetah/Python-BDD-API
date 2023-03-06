import json

courses = '{"name": "Ankita Gondane","attribute": [88, 2, 3]}'

dict_courses = json.loads(courses)
print(dict_courses)
print(type(dict_courses))

print(dict_courses['name'])
listy = dict_courses['attribute']
print(listy[0])

print(dict_courses['attribute'][0])

#/Users/jithin/Downloads /Users/jithin/Downloads/sample4.json

with open('//Users//jithin//Downloads//sample4.json') as reader:
    matter = json.load(reader)
    print(len(matter))
    print(matter['people'])
    print(len(matter['people']))
    for person in matter['people']:
        print(person)
        if person['firstName'] == 'Joe':
            print(person['age'])
    print(len(matter['people'][0]))
    print(matter['people'][1]['age'])


