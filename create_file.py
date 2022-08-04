import csv
import plotly.express as px
import pandas as pd


def create_csv(file_name, mode, columns, rows):
    if mode == "write":
        m = "w"
    elif mode == "read":
        m = "r"
    else:
        print("Wrong mode")
        return

    with open(file_name, m, newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)
        for row in rows:
            writer.writerow(row)


def create_plot(file_name):
    df = pd.read_csv(file_name)
    fig=px.bar(df, x=[1, 2, 3, 4, 5, 6, 7], y='temperature')
    fig.write_image('plot.png')
