# 2021 Experiment: Human-Agent Interaction in "Don't Starve Together"

## 1. Overview
This repository contains the source code and datasets used for our research project on human-agent interaction in the cooperative game "Don't Starve Together". Our research emphasizes the importance of understanding cross-cultural language differences and their effects on social cognition during interactions.

## 2. Scholarly Paper
### Effects of Cross-Cultural Language Differences on Social Cognition during Human-Agent Interaction in Cooperative Game Environments

#### 2.1 Abstract
The research delves into the profound impact of cross-cultural language differences on social cognition during interactions between humans and agents in cooperative game settings.

#### 2.2 Key Findings
- Influence on Perception and Behavior
- Varied Interpretations
- Design Considerations

#### 2.3 Recommendations
- Awareness Among Developers
- Cultural Adaptability in Design

#### 2.4 Publication Details
- **Journal:** Computer speech & language Volume: 81 (2023) ISSN: 0885-2308
- **Authors:** Casey C. Bennett, Young-Ho Bae, Jun Hyung Yoon, Yejin Chae, Eunseo Yoon, Seeun Lee, Uijae Ryu, Benjamin Weiss
- **Link:** [ScienceDirect Paper](https://doi.org/10.1016/j.csl.2023.101521.)

## 3. Features
- Automatic Speech Recognition (ASR)
- Text-to-Speech (TTS)
- Game State Parsing
- Decision Tree Parsing

## 4. Versions
- Korean
- English

## 5. Directory Structure
- **2021 Experiment**:
  - **Korean** and **English**: Both versions have the following structure:
    - **Control_condition**: 
      - Planning: OFF
      - Responsiveness: HIGH/MAX (Chattiness = 3)
      - IOR: ON (Repetition Delay / REP_DELAY_AMT = 3)
    - **H2_condition**: 
      - Planning: OFF
      - Responsiveness: LOW (Chattiness = 1.5)
      - IOR: ON (Repetition Delay / REP_DELAY_AMT = 3)
    - **H3_condition**: 
      - Planning: OFF
      - Responsiveness: HIGH/MAX (Chattiness = 3)
      - IOR: OFF (Repetition Delay / REP_DELAY_AMT = 0)
  - **setting**: Contains experiment condition explanations and

## 6. Setup
1. Install dependencies from `requirements.txt`.
2. Set up Microsoft Azure API keys in `config.py`.
3. Run `__main__.py`.

## 7. Note
Ensure removal of API keys and check files for sensitive information before sharing.

## 8. Acknowledgements
This work was supported by a grant from the National Research Foundation of Korea (NRF) (Grant number:2021R1G1A1003801).
