# -*- coding:utf-8 -*-
'''
All kind of settings (MS Azure API keys, setting the log file, taking *.txt files)
Setting global variables, read data files (*_utterances.txt, *_keywords.txt, settings.txt)
'''
################### load packages
# generaL behavior
import os, json
import pandas as pd
from collections import defaultdict

# for logging:
import warnings, logging

#for TTS
import azure.cognitiveservices.speech as speechsdk

################ set API keys
# MS Auzre / used at 'tts.py' and 'asr.py' files
speech_key, service_region = "YOUR_SPEECH_KEY", "YOUR_SERVICE_REGION"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioConfig(device_name="YOUR_DEVICE_NAME") # CABLE-B Output
################ set API keys end
################### load packages end

################ set logging
# Ignoring the warnings
warnings.filterwarnings(action='ignore')

# Making the 'logs' folder if the folder does not exist
if not os.path.exists("./logs/"):
    os.mkdir("./logs/")

# Set up log file written format ex) 01:39:09
logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(name)s: %(message)s",
    level=logging.DEBUG,
    filename='./logs/dm.log',
    # encoding='utf-8',
    datefmt="%H:%M:%S",
    #stream=sys.stderr,
)

logging.getLogger("chardet.charsetprober").disabled = True
################ set logging end

################ set global variables and constants

################# PLACEHOLDERS (All used at 'parse_tree.py' file)
### Set up repetition delay count
REP_DELAY_AMT = 3 # prevent too much talk
LOCAL_REP_DELAY_AMT = REP_DELAY_AMT
### repetition delay count ends

### Other placeholders
HUNGRY = 50
STARVING = 30
INJURED = 50
DYING = 30
SANITY_SAFE = 80
SANITY_DANGER = 30
CHATTINESS = 1.5 # talkative or not
### Other placeholders end
################## PLACEHOLDERS END

################## Define dictionaries, lists (used at 'state_changed.py file or 'parse_tree.py' file)
### For repetition delay
# Set up state_list that are used at the 'state_changed.py' file
state_list = ['Phase', 'Hunger_AVATAR', 'Health_AVATAR', 'Sanity_AVATAR', 'Curr_Active_Item_AVATAR',
              'Curr_Equip_Hands_AVATAR', 'Attack_Target_AVATAR',  'Defense_Target_AVATAR', 'Food_AVATAR',
              'Tool_AVATAR', 'Lights_AVATAR', 'Is_Light_AVATAR', 'Is_Monster_AVATAR']

# Concatenate above 'state_list' and 'REP_DELAY_AMT' as a dictionary
rep_delay_states = dict.fromkeys(state_list, REP_DELAY_AMT)
### repetition delay ends

data = dict()
initial_state = dict()
status = defaultdict(list)
################## Define dictionaries, lists end

# read settings from 'settings.txt' file
with open('settings.txt', 'r', encoding='utf-8') as settingsfile:
    exec(settingsfile.read())

# read list of utterances from the 'data/*_utterances.txt' file
with open('data/' + THIS_LANGUAGE + '_utterances.txt', 'r', encoding='utf-8') as utterancefile:
    utt_data = utterancefile.read()
    RESPONSE_UTTS = json.loads(utt_data, strict=False)

# read list of keywords from the 'data/*_keywords.txt' file
with open('data/' + THIS_LANGUAGE + '_keywords.txt', 'r', encoding='utf-8') as keywordfile:
    asrkeys_data = keywordfile.read()
    ASR_KEYS_UTTS = json.loads(asrkeys_data, strict=False)

# read list of utterances priority median value from the 'data/*_priority_utterances.xlsx' file as dictionary type
# Read the Excel file under data folder. Currently, use 'category' and 'median' columns for Self-generated utterances
priority_utterance = pd.read_excel('data/' + THIS_LANGUAGE + '_priority_utterances.xlsx', usecols = ['category', 'median'])
# Making 'category' and 'median' dataframe type to list type
category_list = priority_utterance['category'].values.tolist()
median_list = priority_utterance['median'].values.tolist()
# Concatenate both to dictionary
priority_utterance_score = dict(zip(category_list,median_list))

# read list of keyword priority median value from the 'data/*_priority_keywords.xlsx' file as dictionary type
# Read the Excel file under data folder. Currently, use the 'median' column for keywords
priority_keyword = pd.read_excel('data/' + THIS_LANGUAGE + '_priority_keywords.xlsx', usecols = ['median'])
# Making 'median' dataframe type to list type
value_list = priority_keyword.values.tolist()
# Making 'median' list-list type to list (ex. [[3.0]] -> [3.0])
value_list = sum(value_list, [])
# Concatenate 'keywords' and 'median' to dictionary
priority_keyword_score = dict(zip(ASR_KEYS_UTTS.keys(),value_list))

INTERFACE_FILEFOLDER = INTERFACE_FOLDER + INTERFACE_FILE
################ set global variables and constants end
