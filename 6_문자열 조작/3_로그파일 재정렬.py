# https://leetcode.com/problems/reorder-data-in-log-files/

import collections
import headpq
import functools
import itertools
import re   
import sys
import math
import bisect
from typing import * 

## 내가 푼 풀이
# isdigit(), isalpha(), sort() : 람다식으로 key를 두 개씩 설정할 수 있다.
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = [log for log in logs if log.split(' ')[1].isdigit()]
        letter_logs = [log for log in logs if log.split(' ')[1].isalpha()]
        letter_logs.sort(key=lambda x: (x.split(' ')[1:], x.split(' '[0])))
        return letter_logs + digit_logs