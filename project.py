import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("daily.csv")
df["tarikh"] = pd.to_datetime(df["tarikh"])
df["mahina"] = df["tarikh"].dt.month

mahina_total = df.groupby("mahina")["rakam"].sum()
category_total = df.groupby("category")["rakam"].sum()

print("Kul kharcha:", df["rakam"].sum())
print("Sabse bada kharcha:", df["rakam"].max())
print(mahina_total)
print(category_total)

category_total.plot(kind="bar")
plt.title("Category ke hisaab se kharcha")
plt.savefig("project_chart.png")

report = df.groupby(["mahina", "category"])["rakam"].sum().reset_index()
report.to_csv("project_report.csv", index=False)
print("Chart aur report ban gaye")
