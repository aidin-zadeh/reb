
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



### Predictor indicators according to NBER (National Bureau of Economic Research)
- **GDPC1**: [Real Gross Domestic Product](https://fred.stlouisfed.org/series/GDPC1)
- **W875RX1**: [Real personal income excluding current transfer receipts](https://fred.stlouisfed.org/series/W875RX1)
- **PAYEMS**: [All Employees: Total Nonfarm Payrolls](https://fred.stlouisfed.org/series/PAYEMS)
- **INDPRO**: [Industrial Production Index](https://fred.stlouisfed.org/series/INDPRO)
- **CMRMTSPL**: [Real Manufacturing and Trade Industries Sales](https://fred.stlouisfed.org/series/CMRMTSPL)



#### Monthly indicators
- **AWHNONAG**: [Average Weekly Hours of Production and Nonsupervisory Employees: Total private](https://fred.stlouisfed.org/series/AWHNONAG)
- **CES9091000001**: [AAll Employees: Government: Federal](https://fred.stlouisfed.org/series/CES9091000001)
- **CEU0500000003**: [Average Hourly Earnings of All Employees: Total Private](https://fred.stlouisfed.org/series/CEU0500000003)
- **CMRMTSPL**: [Real Manufacturing and Trade Industries Sales](https://fred.stlouisfed.org/series/CMRMTSPL)
- **INDPRO**: [Industrial Production Index](https://fred.stlouisfed.org/series/INDPRO)
- **LNS13023622**: [Job Losers as a Percent of Total Unemployed](https://fred.stlouisfed.org/series/LNS13023622)
- **LNS13023654**: [Job Losers on Layoff as a Percent of Total Unemployed ](https://fred.stlouisfed.org/series/LNS13023654)
- **LNS13023706**: [Job Leavers as a Percent of Total Unemployed](https://fred.stlouisfed.org/series/LNS13023706)
- **LNS13026511**: [ Job Losers Not on Layoff as a Percent of Total Unemployed](https://fred.stlouisfed.org/series/LNS13026511)
- **MARTSMPCSM44000USS**: [Advance Retail Sales: Retail (Excluding Food Services)](https://fred.stlouisfed.org/series/MARTSMPCSM44000USS)
- **MNFCTRIRSA**: [Manufacturers: Inventories to Sales Ratio](https://fred.stlouisfed.org/series/MNFCTRIRSA)
- **MNFCTRMPCIMSA**: [Manufacturers Inventories](https://fred.stlouisfed.org/series/MNFCTRMPCIMSA)
- **MNFCTRMPCSMSA**: [Manufacturers Sales](https://fred.stlouisfed.org/series/MNFCTRMPCSMSA)
- **MPCT00XXS**: [Total Construction Spending: Residential](https://fred.stlouisfed.org/series/MPCT00XXS)
- **MPCTNRXXS**: [Total Construction Spending: Nonresidential](https://fred.stlouisfed.org/series/MPCTNRXXS)
- **MPCTXXXXS**: [Total Construction Spending](https://fred.stlouisfed.org/series/MPCTXXXXS)
- **MVPHGFD027MNFRBDAL**: [ Market Value of Privately Held Gross Federal Debt](https://fred.stlouisfed.org/series/MVPHGFD027MNFRBDAL)
- **PAYEMS**: [All Employees: Total Nonfarm Payrolls](https://fred.stlouisfed.org/series/PAYEMS)
- **UNEMPLOY**: [Unemployment Level](https://fred.stlouisfed.org/series/UNEMPLOY)
- **USGOVT**: [All Employees: Government](https://fred.stlouisfed.org/series/USGOVT)
- **W875RX1**: [Real personal income excluding current transfer receipts](https://fred.stlouisfed.org/series/W875RX1)



#### Monthly indicators - Currently Discarded
- **USPRIV**: [All Employees: Total Private Industries](https://fred.stlouisfed.org/series/USPRIV)
- **LNS13026511**: [Job Losers Not on Layoff as a Percent of Total Unemployed](https://fred.stlouisfed.org/series/LNS13026511)



#### Daily indicators
- **DGS10**: [10-Year Treasury Constant Maturity Rate](https://fred.stlouisfed.org/series/DGS10)
- **DGS5**: [5-Year Treasury Constant Maturity Rate](https://fred.stlouisfed.org/series/DGS5)
- **DGS2**: [2-Year Treasury Constant Maturity Rate](https://fred.stlouisfed.org/series/DGS2)
- **DGS1**: [1-Year Treasury Constant Maturity Rate](https://fred.stlouisfed.org/series/DGS1)


#### Quarterly indicators - Currently Discarded
- **GDPC1**: [Real Gross Domestic Product](https://fred.stlouisfed.org/series/GDPC1)


#### Annual indicators - Currently Discarded
- **MEFAINUSA646N**: [Median Family Income in the United States](https://fred.stlouisfed.org/series/MEFAINUSA646N)
- **MEHOINUSA646N**: [Median Household Income in the United States](https://fred.stlouisfed.org/series/MEHOINUSA646N)
- **MEHOINUSA672N**: [Real Median Household Income in the United States](https://fred.stlouisfed.org/series/MEHOINUSA672N)
- **MEPAINUSA646N**: [Median Personal Income in the United State](https://fred.stlouisfed.org/series/MEPAINUSA646N)
- **MEPAINUSA672N**: [Real Median Personal Income in the United States](https://fred.stlouisfed.org/series/MEPAINUSA672N)



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

