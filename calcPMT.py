import argparse

def calcPMTBegin(n, i, pv, fv):
    if n < 0:
        print("Error: negative number of periods")
        return 0
    ratio = ((1+i)**(n+1)-(1+i))/i
    pmt = (fv-pv*(1+i)**n)/ratio
    return round(pmt,2)

def calcPMTEnd(n, i, pv, fv):
    if n < 0:
        print("Error: negative number of periods")
        return 0
    ratio = ((1+i)**n-1)/i
    pmt = (fv-pv*(1+i)**n)/ratio
    return round(pmt,2)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate PMT given N, I/Y, PV, " +
        "and FV. Payments are made at the END of each period by default.")
    parser.add_argument("-b", "--begin", help="Use BEGIN mode", action="store_true")
    parser.add_argument("number", help="number of periods", type=float)
    parser.add_argument("interest", help="growth rate per period", type=float)
    parser.add_argument("present", help="present value of annuity", type=float)
    parser.add_argument("future", help="present value of annuity", type=float)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    n = round(args.number,2)
    i = round(args.interest,2) / 100.0
    pv = args.present
    fv = args.future
    if args.begin:
        print(calcPMTBegin(n, i, pv, fv))
    else:
        print(calcPMTEnd(n, i, pv, fv))
