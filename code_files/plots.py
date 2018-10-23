#! /usr/bin/env python
"""Module contains graphing code."""

import matplotlib.pyplot as plt
import data_manager as dm


def create_plot():
    """Create plot."""
    fig = plt.figure()
    fig.set_size_inches(6, 3.375)

    # Create the plots
    industry_plot = plt.subplot(1, 3, 1)
    building_plot = plt.subplot(1, 3, 2)
    cre_plot = plt.subplot(1, 3, 3)

    industrial = dm.get_csv_data('../data/energy_industrial.csv', indexCol=0)
    building_data = dm.get_csv_data('../data/energy_building.csv', indexCol=0)
    cre = dm.get_get_csv('../data/cre_total,csv', indexCol=0)

    industry_plot.bar(len(industry_plot.index), )
