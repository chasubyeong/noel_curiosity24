# Noel Curiosity 24

**Legacy Code Notice:**  
This experiment was built upon legacy code originally developed in the Cognitive Science Lab, Kyushu University. The current version includes several modifications.

Noel Curiosity 24 **was a PsychoPy experiment** created for the thesis titled:  
**"What Keeps Us Coming Back for More: An Experimental Study on How Answer Exposure and Social Cues Modulate Curiosity and Memory in Digital Contexts"**,  
conducted at **Kyushu University, School of Systems Life Science, Cognitive Science Lab**.

This repository contains the archived scripts, configurations, and assets used in the experiment.

## Features
- **PsychoPy Compatibility**  
  Fully compatible with PsychoPy, enabling seamless design, execution, and data collection for psychological experiments.
- **Joystick Support**  
  Integrated joystick/controller input compatibility, allowing for more interactive and versatile experimental paradigms—ideal for studies requiring precise or alternative response modalities beyond standard keyboard/mouse input.
- **Modular Python Architecture**  
  Experiment scripts and logic are organized in a modular fashion, making it easy to customize, extend, and maintain the code base for different experimental setups or research questions.
- **Customizable Experimental Flow**  
  Easily modify phases, stimuli presentation order, timing parameters, and feedback mechanisms to fit a variety of experimental designs.
- **Stimuli and Resource Management**  
  Centralized handling of images, fonts, and other assets—resources are organized for straightforward access and swapping as needed.
- **Excel-Based Stimuli Lists**  
  Stimuli (e.g., headlines, posts, images) are managed via Excel files, allowing researchers to update or randomize content without modifying code.
- **Configurable Reference Values**  
  Reference values and experiment constants are maintained in dedicated files for easy adjustment and reproducibility.
- **Multi-Phase Task Structure**  
  Supports complex multi-phase experiments (e.g., curiosity induction, memory testing, social cue manipulation), with clear separation of logic and assets for each phase.
- **Hotfixes & Localization Support**  
  Includes assets and patches (e.g., display fixes for Japanese version) to ensure the experiment functions correctly across languages and system configurations.
- **Archival and Reproducibility Focus**  
  Scripts, configurations, and assets are maintained for archival and reproducibility purposes, facilitating future reference or replication.
- **Documentation & Directory Structure**  
  Well-documented project structure for ease of navigation, onboarding, and reference by future researchers or collaborators.

## Prerequisites
- **PsychoPy v.2024.2.4** installed on your system.
- Python 3.8 or higher.


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
