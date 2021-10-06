import pandas as pd
df = pd.read_csv("Cheapestelectriccars-EVDatabase.csv")

df["Subtitle"] = df["Subtitle"].apply(lambda i: i.split("|       ")[1]).apply(lambda i: i.split(" kWh")[0])
df["Acceleration"] = df["Acceleration"].apply(lambda i: i.split(" sec")[0])
df["TopSpeed"] = df["TopSpeed"].apply(lambda i: i.split(" km/h")[0])
df["Range"] = df["Range"].apply(lambda i: i.split(" km")[0])
df["Efficiency"] = df["Efficiency"].apply(lambda i: i.split(" Wh/km")[0])
df["FastChargeSpeed"] = df["FastChargeSpeed"].apply(lambda i: i.split(" km/h")[0] if i != "-" else i)
df["PriceinGermany"] = df["PriceinGermany"].str.extract(r"(\d.*)")
df["PriceinGermany"] = df["PriceinGermany"].apply(lambda i: i.replace(",", "") if str(i) != "nan" else i)
df["PriceinGermany"] = df["PriceinGermany"].apply(lambda i: int(i) if str(i) != "nan" else i)
df["PriceinUK"] = df["PriceinUK"].str.extract(r"(\d.*)")
df["PriceinUK"] = df["PriceinUK"].apply(lambda i: i.replace(",", "") if str(i) != "nan" else i)
df["PriceinUK"] = df["PriceinUK"].apply(lambda i: int(i) if str(i) != "nan" else i)
df["Brand"] = df["Name"].apply(lambda i: i.split(" ")[0])

df["PriceinAUS"] = df["PriceinGermany"] * 1.6 
df["PriceinAUS"] = df["PriceinUK"] * 1.87

for column in ["Subtitle", "Acceleration", "TopSpeed", "Range", "Efficiency", "PriceinAUS"]:
    df[column] = df[column].agg(float)
df["FastChargeSpeed"] = df["FastChargeSpeed"].apply(lambda i: float(i) if i != "-" else 0)


df["Subtitle Metric"] = df["Subtitle"]/40

# Subtitle
def subtitle(val0, val1):
    if 163.34 <= val0 <= 200:
        val1 = 5
    elif 126.68 <= val0 < 163.34:
        val1 = 4
    elif 90.02 <= val0 < 126.68:
        val1 = 3
    elif 53.36 <= val0 < 90.02:
        val1 = 2
    elif 16.7 <= val0 < 53.36:
        val1 = 1
    return val1
df["Subtitle Metric"] = ""
df["Subtitle Metric"] = df[["Subtitle", "Subtitle Metric"]].apply(lambda i: subtitle(i[0], i[1]), axis = 1)

# Acceleration
def acceleration(val0, val1):
    if 2.1 <= val0 < 6.16:
        val1 = 5
    elif 6.16 <= val0 < 10.22:
        val1 = 4
    elif 10.22 <= val0 < 14.28:
        val1 = 3
    elif 14.28 <= val0 < 18.34:
        val1 = 2
    elif 18.34 <= val0 <= 22.4:
        val1 = 1
    return val1
df["Acceleration Metric"] = ""
df["Acceleration Metric"] = df[["Acceleration", "Acceleration Metric"]].apply(lambda i: acceleration(i[0], i[1]), axis = 1)

# Range
def range(val0, val1):
    if 795 <= val0 <= 970:
        val1 = 5
    elif 620 <= val0 < 795:
        val1 = 4
    elif 445 <= val0 < 620:
        val1 = 3
    elif 270 <= val0 < 445:
        val1 = 2
    elif 95 <= val0 < 270:
        val1 = 1
    return val1
df["Range Metric"] = ""
df["Range Metric"] = df[["Range", "Range Metric"]].apply(lambda i: range(i[0], i[1]), axis = 1)

# Topspeed
def topspeed(val0, val1):
    if 352.6 <= val0 <= 410:
        val1 = 5
    elif 295.2 <= val0 < 352.6:
        val1 = 4
    elif 237.8 <= val0 < 295.2:
        val1 = 3
    elif 180.4 <= val0 < 237.8:
        val1 = 2
    elif 123 <= val0 < 180.4:
        val1 = 1
    return val1
df["TopSpeed Metric"] = ""
df["TopSpeed Metric"] = df[["TopSpeed", "TopSpeed Metric"]].apply(lambda i: topspeed(i[0], i[1]), axis = 1)

# Efficiency
def efficiency(val0, val1):
    if 104 <= val0 < 139.4:
        val1 = 5
    elif 139.4 <= val0 < 174.8:
        val1 = 4
    elif 174.8 <= val0 < 210.2:
        val1 = 3
    elif 210.2 <= val0 < 245.6:
        val1 = 2
    elif 245.6 <= val0 <= 281:
        val1 = 1
    return val1
df["Efficiency Metric"] = ""
df["Efficiency Metric"] = df[["Efficiency", "Efficiency Metric"]].apply(lambda i: efficiency(i[0], i[1]), axis = 1)

# FastChargeSpeed
def fastspeed(val0, val1):
    if 1128 <= val0 <= 1410:
        val1 = 5
    elif 846 <= val0 < 1128:
        val1 = 4
    elif 564 <= val0 < 846:
        val1 = 3
    elif 282 <= val0 < 564:
        val1 = 2
    elif 0 <= val0 < 282:
        val1 = 1
    return val1
df["FastChargeSpeed Metric"] = ""
df["FastChargeSpeed Metric"] = df[["FastChargeSpeed", "FastChargeSpeed Metric"]].apply(lambda i: fastspeed(i[0], i[1]), axis = 1)

# Price
def price(val0, val1):
    if 35904 <= val0 < 99409.2:
        val1 = 5
    elif 99409.2 <= val0 < 162914.4:
        val1 = 4
    elif 162914.4 <= val0 < 226419.6:
        val1 = 3
    elif 226419.6 <= val0 < 289924.8:
        val1 = 2
    elif 289924.8 <= val0 <= 353430:
        val1 = 1
    return val1
df["PriceinAUS Metric"] = ""
df["PriceinAUS Metric"] = df[["PriceinAUS", "PriceinAUS Metric"]].apply(lambda i: price(i[0], i[1]), axis = 1)

df.to_csv("clean_electricity_car.csv", index = False)