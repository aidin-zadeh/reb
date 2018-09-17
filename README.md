
# reb

## Background

## Methodology

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

## To Do
- [ ] TBA

## License
MIT License

