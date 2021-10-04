import pandas as pd
df = pd.read_csv("Cheapestelectriccars-EVDatabase.csv")

df["Subtitle"] = df["Subtitle"].apply(lambda i: i.split("|       ")[1]).apply(lambda i: i.split(" kWh")[0])
df["Acceleration"] = df["Acceleration"].apply(lambda i: i.split(" sec")[0])
df["TopSpeed"] = df["TopSpeed"].apply(lambda i: i.split(" km/h")[0])
df["Range"] = df["Range"].apply(lambda i: i.split(" km")[0])
df["Efficiency"] = df["Efficiency"].apply(lambda i: i.split(" Wh/km")[0])
df["FastChargeSpeed"] = df["FastChargeSpeed"].apply(lambda i: i.split(" km/h")[0] if i != "-" else "")
df["PriceinGermany"] = df["PriceinGermany"].str.extract(r"(\d.*)")
df["PriceinGermany"] = df["PriceinGermany"].apply(lambda i: i.replace(",", "") if str(i) != "nan" else i)
df["PriceinGermany"] = df["PriceinGermany"].apply(lambda i: int(i) if str(i) != "nan" else i)
df["PriceinUK"] = df["PriceinUK"].str.extract(r"(\d.*)")
df["PriceinUK"] = df["PriceinUK"].apply(lambda i: i.replace(",", "") if str(i) != "nan" else i)
df["PriceinUK"] = df["PriceinUK"].apply(lambda i: int(i) if str(i) != "nan" else i)
df["Brand"] = df["Name"].apply(lambda i: i.split(" ")[0])

df["PriceinAUS"] = df["PriceinGermany"] * 1.6 
df["PriceinAUS"] = df["PriceinUK"] * 1.87

df.to_csv("clean_electricity_car.csv", index = False)