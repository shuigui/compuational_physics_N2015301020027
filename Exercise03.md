# 第三次作业
                                
## 题目

The velocity of a freely falling object near Earth's surface is described by the equation 
  
![](http://latex.codecogs.com/gif.latex?\frac{dv}{dt}=-g)

where v is the velocity and  ![](http://latex.codecogs.com/gif.latex?g=9.8m/s^2) is the acceleration due to gravity.Write a program that employs the Euler method to compute the solution to (1.8); that is, calculate v as a funtion of t. For simplicity,assume that the initial velocity is zero-that is, the object starts from rest-and calculate the solution for times t = 0 to t = 10s.repeat the calculation for several different values of time step, and compare the results with the exact solution to (1.8). It turns out that for this case the Euler  method gives the exact result.Verify this with your numerical results and prove it analytically.

## 算法设计

* 定义变量数组v与t并给定初始值为0
* 给定一个dt
* 用欧拉方法计算在此dt下数组v中的每个值与t对应
* 做出几个不同dt下的t-v图像

## 程序链接与运行结果
1. 取dt=3的运行结果
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/timestep3.0.PNG)
2. 取dt=0.5的运行结果
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/timestep0.5.PNG)
3. 取dt=0.2的运行结果
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/time%20step0.2.PNG)

[程序链接](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/Exercise_03.py)

## 结论

用欧拉方法作出了t=0到t=10的图像，并取了几个不同的dt与常微分方程的精确解作了对照，得出结论当导函数为常数时，欧拉解法总能给出常微分方程的精确解。
