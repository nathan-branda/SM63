#defining world records for SM63
ANY_WR = 371.593
NMS_WR = 23*60 + 41
BAD_WR = 46*60 + 40

def sm63_math(time):
    anys = time/ANY_WR
    nmss = time/NMS_WR
    bads = time/BAD_WR
    print("Time in any\%s: " )