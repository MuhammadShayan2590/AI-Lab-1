"""
Barnsley Fern Generator
========================

Generates the classic Barnsley fern fractal using an Iterated Function
System (IFS). The fern shape emerges from repeatedly applying one of
four affine transformations to a point, chosen at random according to
fixed probabilities. Each transformation corresponds to a structural
part of the fern:

    f1 - the stem                (probability 1%)
    f2 - successively smaller    (probability 85%)
         leaflets (self-similar
         copies of the whole fern)
    f3 - the largest left leaflet (probability 7%)
    f4 - the largest right leaflet (probability 7%)

Author: Claude
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def generate_barnsley_fern(n_points: int = 200_000, seed: int | None = 42):
    """
    Generate points on a Barnsley fern using the standard IFS.

    Parameters
    ----------
    n_points : int
        Number of points to generate (higher = denser, more detailed fern).
    seed : int or None
        Random seed for reproducibility.

    Returns
    -------
    x, y : np.ndarray
        Arrays of point coordinates.
    rule_used : np.ndarray
        Which transformation (0-3) generated each point, useful for coloring
        different structural parts of the fern differently.
    """
    rng = np.random.default_rng(seed)

    # Pre-allocate arrays for speed
    x = np.empty(n_points)
    y = np.empty(n_points)
    rule_used = np.empty(n_points, dtype=np.int8)

    # Starting point
    x[0], y[0] = 0.0, 0.0
    rule_used[0] = 1

    # Draw all random choices up front (fast, vectorized)
    # Probabilities: f1=1%, f2=85%, f3=7%, f4=7%
    choices = rng.random(n_points)

    for i in range(1, n_points):
        px, py = x[i - 1], y[i - 1]
        r = choices[i]

        if r < 0.01:
            # f1: the stem -> maps everything to a thin line at the base
            nx = 0.0
            ny = 0.16 * py
            rule = 0
        elif r < 0.86:
            # f2: successively smaller leaflets (85% probability)
            # this is the transformation that builds most of the fern's body
            nx = 0.85 * px + 0.04 * py
            ny = -0.04 * px + 0.85 * py + 1.6
            rule = 1
        elif r < 0.93:
            # f3: largest left-hand leaflet
            nx = 0.20 * px - 0.26 * py
            ny = 0.23 * px + 0.22 * py + 1.6
            rule = 2
        else:
            # f4: largest right-hand leaflet
            nx = -0.15 * px + 0.28 * py
            ny = 0.26 * px + 0.24 * py + 0.44
            rule = 3

        x[i] = nx
        y[i] = ny
        rule_used[i] = rule

    return x, y, rule_used


def plot_fern(x, y, rule_used, output_path="barnsley_fern.png",
              discard=50, dpi=200, background="#05140c"):
    """
    Render the fern with color, shading points by which IFS rule produced
    them (a natural way to highlight the fern's structural parts) and by
    height, so the fern reads as green with darker/lighter natural shading.

    Parameters
    ----------
    x, y : np.ndarray
        Point coordinates from generate_barnsley_fern.
    rule_used : np.ndarray
        Which transformation produced each point.
    output_path : str
        Where to save the rendered PNG.
    discard : int
        Number of initial "settling in" points to discard (transient points
        before the chaos game converges onto the attractor).
    dpi : int
        Resolution of the saved image.
    background : str
        Hex color for the plot background.
    """
    x, y, rule_used = x[discard:], y[discard:], rule_used[discard:]

    # Build a natural green colour gradient based on height (y) so the
    # fern looks lit from above, with the stem/leaflets in distinguishable
    # shades of green.
    norm_height = (y - y.min()) / (y.max() - y.min())

    # Custom green colormap: dark shadow green -> vivid leaf green -> pale tip
    fern_cmap = mcolors.LinearSegmentedColormap.from_list(
        "fern_green",
        ["#0b3d1c", "#1f7a34", "#4caf50", "#9ccc65", "#d4f7a6"]
    )

    fig, ax = plt.subplots(figsize=(10, 12), facecolor=background)
    ax.set_facecolor(background)

    scatter = ax.scatter(
        x, y,
        s=0.15,
        c=norm_height,
        cmap=fern_cmap,
        marker=".",
        linewidths=0,
        alpha=0.85,
    )

    ax.set_xlim(x.min() - 1, x.max() + 1)
    ax.set_ylim(y.min() - 1, y.max() + 1)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.set_title(
        "Barnsley Fern — Iterated Function System",
        color="#e8f5e9",
        fontsize=16,
        pad=15,
        fontweight="bold",
    )

    fig.tight_layout()
    fig.savefig(output_path, dpi=dpi, facecolor=background, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved fern image to: {output_path}")


if __name__ == "__main__":
    NUM_POINTS = 200_000

    print(f"Generating Barnsley fern with {NUM_POINTS:,} points...")
    xs, ys, rules = generate_barnsley_fern(n_points=NUM_POINTS, seed=42)

    print("Rendering and saving image...")
    plot_fern(xs, ys, rules, output_path="/mnt/user-data/outputs/barnsley_fern.png")

    print("Done!")
