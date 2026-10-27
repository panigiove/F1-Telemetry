import matplotlib.pyplot as plt

import fastf1.plotting

# Enable Matplotlib patches for plotting timedelta values and load
# fastF1's dark color scheme

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')

#load a session and its telemetry data
session = fastf1.get_session(2026, 'Austrian grand Prix', 'Q')
session.load()

ant_lap = session.laps.pick_drivers('ANT').pick_fastest()
lec_lap = session.laps.pick_drivers('RUS').pick_fastest()

ant_tel = ant_lap.get_car_data().add_distance()
lec_tel = lec_lap.get_car_data().add_distance()

mer_color = fastf1.plotting.get_team_color(ant_lap['Team'], session=session)
fer_color = fastf1.plotting.get_team_color(lec_lap['Team'], session=session)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

ax1.plot(
    ant_tel['Distance'],
    ant_tel['Speed'],
    color=mer_color,
    linewidth=2.2,
    label='ANT Speed'
)
ax1.plot(
    lec_tel['Distance'],
    lec_tel['Speed'],
    color=fer_color,
    linewidth=2.2,
    linestyle='--',
    label='LEC Speed'
)
ax1.set_ylabel('Speed (km/h)')
ax1.set_title('Speed Comparison')
ax1.grid(True, alpha=0.3)

ax2.plot(
    ant_tel['Distance'],
    ant_tel['Throttle'],
    color=mer_color,
    linewidth=1.8,
    alpha=0.8,
    label='ANT Throttle'
)
ax2.plot(
    lec_tel['Distance'],
    lec_tel['Throttle'],
    color=fer_color,
    linewidth=1.8,
    linestyle='--',
    alpha=0.8,
    label='LEC Throttle'
)
ax2.plot(
    ant_tel['Distance'],
    ant_tel['Brake'],
    color=mer_color,
    linewidth=1.2,
    alpha=0.6,
    linestyle=':',
    label='ANT Brake'
)
ax2.plot(
    lec_tel['Distance'],
    lec_tel['Brake'],
    color=fer_color,
    linewidth=1.2,
    linestyle=':',
    alpha=0.6,
    label='LEC Brake'
)
ax2.set_xlabel('Distance (m)')
ax2.set_ylabel('Throttle / Brake')
ax2.set_title('Throttle and Brake Comparison')
ax2.grid(True, alpha=0.3)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
fig.legend(lines1 + lines2, labels1 + labels2, loc='upper center', ncol=4, bbox_to_anchor=(0.5, 0.98))

plt.suptitle(f"Telemetry Comparison\n{session.event['EventName']} {session.event.year} Qualifying")
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()