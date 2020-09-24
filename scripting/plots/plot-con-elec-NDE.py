#Update the directory paths accordingly

import plotly.offline as offline
from oemof.tabular.tools.plots_NDE import hourly_plot
name = "con-elec-NDE"
offline.plot(
    hourly_plot(
        name,
        "elec_Bus_NDE",
        '/home/dozeummam/Insync/mnimaruf@gmail.com/Google Drive/projects/models/OSeEM-DE/results/scenarios/con-NDE-SDE',
        plot_filling_levels=False
    ),
    filename= '/home/dozeummam/Insync/mnimaruf@gmail.com/Google Drive/projects/models/OSeEM-DE/results/plots/con-elec-NDE ' 'hourly-plot.html'
    )
