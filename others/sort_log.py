import re
from datetime import date, datetime
from collections import defaultdict
import sys
log_dict = defaultdict(list)
if len(sys.argv) == 1:
    print "Please provide list of files......!!!!!\n";exit()
for i in range(len(sys.argv)-1):
    with open(sys.argv[i+1]) as f:
        for line in f:
            line = line.strip()
            match = re.findall(':(\d+)-(\d+)-(\d+) (\d+):(\d+):(\d+),(\d+) ', line)
            if match:
                year, month, date, hour, minute, sec, msec = match[0]
                time_of_log  = datetime(int(year), int(month), int(date), int(hour), int(minute), int(sec), int(msec)*1000)
                cleaned_line =  ":".join(line.split(':')[1:])
                log_dict[time_of_log].append(cleaned_line)
            
write_file = open("log_script_output.txt", "w+")
write_file.truncate()

for key, value in sorted(log_dict.items()):
    write_file.write("\n".join(value)+'\n')
    print "\n".join(value)
write_file.close()
