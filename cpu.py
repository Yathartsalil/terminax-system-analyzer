import psutil

def get_cpu_info():
    return {
        "usage": psutil.cpu_percent(interval=1),
        "per_core": psutil.cpu_percent(percpu=True),
        "load_avg": psutil.getloadavg()
    }
