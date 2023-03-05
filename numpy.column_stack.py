#合并多个一维数组成为多维数组，按列排序
#The merger of multiple one -dimensional number is composed of multiple dimensions, and sorted by columns.
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2,3,200)
y = (-0.1)*(0.25*x**4-x**3/3-3*x**2)+0.8
z = np.zeros(200)
#plt.plot(x,y)
#plt.show()
result = np.column_stack((x,y,z)) #可以使用多个一维数组来进行合并，合并后为列。（如果需要为行，可以使用T进行数组转置）
with open('1.txt','w') as f:  #写入模式打开文件
    f.write(str(200)+'\n')  #在第一行写入数字200，然后换行到第二行
    np.savetxt(f,result)  #使用numpy的savetxt()把合并后的数组写入文件中，第二行开始

