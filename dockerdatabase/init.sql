CREATE TABLE students (
  RegNo INT PRIMARY KEY,
  Name VARCHAR(50),
  Vaccination_Status ENUM('Yes', 'No')
);

INSERT INTO students (RegNo, Name, Vaccination_Status) VALUES 
(1234, 'John Doe', 'Yes'),
(5678, 'Jane Smith', 'No'),
(9012, 'Bob Johnson', 'Yes');

