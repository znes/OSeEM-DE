#Update the directory paths accordingly

import plotly.offline as offline
from oemof.tabular.tools.plots_SDE import hourly_plot
name = "base-elec-SDE"
offline.plot(
    hourly_plot(
        name,
        "elec_Bus_SDE",
        '/home/dozeummam/Insync/mnimaruf@gmail.com/Google Drive/projects/models/OSeEM-DE/results/scenarios/base-NDE-SDE',
        plot_filling_levels=False
    ),
    filename= '/home/dozeummam/Insync/mnimaruf@gmail.com/Google Drive/projects/models/OSeEM-DE/results/plots/base-elec-SDE ' 'hourly-plot.html'
    )
