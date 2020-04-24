# FinancialCalculator

Perform calculations on annuities to find any one of the following, given some
 other values:

* 'N' ------- number of periods (int)
* 'I/Y' ------ interest rate per period
* 'PV' ------ present value
* 'PMT' ---- payment amount
* 'FV' ------ future value

## Calculate Payment (PMT)
Calculates PMT given N, I/Y, PV, and FV values. Payments are made at the END
of each period by default.

usage:
* `python calcFV.py [-b] <number> <interest> <present> <future>`

* `python calcFV.py -h`

## Calculate Present Value (PV)
Calculates PV given N, I/Y, PMT, and FV values. Payments are made at the END
of each period by default.

usage:
* `python calcFV.py [-b] <number> <interest> <payment> <future>`

* `python calcFV.py -h`

## Calculate Future Value (FV)
Calculates FV given N, I/Y, PV, and PMT values. Payments are made at the END
of each period by default.

usage:
* `python calcFV.py [-b] <number> <interest> <present> <payment>`

* `python calcFV.py -h`
