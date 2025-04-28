import platform
CPU_SERIAL = ""

class PIInfo:
    """ Get Pi Details """
    def serial_number(self):
        """ Collect Serial Number """
        if platform.system() == "Windows":
            return CPU_SERIAL
        else:
            with open('/proc/cpuinfo', 'r', encoding="utf-8") as pi_serial_file:
                for line in pi_serial_file:
                    if line.startswith("Serial"):
                        return line.split(":")[1].strip()
            return None
    def cpu_temp(self):
        """Get cpu temperature"""
        try:
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as temp_file:
                temp = int(temp_file.read()) / 1000  # Convert to degrees Celsius
            temp_str = f"{temp:.2f} °C"
            return temp_str
        except FileNotFoundError:
            return None
        
    def ram_usage(self):
        """Get Ram Usage"""
        try:
            with open('/proc/meminfo', 'r') as mem_file:
                lines = mem_file.readlines()

            # Extract relevant fields (values are in kB)
            total_mem = 0
            free_mem = 0
            available_mem = 0

            for line in lines:
                if line.startswith('MemTotal:'):
                    total_mem = int(line.split()[1])  # kB
                elif line.startswith('MemFree:'):
                    free_mem = int(line.split()[1])   # kB
                elif line.startswith('MemAvailable:'):
                    available_mem = int(line.split()[1])  # kB

            # Calculate used memory (MemTotal - MemAvailable)
            used_mem = total_mem - available_mem

            # Calculate RAM usage percentage
            ram_percent = (used_mem / total_mem) * 100 if total_mem > 0 else 0

            # Convert to MB
            total_mem_mb = total_mem / 1024
            used_mem_mb = used_mem / 1024
            free_mem_mb = free_mem / 1024
            raminfo = {"Total":str(total_mem_mb) + " MB","Used":str(used_mem_mb) + " MB","Free":str(free_mem_mb) + " MB","Used%":str(ram_percent) + " %"}
            return raminfo
        except FileNotFoundError:
            return None