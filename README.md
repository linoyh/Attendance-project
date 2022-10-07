# Attendance

Attendance is an app for calculate the Attendance amount for the Devops course participants.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
attendance.py <csv_attendance_files_path>
# returns attendance by date
# returns final attendance file with percentages

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## preparation
Table was created in the linoyhdb database with the csv default columns(except the 1st anf last):

use linoyhdb;

CREATE TABLE attendance_csv (id integer not null auto_increment primary key, `meeting start time` timestamp, `meeting end time` timestamp, name varchar(128),  email varchar(128) not null, `join time` timestamp, `leaving time` timestamp, `attendance duration` varchar(128));

jeff user is granted all priviliges on the DB - he is the user making the quaries

.env file with environment variables for the DB connection is included in order of not expose personal info for everyone

The csv files were taken fron the course remote AWS serves via SFTP bt pysftp module
## License
[MIT](https://choosealicense.com/licenses/mit/)obar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)