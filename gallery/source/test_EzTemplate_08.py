import EzTemplate
## 12 plots plotted with different spacing param

bg = False

M=EzTemplate.Multi(rows=4,columns=3)
M.spacing.horizontal=.25
M.spacing.vertical=.1
M.preview('test_EzTemplate_8')
