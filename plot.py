from matplotlib import pyplot as plt
import seaborn as sns


def draw_bar(path: str, categories: dict) -> None:
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(figsize=(6, 4), dpi=120)
    sns.barplot(x=list(categories.keys()),
                y=list(categories.values()), axes=axes, color='blue', linewidth=3, edgecolor='black')
    axes.set_xticklabels(categories.keys(), size=10)
    axes.set_yticklabels(labels=axes.get_yticklabels(), size=10)
    axes.set_ylabel('number of proteins', size=12)
    axes.set_title('Categories', size=14)
    plt.plot()
    plt.savefig(f"{path}/bar.png", dpi=150)
