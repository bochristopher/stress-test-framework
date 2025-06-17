
# Project Walkthrough: ReliLab Test Automation Framework

## Overview
ReliLab is a Python-based hardware automation framework used to validate stress racks under power and thermal stress. It simulates and automates power cycles, temperature conditions, and system health monitoring. It's modular, scalable, and CI-ready.

## What It Does
- Simulates power cycling hardware and thermal behavior.
- Monitors simulated system status after each cycle.
- Automatically logs all test activity.
- Generates HTML reports with results.
- Retries failed checks before declaring test failure.

## Key Technologies
- Python 3.10
- Modular structure (framework/automation/test_cases/utils)
- GitHub Actions for CI
- Simulated hardware with mock test data
- HTML reports and CLI logs
