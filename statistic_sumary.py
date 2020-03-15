import numpy as np
import json
import os
import matplotlib.pyplot as plt
map2color = {
    '2s3z': '#009B48',
    '3s5z': '#B90000',
    '1c3s5z': '#0045AD',
    '3m': '#FF5900',
    '8m': '#FFD500',
    '27m_vs_30m': '#5D5453',
    'MMM2': '#DA4D84',
    '5m_vs_6m': '#0E0D0C',
    '3s_vs_5z': '#4E8BBC',
    '2c_vs_64zg': '#C37DDE',
}
maps = []
win_rates = []
t = []
for i in range(8, 10):
    config_file = f"./results/sacred/{i}/config.json"
    info_file = f"./results/sacred/{i}/info.json"
    if not os.path.isfile(info_file):
        continue
    with open(config_file) as f:
        config = json.load(f)
        map = config['env_args']['map_name']
        maps.append(map)
    with open(info_file) as f:
        info = json.load(f)
    win_rates.append(info['battle_won_mean'])
    t.append(info['battle_won_mean_T'])
#     win_rates.append(info['test_battle_won_mean'])
#     t.append(info['test_battle_won_mean_T'])
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(len(maps)):
    ax.plot(t[i], win_rates[i], label=maps[i], color=map2color[maps[i]])
ax.legend(bbox_to_anchor=(1, 1))
leg = ax.get_legend()
hl_dict = {handle.get_label(): handle for handle in leg.legendHandles}
for key, values in hl_dict.items():
    hl_dict[key].set_color(map2color[key])
ax.ticklabel_format(style='sci',axis='x')
ax.set_xlabel("T")
ax.set_ylabel("Test Win Rate %")
ax.set_ylim(0, 1)
ax.set_xticklabels(['0', '0', '500.0k', '1.0m', '1.5m', '2.0m'])
fig.savefig('qmix_result.png', bbox_inches='tight', dpi=200)

