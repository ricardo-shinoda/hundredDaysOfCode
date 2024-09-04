def format_name(f_name, l_name):
    first_cap = f_name.title()
    last_cap = l_name.title()
    return f'{first_cap} {last_cap}'


answer = format_name(f_name="RICARDO tetsuo", l_name="shinoda")
print(answer)
