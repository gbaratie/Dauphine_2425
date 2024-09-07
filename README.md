# TP Dauphine


## Getting Started

### Fork the Project

  Click on the "Fork" button at the top right of the page to create a copy of the repository under your own GitHub account.

### Clone the Repository

After forking the project, clone the repository to your local machine:

1. Open your terminal and navigate to the directory where you want to store the project.
2. Run the following command to clone the repository:
    ```bash
    git clone https://github.com/yourusername/Dauphine_2425.git
    ```

## Installation

Follow these steps to set up the project on your local machine:

### Step 1: Create a Python Virtual Environment

Creating a virtual environment helps to manage dependencies and avoid conflicts with other projects:

```bash
python3 -m venv {name_of_your_venv}
```
Or
```bash
python -m venv {name_of_your_venv}
```

### Step 2: Activate the Virtual Environment

Activating your virtual environment ensures that the dependencies you install will only affect this project:

```bash
source {name_of_your_venv}/bin/activate
```

You should see the name of your environment on the left of your terminal, indicating that it is active.

### Step 3: Install the Required Dependencies

Install the project's dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install all the necessary packages to run the project.

### Step 4: Launch the Frontend

Ensure you are working within your activated Python environment to avoid issues. Launch the frontend of the project using Streamlit:

```bash
streamlit run main.py
```

This command will start the Streamlit server, and a new tab will open in your web browser displaying the application.

---

By following these steps, you will have the project set up and running locally on your machine. Happy coding!


## Special Thanks

A special thanks to William Hoareau for his work on a project that served as the foundation for my initial commit


