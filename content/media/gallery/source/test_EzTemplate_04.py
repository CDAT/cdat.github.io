import EzTemplate
## 12 plot playing with margins and legend thickness

bg = False

M=EzTemplate.Multi(rows=4,columns=3)
M.margins.top=.25
M.margins.bottom=.25
M.margins.left=.25
M.margins.right=.25

## The legend uses the bottom margin for display are
## We need to "shrink it"
M.legend.thickness=.1
for i in range(12):
    t=M.get()

M.preview('test_EzTemplate_4',bg=bg)


