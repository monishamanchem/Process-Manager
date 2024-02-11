import psutil

def process_manager():
    processes = []
    # Get all running processes
    all_processes = psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'io_counters'])
    for process in all_processes:
        process_info = {}

        # Process ID       
        process_info['pid'] = process.info['pid']

        # Process name        
        process_info['name'] = process.info['name']

        # CPU utilization in percentage        
        process_info['cpu_percent'] = process.info['cpu_percent']

        # Memory utilization in percentage
        process_info['memory_percent'] = process.info['memory_percent']

        # I/O utilization
        io_counters = process.info['io_counters']
        process_info['io_read_bytes'] = io_counters.read_bytes
        process_info['io_write_bytes'] = io_counters.write_bytes

        # Tag process as CPU bound or I/O bound
        if io_counters.read_bytes > 0 or io_counters.write_bytes > 0:
            process_info['bound'] = 'I/O bound'
        else:
            process_info['bound'] = 'CPU bound'

        processes.append(process_info)
    return processes

# Test the process_manager function
processes = process_manager()

# Print the process details
for process in processes:
    print(f"PID: {process['pid']}")
    print(f"Name: {process['name']}")
    print(f"CPU Percent: {process['cpu_percent']}")
    print(f"Memory Percent: {process['memory_percent']}")
    print(f"I/O Read Bytes: {process['io_read_bytes']}")
    print(f"I/O Write Bytes: {process['io_write_bytes']}")
    print(f"Bound: {process['bound']}")
    print("-" * 20)
