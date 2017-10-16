# 第四次作业  
2015301020027 &emsp; &emsp;曾伟豪
## 题目
**2.6**  Use the Euler method to caculate cannon shell rajectories ignoring both air drag and the effect of air density. 
Compare your results with those in Figure 2.4, and with the exact solution.
## 分析
**1.题目要求**  
用欧拉解法解两个关于坐标的二阶常微分方程，作出图像  
**2.方程解法**  
忽略空气阻力时，x和y分别满足方程:  
![](http://latex.codecogs.com/gif.latex?\frac{d^2x}{dt^2}=0)&emsp; &emsp;![](http://latex.codecogs.com/gif.latex?\frac{d^2y}{dt^2}=-g) ,  
引入变量vx,vy 降阶为一阶方程，得到：  
![](http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_x)  
![](http://latex.codecogs.com/gif.latex?\frac{dv_x}{dt}=0)  
![](http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_y)  
![](http://latex.codecogs.com/gif.latex?\frac{dv_y}{dt}=-g)  
用欧拉法解上述几个方程,得：  
![](http://latex.codecogs.com/gif.latex?x_{i+1}=x_i+v_{x,i}dt)  
![](http://latex.codecogs.com/gif.latex?v_{x,i+1}=v_{x,i})  
![](http://latex.codecogs.com/gif.latex?y_{i+1}=y_i+v_{y,i}dt)  
![](http://latex.codecogs.com/gif.latex?v_{y,i+1}=v_{y,i}-gdt)  
使用python设计程序计算即可作图。  
## 程序设计及链接
* 定义所需变量:坐标，速度， dt。
* 给定初始条件坐标x,y;速度v;炮弹出射角度θ。
* 根据如上几个关系式构建函数。
* 将变量不断带入函数中计算并添加到数组中
* 根据结果作图  
[程序链接点我](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/Exercise_04.py)  
## 结果图像
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/exercise04.PNG)  
## 结论
运行结果与书上的图一致，在出射角度为45度时，炮弹射程最远。
















