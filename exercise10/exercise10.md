
# 第十次作业  
2015301020027 &emsp; &emsp;曾伟豪

## 题目
本次解决5.1题，利用拉普拉斯方程模拟带电平板的电场、电势。

## 解法思想

二维情形下，将空间分成小块，无电荷存在时，电势满足的拉普拉斯方程可简化为    
V(i,j)=[V(i+1,j,k)+V(i-1,j,k)+V(i,j+1,k)+V(i,j-1,k)]/4   
用迭代法即可解此方程。  
代码链接：  
[代码](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/exercise10/exercise10.py) 

## 结果图像
等势线：  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/exercise10/等势线.png)  
电场线：  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/exercise10/电场线.png)   
电势的三围图迭代演化：  
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/exercise10/3d0.png)   
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/exercise10/3d2.png)   
![](https://github.com/shuigui/compuational_physics_N2015301020027/blob/master/exercise10/三维图.png)  

## 结论
Jacobi方法对于解拥有简单结构边界条件的模型简单有效。





