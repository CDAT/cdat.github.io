import EzTemplate,vcs
## 12 plot one legend per row

## Initialize VCS
x=vcs.init()
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
fnm = "test_EzTemplate_12_plots_margins_thickness.png"
M.preview(fnm,bg=True)
