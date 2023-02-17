from aiogram.dispatcher.filters.state import StatesGroup, State


class FormFeedback(StatesGroup):
    # feedback = State()  # Will be represented in storage as 'FormFeedback:feedback'
    feedback_text = State()  # Will be represented in storage as 'FormFeedback:feedback_text'


class FormRegistration(StatesGroup):
    # user_id = State()  # Will be represented in storage as 'FormRegistration:user_id'
    fname = State()  # Will be represented in storage as 'FormRegistration:fname'
    lname = State()  # Will be represented in storage as 'FormRegistration:lname'
    email = State()  # Will be represented in storage as 'FormRegistration:email'
    cell_phone = State()  # Will be represented in storage as 'FormRegistration:cell_phone'
    work_phone = State()  # Will be represented in storage as 'FormRegistration:work_phone'


class FormActivation(StatesGroup):
    # user_id = State()  # Will be represented in storage as 'FormRegistration:user_id'
    activation_code = State()  # Will be represented in storage as 'FormRegistration:activation_code'
