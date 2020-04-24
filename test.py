from calcPMT import calcPMTBegin, calcPMTEnd
from calcPV import calcPVBegin, calcPVEnd
from calcFV import calcFVBegin, calcFVEnd



if __name__ == '__main__':
    test_count = 0
    fail_count = 0
    threshold = 0.01

    # (N, I, PV, PMT, FV)
    cases_end = []
    cases_end.append((4.0, 0.1, -792.47, 250.0,     0.0))
    cases_end.append((4.0, 0.1,    0.0,  215.47, 1000.0))
    cases_end.append((4.2, 0.1,    0.0,  200.0,   984.55))
    cases_beg = []
    cases_beg.append((4.0, 0.1, -871.71, 250.0,     0.0))
    cases_beg.append((4.0, 0.1,    0.0,  195.88, 1000.0))
    cases_beg.append((4.2, 0.1,    0.0,  200.0,  1083.01))

    # ---------- Test calcN -----------


    # ---------- Test calcI -----------


    # ---------- Test calcPV ----------


    # --------- Test calcPMT ----------
    for case in cases_end:
        test_count += 1
        pmt = calcPMTEnd(case[0],case[1],case[2],case[4])
        if pmt != case[3]:
            if abs(pmt-case[3]) > threshold:
                print("\ncalcPMT failed: expected %f, found %.2f"%(case[3], pmt))
                print(case)
                fail_count += 1
    for case in cases_beg:
        test_count += 1
        pmt = calcPMTBegin(case[0],case[1],case[2],case[4])
        if pmt != case[3]:
            if abs(pmt-case[3]) > threshold:
                print("\ncalcPMT failed: expected %f, found %.2f"%(case[3], pmt))
                print(case)
                fail_count += 1

    # ---------- Test calcFV ----------
    for case in cases_end:
        test_count += 1
        fv = calcFVEnd(case[0],case[1],case[2],case[3])
        if fv != case[4]:
            if abs(fv-case[4]) > threshold:
                print("\ncalcFV failed: expected %f, found %f"%(case[4], fv))
                print(case)
                fail_count += 1
    for case in cases_beg:
        test_count += 1
        fv = calcFVBegin(case[0],case[1],case[2],case[3])
        if fv != case[4]:
            if abs(fv-case[4]) > threshold:
                print("\ncalcFV failed: expected %f, found %f"%(case[4], fv))
                print(case)
                fail_count += 1

    # -------- Display results --------
    print("\n================================================")
    print("\n\t%2d / %2d test cases successful" % (test_count-fail_count, test_count))
