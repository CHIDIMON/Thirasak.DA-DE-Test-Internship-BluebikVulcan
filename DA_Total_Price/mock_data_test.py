#mock_data_test.py
import sqlite3
import pandas as pd
import os

#connect to in-memory SQLite database
conn = sqlite3.connect(':memory:')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def run_test():
    try:
        database_path = os.path.join(BASE_DIR, 'database.sql')
        solution_path = os.path.join(BASE_DIR, 'solution.sql')
        #setup database from database.sql
        with open(database_path, 'r', encoding='utf-8') as f:
            setup_sql = f.read()
        
        #use executescript to run multiple SQL statements
        conn.executescript(setup_sql)
        print("Database Setup: Success (Loaded from database.sql)")

        #pull SQL query from solution.sql
        with open(solution_path, 'r', encoding='utf-8') as f:
            original_sql = f.read()
 
        #change SQL syntax from PostgreSQL to SQLite extract to strftime
        test_sql = original_sql.replace('EXTRACT(YEAR FROM t."date")', "STRFTIME('%Y', t.date)")
        test_sql = test_sql.replace('EXTRACT(YEAR FROM "date")', "STRFTIME('%Y', date)")
        test_sql = test_sql.replace('"Transaction"', '[Transaction]')

        #run the modified SQL query
        result = pd.read_sql_query(test_sql, conn)
        
        print("\nSQL Query Result:")
        print(result)

        #check if the result matches expected value
        actual_val = result['total_price'][0]
        if actual_val == 3600:
            print(f"\nValidation Passed: Total price is {actual_val}")
        else:
            print(f"\nValidation Failed: Expected 3600 but got {actual_val}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_test()