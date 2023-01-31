# About The Project
This project makes use of an artificial intelligence for object detection. It is is programmed and initially tested with pollens. It implements the following: 
- accepts image input
- performs digital image processing
- detects pollens at the sample image
- classifies pollens into fertilized (dark-colored) and unfertilized (light-colored)
- counts the fertilized, unfertilized, and total number of pollens
- outputs an image with classification and count

![2](https://user-images.githubusercontent.com/70369183/215335690-3b5ad38d-7ca1-488e-8a8c-45374e164c47.png)

### Specifications
* reads image and resizes to 40% of its original size
* removes noise through Gaussian Blur
* applies pseudocoloring through Jet Colormap
* performs binary dilatiion then erosion
* masks fertilized pollens through binary cleaning and isolation techniques
* counts classified pollens

### Built With
* Python

# Getting Started
To get a local copy up and running, kindly follow these steps.

### Prerequisites
1. Python 3.x
2. PyQt5

### Installation

1. Install PyQt5
2. Clone the repo
```
git clone https://github.com/r-clarissa/ai-object-detector.git
```
4. Find and change your terminal path where the cloned folder on your local directory is found.
5. On your terminal, run the `App.py`.

# Special Note
This is a school project where functionalities are specified by the UPLB - ICS. To prohibit any undesired academic matters, the complete source code is located on another private repository. You may email me at cgrodriguez@up.edu.ph if you have any questions given that the purpose is validated.
