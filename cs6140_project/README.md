# NFL_Gambling_Models

This is the final project for CS6140 - Machine Learning at Northeastern University. Created by John O'Connell

## Data Set

The data used for this project can be found at:
https://drive.google.com/drive/u/0/folders/1jXk3LYG6L0_vaFYT0cq4tnqs8ulTSeVS

## Dependencies 

The execution of the code in this project requires the following Python packages: 
numpy, pandas, scikit-learn, pytorch, and matplotlib

## Run Instructions

In order to run the code, the data must be downloaded from the link provided above. Once the zip file of the data is downloaded, unzip the folder and make sure that is saved in the same directory as the code files. The name of the unzipped folder should be 'stats'. If this is not the case, rename the folder to 'stats'. The code is expecting to access the data in a folder named 'stats', and will not run correctly if this folder does not exist. Additionally, make sure the 'results' folder exists in the directory where the code files are saved. This is where the results of the models will be saved. Once again, the code will not run correctly if this folder does not exist. Once the code files, 'stats' folder, and 'results' folder are in the same directory the code is ready to be run. Open and run any of the code files with Jupyter Notebook or any other application that can handle .ipynb files. Each of the code files is the execution of a different type of model used in the project. There are four code files total, one for the standard linear regression, one for Huber regression, one for Ridge regression with Basis Function Expansion, and finally one for Feed Forward Neural Networks.