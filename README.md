
# REB ( Recession Eye Ball )

## Background
Back in 2007-2008 due to Housing market and anemic Unemployment was a major disaster and stock market collapsed , Fannie mae and Freddie Mac Federal Agencies mortgage securities meltdown, this contributed to a general credit crisis, which evolved into a worldwide financial crisis.

Based on the different KPI's(Key performance indicators) trying to predict the next recession, how it will impact on various sectors and what sectors are going to blame, how big it is impacting the whole world , How for the next recession, is it hiding somewhere near 2019? 
Let’s our Recession Eye Ball will let us know what ,where ,when and How?


## Methodology
We will be using varioues ML Algorithoms to predict the future of the recession.
Algorithoms :
	1— Linear Discriminant Analysis. 
	2 — Classification and Regression Trees.
	3 — Naive Bayes. 
	4 — K-Nearest Neighbors. 
	5 — Learning Vector Quantization.  
	6 — Support Vector Machines. 
	7 — Bagging and Random Forest. 
	8 — Boosting and AdaBoost.

## Data
- **ID**: internal ID, _numeric_
- **date**, date, _datetime_
- **year**, year, _numeric_
- **month**, month, _numeric_
- **day**, day, _numeric_
- **USSLIND**, Leading Index for the United States, _numeric_, ***target variable*
- **USRECD**: NBER based Recession Indicators for the United States from the Period following the Peak through the Trough, _numeric_
- **USARECDM**: OECD based Recession Indicators for the United States from the Peak through the Trough, _numeric_
- **USRECDM**: NBER based Recession Indicators for the United States from the Peak through the Trough, _numeric_
- **USRECDP**: NBER based Recession Indicators for the United States from the Peak through the Period preceding the Trough, _numeric_
- **USARECD**: OECD based Recession Indicators for the United States from the Period following the Peak through the Trough, _numeric_
- **USARECDP**: OECD based Recession Indicators for the United States from the Peak through the Period preceding the Trough, _numeric_
- **TERMCBAUTO48NS**:Finance Rate on Consumer Installment Loans at Commercial Banks, New Autos 48 Month Loan 
- **TERMCBPER24NS**: Finance Rate on Personal Loans at Commercial Banks, 24 Month Loan
- **DCOILWTICO**: Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma --data :YY-MM-DD start from 2013
- **GFDEGDQ188S**: Federal Debt: Total Public Debt as Percent of Gross Domestic Product
- **HBATGDQ188S**: Federal Debt Held by Agencies and Trusts as Percent of Gross Domestic Product
- **HBFIGDQ188S**: Federal Debt Held by Foreign and International Investors as Percent of Gross Domestic Product 
- **HBFRGDQ188S**: Federal Debt Held by Federal Reserve Banks as Percent of Gross Domestic Product 
- **HBPIGDQ188S**:  Federal Debt Held by Private Investors as Percent of Gross Domestic Product 
- **MVPHGFD027MNFRBDAL**: Market Value of Privately Held Gross Federal Debt
- **MDSP**: Mortgage Debt Service Payments as a Percent of Disposable Personal Income
- **RSAHORUSQ156S**: Homeownership Rate for the United States
- **TDSP**: Household Debt Service Payments as a Percent of Disposable Personal Income
- **MEFAINUSA646N**:  Median Family Income in the United States
- **MEHOINUSA646N**: Median Household Income in the United States
- **MEHOINUSA672N**: Real Median Household Income in the United States
- **MEPAINUSA646N**: Median Personal Income in the United States
- **MEPAINUSA672N**: Real Median Personal Income in the United States
- **MNFCTRIRSA**: Manufacturers: Inventories to Sales Ratio
- **MNFCTRMPCIMSA**: Manufacturers Inventories
- **MNFCTRMPCSMSA**: Manufacturers Sales
- **MARTSMPCSM44000USS**: Advance Retail Sales: Retail (Excluding Food Services)
- **MORTGAGE30US**: 30-Year Fixed Rate Mortgage Average in the United States
- **MORTGAGE15US**: 15-Year Fixed Rate Mortgage Average in the United States
- **TERMCBPER24NS**: Finance Rate on Personal Loans at Commercial Banks, 24 Month Loan
- **DGS1**: 1-Year Treasury Constant Maturity Rate 
- **DGS2**: 2-Year Treasury Constant Maturity Rate 
- **DGS5**: 5-Year Treasury Constant Maturity Rate 
- **DGS10**: 10-Year Treasury Constant Maturity Rate 
- **AWHNONAG**:  Average Weekly Hours of Production and Nonsupervisory Employees
- **CES9091000001**: All Employees: Government: Federal 
- **LNS13023622**: Job Losers as a Percent of Total Unemployed 
- **LNS13023654**: Job Losers on Layoff as a Percent of Total Unemployed
- **LNS13023706**: Job Leavers as a Percent of Total Unemployed
- **LNS13026511**: Job Losers Not on Layoff as a Percent of Total Unemployed 
- **PAYEMS**: All Employees: Total Nonfarm Payrolls
- **USGOVT**: All Employees: Government
- **USPRIV**: All Employees: Total Private Industries
- **MPCT00XXS**: Total Construction Spending: Residential
- **MPCTNRXXS**: Total Construction Spending: Nonresidential
 **MPCTXXXXS**: Total Construction Spending
