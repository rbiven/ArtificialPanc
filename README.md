# ArtificialPanc
This is my Capstone project performed for the Machine Learning nanodegree at Udacity.

### Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included. Make sure that you select the Python 2.7 installer and not the Python 3.x installer. 

### Code

This is my code for my Udacity Capstone Project.  The attached text files are my personal data that are used as the dataset for a supervised learning algorithm.  The other python codes are used inside the IPython Notebook and do not need adjusting at this time.

### Run

Run the Jupyter Notebook software and project file in your browser.  The file name is `CapstoneDiabetes1.ipynb`.

## Data

The diabetes data is included as a selection of 576 data points collected on my (Richard Biven) personal devices (Dexcom CGM, Omnipod Pump, and my journey for carb entries. 

**Features**
1) `Bolus Taken`: amount of units of insulin taken at a specific moment in the day (units of insulin) (Continuous); 
2) `Basal Insulin`: amount of units of insulin delivered continuous throughout the day (units of insulin) (Continuous); 
3) `Basal Carbs (Liver)`: amount of carbs body produces continuously throughout the day (grams) (Continuous); 
4) `Carbs Eaten`:  amount of carbs taken at a specific moment in the day (grams) (Continuous);

*Dependent Features:*
* `Bolus Ingested`: Use `Bolus Taken` to calculate how the body actually ingests the insulin over a period of time (Continuous)
* `Carbs Ingested`: Use `Carbs Eaten` to calculate how the body actually ingests the carbs over a period of time (Continuous)
* `Blood GLucose (BG)`: Using the features above to calculate the BG at all times in the day.

# From Rbiven
The above is the documentation for my Capstone project in the Udacity Machine Learning nanodegree.  I am putting my results on Github for peer review.  If you are interesting in my work or have questions about my methods, please let me know. If you are interesting in learning more about machine learning, I highly recommend the Udacity Nanodegree course.