import time

while True:
    current_time = time.strftime('%H:%M:%S %p')
    print(current_time, end='\r', flush=True)  # 使用 '\r' 实现覆盖输出
    time.sleep(1)
