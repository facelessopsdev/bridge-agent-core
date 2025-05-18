"""Command line interface for Bridge Agent."""
from crm_manager import CRMManager
from task_runner import TaskRunner
import sys
import json
import os

class BridgeAgent:
    def __init__(self, config_path="config.json"):
        self.config = {}
        self.modules = {}
        self.load_config(config_path)
        self.register_default_modules()

    def load_config(self, path):
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as cfg:
                    self.config = json.load(cfg)
            except json.JSONDecodeError:
                print(f"Error: Failed to parse configuration file {path}")
        else:
            self.config = {}

    def register_default_modules(self):
        self.modules["crm_manager"] = CRMManager()
        self.modules["task_runner"] = TaskRunner()

def create_client(crm, tasks):
    name = input("Enter client name: ")
    tier = input("Enter tier: ")
    crm.create_client(name, tier)

def list_clients(crm, tasks):
    crm.list_clients()

def add_task(crm, tasks):
    task = input("Enter task: ")
    tasks.add_task(task)

def list_tasks(crm, tasks):
    tasks.list_tasks()

def clear_tasks(crm, tasks):
    tasks.clear_tasks()

def main():
    crm = CRMManager()
    tasks = TaskRunner()

    commands = {
        "create_client": create_client,
        "list_clients": list_clients,
        "add_task": add_task,
        "list_tasks": list_tasks,
        "clear_tasks": clear_tasks
    }

    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("Available commands:")
        for name in commands:
            print(f"- {name}")
        return

    command = sys.argv[1]
    commands[command](crm, tasks)

if __name__ == "__main__":
    main()

