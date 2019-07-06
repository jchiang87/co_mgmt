CREATE TABLE Deliverables (
       id INTEGER PRIMARY KEY,
       deliverableName TEXT,
       deliverableType TEXT,
       deliveryDate DATE
);

CREATE TABLE Activities (
       id INTEGER PRIMARY KEY,
       activityName TEXT,
       startDate DATE,
       endDate DATE,
       effortLevel REAL
);

CREATE TABLE ActivityDependencies (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       activityId INT,
       deliverableId INT,
       required, INT,
       FOREIGN KEY(activityId) REFERENCES Activities(id),
       FOREIGN KEY(deliverableId) REFERENCES Deliverables(id)
);

CREATE TABLE DeliveryDependencies (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       deliverableId INT,
       activityId INT,
       FOREIGN KEY(deliverableId) REFERENCES Deliverables(id),
       FOREIGN KEY(activityId) REFERENCES Activities(id)
);
