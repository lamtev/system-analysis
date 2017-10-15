from math import inf

from fillplots import Plotter, annotate_regions

plotter = Plotter([
    [(lambda x1: -x1 + 5.7, True),
     (lambda x1: x1 - 1.6,),
     (lambda x1: -x1 / 2,),
     (0,),
     (lambda x1: x1 / inf,),
     (lambda x1: x1 / inf + 5, True)],
], xlim=(-1, 7), ylim=(-2, 7))
(ineq0, ineq1, ineq2, ineq3, ineq4, ineq5) = plotter.regions[0].inequalities
ineq0.boundary.config.line_args['label'] = '$x_1 + x_2 = 5.7$'
ineq1.boundary.config.line_args['label'] = '$x_1 - x_2 = 1.6$'
ineq2.boundary.config.line_args['label'] = '$x_1 + 2x_2 = 0$'
ineq3.boundary.config.line_args['label'] = '$x_1 = 0$'
ineq4.boundary.config.line_args['label'] = '$x_2 = 0$'
ineq5.boundary.config.line_args['label'] = '$x_2 = 5$'
for reg in plotter.regions:
    reg.config.fill_args['facecolor'] = 'pink'
plotter.regions[0].inequalities[0].config.line_args = {'color': 'blue', 'linewidth': 2}
plotter.regions[0].inequalities[1].config.line_args = {'color': 'green', 'linewidth': 2}
plotter.regions[0].inequalities[2].config.line_args = {'color': 'black', 'linewidth': 2}
plotter.regions[0].inequalities[3].config.line_args = {'color': 'blue', 'linewidth': 1, 'linestyle': 'dashed'}
plotter.regions[0].inequalities[4].config.line_args = {'color': 'black', 'linewidth': 1, 'linestyle': 'dashed'}
plotter.regions[0].inequalities[5].config.line_args = {'color': 'red', 'linewidth': 2}
plotter.plot()
plotter.ax.legend(loc='center right', fontsize='x-large')
plotter.ax.set_xlabel('$x_1$', fontsize=20, labelpad=20)
plotter.ax.set_ylabel('$x_2$', fontsize=20, labelpad=20)
annotate_regions(plotter.regions, 'ОДР')
