#Update the directory paths accordingly

import plotly.offline as offline
from oemof.tabular.tools.plots_heat_SDE import hourly_plot
name = "con-heat-SDE"
offline.plot(
    hourly_plot(
        name,
        "heat_Bus_SDE",
        '/home/dozeummam/Insync/mnimaruf@gmail.com/Google Drive/projects/models/OSeEM-DE/results/scenarios/con-NDE-SDE',
        plot_filling_levels=False
    ),
    filename= '/home/dozeummam/Insync/mnimaruf@gmail.com/Google Drive/projects/models/OSeEM-DE/results/plots/con-heat-SDE ' 'hourly-plot.html'
    )
