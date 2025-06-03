#bjh 3d 玫瑰
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
# 创建Figure窗口及Axes坐标轴区域
fig = plt.figure()
ax = plt.axes(projection='3d')
# 构造函数曲面
x = np.linspace(0, 1, 200)
theta = np.linspace(-2*np.pi,15*np.pi,300)
[x, theta] = np.meshgrid(x, theta)
phi = (np.pi/2)*np.exp(-theta/8/np.pi)
X = 1-.5*pow(1.25*pow(1-np.mod(3.6*theta,2*np.pi)/np.pi,2)-1/4,2)
y = 1.95653*pow(x,2)*pow(1.27689*x-1,2)*np.sin(phi)
r = X*(x*np.sin(phi)+y*np.cos(phi))
h = X*(x*np.cos(phi)-y*np.sin(phi))
# 设置颜色并绘制曲面
c = cm.get_cmap('magma')
surf = ax.plot_surface(r * np.cos(theta), r * np.sin(theta), h, rstride=1, cstride=1,cmap=c, linewidth=0, antialiased=True)
# 减少空白区域并紧凑布局
ax.set_position([0, 0, 1, 1])
plt.show()
