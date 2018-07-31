import re, time


class Vreport:

    ''' Checking the virt-who today's report status '''

    def __init__(self, logfile=None):
        self.logfile = logfile


    def lastreport(self):

        if self.logfile != None:

            try:

                with open(self.logfile, 'r') as mylogfile:
                    timestemp = time.strftime("%Y-%m-%d")

                    for line in mylogfile:
                        if re.search(timestemp, line) and re.search('Host-to-guest', line):
                            print(line)
            except Exception:
                print("[WARN] Log file not found :", self.logfile)

if __name__ == '__main__':

    LOGFILE = "/var/log/rhsm.log"
    REPORTCHECK = Vreport(logfile=LOGFILE)
    print("**** Today's virt-who Host-to-guest mapping sent to Satellite as below ****\n")
    REPORTCHECK.lastreport()




