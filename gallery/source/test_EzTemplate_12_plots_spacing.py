import EzTemplate,vcs
## 12 plot one legend per row

## Initialize VCS
x=vcs.init()

bg = True
M=EzTemplate.Multi(rows=4,columns=3)
M.spacing.horizontal=.25
M.spacing.vertical=.1

fnm = "test_EzTemplate_12_plots_spacing.png"
M.preview(fnm,bg=bg)
