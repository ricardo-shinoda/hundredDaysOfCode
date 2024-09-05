def format_name(f_name, l_name):
    # this is a docstring, must always be on the first idented line inside a function
    """Take a first and last name and format it to
    return the title case version of the name"""
    first_cap = f_name.title()
    last_cap = l_name.title()
    return f'{first_cap} {last_cap}'


answer = format_name(f_name="RICARDO tetsuo", l_name="shinoda")
print(answer)
