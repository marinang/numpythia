from numpythia import generate
from numpythia.testcmnd import get_cmnd

for event in generate(get_cmnd('w.cmnd'), events=2):
    print(event)