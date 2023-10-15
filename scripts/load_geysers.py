from agi.stk12.stkdesktop import STKDesktop
from pathlib import Path
import pandas as pd
from agi.stk12.stkobjects import (
    IAgStkObject,
    IAgPlace,
)


GEYSER_DATA_PATH: Path = Path("./data/geysers.csv")

if __name__ == "__main__":
    print("Connecting to STK...")
    stk = STKDesktop.AttachToApplication()
    print(stk)
    stk_root = stk.Root
    stk_scenario_obj: IAgStkObject = stk_root.CurrentScenario

    print("Loading data...")
    df = pd.read_csv(GEYSER_DATA_PATH)
    print(df)

    df["Lon"] = df["Lon"] * -1  # flip West longitude to East longitude as STK expects

    # create a Place object for each geyser
    for index, row in df.iterrows():
        geyser_id = int(row["ID"])
        lat = float(row["Lat"])
        lon = float(row["Lon"])

        geyser_name = f"Geyser_{geyser_id}"

        print(f"Adding '{geyser_name}' at LAT:{lat} LON:{lon}")
        geyser: IAgPlace = stk_scenario_obj.Children.New(
            32, geyser_name
        )  # '32' corresponds to the type 'Place'
        geyser.Graphics.LabelVisible = False
        geyser.Position.AssignGeodetic(lat, lon, 0)

    input("Done. Press any key to quit...")
