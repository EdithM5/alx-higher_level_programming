#!/usr/bin/python3

import sys

codes_count = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
file_size = 0
total_lines = 0

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            words = line.split()
            file_size += int(words[-1])
            status_code = words[-2]
            if status_code in codes_count:
                codes_count[status_code] += 1
            total_lines += 1
        except Exception:
            pass
        if i % 10 == 0:
            print(f'File size: {file_size}')
            for code, count in sorted(codes_count.items()):
                if count != 0:
                    print(f'{code}: {count}')
except KeyboardInterrupt:
    print(f'File size: {file_size}')
    for code, count in sorted(codes_count.items()):
        if count != 0:
            print(f'{code}: {count}')

print(f'File size: {file_size}')
for code, count in sorted(codes_count.items()):
    if count != 0:
        print(f'{code}: {count}')

