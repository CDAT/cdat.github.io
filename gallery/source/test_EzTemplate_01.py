import EzTemplate

bg= False

M=EzTemplate.Multi(rows=4,columns=3)

for i in range(12):
    t=M.get()
##     x.plot(s[i],t,iso)
M.preview('test_EzTemplate_01',bg=bg)
