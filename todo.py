import argparse
import sys
from db import init_db, add_task, list_tasks, mark_done, delete_task

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
GRAY   = "\033[90m"
RESET  = "\033[0m"
BOLD   = "\033[1m"


def cmd_add(args):
    task_id = add_task(args.task)
    print(f"{GREEN}✔ Task #{task_id} added:{RESET} {args.task}")


def cmd_list(args):
    tasks = list_tasks(show_all=args.all)
    if not tasks:
        msg = "No tasks found." if args.all else "No tasks yet. 🎉"
        print(f"{GRAY}{msg}{RESET}")
        return

    label = "All tasks" if args.all else "Active tasks"
    print(f"\n{BOLD}{CYAN}{label}{RESET}")
    print(f"{GRAY}{'─' * 40}{RESET}")

    for t in tasks:
        status = f"{GREEN}✔{RESET}" if t["done"] else f"{YELLOW}○{RESET}"
        task_text = f"{GRAY}{t['task']}{RESET}" if t["done"] else t["task"]
        print(f"  {status}  [{BOLD}#{t['id']}{RESET}] {task_text}")

    print(f"{GRAY}{'─' * 40}{RESET}")
    done_count = sum(1 for t in tasks if t["done"])
    print(f"{GRAY}  {done_count}/{len(tasks)} completed{RESET}\n")


def cmd_done(args):
    success = mark_done(args.id)
    if success:
        print(f"{GREEN}✔ Task #{args.id} marked as done.{RESET}")
    else:
        print(f"{RED}✖ Task #{args.id} not found or already done.{RESET}")
        sys.exit(1)


def cmd_delete(args):
    success = delete_task(args.id)
    if success:
        print(f"{RED}🗑 Task #{args.id} deleted.{RESET}")
    else:
        print(f"{RED}✖ Task #{args.id} not found.{RESET}")
        sys.exit(1)


def main():
    init_db()

    parser = argparse.ArgumentParser(
        prog="todo",
        description="📝 A command-line task manager."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_add = subparsers.add_parser("add", help="Add a task")
    p_add.add_argument("task", type=str, help="Task description")
    p_add.set_defaults(func=cmd_add)

    p_list = subparsers.add_parser("list", help="List tasks")
    p_list.add_argument("--all", action="store_true", help="Show completed tasks too")
    p_list.set_defaults(func=cmd_list)

    p_done = subparsers.add_parser("done", help="Mark a task as done")
    p_done.add_argument("id", type=int, help="Task ID")
    p_done.set_defaults(func=cmd_done)

    p_delete = subparsers.add_parser("delete", help="Delete a task")
    p_delete.add_argument("id", type=int, help="Task ID")
    p_delete.set_defaults(func=cmd_delete)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()    