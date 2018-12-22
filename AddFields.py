import pandas
df = pandas.read_csv('hotels_data.csv')
df.head()
df["DayDiff"] = (pandas.to_datetime(df["Checkin Date"]) - pandas.to_datetime(df["Snapshot Date"])).dt.days
df["WeekDay"] = (pandas.to_datetime(df["Checkin Date"])).dt.day_name()
df["DiscountDiff"] = df["Original Price"] - df["Discount Price"]
df["DiscountPerc"] = (df["DiscountDiff"] / df["Original Price"]) * 100
df.head()
df.to_csv("Hotels_data_Changed.csv")
