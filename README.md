`ronyRobot` is a Python robot simulator application that provides two methods for controlling a toy robot's movements on a tabletop: direct user input through a user interface and processing commands from a file.

## Table of Contents
- [Features](#Features)
- [Installation](#installation)
- [How does it work ](#How-does-it-work)
- [Testing](#testing)
- [Linting and Formatting](#linting-and-formatting)
- [Contributing](#Contributing-(optional))
- [License](#license)

## Features

- Direct user input for manual command execution.
- Processing commands from a file.
- Command validation for error-free operation.


## Installation

Before you can run the ronyRobot application, make sure you have the following dependencies installed:

To install the project dependencies, run the following command:

```bash
pip install -r requirements.txt
```

This will install all the required packages as specified in the `requirements.txt` file.

## How does it work 

```bash
 python advanced/uiRobot.py --help
 Usage: uiRobot.py [OPTIONS]

  _summary_

  Args:     table_size (int, optional): _description_. Defaults to 5.     file
  (_type_, optional): _description_. Defaults to None.

Options:
  --table-size INTEGER  Size of the table (default: 5)
  --file FILENAME       Process commands from a file
  --help                Show this message and exit.
  
command examples:

python advanced/uiRobot.py   

python advanced/uiRobot.py --file data/command.txt 

data folder and its default command file: command.txt
```
### User Interface

1. **Enter Commands Directly**: Allows you to interact with the robot by entering commands directly through the console.

2. **Process Commands from a File**: Enables you to execute a sequence of commands from a file. 

3. **Exit**: Exits the application.

### User Input

When you choose to enter commands directly, the application presents you with a user-friendly interface. You can input commands as follows:

- `PLACE X,Y,F`: Place the robot on the tabletop with the specified coordinates and facing direction (e.g., `PLACE 0,0,NORTH`).

- `MOVE`: Move the robot one unit forward in the current direction.

- `LEFT`: Rotate the robot 90 degrees to the left.

- `RIGHT`: Rotate the robot 90 degrees to the right.

- `REPORT`: Retrieve and display the robot's current position and facing direction.

- `QUIT`: Exit the application.

### Processing Commands from a File

If you choose to process commands from a file, you can provide the path to the command file. The application will execute the commands sequentially, and you will see the results in the console. If the specified file does not exist, you will be prompted to enter a valid file path.

### Command Validation

The application performs command validation to ensure the commands entered are correct and adhere to the specified format. If an invalid command is detected, you will receive a prompt to enter a valid one.

## Testing

To run unit tests and end-to-end test, use the following command:

```bash
Python -m unittest advanced/test-ui-robot.py 
or 
coverage run -m unittest advanced/test-ui-robot.py

coverage report

an example for end to end test delivered in the source file of advanced/test-ui-robot.py

def test_handle_commands(self):
        self.robot.place(0, 0, "NORTH")  # Place the robot first
        command = "MOVE\nREPORT"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            commands = command.split("\n")
            for command in commands:
               handle_commands(self.robot, command)       
        self.assertEqual(self.robot.report(), "0,1,NORTH")
        self.assertEqual(mock_stdout.getvalue(), "0,1,NORTH\n")

```
## Linting and Formatting

To check your code for linting issues, use the following command:

```bash
pylint advanced/uiRobot.py
```

To format your code with autopep8

```bash
autopep8 --in-place advanced/uiRobot.py 

```
It is recommended to directly use plugins for VScode IDE to fix the issues/errors to follow pylint guide  

## Contributing (optional)

Contributions to the ronyRobot project are welcome! If you want to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Create a pull request.

Please make sure to write clear and descriptive commit messages.


Note: there is another python code for this applications in the folder basic for old Python version

basic/main.py and toy_robot.py and test file of test_toy_robot.py



## License

This project is licensed under the [ISC License](LICENSE).

---

For more details on how to use the  application, please visit the [project repository](https://github.com/rogeraubi/robot#readme).

