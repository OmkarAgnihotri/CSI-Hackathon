import math
from fuzzywuzzy import fuzz

def match_score(text,answer):
    # print(fuzz.token_set_ratio(answer, text))
    return math.ceil(fuzz.token_set_ratio(answer, text) * 6 / 100)