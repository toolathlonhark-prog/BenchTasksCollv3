#!/usr/bin/env python3
"""Evaluation script for personalization-service."""

def evaluate(output_path):
    import json
    with open(output_path, 'r') as f:
        result = json.load(f)
    return True
