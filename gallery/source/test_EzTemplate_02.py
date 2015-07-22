import EzTemplate
## 12 plot one legend per plot

bg = False


M=EzTemplate.Multi(rows=4,columns=3)
M.legend.direction='vertical'
for i in range(12):
    t=M.get(legend='local')

M.preview('test_EzTemplate_02',bg=bg)


