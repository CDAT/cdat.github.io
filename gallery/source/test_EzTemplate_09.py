import EzTemplate,vcs
## 12 plots 1 legend per row on the right

bg= False

## Initialize VCS
x=vcs.init()

M=EzTemplate.Multi(rows=4,columns=3)
M.legend.direction='vertical'
for i in range(12):
    t=M.get(legend='local')
    if i%3 !=2:
        t.legend.priority=0 # Turn off legend
##     x.plot(s[i],t,iso)
M.preview('test_EzTemplate_09',bg=bg)
