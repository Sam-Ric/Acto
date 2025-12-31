/*
    Activities
*/
CREATE TABLE IF NOT EXISTS activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

/*
    Apps per activity
*/
CREATE TABLE IF NOT EXISTS apps (
    name TEXT UNIQUE NOT NULL,
    activity_id INTEGER NOT NULL,
    FOREIGN KEY (activity_id) REFERENCES activities(id),
    PRIMARY KEY (activity_id, name)
);

/*
    Focused time per activity
    
    Each entry stores a segment of focus for a certain
    activity, which allows for later visualization and 
    statistical analysis.
*/
CREATE TABLE IF NOT EXISTS focus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity_id INTEGER NOT NULL,
    focus_time INTEGER NOT NULL DEFAULT 0,
    reg_date DATE NOT NULL,
    FOREIGN KEY (activity_id) REFERENCES activities(id)
);

/*
    Logging of user's loss of focus
*/
CREATE TABLE IF NOT EXISTS focus_loss (
    reg_time TIME NOT NULL,
    reg_date DATE NOT NULL,
    PRIMARY KEY (reg_time, reg_date)
);
