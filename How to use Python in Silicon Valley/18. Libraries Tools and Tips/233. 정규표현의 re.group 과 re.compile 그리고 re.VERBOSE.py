import re

s1 = (r'arn:aws:cloudformation:us-east-1:123456789012:stack/'
      r'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')

s2 = (r'arn:aws:cloudformation:us-east-2:123456789012:stack/'
      r'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0111111')

# # 읽기 어려운 버전
# RE_STACK_ID = re.compile(r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+):stack/'
#                          r'(?P<stack_name>[\w-]+)/[\w\d-]+')


# 읽기 쉬운 버전
RE_STACK_ID = re.compile(r"""
    arn:aws:cloudformation:
    (?P<region>[\w-]+):      # region
    (?P<account_id>[\d]+)    # account_id
    :stack/
    (?P<stack_name>[\w-]+)   # stack name
    /[\w\d-]+
    """, re.VERBOSE)

for s in [s1, s2]:
    m = RE_STACK_ID.match(s)
    if m:
        print(m)  # <re.Match object; span=(0, 123), match='arn:aws:cloudformation:us-east-1:123456789012:sta>
        print(m.group('region'))
        print(m.group('account_id'))
        print(m.group('stack_name'))