- **WPU5121010112**: Producer Price Index by Commodity for Health Care Services: Medicaid Patients: Hospital Inpatient Care, General Medical and Surgical Hospitals  s

### Money, Banking, & Finance
#### Automobile Loan Rates
- https://fred.stlouisfed.org/series/TERMCBAUTO48NS
#### Mortgage Rates
- https://fred.stlouisfed.org/series/MORTGAGE30US
- https://fred.stlouisfed.org/series/MORTGAGE15US
- https://fred.stlouisfed.org/series/TERMCBPER24NS
#### Personal Loan Rates
- https://fred.stlouisfed.org/series/TERMCBPER24NS
#### Treasury Constant Maturity
- https://fred.stlouisfed.org/series/DGS1 
- https://fred.stlouisfed.org/series/DGS2
- https://fred.stlouisfed.org/series/DGS5
- https://fred.stlouisfed.org/series/DGS10

### Population, Employment, & Labor Markets
#### Employment
- https://fred.stlouisfed.org/series/PAYEMS
- https://fred.stlouisfed.org/series/CEU0500000003

- https://fred.stlouisfed.org/series/PAYEMS
- https://fred.stlouisfed.org/series/USPRIV
- https://fred.stlouisfed.org/series/AWHNONAG

- https://fred.stlouisfed.org/series/CES9091000001
- https://fred.stlouisfed.org/series/USGOVT

- https://fred.stlouisfed.org/series/UNEMPLOY
- https://fred.stlouisfed.org/series/LNS13023706
- https://fred.stlouisfed.org/series/LNS13023622
- https://fred.stlouisfed.org/series/LNS13023654
- https://fred.stlouisfed.org/series/LNS13026511

#### Income
- https://fred.stlouisfed.org/series/MEHOINUSA672N
- https://fred.stlouisfed.org/series/MEPAINUSA672N
- https://fred.stlouisfed.org/series/MEFAINUSA646N
- https://fred.stlouisfed.org/series/MEHOINUSA646N
- https://fred.stlouisfed.org/series/MEPAINUSA646N

#### Tax

### National Accounts
#### Federal Government Debt
- https://fred.stlouisfed.org/series/GFDEGDQ188S
- https://fred.stlouisfed.org/series/HBFIGDQ188S
- https://fred.stlouisfed.org/series/HBPIGDQ188S
- https://fred.stlouisfed.org/series/HBFRGDQ188S
- https://fred.stlouisfed.org/series/HBFRGDQ188S
- https://fred.stlouisfed.org/series/HBATGDQ188S
- https://fred.stlouisfed.org/series/MVPHGFD027MNFRBDAL

### Production & Business Activity
#### Construction
- https://fred.stlouisfed.org/series/MPCTXXXXS
- https://fred.stlouisfed.org/series/MPCTNRXXS
- https://fred.stlouisfed.org/series/MPCT00XXS

#### Housing
- https://fred.stlouisfed.org/series/TDSP
- https://fred.stlouisfed.org/series/RSAHORUSQ156S
- https://fred.stlouisfed.org/series/MDSP
#### Manufacturing
- https://fred.stlouisfed.org/series/MNFCTRIRSA
- https://fred.stlouisfed.org/series/MNFCTRMPCSMSA
- https://fred.stlouisfed.org/series/MNFCTRMPCIMSA
#### Retail Trade
- https://fred.stlouisfed.org/series/MARTSMPCSM44000USS

### Prices
#### Commodities
- https://fred.stlouisfed.org/series/DCOILWTICO

## Report

## Requirements
- requests          2.19.1
- numpy             1.15.1
- pandas            0.23.4
- matplotlib        2.2.3
- tqdm              4.26.0
- cython            0.28.5
## Directory Structure
```
.
├── docs                <- Documents related to this project
├── images              <- Images for README.md files
├── notebooks           <- Ipythoon Notebook files
├── reports             <- Generated analysis as HTML, PDF, Latex, etc.
│   ├── figures         <- Generated graphics and figures used in reporting
│   └── logs            <- Generated log files  
└── reb
    ├── conf
    ├── data            <- data utilized in this project
    │   ├── ext
    │   ├── int
    │   └── raw
    ├── src             <- Source files used in this project
    ├── static          <- CSS/SCSS/JS/Vedoer source files
    └── templates       <- Flask templates 
```
## Installation
Install python dependencies from  `requirements.txt` using conda.
```bash
conda install --yes --file conda-requirements.txt
```

Or create a new conda environment `<new-env-name>` by importing a copy of the working conda environment `conda-reb.yml` at the project root directory:
```bash
conda env create --name <new-env-name> -f conda-reb.yml
```
## Usage
```bash
python run.py
```
## References
https://towardsdatascience.com/a-tour-of-the-top-10-algorithms-for-machine-learning-newbies-dde4edffae11
## To Do
- [ ] TBA

## License
MIT License

