import sqlite3


class DatabaseHandler:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        self.prepareDB()

    def prepareDB(self):
        """
            Create important table if doesnt exists
        """
        try:
            self.cur.execute(
                "CREATE TABLE User(Phone TEXT, Name TEXT, Age INTEGER, Gender TEXT)")
        except sqlite3.OperationalError:
            # Table already exists, so skip
            pass

    def add_users(self, user_dictionary):
        """
            Push data from dictionary if the same user is not alerady in the dbms
        """
        SUCCESSFUL = True
        FAILED = False
        try:
            self.cur.execute("SELECT Phone from User where Phone=:number", {
                             "number": user_dictionary["Phone"]})
            if self.cur.fetchone() == None:
                self.cur.execute("INSERT INTO User values(?,?,?,?)", (
                    user_dictionary["Phone"], user_dictionary["Name"], user_dictionary["Age"], user_dictionary["Gender"]))
                self.commitDB()
                return SUCCESSFUL
            else:
                return FAILED
        except sqlite3.OperationalError:
            print("Error")
            return FAILED

    def get_user_data(self, phone):
        """
            Returns user data as a list
        """
        
    def commitDB(self):
        """
            Confirm transaction of the current dbms
        """
        self.conn.commit()

    def closeDB(self):
        """

        """
        self.conn.close()
