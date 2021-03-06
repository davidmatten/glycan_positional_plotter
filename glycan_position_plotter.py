# __author__ == "david Matten"

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

source_fn = "generalized_plot_source-lots_of_data.csv"

df = pd.read_csv(source_fn)

all_seqids = df['seqid'].unique()
all_positions = df['position'].unique()

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
cmap = plt.cm.get_cmap("bwr")

font = {'family': 'monospace',
        'color':  'black',
        'weight': 'normal',
        'size': 7,
        }

position_mapping_dct = {}
for i, position in enumerate(all_positions):
    position_mapping_dct[position] = i

y_val_dict = {}
for i, seqid in enumerate(all_seqids):
    y_val_dict[seqid] = i

clr = "black"
longest_seqid = max([len(str(id)) for id in all_seqids])

for row in df.itertuples():
    index = row[0]
    seqid = row[1]
    position = row[2]
    black = row[3]
    grey = row[4]
    this_y = y_val_dict[seqid]
    if black == 1:
        clr = "black"
        ax1.add_patch(patches.Rectangle((position_mapping_dct[position] + 0.1, this_y + 0.1), 0.8, 0.8, facecolor=clr))
    if grey == 1:
        clr = "lightgrey"
        ax1.add_patch(patches.Rectangle((position_mapping_dct[position] + 0.1, this_y + 0.1), 0.8, 0.8, facecolor=clr))

    # plotting the labels on the y axis.
    plt.text(-1*(longest_seqid/2)-1, this_y+0.1, seqid, fontdict=font)

# plotting labels on the x axis. && vertical thin blue lines through boxes.
for i, pos in enumerate(all_positions):
    plt.text(i+0.1, -1, "N{}".format(pos), rotation=90, fontdict=font)
    ax1.axvline(i+0.5, ymin=-3, ymax=100, linewidth=1, alpha=0.3)

#  because no "data" is being plotted, only patches - matplotlib doesn't know how large to make the plot.
ax1.set_xlim(0, len(all_positions)) #, auto=True
ax1.set_ylim(0, len(all_seqids), auto=True)

plt.tick_params(
    axis='x',           # changes apply to the x-axis
    which='both',       # both major and minor t    icks are affected
    bottom='off',       # ticks along the bottom edge are off
    top='off',          # ticks along the top edge are off
    labelbottom='off')  # labels along the bottom edge are off

plt.tick_params(
    axis='y',           # changes apply to the x-axis
    which='both',       # both major and minor ticks are affected
    bottom='off',       # ticks along the bottom edge are off
    top='off',          # ticks along the top edge are off
    labelbottom='off')  # labels along the bottom edge are off

frame1 = plt.gca()
frame1.axes.get_yaxis().set_ticks([])

plt.title("Occupied glycan positions")

plt.show()
fig1.savefig('glycans.pdf', dpi=400, bbox_inches='tight')
fig1.savefig('glycans.png', dpi=400, bbox_inches='tight')