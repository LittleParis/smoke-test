import requests
import re
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
}

# Step 1: Login
login_url = 'https://login.demo.ehi.com.cn/Account/Login?returnUrl=https%3A%2F%2Fdjeoadmin.demo.ehi.com.cn%2F'
resp1 = session.get(login_url, headers=headers, verify=False)
token_match = re.search(r'__RequestVerificationToken[^>]*value="([^"]+)"', resp1.text)
if not token_match:
    token_match = re.search(r'name="__RequestVerificationToken"[^>]*value="([^"]+)"', resp1.text)
csrf_token = token_match.group(1) if token_match else ''

data = {
    'ReturnUrl': 'https://djeoadmin.demo.ehi.com.cn/',
    'Client': '', 'Ticket': '', 'Randstr': '',
    'username': '33418',
    'plainPassword': 'Demo:_password1',
    'Password': 'Demo:_password1',
    '__RequestVerificationToken': csrf_token
}
headers['Referer'] = login_url
headers['Origin'] = 'https://login.demo.ehi.com.cn'
resp2 = session.post(login_url, data=data, headers=headers, allow_redirects=False, verify=False)
print(f'Login: {resp2.status_code}')

# Step 2: Call GetComplaints - positive test
api_url = 'https://aftersaleapi.demo.ehi.com.cn/api/Complaint/GetComplaints'
params = {
    'Platform': 'MyEhi',
    'MaxResultCount': 5,
    'SkipCount': 0
}
resp3 = session.get(api_url, params=params, verify=False)
result = resp3.json()
print(f'\n=== Positive Test ===')
print(f'Status: {resp3.status_code}')
print(f'isSuccess: {result.get("isSuccess")}')
print(f'errorCode: {result.get("errorCode")}')
print(f'message: {result.get("message")}')
if result.get("result") and result["result"].get("items"):
    print(f'TotalCount: {result["result"].get("totalCount", "N/A")}')
    print(f'Items count: {len(result["result"]["items"])}')
    print(f'First item keys: {list(result["result"]["items"][0].keys())[:10]}')
else:
    print(f'result: {json.dumps(result.get("result"), ensure_ascii=False)[:200]}')

# Step 3: Boundary tests
print(f'\n=== Boundary Tests ===')

# Test: missing Platform (required)
resp4 = session.get(api_url, params={'MaxResultCount': 5}, verify=False)
r4 = resp4.json()
print(f'No Platform: isSuccess={r4.get("isSuccess")} errorCode={r4.get("errorCode")} message={r4.get("message","")[:80]}')

# Test: invalid BizType
resp5 = session.get(api_url, params={'Platform': 'MyEhi', 'BizType': 999}, verify=False)
r5 = resp5.json()
print(f'BizType=999: isSuccess={r5.get("isSuccess")} errorCode={r5.get("errorCode")} message={r5.get("message","")[:80]}')

# Test: invalid ComplaintState
resp6 = session.get(api_url, params={'Platform': 'MyEhi', 'ComplaintState': 999}, verify=False)
r6 = resp6.json()
print(f'ComplaintState=999: isSuccess={r6.get("isSuccess")} errorCode={r6.get("errorCode")} message={r6.get("message","")[:80]}')

# Test: empty OrderNo
resp7 = session.get(api_url, params={'Platform': 'MyEhi', 'OrderNo': ''}, verify=False)
r7 = resp7.json()
print(f'OrderNo="": isSuccess={r7.get("isSuccess")} errorCode={r7.get("errorCode")}')

# Test: long string in CarNo
resp8 = session.get(api_url, params={'Platform': 'MyEhi', 'CarNo': 'A'*300}, verify=False)
r8 = resp8.json()
print(f'CarNo=300chars: isSuccess={r8.get("isSuccess")} errorCode={r8.get("errorCode")}')
