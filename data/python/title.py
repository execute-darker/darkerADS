import datetime
import pytz
import glob

# 获取当前时间并转换为北京时间
utc_time = datetime.datetime.now(pytz.timezone('UTC'))
beijing_time = utc_time.astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')

# 获取文件列表
file_list = glob.glob('./data/rules/*.txt')

# 遍历文件列表
for file_path in file_list:
    # 打开文件并读取内容
    with open(file_path, 'r') as file:
        content = file.read()

    # 计算文件的行数
    line_count = content.count('\n') + 1

    # 在文件顶部插入内容
    new_content = f"[Adblock Plus 2.0]\n" \
                  f"! Title: darkerADS\n" \
                  f"! Homepage: https://github.com/execute-darker/darkerADS\n" \
                  f"! Expires: 12 Hours\n" \
                  f"! Version: {beijing_time} (UTC+8)\n" \
                  f"! Description: Ad-blocking rules for AdGuard, combining high-quality upstream rules with deduplication and organized sorting.\n" \
                  f"! Total count: {line_count}\n" \
                  f"{content}"

    # 将更新后的内容写入文件
    with open(file_path, 'w') as file:
        file.write(new_content)
