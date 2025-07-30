# hackathon_project_2025_bot_detection_submission_times

This is the repository for the Civic Tech DC Hackathon 2025. The problem statement this repository focuses on detecting fraudulent bot comments for rule dockets.

**Contributors Of This Problem Statement**:

- Anshu Sharma (anshu.g.sharma@gmail.com) (https://www.linkedin.com/in/anshugsharma/)
- Dean Eby
- [Kristijan Armeni](https://github.com/kristijanarmeni), https://www.linkedin.com/in/kristijanarmeni
- Stefan Netterfield

Before pip install you may want to create a virtual environment with `python3 -m venv <name of venv>`; to activate, in a terminal run `source <name of venv>/bin/activate`, to deactivate, run `deactivate`.

### Setting the data path variable

Create a `.env` file in the project root and set the `MIRRULATIONS_FOLDER` to point to the location where you downloaded the mirrulations dataset. For example:

```sh
MIRRULATIONS_FOLDER="/users/myusername/data/mirrulations"
```

### Start the marimo notebook
To run after `pip install -r requirements.txt` run `marimo edit notebook.py`.  

Update DATA_PATH and path_template in data.py 

