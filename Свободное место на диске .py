import shutil

free = shutil.disk_usage('/').free/(1024*1024*1024)

print(f'Свободное место на всех дисках {free:.5} Gb')
