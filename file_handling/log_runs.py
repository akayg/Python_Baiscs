import datetime as dt

try:
    current_time = dt.datetime.now()
    # print(current_time)
    with open("file_handling/logs.txt","a") as f:
        f.write(f"program run at {current_time}\n")
        print("Data saved")

except Exception as e :
    print(f"Uhh Something seems off {e}")