from prettytable import PrettyTable

table = PrettyTable()
# print(table)

table.field_names = ["Poketmon Name", "Type"]

table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["charmander", "Fire"]
    ]
)

# table.align = "c"
table.get_string(align = "l")

print(table)