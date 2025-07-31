# Noel Curiosity 24

Noel Curiosity 24 **was a PsychoPy experiment** created for the thesis titled:  
**"What Keeps Us Coming Back for More: An Experimental Study on How Answer Exposure and Social Cues Modulate Curiosity and Memory in Digital Contexts"**,  
conducted at **Kyushu University, School of Systems Life Science, Cognitive Science Lab**.

This repository contains the archived scripts, configurations, and assets used in the experiment.

## Features
- PsychoPy compatibility for building and running psychological experiments.
- Modular Python code for ease of customization.
- [Optional] Add more features as you develop the project.

## Prerequisites
- **PsychoPy v.2024.2.4** installed on your system.
- Python 3.8 or higher.
- Dependencies listed in `requirements.txt` (if applicable).

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/chasubyeong/noel_curiosity24.git
    ```
2. Navigate to the project directory:
    ```bash
    cd noel_curiosity24
    ```
3. Install dependencies (if applicable):
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Open PsychoPy and load the project file (e.g., `.psyexp` if provided).
2. Run the experiment directly from PsychoPy or execute the Python script:
    ```bash
    python main.py
    ```

## Directory Structure

```
Noel_SocCuriosity.py          # Main Python script to run the experiment logic
README.md                     # Project documentation
bg.png                        # Background image for the experiment interface

fontpack/                     # Package of fonts for the experiment

header_list.xlsx              # Headlines suggested in the 1st phase of the experiment
header_list_original.xlsx     # Previous version of header_list.xlsx

hotfix_tick_post.png          # Jury-rigged patch for display issue on Japanese version, 2nd phase
hotfix_tick_pre.png           # Jury-rigged patch for display issue on Japanese version, 1st phase

image_list.xlsx               # List of post images shown in the 2nd phase

main.psyexp                   # PsychoPy experiment file (used to run the experiment in PsychoPy)

post_list.xlsx                # List of posts (metadata) shown in the 2nd phase
post_list_original.xlsx       # Previous version of post_list.xlsx

posts/                        # Image files of posts

reference_values.txt          # Contains reference values or constants used in the experiment

resources/                    # Directory containing supplementary resources for the experiment (e.g., instructions, configuration files)
```

## Contributing
**This project is no longer accepting contributions.** The experiment has been completed, and the repository remains as an archive for reference purposes only.

## License
This project currently does not have a license. However, it is important to acknowledge that this experiment was built using **PsychoPy**, an open-source application for running behavioral experiments. Please refer to the [PsychoPy license](https://github.com/psychopy/psychopy/blob/release/LICENSE) for details on the usage and distribution of PsychoPy itself.

For any usage permissions related to this repository, please contact the repository owner.

## Contact
For questions or issues, please contact the repository owner.
