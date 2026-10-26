import pandas as pd
import matplotlib.pyplot as plt

# 1. Read data
df = pd.read_csv("train.csv", encoding="latin-1")

# 2. Clean
df = df.drop_duplicates()
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Year"] = df["Order Date"].dt.year

# 3. Analyze
by_category = df.groupby("Category")["Sales"].sum().sort_values()
by_region = df.groupby("Region")["Sales"].sum().sort_values()
by_year = df.groupby("Year")["Sales"].sum()
top_sub = df.groupby("Sub-Category")["Sales"].sum().nlargest(10).sort_values()

print("Top category:", by_category.idxmax())
print("Top region:", by_region.idxmax())
print("Best year:", by_year.idxmax())
print("Top sub-category:", top_sub.idxmax())

# 4. Charts
by_category.plot(kind="barh", title="Sales by Category")
plt.tight_layout(); plt.savefig("sales_by_category.png"); plt.close()

by_region.plot(kind="barh", title="Sales by Region")
plt.tight_layout(); plt.savefig("sales_by_region.png"); plt.close()

by_year.plot(kind="line", marker="o", title="Sales by Year")
plt.tight_layout(); plt.savefig("sales_by_year.png"); plt.close()

top_sub.plot(kind="barh", title="Top 10 Sub-Categories")
plt.tight_layout(); plt.savefig("top_subcategories.png"); plt.close()

print("Done!")