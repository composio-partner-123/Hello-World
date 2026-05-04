#!/usr/bin/env python3
# This is a test file

class Example:
    def __init__(self, name: str = "default"):
        self.name = name
        self.data = {'key': 'value', 'nested': {'a': 1}}
    
    def process(self):
        """Process the data with quotes and newlines"""
        result = f"Processing {self.name}..."
        return result
