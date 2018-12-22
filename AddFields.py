import pandas
df = pandas.read_csv('hotels_data.csv')
df.head()
df["Snapshot Date"] = pandas.to_datetime(df["Snapshot Date"])
df["Checkin Date"] = pandas.to_datetime(df["Checkin Date"])
df["DayDiff"] = df["Checkin Date"] - df["Snapshot Date"]
df["WeekDay"] = df["Checkin Date"].dt.day_name()
df["DiscountDiff"] = df["Original Price"] - df["Discount Price"]
df["DiscountPerc"] = (df["DiscountDiff"] / df["Original Price"]) * 100
df.head()
df.to_csv("Hotels_data_Changed.csv")
