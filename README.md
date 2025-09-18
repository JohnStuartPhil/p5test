# Iowa House Prices

## Dataset Content 
The dataset is sourced from Kaggle(https://www.kaggle.com/datasets/codeinstitute/housing-prices-data). It is a fictitious user story where predictive analytics is applied in the project. Each row represents a house in Iowa, each column contains an attribute about each house. The data set includes information about:

- 1st/2nd floor
- Basement
- Garage
- Kitchen
- Lot
- Porch
- Years Built/Modified


| Column  | Variable | Meaning | Unit | Missing data? | 
| ----------- | ----------- | ----------- | ----------- | ----------- | 
|   A  | 1stFlrSF     |  First Floor in square feet   |   334 to 4,692     |  no  | 
|   B   |  2ndFlrSF    |  Second floor in square feet   |   0 to 2,065     |  yes  | 
|   C   |  BedroomAbvGr    | Bedrooms above grade (does NOT include basement bedrooms)    |   0 to 8     |  yes  | 
|    D  |  BsmtExposure    |  Refers to walkout or garden level walls   |  Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement| no  | 
|   E   |  BsmtFinSF1    |  Type 1 finished in square feet   |  0 to 5,644     |  no  | 
|    F  |  BsmtFinType1    | Rating of basement finished area    |  GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement |  yes  | 
|    G  |  BsmtUnfSF    |  Unfinished square feet of basement area   |  0 to 2,336      |  no  | 
|    H  |   EnclosedPorch   | Enclosed porch area in square feet    |  0 to 286      |  yes  | 
|    I  |  GarageArea    |  Size of garage in square feet   |  0 to 1,418      | no   | 
|     J |    GarageFinish  |  Interior finish of the garage   |  Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|  yes  | 
|     K |  GarageYrBlt    | Year garage was built    |     1900 to 2010   |  yes  | 
|     L |   GrLivArea   |  Above grade (ground) living area in square feet   | 334 to 5,642 | no   | 
|     M | KitchenQual     |  Kitchen quality   |   Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; [Po: Poor]     |  no  | 
|     N |LotArea      |  Lot size in square feet   |   1,300 to 215,245     |  no  | 
|    O  |Lot Frontage      |  Linear feet of street connected to property   |  21 to 313      |   yes | 
|    P  | MasVnrArea     | Masonry veneer area in square feet    | 0 to 1,600       | yes  | 
|    Q  | OpenPorchSF     |  Open porch area in square feet   |    0 to 547    |  no  | 
|    R  |  OverallCond    | Rates the overall condition of the house    |   [10: Very Excellent;] 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor |  no  | 
|    S  | OverallQual     | Rates the overall material and finish of the house    | 10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor  |  no  | 
|    T  | TotalBsmtSF     |  Total square feet of basement area   |   0 to 6,110     | yes  | 
|    U  |WoodDeckSF     |   Wood deck area in square feet  |  0 to 736      | yes  | 
|    V  | YearBuilt     |  Original construction date   |  1872 to 2010      |  no  | 
|    W  | YearRemodAdd     |  Remodel date (same as construction date if no remodeling or additions)   |    1950 to 2010    | no   | 
|    X  |  SalePrice    |   Sale Price   |   34,900 to 755,000     |no    | 

## Product Terms & Jargon 
TBC

## Business Requirements 
1.	The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
2.	The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa.

## Hypothesis and how to validate 
- It was found that the attributes <TBC> gave the higher sale prices.

## The rationale to map the business requirements to the Data Visualizations and ML task 
- **Business Requirement 1:** Data Visualization and Correlation study
	- We will inspect the data related to the customer base.
	- We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to the Sale Price.
	- We will plot the main variables against the Sale Price to visualise insights.

- **Business Requirement 2:** House Price Prediction
	- We want to predict the sale price of houses in Iowa based on the best factors on each house.


## ML Business Case 
1.	Business Requirement 1: Data Visualization and Correlation study
2.	Business Requirement 2: Prediction of House Sale Prices

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick project summary
- Quick project summary
	- Project Terms & Jargon
	- Describe Project Dataset
	- State Business Requirements

### Page 2: House Price Study
- Before the analysis, we knew we wanted this page to answer business requirement 1, but we couldn't know in advance which plots would need to be displayed.
- After data analysis, we agreed with stakeholders that the page will: 
	- State business requirement 1
	- Checkbox: data inspection on customer base (display the number of rows and columns in the data, and display the first ten rows of the data)
	- Display the most correlated variables to the sale prices and the conclusions
	- Checkbox: Individual plots showing the sale prices for each correlated variable

### Page 3: Sale Price Predictor
- State business requirement 2
- Set of widgets inputs, which relates to the predict profile. Each set of inputs is related to a given ML task to predict Sale Price.
- "Run predictive sale price" button that serves the predict data to our ML pipelines and predicts the sale price. 

### Page 4: Project Hypothesis and Validation
- Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:
- 1 - TBC.
- 2 - TBC.

### Page 5: ML Pipeline: Predict Sale Price
- Considerations and conclusions after the pipeline is trained
- Present ML pipeline steps
- Feature importance
- Pipeline performance


## References
Much of the code was taken from the Chrunometer walkthrough and amended accordingly

## Thank you
Mentor: Rohit Sharma
