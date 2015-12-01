#!/usr/bin/env bash
grep '\d\{1,3\}\.\d\{1,3\}\.\d\{1,3\}\.\d\{1,3\}' shuffled_data | sort | uniq -c | sort -nr | head -10 | awk '{print$2}'