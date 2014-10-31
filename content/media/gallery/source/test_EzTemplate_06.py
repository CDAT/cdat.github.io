import EzTemplate

bg = False
## 12 plot one legend every other plot various orientation for legend

M=EzTemplate.Multi(rows=4,columns=3)
for i in range(12):
    if i%2==1:
        if i%4 == 3:
            M.legend.direction='vertical'
        t=M.get(legend='local')
        M.legend.direction='horizontal'
    else:
        t=M.get()
M.preview('test_EzTemplate_6',bg=bg)

