"""Publication figure generation utilities."""

def save_figure(fig, path):
    fig.savefig(path, dpi=300, bbox_inches="tight")
