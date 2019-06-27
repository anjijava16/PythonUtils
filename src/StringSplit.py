
import io
import csv;
import io

stream_str = io.BytesIO(b"JournalDev Python")
fileN=open("E:/anjidev2.csv","wb+");
Body=stream_str.getvalue()
fileN.write(Body)

# import os
# import errno
#
#
# filename = "E:/myDev/anjiWOrks/obc.csv"
# if not os.path.exists(os.path.dirname(filename)):
#     try:
#         os.makedirs(os.path.dirname(filename))
#     except OSError as exc: # Guard against race condition
#         if exc.errno != errno.EEXIST:
#             raise
#
# fns= open(filename,"w+")

