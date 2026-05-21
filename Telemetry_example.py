import matplotlib.pyplot as plt

import fastf1.plotting

# Enable Matplotlib patches for plotting timedelta values and load
# fastF1's dark color scheme

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')

#load a session and its telemetry data
session = fastf1.get_session(2026, 'Miami Grand Prix', 'Q')
session.load()

ant_lap = session.laps.pick_drivers('ANT').pick_fastest()
lec_lap = session.laps.pick_drivers('LEC').pick_fastest()

ant_tel = ant_lap.get_car_data().add_distance()
lec_tel = lec_lap.get_car_data().add_distance()

mer_color = fastf1.plotting.get_team_color(ant_lap['Team'], session=session)
fer_color = fastf1.plotting.get_team_color(lec_lap['Team'], session=session)

fig, ax = plt.subplots()
ax.plot(ant_tel['Distance'], ant_tel['Speed'], color=mer_color, label='ANT')
ax.plot(lec_tel['Distance'], lec_tel['Speed'], color=fer_color, label='LEC')
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Speed (km/h)')

ax.legend()
plt.suptitle(f"Fastest Lap Comparison\n " f"{session.event['EventName']} {session.event.year} Qualifying")

plt.show()