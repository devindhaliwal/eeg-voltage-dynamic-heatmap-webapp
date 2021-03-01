import pandas as pd
import plotly.express as px

def generate_plot():
    df = pd.read_csv("VoltageTimeSeries_Updated.csv")
    df_peripheral = pd.read_csv("129Channels_v2.csv")
    df_peripheral.rename(columns={"Unnamed: 0": "Electrode"}, inplace=True)
    df_peripheral.fillna(0, inplace=True)
    df_peripheral.drop(columns=["X", "Y", "Z"], inplace=True)
    # dropping last 1 row
    df.drop(df.tail(1).index, inplace=True)

    # melting dataframe so each row contains information about time and voltage for each electrode,
    # instead of having time as a column
    df = pd.melt(df, id_vars=df.columns[:4].tolist(), value_vars=df.columns[4:].tolist(),
                 var_name='Time', value_name='Voltage (uV)')

    # calculating which epoch each time corresponds to
    df["Epoch"] = df.Time.str.split(".").str[1]
    df.Time = df.Time.str.split(".").str[0]
    df.Epoch.fillna(0, inplace=True)
    df.Epoch = pd.to_numeric(df.Epoch)
    df.Epoch = df.Epoch + 1
    # creating Frame column to display on the slider
    df["Frame"] = "Epoch: " + df.Epoch.astype(str) + ", Time(ms): " + df.Time

    # creating plot
    fig = px.scatter_3d(df, x="X", y="Y", z="Z", color="Voltage (uV)",
                        animation_frame="Frame", animation_group="Voltage (uV)", range_color=[-33, 33],
                        color_continuous_scale=px.colors.sequential.Agsunset,
                        title="EEG Electrode Voltage Heatmap over 5 Epochs")

    # modifying animation speed
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = .000000001
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = .000000001

    return fig

