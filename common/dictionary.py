data= { 
    'name':'john',
    'age':30,
    'skills':['python','c','c++']

}
print(data['name'])
print(data['age'])
print(data['skills'][-1])


data2={
    'report':{
        'alex': {
            'maths':[40,38,78],
            'science':[30,40,50]
        },
        'ashish':{
            'maths':[45,48,98],
            'science':[50,40,90]
        }
    }
}
print(data2['report']['alex'])
print(data2['report']['ashish'])
print(data2['report']['alex']['maths'])
print(sum(data2['report']['alex']['maths']))
