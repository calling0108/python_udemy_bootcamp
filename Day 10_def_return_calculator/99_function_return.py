# Functions with Outputs

def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())

format_name("angela", "ANGELA") # Angela, Angela


# return : 함수를 출력값을 가지도록 해주는 것 
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("AnGElA", "YU"))
