import argparse

def calcFVBegin(n, i, pv, pmt):
    if n < 0:
        print("Error: negative number of periods")
        return 0
    ratio = ((1+i)**(n+1)-(1+i))/i
    pmt_sum = ratio*pmt
    fv = pv * (1+i)**n + pmt_sum
    return round(fv,2)

def calcFVEnd(n, i, pv, pmt):
    if n < 0:
        print("Error: negative number of periods")
        return 0
    ratio = ((1+i)**n-1)/i
    pmt_sum = ratio*pmt
    fv = pv * (1+i)**n + pmt_sum
    return round(fv,2)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate FV given N, I/Y, PV, PMT." +
        " Payments are made at the END of each period by default.")
    parser.add_argument("-b", "--begin", help="Use BEGIN mode", action="store_true")
    parser.add_argument("number", help="number of periods", type=float)
    parser.add_argument("interest", help="growth rate per period", type=float)
    parser.add_argument("present", help="present value of annuity", type=float)
    parser.add_argument("payment", help="payment value", type=float)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    n = round(args.number,2)
    i = round(args.interest,2) / 100.0
    pv = round(args.present,2)
    pmt = round(args.payment,2)
    if args.begin:
        print(calcFVBegin(n, i, pv, pmt))
    else:
        print(calcFVEnd(n, i, pv, pmt))
