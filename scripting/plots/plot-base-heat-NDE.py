#Update the directory paths accordingly

import plotly.offline as offline
from oemof.tabular.tools.plots_heat_NDE import hourly_plot
name = "base-heat-NDE"
offline.plot(
    hourly_plot(
        name,
        "heat_Bus_NDE",
        '/home/dozeummam/Insync/mnimaruf@gmail.com/Google Drive/projects/models/OSeEM-DE/results/scenarios/base-NDE-SDE',
        plot_filling_levels=False
    ),
    filename= '/home/dozeummam/Insync/mnimaruf@gmail.com/Google Drive/projects/models/OSeEM-DE/results/plots/base-heat-NDE ' 'hourly-plot.html'
    )
