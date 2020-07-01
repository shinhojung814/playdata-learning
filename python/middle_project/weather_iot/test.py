from datetime import datetime

from home_iot import homeIOT

if __name__ == "__main__":
    print("Home IOT system is running...")
    current_time = datetime.now()
    current_time = current_time.strftime(("%Y-%m-%d %H:%M"))
    current_cycle  = homeIOT()
    if current_cycle['code']:
        f = open(f"log/{current_time}.txt", "a")
        for log in current_cycle['logs']:
            f.write(f"{log}\n")

    else:
        f = open(f"log/{current_time}_error.txt", "a")
        f.write(current_cycle['log'])
    f.close()
    print("close")

