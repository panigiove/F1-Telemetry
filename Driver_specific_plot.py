from matplotlib import pyplot as plt
import fastf1
from fastf1 import plotting

#Enable Matplotlib patches for plotting timedelta values and load
#FastF1's dark color scheme

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')

race = fastf1.get_session(2026, 'Chinese Grand Prix', 'R')
race.load()

fig, ax = plt.subplots(figsize=(10, 6))

for driver in race.drivers:
    driver_info = race.get_driver(driver)
    driver_code = driver_info['Abbreviation']
    laps = race.laps.pick_drivers(driver).pick_quicklaps().reset_index()
    style = plotting.get_driver_style(identifier=driver_code, style=['color', 'linestyle'],
                                      session=race)
    ax.plot(laps['LapNumber'], laps['LapTime'], **style, label=driver_code)

# add axis labels and a legend

ax.set_xlabel('Lap Number')
ax.set_ylabel('Lap Time')
plotting.add_sorted_driver_legend(ax, race)
plt.show()
