from fillplots import Plotter

plotter = Plotter([
    [(lambda x1: -x1 + 5.7, True),
     (lambda x1: x1 - 1.6,),
     (lambda x1: -x1 / 2,)],
], xlim=(0, 6), ylim=(0, 6))
(ineq0, ineq1, ineq2) = plotter.regions[0].inequalities
ineq0.boundary.config.line_args['label'] = '$x_2 \leq 5.7 - x_1$'
ineq1.boundary.config.line_args['label'] = '$x_2 \geq x_1 - 1.6$'
ineq2.boundary.config.line_args['label'] = '$x_2 = -x_1 / 2$'
for reg in plotter.regions:
    reg.config.fill_args['facecolor'] = 'pink'
plotter.regions[0].inequalities[0].config.line_args = {'color': 'blue', 'linewidth': 3}
plotter.regions[0].inequalities[1].config.line_args = {'color': 'green', 'linewidth': 3}
plotter.regions[0].inequalities[2].config.line_args = {'color': 'black', 'linewidth': 3}
plotter.plot()
plotter.ax.legend(loc='best')
plotter.ax.set_xlabel('$x_1$', fontsize=20, labelpad=20)
plotter.ax.set_ylabel('$x_2$', fontsize=20, labelpad=20)
