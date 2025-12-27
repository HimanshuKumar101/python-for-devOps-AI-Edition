#aapko kaam karna hai ki user se CPU threshold lo
# current cpu usage check pata karo
# agar cpu usage threshold se zyada hai to warning print karo


import psutil

def check_cpu_threshold():
    cpu_threshold = int(input("Enter The CPU threshold percentage"))

    current_cpu = psutil.cpu_percent(interval=1)

    print("Current Cpu usage is :", current_cpu)

    if current_cpu > cpu_threshold:
        print("Warning: CPU usage is above the threshold.")
    else:
        print("CPU IS SAFE state")    


check_cpu_threshold()        