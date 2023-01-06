import matplotlib.pyplot as plt
x = [300, 450, 150, 400, 650]
y = [400, 500, 350, 300, 500]
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle="dotted", color="cyan", marker="h", markerfacecolor="magenta", markersize="8")
plt.xlabel("Days of week")
plt.ylabel("Sales of Drinks")
plt.title("Sales Data 1", loc="right")
plt.subplot(2, 1, 2)
plt.plot(x, y, linestyle="dashed", color="yellow", marker="d", markerfacecolor="green", markersize="8")
plt.xlabel("Days of Week")
plt.ylabel("Sales of Food")
plt.title("Sales Data 2")
plt.show()
