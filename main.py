# This is a sample Python script.
from scopes import scopes


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    set()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    from scopes import scopes
    a = scopes('launch offline_access patient/Medication.rs')
    b = scopes('patient/Medication.cruds')
    print(a&b)

