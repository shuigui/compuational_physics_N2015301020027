# 第六次作业  
2015301020027 &emsp; &emsp;曾伟豪
## 题目
**3.11** For the three values of ![](http://latex.codecogs.com/gif.latex?F_D) shown in Figure 3.6, compute and plot the total energry of 
the system as a function of the time and discuss the results.
## 题目要求  
根据书上图3.6的参数计算并画出谐振子能量随时间变化的关系
## 解题思路
图3.6描述的是考虑强迫力与阻尼的一维谐振子，根据euler_cromer解法，其满足方程：
![](http://latex.codecogs.com/gif.latex?\omega_{i+1}=\omega_i-[(g/l)sin\theta_i-q\omega_i+F_Dsin(\Omega_Dt_i)]{\Delta}t)  
![](http://latex.codecogs.com/gif.latex?\theta_{i+1}=\theta_i+\omega_{i+1}{\Delta}t)  
使用python程序计算得到关于角速度与角度的数组即可计算总能量，代入公式：  
![](http://latex.codecogs.com/gif.latex?E_i=\frac{1}{2}ml^2\omega_i^2+mgl(1-cos\theta_i))  
得到数组E即可作出能量随时间变化的图像
## 程序设计
* 根据图3.6给定初始条件 确定步长dt=0.04
* 用上述公式进行计算，并使θ的值保持在-π到π之间。
* 带入不同的驱动力进行计算，作出能量随时间变化的图像  
[代码链接](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/Exercise_06.py) 
## 相关图像及分析  
* 首先检验程序的运行结果，将figure3.6的参数代入进行计算。得到几个不同驱动力下角度随时间变化的图像：   
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/exercise06%CE%B8t.png)  
可见驱动力为0与0.5时，结果都遵循较好的规律，而FD=1.2时曲线变化无常，这与书上的结果一致。  
在相空间中作出图像如下：  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/6%CE%A9-%CE%B8.png)  
显然FD=1.2的解是混沌的。  
其能量随时间变化的关系:  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/6E-t.png) 
从中可见没有外力时，受到阻力的影响能量逐渐衰减为0。
FD=0.5时。简谐摆先在自身的震动与阻力周期性外力的共同影响下振动，能量是这三个效应的叠加。随后自身振动的效应逐渐消失。能量等于外界周期性输入的能量减去摩擦
造成的损耗。其结果有规律可循。  
FD=1.2时，系统变得不稳定，能量随时间变化的关系变得复杂。存在一大约为200J的极大值。是个混沌的解。稍微改变一下θ的初始值，得到如下的效果：  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/06change%CE%B8.png)  
可见稍微改变初始条件时，前期两曲线比较相近，随时间演化足够长的时间后，两个系统的解开始分离，相差较大，但能量的最大值没有改变。  
## 结论  
非线性的谐振子能量随时间变化的解是混沌的，对初始条件有极强的依赖性，但仍可求出能量的极大值，也可观察短时间内曲线的走势.

