class Article:
    author=""
    title=""
    content=""
    likes=0
    def __str__(self):
        return self.title
    def summary(self):
        return self.content[:15]
    
a1=Article()
a1.author="john"
a1.title="python is awesome"
a1.content="tum kaha chle gye"
a1.likes=100

a2=Article()
a2.author="janagana"
a2.title="hum sath sath hain"
a2.content="same content will be here soon"
a2.likes=1000


a3=Article()
a3.author="john doe"
a3.title="tum bhi ho"
a3.content="same contentn will  be here soon"
a3.likes=100

print("our article are:")
print(a1)
print(a1.summary())
print(a2)
print(a2.summary())
print(a3)
print(a3.summary())



    





