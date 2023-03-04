SET PATH=C:\Program Files\DSI\EEMS10.3;%PATH%
SET KMP_AFFINITY=granularity=fine,compact,1,0

TITLE D:\EEMS\try
D:
CD "D:\EEMS\try"
"C:\Program Files\DSI\EEMS10.3\EFDCPlus_MPI_10.3.2_SP64_210525.exe"  -NT3
PAUSE
