# __author__ == "david Matten"

import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import argparse


def main(source_fn, wd):
    if wd is None:
        outfile = os.path.join(os.path.split(source_fn)[0], "glycans")
    else:
        outfile = os.path.join(wd, "glycans")

    df = pd.read_csv(source_fn)

    all_seqids = df['seqid'].unique()
    all_positions = df['position'].unique()

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')

#    fig1.set_size_inches(18.5*2, 10.5*2)

    position_mapping_dct = {}
    for i, position in enumerate(all_positions):
        position_mapping_dct[position] = i

    y_val_dict = {}
    for i, seqid in enumerate(all_seqids):
        y_val_dict[seqid] = i

    all_black_marks = df[df['black'] == 1]
    print(all_black_marks)

    all_grey_marks = df[df['grey'] == 1]
    print(all_grey_marks)

    marker_size = 10
    black_x, black_y, grey_x, grey_y, black_sizes, grey_sizes = [], [], [], [], [], []
    all_x, all_y = [], []
    for row in df.itertuples():
        i += 1
        index = row[0]
        seqid = row[1]
        position = row[2]
        black = row[3]
        grey = row[4]
        this_y = y_val_dict[seqid]
        this_x = position_mapping_dct[position]
        all_x.append(this_x)
        all_y.append(this_y)

        if black == 1:
            black_x.append(this_x)
            black_y.append(this_y)
            black_sizes.append(marker_size)
        else:
            grey_x.append(this_x)
            grey_y.append(this_y)
            grey_sizes.append(marker_size)

    all_x = list(set(all_x))
    all_y = list(set(all_y))
    for x in all_x:
        ax1.axvline(x, ymin=-3, ymax=999, linewidth=0.5, alpha=0.3)
    for y in all_y:
        ax1.axhline(y, xmin=-3, xmax=999, linewidth=0.5, alpha=0.3)

    # The order of plotting matters if there is overlap
    plt.scatter(grey_x, grey_y, marker='s', c='lightgrey', s=grey_sizes)
    plt.scatter(black_x, black_y, marker='s', c='black', s=black_sizes)

    # Apply x and y ticks to axes.
    plt.yticks(list(y_val_dict.values()), list(y_val_dict.keys()), size=6)
    plt.xticks(list(position_mapping_dct.values()), list(position_mapping_dct.keys()), rotation='vertical', size=6)

    ax1.set_xlim(-0.8, len(all_x)) #, auto=True
    ax1.set_ylim(-0.8, len(all_y), auto=True)

    plt.show()

    fig1.savefig(outfile + '.pdf', dpi=400, bbox_inches='tight')
    fig1.savefig(outfile + '.png', dpi=400, bbox_inches='tight')


if __name__ == "__main__":
    if not sys.version_info >= (3,2):
        print("Please run using python version >= 3.2\nNow exiting")
        sys.exit()

    parser = argparse.ArgumentParser(description='Plotter for visualizing glycan attachment from .csv files.')
    parser.add_argument('-in_file', '--input_file', type=str,
                        help='Input .csv file.', required=True)
    parser.add_argument('-wd', '--working_directory', type=str, required=False,
                        help='If you would like output to be created elsewhere to the source file, specify a working '
                             'directory here. ')

    args = parser.parse_args()

    in_file = args.input_file
    wd = args.working_directory

    # in_file = "generalized_plot_source-lots_more_data.csv"
    # in_file = "generalized_plot_source-lots_of_data.csv"
    # in_file = "generalized_plot_source.csv"
    #in_file = "generalized_plot_source-medium.csv"

    main(in_file, wd)


