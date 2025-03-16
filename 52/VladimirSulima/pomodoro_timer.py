from task import Task


class PomodoroTimer:
    def __init__(self):
        self.tasks = []

    def get_all_available_tasks(self):
        if self.tasks:
            print("Existing tasks:")
            for (index, value) in enumerate(self.tasks):
                if value.is_task_completed:
                    task_status = "Completed"
                else:
                    task_status = "Not completed"
                print(f"{index + 1} - {value.task_name}. \t Status: {task_status}")
        else:
            input("There are no existing tasks. \n")
            return "Empty list"

    def add_new_task(self):
        aborted = False
        is_user_input_valid = False
        while not is_user_input_valid:
            task_name = self.set_task_name()
            if task_name is None:
                aborted = True
                break
            work_section_duration = self.set_work_section_duration()
            if work_section_duration is None:
                aborted = True
                break
            break_section_duration = self.set_break_section_duration()
            if break_section_duration is None:
                aborted = True
                break
            if aborted:
                print("Operation was aborted.")
                input("Press ENTER to continue...")
                is_user_input_valid = True
                return None
            else:
                self.tasks.append(Task(task_name, work_section_duration, break_section_duration))
                is_user_input_valid = True
                input(f"New {task_name} with working section duration {work_section_duration} minutes and break section duration {break_section_duration} minutes successfully added \n")

    def set_task_name(self):
        is_string_empty = True
        aborted = False
        task_name = None
        while is_string_empty:
            task_name = input("Set Task name:")
            if not task_name:
                print("Task name can't be empty. Please, try again or e[x]it")
            elif task_name == "x":
                    is_string_empty = False
                    aborted = True
            else:
                is_string_empty = False
        if not aborted:
            return task_name
        else:
            pass

    def set_work_section_duration(self):
        aborted = False
        is_user_input_valid = False
        work_section_duration = None
        while not is_user_input_valid:
            try:
                user_input = input("Set work section duration in minutes:")
                if user_input.lower() == 'x':
                    aborted = True
                    break
                else:
                    work_section_duration = int(user_input)
                    if work_section_duration <= 0:
                        raise ValueError
                    is_user_input_valid = True
            except ValueError as vl:
                print("Task work section can't be empty, not a number, zero or negative. Please, try again or e[x]it")

        if not aborted:
            return work_section_duration
        else:
            pass

    def set_break_section_duration(self):
        aborted = False
        is_user_input_valid = False
        break_section_duration = None
        while not is_user_input_valid:
            try:
                user_input = input("Set break section duration in minutes:")
                if user_input.lower() == 'x':
                    aborted = True
                    break
                else:
                    break_section_duration = int(user_input)
                    if break_section_duration <= 0:
                        raise ValueError
                    is_user_input_valid = True
            except ValueError as vl:
                print("Task work section can't be empty, not a number, zero or negative. Please, try again or e[x]it")

        if not aborted:
            return break_section_duration

    def select_existing_task(self):
        aborted = False
        is_user_input_valid = False
        if self.tasks:
            self.get_all_available_tasks()
            while not is_user_input_valid:
                user_input = input("Select task number to proceed:")
                try:
                    if user_input.lower() == 'x':
                        aborted = True
                        break
                    else:
                        user_input = int(user_input)
                        if user_input > len(self.tasks) or user_input < 0:
                            raise ValueError
                        is_user_input_valid = True
                except ValueError as vl:
                    print("You selected unexciting task. Please, try again or e[x]it.")

            if not aborted:
                return user_input - 1
        else:
            input("There are no available tasks. Please, add new one to proceed...\n")

    def run_task_session(self, task_index):
        aborted = False

        while not aborted:
            is_user_input_valid = False
            self.tasks[task_index].start_working_timer()
            self.tasks[task_index].add_work_duration()
            print("Did you managed to complete task?")
            while not is_user_input_valid:
                user_input = input("[Y] - complete, [N] - proceed with break session, [X] - exit\n").lower()
                if user_input not in ["y", "n", "x"]:
                    print("Invalid choice, please, select again...")
                else:
                    is_user_input_valid = True
                    if user_input == "y":
                        self.tasks[task_index].is_task_completed = True
                        aborted = True
                        print(f"Congratulations, you've completed your{self.tasks[task_index].task_name}. Total work time - {self.tasks[task_index].total_task_duration}, total break time = - {self.tasks[task_index].total_break_duration} ")
                        input("Press ENTER to proceed")
                        break
                    elif user_input == "x":
                        aborted = True
                        break
                    elif user_input == "n":
                        self.tasks[task_index].start_break_timer()
                        self.tasks[task_index].add_break_duration()
                        input("Your BREAK session completed. Press enter to start you new working session")
                        break


