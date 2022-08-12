import numpy as np
import matplotlib.pyplot as plt

def main():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Compute areas and colors
    N = 150
    r = 2 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    area = 200 * r**2
    colors = theta

    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)



    plt.savefig("/home/student/mycode/graphing/2018summary.png")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/2018summary.png")


if __name__ == "__main__":
    main()
