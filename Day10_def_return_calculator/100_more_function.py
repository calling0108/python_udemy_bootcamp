def format_name(f_name, l_name):
    # user의 입력값이 없을 때, 함수 조기 종료
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

# user의 입력값을 input으로 받을 때, user가 아무 입력을 하지 않을 수도 있음
print(format_name(input("What is your first name? "), input("What is your last name? ")))

# input값에 입력이 되지 않을 경우, None으로 출력됨.
# user가 알 수 있도록 return(반환값)에 메시지 "You...inputs."를 작성해줌.
