import csv
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

if len(sys.argv) != 2:
    sys.exit('usage: python3 plot.py file.csv')

csv_path = sys.argv[1]
with open(csv_path, encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

periods = [
    ('E_4ps_meV', '4 ps', '#cfcfcf'),
    ('E_40ps_meV', '40 ps', '#8fb3e0'),
    ('E_400ps_meV', '400 ps', '#1f4e9a'),
]

plt.rcParams.update({'font.size': 9, 'font.family': 'serif', 'mathtext.fontset': 'dejavuserif'})
fig, ax = plt.subplots(figsize=(4.6, 2.7))

w = 0.26
for k, (col, label, color) in enumerate(periods):
    xs = [i + (k - 1) * w for i in range(len(rows))]
    ys = [float(r[col]) for r in rows]
    ax.bar(xs, ys, w, label=label, color=color, edgecolor='#333333', linewidth=0.5, zorder=3)

ax.axhline(0.0597, color='#a01818', ls='--', lw=1, zorder=4, label='Landauerjeva limita (pri 1 K)')

ax.set_ylim(0, 5)
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:g}'.replace('.', ',')))
ax.set_ylabel('Energija na seštevanje [meV]')

ax.set_xticks(range(len(rows)))
ax.set_xticklabels([r['oznaka'] for r in rows])
ax.set_xlim(-0.55, len(rows) - 0.45)

ax.grid(axis='y', color='#e3e3e3', zorder=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(ncol=4, handlelength=1.5, columnspacing=0.9, frameon=False,
          loc='lower center', bbox_to_anchor=(0.5, 1.0), fontsize=7.5)

fig.tight_layout()
out = os.path.splitext(csv_path)[0] + '.pdf'
fig.savefig(out)
print(out)
