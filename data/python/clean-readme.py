import subprocess
import datetime
import pytz

# 提取规则计数
num_adblock = subprocess.getoutput("sed -n 's/^! Total count: //p' ./data/rules/adblock.txt")

# 获取当前时间并转换为北京时间
time = datetime.datetime.now(pytz.timezone('UTC'))
beijing_time = time.astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')

# 用提取的规则计数和当前时间更新README.md
subprocess.run(f"sed -i 's/^更新时间:.*/更新时间: {beijing_time} （北京时间） /g' README.md", shell=True)
subprocess.run(f"sed -i 's/^拦截规则数量:.*/拦截规则数量: {num_adblock} /g' README.md", shell=True)

subprocess.run(f"sed -i 's/^更新日時:.*/更新日時: {beijing_time} (UTC+8) /g' README-JP.md", shell=True)
subprocess.run(f"sed -i 's/^ブロックルール数:.*/ブロックルール数: {num_adblock} /g' README-JP.md", shell=True)

subprocess.run(f"sed -i 's/^Last updated:.*/Last updated: {beijing_time} (UTC+8) /g' README-EN.md", shell=True)
subprocess.run(f"sed -i 's/^Adblock rule count:.*/Adblock rule count: {num_adblock} /g' README-EN.md", shell=True)

print("已成功更新README.md中的规则计数和时间")
