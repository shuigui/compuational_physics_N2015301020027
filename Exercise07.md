# 第七次作业  
2015301020027 &emsp; &emsp;曾伟豪
## 题目
**3.20** Calculate the bifuraction diagram for the pendulum in the vicinity of ![](http://latex.codecogs.com/gif.latex?F_D)=1.35 to 1.5.
Make a magnified plot of the diagram(as compared to Figure 3.11) and obtain an estimate of the Feigenbaum δ parameter.
##　要求
画出ＦＤ从１．３５－１．５的分叉图，并进行放大比较，估算δ的值。
## 解法
此题解法与上次作业大致相同，只需加入筛选条件选出300周期后符合条件的θ值即可。  
直接贴上[代码链接](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/Exercise_07.py)  
## 结果图像与相关分析  
取积分步长dt=0.04,得到如下结果图：  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/7.png)  
可以观察到周期倍增现象最终通向混沌。  
对图像进行局部放大得到如下几个图：  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/7_1.png)  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/7-2.png)  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/7-3.png)  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/7-3.png)  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/7-4.png)  
通过以上几个局部放大图，可得F1=1.42 F2=1.45 F3=1.47  
δ2=1.5......与4.6相差较大
## 最后感谢
刘庆康同学的代码指导

