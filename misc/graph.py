import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')
# plt.plot(df['X'])
# plt.title('X-axis')
# plt.show()

# plt.plot(df['Y'])
# plt.title('Y-axis')
# plt.show()

plt.plot(df['Z'])
plt.title('Z-axis')
plt.show()
# fig, axs = plt.subplots(3)
# fig.suptitle('Vertically stacked subplots')
# axs[0].plot(df['X'])
# axs[1].plot(df['Y'])
# axs[2].plot(df['Z'])

# sea = sns.FacetGrid(df, col = "axis", hue = "kind")
# sea.map(sns.scatterplot, "time", "value", alpha = .8)
# sea.add_legend()
# sns.lineplot(data=df, x="X", y="value")