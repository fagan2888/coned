#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd

if __name__=="__main__":

    # -- read the usage data
    epath = os.path.join("..", "data", "coned", "ele_network_hourly_load")
    efile = "Historical_Network and System Meter 01-01-2008-07-17-2016.csv"
    iname = os.path.join(epath, efile)
    print("reading usage data from {0}...".format(iname))
    ele   = pd.read_csv(iname, encoding="utf-8-sig")

    # -- clip to 2012
    print("restricting to 2012...")
    sub = ele[ele.DT.apply(lambda x: "2012" in x)]

    # -- pivot and reindex
    print("pivoting table to group by datetime...")
    data = sub.pivot("DT", "\"IMPORTID\"", "READING").reset_index()

    # -- anonymize networks
    print("stripping out network names...")
    data.columns = [data.columns[0]] + range(len(data.columns) - 1)

    # -- write to csv
    oname = os.path.join("..", "output", "usage_2012.csv")
    print("writing to {0}...".format(oname))
    data.to_csv(oname, index=False)
