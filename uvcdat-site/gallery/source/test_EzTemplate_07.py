import EzTemplate
## 12 plots plotted in reverse order

bg = False

M=EzTemplate.Multi(rows=4,columns=3)


icol=3
irow=4
for i in range(12):
    if i % 3 == 0:
        irow-=1
    icol-=1
    t=M.get(column=icol,row=irow)
    if icol==0 : icol=3
M.preview('test_EzTemplate_7',bg=bg)


