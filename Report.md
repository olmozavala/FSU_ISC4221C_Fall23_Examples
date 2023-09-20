# Lauren Sargent, LAS20D@fsu.edu

## Loops, conditionals, recursive functions (5 pts)
1) The proposed function is at file [answers_module.py](answers_module.py) and the function is called `myrec`.
This function takes an input, x. If the input is below 0, an exception is raised, if the input is 0 then a constant return value is set as 0. If the input i a non-zero positive number, the function performs a recursive function, f(x)=2x-f(x-1). 

```python
def myrec(x):
     if x== 0:
        return 0
    elif x > 0: 
        return 2*x-myrec(x-1)
    else:
        raise Exception("Negative number!")
```

## IO (5 pts)

2) The proposed function is at file [answers_module.py](answers_module.py) and the function is called `basic_io`.
The function takes a directory path as an input. If the input path does not exist, an error message is printed. If the path does exist, the function returns a dictionary which includes the number of files, the names of each file and directory in the directory, and a corresponding list denoting whether each object in the directory is a file or folder. 

```python
def basic_io(x):
     input_path = os.path.join(input_path)
    if not os.path.exists(input_path):
        print ("Folder does not exist")
    else:
        number_files=len(os.listdir(input_path))
        files = os.listdir(input_path)
        files=sorted(files)
        file_or_folder=[]
        for file in range (0, number_files):
            if os.path.isfile(os.path.join(input_path, files[file])):
                file_or_folder.append("file")
            elif os.path.isdir(os.path.join(input_path, files[file])):
                file_or_folder.append("folder")
        output = {'number_files': number_files,
                  'files': files,
                  'file_or_folder':file_or_folder,}
        print(output)
        return output
```

# Numpy (6 pts)
3) The proposed function is at file [answers_module.py](answers_module.py) and the function is called `add2and3`
   This function takes a matrix as input. If the matrix is smaller than 2 by 3, an error message is printed. Otherwise, the function calculates the sum ofthe second row and third column of the matrix.
   
``` python
def add2and3 (matrix):
    row, col = matrix.shape
    if row < 2 or col < 3:
        print("Matrix too small.")
    else:
        row_2 = matrix[1]
        col_3 = matrix[:, 2]
        print (row_2, col_3)
        row_sum=sum(row_2)
        col_sum=sum(col_3)
        total_sum=row_sum+col_sum
        return total_sum
```
4) The proposed function is at file [answers_module.py](answers_module.py) and the function is called `squareme`
   This function takes a matrix and a row number as inputs. If the matrix does not contain the row corresponding to the inputted row number, an error message is printed. Otherwise, the function returns the square of that row.
   
``` python
def squareme(matrix, row_number):
    row_number=row_number-1
    row, col = matrix.shape
    if row < row_number:
        print("Row not found.")
    else:
        row=matrix[row_number]
        print(row)
        row_squared=np.square((row))
        return row_squared
```
# Matplolib (5 pts)
5) I chose the box plot, bar plot, and annotated heat map examples. The box plot creates a box plot showing the distribution of a randomized data set. The bar plot shows 2 bars per object (named "name 1" and "name 2"), whose data is generated with the plot. The annotated heat map shows the distribution of randomized data with the annotation "Sopas perico lico" at the midway points of each axis (the center of the graph).
![box_plot](https://github.com/fsu-sc/python-overview-laslauren/assets/122302455/cf585009-b32b-4b4c-a105-667b243ea931)
![Bar_plot](https://github.com/fsu-sc/python-overview-laslauren/assets/122302455/2c8f83ed-edb2-4420-8711-50007f866795)
![Annotated_heat_map](https://github.com/fsu-sc/python-overview-laslauren/assets/122302455/ef5b32a3-3ac5-4b16-b437-dda6d625aeb5)

```python
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation
import numpy as np

#%% ------------ Box plot -----------
# https://matplotlib.org/3.1.1/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py
fig, ax = plt.subplots(figsize=(10,6))
plt.title('Basic Plot')
names = ['name1', 'name2']
data = [np.random.rand(50) * 100, np.random.rand(50) * 100]
bp = plt.boxplot(data, notch=True, labels= names, patch_artist=True)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xlabel("Sopas")
ax.set_ylabel("Pericon")

# fill with colors
colors = ['pink', 'lightblue']
for patch, color in zip(bp['boxes'], colors):
   patch.set_facecolor(color)

plt.show()

#%% ------------ bar plot-----------
fig, ax = plt.subplots(1,1,figsize=(10,10))
plt.title('BarPlot')
# Multibars are hard to do directly with matplotlib
names = ['name1', 'name2']
pos = np.arange(2)
ax.bar(pos, [2,2.1], color='r')
ax.set_xticks(pos, labels=names)
ax.bar(pos+ .2, [2.1,2.0])
ax.legend()
plt.show()

#%% ---- Heat maps / images
n = 100
x = np.linspace(0,np.pi,n)
y = np.sin(x)*2
X, Y = np.meshgrid(y, y)

#%% Annotated heatmap
fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.imshow(X+Y)
ax.text(n/2, n/2, "Sopas perico lico", color="red")
plt.show()

```

