
# 第五次作业  
2015301020027 &emsp; &emsp;曾伟豪
## 题目
**2.19** Model the effect of backspin on a batted ball. Assume an angular velocity of 2000 rpm.
## 关于球运动的微分方程  
![](http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_x)  
![](http://latex.codecogs.com/gif.latex?\frac{dv_x}{dt}=\frac{-B_2}{m}vv_x)  
![](http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_y)  
![](http://latex.codecogs.com/gif.latex?\frac{dv_y}{dt}=-g)  
![](http://latex.codecogs.com/gif.latex?\frac{dz}{dt}=v_z)  
![](http://latex.codecogs.com/gif.latex?\frac{dv_z}{dt}=\frac{-S_0v_xw}{m})  
用欧拉法解方程得：  
![](http://latex.codecogs.com/gif.latex?x_{i+1}=x_i+v_{x,i}dt)  
![](http://latex.codecogs.com/gif.latex?v_{x,i+1}=\frac{-B_2}{m}vv_xdt+v_{x,i})  
![](http://latex.codecogs.com/gif.latex?y_{i+1}=y_i+v_{y,i}dt)  
![](http://latex.codecogs.com/gif.latex?v_{y,i+1}=v_{y,i}-gdt)  
![](http://latex.codecogs.com/gif.latex?v_{z,i+1}=\frac{-S_0v_xw}{m}dt+v_{z,i})  
![](http://latex.codecogs.com/gif.latex?z_{i+1}=z_i+v_{z,i}dt)  
## 程序设计及链接
* 定义所需变量:坐标，速度， dt。
* 给定初始条件坐标x,y,z;速度v;击出角度θ。
* 根据如上几个关系式构建函数。
* 将变量不断带入函数中计算并添加到数组中
* 根据结果作图   
[程序链接](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/Exercise_05.py)   
运行结果图  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/exercise5.PNG)  
## 结论
考虑球的旋转后，z方向会有些偏离。






