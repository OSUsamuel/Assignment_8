# microservice_sort.py
# Waits for a sort command ('asc' or 'desc') in command.txt and sorts items from list.txt accordingly.
import time
import os

def read_list(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def write_output(items, output_path):
    with open(output_path, "w") as f:
        for item in items:
            f.write(item + "\n")

def monitor_for_command(list_path="list.txt", command_path="command.txt", output_path="response.txt"):
    print("Waiting for sort command (asc or desc)...")
    last_command = ""

    while True:
        if os.path.exists(command_path):
            with open(command_path, "r") as cmd_file:
                command = cmd_file.read().strip().lower()

            if command and command != last_command:
                last_command = command

                try:
                    items = read_list(list_path)
                    if command == "asc":
                        sorted_items = sorted(items)
                    elif command == "desc":
                        sorted_items = sorted(items, reverse=True)
                    else:
                        write_output(["ERROR: Invalid command. Use 'asc' or 'desc'."], output_path)
                        print("Invalid command detected. Waiting for new command...")
                        time.sleep(1)
                        continue

                    write_output(sorted_items, output_path)
                    print(f"Sorted ({command}) list written to {output_path}.")

                except Exception as e:
                    write_output([f"ERROR: {str(e)}"], output_path)

        time.sleep(1)

if __name__ == "__main__":
    monitor_for_command()
