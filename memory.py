import psutil

def get_memory_info():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        "total": mem.total,
        "used": mem.used,
        "percent": mem.percent,
        "swap_percent": swap.percent
    }
