import pandas as pd
df = pd.read_csv("Cheapestelectriccars-EVDatabase.csv")

df["Subtitle"] = df["Subtitle"].apply(lambda i: i.split("|       ")[1]).apply(lambda i: i.split(" kWh")[0])
df["Acceleration"] = df["Acceleration"].apply(lambda i: i.split(" sec")[0])
df["TopSpeed"] = df["TopSpeed"].apply(lambda i: i.split(" km/h")[0])
df["Range"] = df["Range"].apply(lambda i: i.split(" km")[0])
df["Efficiency"] = df["Efficiency"].apply(lambda i: i.split(" Wh/km")[0])
df["FastChargeSpeed"] = df["FastChargeSpeed"].apply(lambda i: i.split(" km/h")[0] if i != "-" else "")
df["PriceinGermany"] = df["PriceinGermany"].str.extract(r"(\d.*)")
df["PriceinUK"] = df["PriceinUK"].str.extract(r"(\d.*)")
df["Brand"] = df["Name"].apply(lambda i: i.split(" ")[0])

df.to_csv("clean_electricity_car.csv", index = False)