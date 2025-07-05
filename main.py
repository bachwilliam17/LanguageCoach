from csv_to_db import conversion_procedure
from quiz_db import generate_quiz

quiz_db_name = conversion_procedure()
generate_quiz(quiz_db_name)