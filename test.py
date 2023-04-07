'''l1=[1,2,3,4]
l2=[2,4,5,6]
l3=[2,6,7,8]
res= list()
res.extend(i for i in l1 if i not in (l2+l3) and i not in res)
res.extend(i for i in l2 if i not in (l1+l3) and i not in res)
res.extend(i for i in l3 if i not in (l1+l2) and i not in res)
print(res)'''
def dos(**kw):
    print(type(kw))
    for k in kw:
        print(kw.get(k)  )
dos(x=2,y=26)