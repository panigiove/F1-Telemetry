import seaborn as sns
from matplotlib import pyplot as plt

import fastf1
import fastf1.plotting

# Enable Matplotlib patches for plotting timedelta values and load
# FastF1's dark color scheme
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')

race = fastf1.get_session(2024, 'Monaco Grand Prix', 'R')
race.load()

point_finishers = race.drivers[:16]
print(point_finishers)

driver_laps = race.laps.pick_drivers(point_finishers).pick_quicklaps()
driver_laps = driver_laps.reset_index()

finishing_order = [race.get_driver(i)["Abbreviation"] for i in point_finishers]
print(finishing_order)

# Create the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Seaborn doesn't have proper timedelta support,
# so we have to convert timedelta to float (in seconds)

driver_laps["LapTime(s)"] = driver_laps["LapTime"].dt.total_seconds()

sns.violinplot(data=driver_laps,
               x='Driver',
               y='LapTime(s)',
               hue="Driver",
               density_norm="area",
               order=finishing_order,
               palette=fastf1.plotting.get_driver_color_mapping(session=race),
               )

sns.swarmplot(data=driver_laps,
            x="Driver",
            y="LapTime(s)",
            order=finishing_order,
            hue="Compound",
            palette=fastf1.plotting.get_compound_mapping(session=race),
            hue_order=["SOFT", "MEDIUM", "HARD"],
            linewidth=0,
            size=4
            )

ax.set_xlabel("Driver")
ax.set_ylabel("Lap Time (s)")
plt.suptitle("2024 Monaco Grand Prix Laptime Distribution")
sns.despine(left=True, bottom=True)

plt.tight_layout()
plt.show()

# 0423 22744

# Domani pomeriggio, Dottor Curato, 17:40, costo 137 €
# Sabato mattina alle 8, 
