from pyscript import document


def to_int_safe(el_id):
    v = document.getElementById(el_id).value
    try:
        return int(float(v))
    except Exception:
        return 0


def Calculate(e=None):
    fname = document.getElementById("Fname").value or ""
    lname = document.getElementById("Lname").value or ""


    science = to_int_safe("science")
    math = to_int_safe("Math")
    english = to_int_safe("English")
    ict = to_int_safe("ICT")
    fil = to_int_safe("Filipino")
    peh = to_int_safe("PEH")


    total = science + math + english + ict + fil + peh
    average = round(total / 6, 2)


    # update page elements
    document.getElementById("name").innerText = f"Name: {fname} {lname}"
    grades_text = (
        f"Science: {science}\n"
        f"Math: {math}\n"
        f"English: {english}\n"
        f"ICT: {ict}\n"
        f"Filipino: {fil}\n"
        f"PEH: {peh}\n"
        f"Total: {total}"
    )
    document.getElementById("grades").element.innerText = grades_text
    document.getElementById("average").innerText = f"Your general weighted average is {average}"
