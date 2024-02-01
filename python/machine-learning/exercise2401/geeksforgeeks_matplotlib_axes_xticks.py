#!/usr/bin/env python3

"""https://www.geeksforgeeks.org/matplotlib-axes-axes-set_xticks-in-python/"""

def example1() -> None:
    """illustrate the matplotlib.axes.Axes.set_xticks() function in matplotlib.axes"""

    # Implementation of matplotlib function
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon

    def func(x):
        return (x - 4) * (x - 6) * (x - 5) + 100

    a, b = 2, 9 # integral limits
    x = np.linspace(0, 10)
    y = func(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, "k", linewidth = 2)
    ax.set_ylim(bottom=0)

    # Make the shaded region
    ix = np.linspace(a, b)
    iy = func(ix)
    verts = [(a, 0), *zip(ix, iy), (b, 0)]
    poly = Polygon(verts, facecolor='green', edgecolor='0.5', alpha=0.4)
    ax.add_patch(poly)

    ax.text(0.5 * (a + b), 30,
        r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment='center', fontsize=20
    )

    fig.text(0.9, 0.05, '$x$')
    fig.text(0.1, 0.9, '$y$')

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticks((a, b))

    fig.suptitle('matplot.axes.Axes.set_xticks()\
        function Example\n\n', fontweight="bold")
    fig.canvas.draw()
    plt.show()

def example2() -> None:
    # Implemention of matplotlib function
    import numpy as np
    import matplotlib.pyplot as plt

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    y2 = y + 0.2 * np.random.normal(size = x.shape)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(x, y2)

    ax.set_xticks([0, np.pi, 2 * np.pi])

    ax.spines['left'].set_bounds(-1, 1)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    fig.suptitle('matplotlib.axes.Axes.set_xticks() \
    function Example\n\n', fontweight="bold")
    fig.canvas.draw()
    plt.show()



if __name__ == "__main__":
    #example1()
    example2()
