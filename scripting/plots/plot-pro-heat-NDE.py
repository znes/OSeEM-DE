#Update the directory paths accordingly

import plotly.offline as offline
from oemof.tabular.tools.plots_heat_NDE import hourly_plot
name = "pro-heat-NDE"
offline.plot(
    hourly_plot(
        name,
        "heat_Bus_NDE",
        '/home/dozeummam/Insync/mnimaruf@gmail.com/Google Drive/projects/models/OSeEM-DE/results/scenarios/pro-NDE-SDE',
        plot_filling_levels=False
    ),
    filename= '/home/dozeummam/Insync/mnimaruf@gmail.com/Google Drive/projects/models/OSeEM-DE/results/plots/pro-heat-NDE ' 'hourly-plot.html'
    )
