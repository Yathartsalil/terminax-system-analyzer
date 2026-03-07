import time
from rich.console import Console
from rich.table import Table
from rich.live import Live

from analyzer.cpu import get_cpu_info
from analyzer.memory import get_memory_info
from analyzer.processes import get_top_processes

console = Console()

def generate_table():
    cpu = get_cpu_info()
    mem = get_memory_info()
    procs = get_top_processes()

    table = Table(title="Terminal System Analyzer")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row("CPU Usage", f"{cpu['usage']}%")
    table.add_row("Memory Usage", f"{mem['percent']}%")
    table.add_row("Swap Usage", f"{mem['swap_percent']}%")
    table.add_row("Load Avg", f"{cpu['load_avg']}")

    table.add_section()

    table.add_column("PID")
    table.add_column("Name")
    table.add_column("CPU %")
    table.add_column("Memory %")

    for proc in procs:
        table.add_row(
            str(proc['pid']),
            str(proc['name']),
            str(proc['cpu_percent']),
            f"{proc['memory_percent']:.2f}"
        )

    return table

def run_dashboard():
    with Live(generate_table(), refresh_per_second=1) as live:
        while True:
            live.update(generate_table())
            time.sleep(1)
