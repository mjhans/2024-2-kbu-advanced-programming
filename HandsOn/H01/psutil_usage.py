import psutil

print("CPU 사용량: ", psutil.cpu_percent(interval=1))