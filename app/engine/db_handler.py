"""
This module receives data from the AppMonitors and stores it
in the database.
"""

from os import path
from datetime import datetime
from app.db.database import Database

class DBHandler:
    def __init__(self):
        """
        Handles all database operations. This object holds
        exclusive access to the database.
        """
        self.db = Database()


    def create_activity(self, name: str, apps: list) -> bool:
        """
        Stores a new activity in the database and its
        app associations.
        
        :param name: Name of the activity
        :type name: str
        :param apps: List of apps to be associated with the activity
        :type apps: list
        """
        # Query to create the activity
        query1 = '''
            INSERT INTO activities (name)
            VALUES (LOWER(?))
            RETURNING id;
        '''

        # Query to associate the apps to the activity
        query2 = '''
            INSERT INTO apps (activity_id, name)
            VALUES (?, LOWER(?));
        '''

        try:
            self.db.cursor.execute(query1, [name.lower()])
            id = self.db.cursor.fetchone()[0]
            self.db.cursor.executemany(query2, [[id, app_name.lower()] for app_name in apps])
            self.db.conn.commit()
            return True
        except Exception as e:
            self.db.conn.rollback()
            msg = "Error creating an activity"
            self.error_logging(msg, e)
            return False


    def get_activities(self) -> list[tuple[int, str]]:
        """
        Fetches all of the registered activites.

        :return: List of tuples with the activity IDs and names
        :rtype: list[tuple[int, str]]
        """

        query = '''
            SELECT id, name FROM activities;
        '''

        try:
            self.db.cursor.execute(query)
            results = self.db.cursor.fetchall()
            return results
        except Exception as e:
            msg = "Error fetching activities"
            self.error_logging(msg, e)
            return None


    def remove_activity(self, id: int) -> bool:
        """
        Removes the activity with the given ID.

        :param id: Activity ID
        :type id: int
        """

        queries = [
            'DELETE FROM focus WHERE id = ?;',
            'DELETE FROM apps WHERE id = ?;',
            'DELETE FROM activities WHERE id = ?;'
        ]

        try:
            self.db.cursor.executemany(queries, [[id] * 3])
            self.db.conn.commit()
            return True
        except Exception as e:
            self.db.conn.rollback()
            msg = "Error removing activity"
            self.error_logging(msg, e)
            return False


    def add_app(self, activity_id: int, name: str) -> bool:
        """
        Associates an app with an already existing activity.
        
        :param activity_id: ID of the activity
        :type activity_id: int
        :param name: Name of the app
        :type name: str
        """

        query = '''
            INSERT INTO apps (activity_id, name)
            VALUES (?, ?);
        '''

        try:
            self.db.cursor.execute(query, [activity_id, name.lower()])
            self.db.conn.commit()
            return True
        except Exception as e:
            self.db.conn.rollback()
            msg = "Error associating an app with an activity"
            self.error_logging(msg, e)
            return False


    def get_activity_id(self, app_name: str) -> int:
        """
        Returns the ID of the activity associated with a certain app.
        
        :param app_name: Name of the app
        :type app_name: str
        :return: ID of the associated activity or -1 if the app isn't
                associated with any activity
        :rtype: int
        """

        query = '''
            SELECT activity_id
            FROM apps
            WHERE name = ?;
        '''

        try:
            self.db.cursor.execute(query, [app_name.lower()])
            id = self.db.cursor.fetchone()
            if id is None:
                return -1
            return id[0]
        except Exception as e:
            msg = "Error fetching activity ID"
            self.error_logging(msg, e)
            return False


    def get_apps(self, activity_id: int) -> list[tuple[int, str]]:
        """
        Fetches the list of apps associated with a certain activity.
        
        :param activity_id: ID of the activity
        :type activity_id: int
        :return: List of apps associated with the activity
        :rtype: list[tuple[int, str]]
        """

        query = '''
            SELECT activity_id, name
            FROM apps
            WHERE activity_id = ?;
        '''

        try:
            self.db.cursor.execute(query, [activity_id])
            results = self.db.cursor.fetchall()
            return results
        except Exception as e:
            msg = "Error fetching apps"
            self.error_logging(msg, e)
            return None


    def remove_app(self, activity_id:int, app_name: str) -> bool:
        """
        Deletes the association between an app and an activity.
        
        :param activity_id: ID of the activity the app is associated with
        :type activity_id: int
        :param app_id: Name of the app to be removed
        :type app_id: str
        """
        
        query = '''
            DELETE FROM apps
            WHERE activity_id = ?
            AND app_name = ?;
        '''

        try:
            self.db.cursor.execute(query, [activity_id, app_name.lower()])
            self.db.conn.commit()
        except Exception as e:
            self.db.conn.rollback()
            msg = "Error removing an app association"
            self.error_logging(msg, e)
            return False


    def register_focus(self, activity_id: int, focus_time: int) -> bool:
        """
        Registers a user's focus period for a certain activity.
        
        :param activity_id: ID of the activity
        :type activity_id: int
        :param focus_time: Duration of the activity period in seconds
        :type focus_time: int
        """

        query = '''
            INSERT INTO focus (activity_id, focus_time, reg_date)
            VALUES (?, ?, DATE());
        '''

        try:
            self.db.cursor.execute(query, [activity_id, focus_time])
            self.db.conn.commit()
            return True
        except Exception as e:
            self.db.conn.rollback()
            msg = "Error registering focus"
            self.error_logging(msg, e)
            return False


    def register_focus_loss(self) -> bool:
        """
        Registers a user's focus loss in the database.
        """

        query = '''
            INSERT INTO focus_loss (reg_time, reg_date)
            VALUES (TIME(), DATE());
        '''

        try:
            self.db.cursor.execute(query)
            self.db.conn.commit()
            return True
        except Exception as e:
            self.db.conn.rollback()
            msg = "Error registering focus loss"
            self.error_logging(msg, e)
            return False


    def error_logging(self, msg: str, e: Exception):
        """
        Log an error in the database handling to the respective
        log file.
        
        :param msg: Error message
        :type msg: str
        :param e: Caught exception
        :type e: Exception
        """
        log_path = path.join(path.dirname(__file__), '..', '..', 'errors.log')
        reg_time = datetime.now().strftime("%H:%M:%S")
        reg_date = datetime.now().strftime("%d/%m/%Y")
        with open(log_path, "a") as f:
            msg = f'[{reg_date} - {reg_time}] {msg} - {e}\n'
            f.write(msg)