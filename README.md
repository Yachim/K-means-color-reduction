# K-means Color Reduction
Python project using the [k-means algorithm](https://en.wikipedia.org/wiki/K-means_clustering) to reduce colors in an image. The user inputs the image name located in the `source_images` folder and colors. The program then reduces the colors to the colors selected by the user.

## Algorithm
### Input Data
The initial values for centroids are the colors inputted by the user. The points are set of colors gathered from the image.

### The Conversion Process
The program supports two metrics for measuring distance - Euclidean and Taxicab. This is used when calculating the closest centroid from given point.

## Running the Program
When running the `main` function, the program will ask for the filename along with colors in the hex format. 
After providing inputs it will start two different conversion each with different metrics.

## Output
The `main` function will create a folder with the name of the image (without extension) with 3 files in it: 
 - converted_euc_[image_name].[image_format]
 - converted_tax_[image_name].[image_format]
 - details.txt

Image with prefix `converted_euc_` is the converted result using the Euclidean metric. The other image is the converted result using the Taxicab metric. 
The file `details.txt` contains information about the conversion - the name of the image, colors used and number of iterations and time elapsed.

## Results
All images are from Unsplash and have a high resolution.

### First Image
Colors used:

- 12, 61, 1 ![#0c3d01](https://via.placeholder.com/15/0c3d01/0c3d01.png) 
- 61, 46, 1 ![#3d2e01](https://via.placeholder.com/20/3d2e01/3d2e01.png)
- 0, 0, 0 ![#000000](https://via.placeholder.com/20/000000/000000.png)
- 207, 194, 163 ![#cfc2a3](https://via.placeholder.com/20/cfc2a3/cfc2a3.png)
- 166, 118, 60 ![#a6763c](https://via.placeholder.com/20/a6763c/a6763c.png)

![First image](source_images/image1.jpg)
<p align="center">Photo by <a href="https://unsplash.com/@presetbase?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Presetbase Lightroom Presets</a> on <a href="https://unsplash.com/t/animals?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></p>

<p align="middle">
  <img div align="top" alt="Fist conversion euclidean" src="converted_images/image1/converted_euc_image1.jpg" width="49%">
  <img div align="top" alt="Fist conversion taxicab" src="converted_images/image1/converted_tax_image1.jpg" width="49%">
</p>
<p align="center">Euclidean (left) and Taxicab (right) metric</p>

There can be seen some very small differences between conversion.

#### Number of Iterations
Euclidean: 33

Taxicab: 35

#### Time Elapsed
Euclidean: 30 seconds

Taxicab: 42 seconds

### Second Image
Colors used:

- 105, 85, 60 ![#69553c](https://via.placeholder.com/15/69553c/69553c.png) 
- 17, 116, 191 ![#1174bf](https://via.placeholder.com/20/1174bf/1174bf.png)
- 6, 81, 138 ![#06518a](https://via.placeholder.com/20/06518a/06518a.png)
- 100, 162, 209 ![#64a2d1](https://via.placeholder.com/20/64a2d1/64a2d1.png)
- 18, 79, 2 ![#124f02](https://via.placeholder.com/20/124f02/124f02.png)

![Second image](source_images/image2.jpg)
<p align="center">Photo by <a href="https://unsplash.com/es/@glennsouer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Glenn Souer</a> on <a href="https://unsplash.com/t/travel?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></p>

<p align="middle">
  <img div align="top" alt="Fist conversion euclidean" src="converted_images/image2/converted_euc_image2.jpg" width="49%">
  <img div align="top" alt="Fist conversion taxicab" src="converted_images/image2/converted_tax_image2.jpg" width="49%">
</p>
<p align="center">Euclidean (left) and Taxicab (right) metric</p>

There are visible differences between the metrics.

#### Number of Iiterations
Euclidean: 20

Taxicab: 23

#### Time Elapsed
Euclidean: 22 seconds

Taxicab: 32 seconds

### Third Image
Colors used:

- 153, 224, 242 ![#99e0f2](https://via.placeholder.com/15/99e0f2/99e0f2.png) 
- 109, 175, 191 ![#6dafbf](https://via.placeholder.com/20/6dafbf/6dafbf.png)
- 18, 135, 163 ![#1287a3](https://via.placeholder.com/20/1287a3/1287a3.png)
- 202, 216, 219 ![#cad8db](https://via.placeholder.com/20/cad8db/cad8db.png)
- 242, 244, 245 ![#f2f4f5](https://via.placeholder.com/20/f2f4f5/f2f4f5.png)
- 156, 160, 161 ![#9ca0a1](https://via.placeholder.com/20/9ca0a1/9ca0a1.png)

![Third image](source_images/image3.jpg)
<p align="center">Photo by <a href="https://unsplash.com/@tuninglever?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alfred Leung</a> on <a href="https://unsplash.com/t/animals?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></p>

<p align="middle">
  <img div align="top" alt="Fist conversion euclidean" src="converted_images/image3/converted_euc_image3.jpg" width="49%">
  <img div align="top" alt="Fist conversion taxicab" src="converted_images/image3/converted_tax_image3.jpg" width="49%">
</p>
<p align="center">Euclidean (left) and Taxicab (right) metric</p>

There are also visible differences between the metrics.

#### Number of Iterations
Euclidean: 53

Taxicab: 69

#### Time Elapsed
Euclidean: 42 seconds

Taxicab: 70 seconds

## Conclusion
While working on this project I learned about the k-means algorithm. I observed the differences the metric selection made and the time it took to complete. 
