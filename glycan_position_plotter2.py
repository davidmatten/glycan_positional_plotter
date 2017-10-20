# __author__ == "david Matten"

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

source_fn = "generalized_plot_source-lots_of_data.csv"
#source_fn = "generalized_plot_source.csv"

df = pd.read_csv(source_fn)

all_seqids = df['seqid'].unique()
all_positions = df['position'].unique()

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')

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

all_black_marks = df[df['black']==1]
print(all_black_marks)

all_grey_marks = df[df['grey']==1]
print(all_grey_marks)

black_x, black_y, grey_x, grey_y = [], [], [], []
for row in df.itertuples():
    index = row[0]
    seqid = row[1]
    position = row[2]
    black = row[3]
    grey = row[4]
    this_y = y_val_dict[seqid]
    this_x = position_mapping_dct[position]

    if black == 1:
        black_x.append(this_x)
        black_y.append(this_y)
    else:
        grey_x.append(this_x)
        grey_y.append(this_y)

# The order of plotting matters if there is overlap
plt.plot(grey_x, grey_y, 's', c='lightgrey')
plt.plot(black_x, black_y, 's', c='black')

plt.yticks(list(y_val_dict.values()), list(y_val_dict.keys()))
plt.xticks(list(position_mapping_dct.values()), list(position_mapping_dct.keys()), rotation='vertical')

plt.show()
fig1.savefig('glycans.pdf', dpi=400, bbox_inches='tight')
fig1.savefig('glycans.png', dpi=400, bbox_inches='tight')
