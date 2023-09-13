# 2021 Experiment: Human-Agent Interaction in "Don't Starve Together"

This repository contains the code for a speech system designed to facilitate human-agent interactions during gameplay in "Don't Starve Together". The project aims to provide speech capabilities to a character in the game, enabling dynamic interactions based on the game's state and player's actions.

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
We would like to thank our other research collaborators who contributed to this work.
