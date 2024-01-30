import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    print(f"专注倒计时开始，时长: {minutes} 分钟.")
    
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        time_format = f'{minutes:02d}:{seconds:02d}'
        
        print(f"剩余时间: {time_format}", end='\r')
        time.sleep(1)
    
    print("专注时钟结束！")

# 使用示例: 专注60分钟
focus_timer(60)
