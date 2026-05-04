#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test file with various special characters and formatting.

This includes:
- Unicode: Ω, π, ∑
- Quotes: "double" and 'single'
- Backslashes: \\ \n \t
- JSON: {"key": "value", "nested": {"a": 1}}
"""

import json

def process_data(data: dict) -> str:
    '''Process data and return formatted string.'''
    result = f"Processing: {json.dumps(data)}"
    return result

if __name__ == "__main__":
    test_data = {
        "name": "test",
        "values": [1, 2, 3],
        "meta": {"π": 3.14159}
    }
    print(process_data(test_data))
