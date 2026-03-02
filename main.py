from pyscript import document, window, display

# --- Page 1: Account Creation Logic ---
def username_verification():
    username = document.getElementById('username').value
    username_length = len(username)
    if username_length < 7:
        display(f'Username too short. Add {7 - username_length} more chars.', target='output')
        return False
    return True

def password_verification():
    password = document.getElementById('password').value
    if len(password) < 10:
        display(f'Password too short.', target='output')
        return False
    # Checks for at least one number and one letter
    if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        display(f'Password needs letters and numbers.', target='output')
        return False
    return True

def account_creation(e):
    document.getElementById('output').innerHTML = ''
    if username_verification() and password_verification():
        # Redirects to the second page
        window.location.href = "intrams.html"
    else:
        # Fallback message if logic fails
        pass

# --- Page 2: Intrams Checker Logic ---
def intrams_checker(e):
    # Clear previous output
    document.getElementById('output').innerHTML = ''
    
    try:
        reg_element = document.querySelector('input[name="registration"]:checked')
        clr_element = document.querySelector('input[name="clearance"]:checked')
        
        if not reg_element or not clr_element:
            display("Please answer all questions.", target='output')
            return

        registration = reg_element.value
        clearance = clr_element.value
        grade_section = document.getElementById('grade_section').value

        if registration != 'registered':
            display('Not eligible: Register with PE teacher.', target='output')
        elif clearance != 'cleared':
            display('Not eligible: Medical clearance required.', target='output')
        elif grade_section in ['7emerald', '10emerald']:
            display('Congratulations! You are part of the Green Hornets', target='output')
        elif grade_section in ['7ruby', '10ruby']:
            display('Congratulations! You are part of the Yellow Tigers', target='output')
        elif grade_section in ['8emerald', '9emerald']:
            display('Congratulations! You are part of the Red Bulldogs', target='output')
        elif grade_section in ['8ruby', '9ruby']:
            display('Congratulations! You are part of the Blue Bears', target='output')
    except Exception as err:
        # Handles cases where script runs on Page 1 but looks for Page 2 elements
        pass