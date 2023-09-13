# 2021 Experiment: Human-Agent Interaction in "Don't Starve Together"

## Overview
This repository contains the source code and datasets used for our research project on human-agent interaction in the cooperative game "Don't Starve Together". Our research emphasizes the importance of understanding cross-cultural language differences and their effects on social cognition during interactions.

## Scholarly Paper: Effects of Cross-Cultural Language Differences on Social Cognition during Human-Agent Interaction in Cooperative Game Environments

### Abstract
The research delves into the profound impact of cross-cultural language differences on social cognition during interactions between humans and agents in cooperative game settings. This study underscores the paramount importance of understanding these effects to enhance the design of human-agent interaction systems, especially in multicultural contexts.

### Key Findings
1. **Influence on Perception and Behavior:** Cross-cultural language differences significantly sway the perception and behavior of players in cooperative game environments.
2. **Varied Interpretations:** Players hailing from diverse cultural backgrounds might interpret and respond to agent behaviors in different ways, leading to a spectrum of game outcomes.
3. **Design Considerations:** The design of agents should be mindful of cultural nuances to ensure effective communication and cooperation among diverse user groups.

### Recommendations
- **Awareness Among Developers:** Developers should be cognizant of cultural differences and the potential ramifications they might have on human-agent interactions.
- **Cultural Adaptability in Design:** Incorporating a sense of cultural adaptability in agent design can pave the way for more inclusive and effective gaming experiences.

### Publication Details
- **Journal:** [Computer speech & language Volume: 81 (2023) ISSN: 0885-2308]
- **Authors:** [Casey C. Bennett, Young-Ho Bae, Jun Hyung Yoon, Yejin Chae, Eunseo Yoon, Seeun Lee, Uijae Ryu, Benjamin Weiss]
- **Link:** [ScienceDirect Paper](https://doi.org/10.1016/j.csl.2023.101521.)

## Features

- **Automatic Speech Recognition (ASR)**: Recognizes player's speech and responds based on keyword files.
- **Text-to-Speech (TTS)**: Synthesizes utterances using Microsoft Azure TTS SDK.
- **Game State Parsing**: Reads and processes game states from CSV files, updating the state based on player actions and game events.
- **Decision Tree Parsing**: Uses a decision tree structure to determine appropriate responses based on the game state.

## Versions

The project is available in two versions:
1. **Korean**: Contains scripts with Korean annotations and is tailored for Korean gameplay interactions.
2. **English**: Contains scripts with English annotations and is tailored for English gameplay interactions.

## Directory Structure

- **2021 Experiment**:
  - **Korean**: Contains the Korean version of the project.
    - **Control_condition**: Houses the main scripts for the Korean version.
      - **Working_code**: Core scripts for ASR, TTS, game state parsing, and decision tree parsing.
  - **English**: Contains the English version of the project (structure similar to the Korean version).

## Setup

1. Ensure you have the required dependencies installed. Check the `requirements.txt` file for a list.
2. Set up the necessary API keys for Microsoft Azure in the `config.py` file.
3. Run the `__main__.py` script to start the speech system.

## Note

Before uploading or sharing this repository, ensure you remove or replace any API keys and check any files (like 'test.csv') that the scripts interact with for personal or sensitive information.

## Acknowledgements

This work was supported by a grant from the National Research Foundation of Korea (NRF) (Grant number:2021R1G1A1003801).
