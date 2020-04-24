import argparse

def calcPVBegin(n, i, pmt, fv):
    if n < 0:
        print("Error: negative number of periods")
        return 0
    ratio = ((1+i)**(n+1)-(1+i))/i
    pmt_sum = ratio*pmt
    pv = (fv-pmt_sum) / ((1+i)**n)
    return round(pv,2)

def calcPVEnd(n, i, pmt, fv):
    if n < 0:
        print("Error: negative number of periods")
        return 0
    ratio = ((1+i)**n-1)/i
    pmt_sum = ratio*pmt
    pv = (fv-pmt_sum) / ((1+i)**n)
    return round(pv,2)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate PV given N, I/Y, PMT, FV." +
        " Payments are made at the END of each period by default.")
    parser.add_argument("-b", "--begin", help="Use BEGIN mode", action="store_true")
    parser.add_argument("number", help="number of periods", type=float)
    parser.add_argument("interest", help="growth rate per period", type=float)
    parser.add_argument("payment", help="payment value", type=float)
    parser.add_argument("future", help="future value of annuity", type=float)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    n = round(args.number,2)
    i = round(args.interest,2) / 100.0
    pmt = round(args.payment,2)
    fv = round(args.future,2)
    if args.begin:
        print(calcPVBegin(n, i, pmt, fv))
    else:
        print(calcPVEnd(n, i, pmt, fv))
