# SleepTracker

SleepTracker is a toolbox of numerous commands for developing sleep tracking features for the PineTime smartwatch.

## Install

1. **Creation of the virtual environment:**
	- Choose a directory for your project and open a terminal in that directory.
    - Run the following command to create a virtual environment (replace `my_env` with the name you want to give to your environment):
     ```bash
     python -m venv my_env
     ```

2. **Enabling the virtual environment:**
   - On Linux/UNIX:
     ```bash
     source my_env/bin/activate
     ```

3. **Installing dependencies:**
	- With the virtual environment enabled, use pip to install your project's dependencies:
     ```bash
     pip install -r requirements.txt
     ```

4. **Disabling the virtual environment:**
   - When you have finished working on your project, deactivate the virtual environment:
     ```bash
     deactivate
     ```

## Use

| Command               | Description                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------------|
| `help`                | Display the list of available commands.                                                                          |
| `connect`             | Connect with pinetime then collect the data from your watch in the data folder.                                  |
| `analysis`            | Generate a graph of the backup you select.                                                                       |
| `profile`             | Allows you to personalize the analysis according to your age and any pathology having consequences on your sleep.|