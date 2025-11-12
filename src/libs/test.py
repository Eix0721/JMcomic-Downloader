from InquirerPy import prompt
# 注意：我们不再需要导入 NumberValidator

# 1. 定义验证函数
def validate_port_range(text: str):
    """同时验证输入是否为数字和是否在有效端口范围内 (1024-65535)"""
    try:
        port = int(text)
    except ValueError:
        return "❌ 请输入一个有效的数字。"

    if 1024 <= port <= 65535:
        return True  # 验证成功
    else:
        return "❌ 端口号必须在 1024 到 65535 之间。"

try:
    questions = [
        {
            "type": "list",
            "message": "请选择一个你喜欢的前端框架:",
            "choices": ["React", "Vue", "Angular", "Svelte"],
            "default": "React",
            "name": "framework",
        },
        {
            "type": "text",
            "message": "请输入应用运行的端口号:",
            
            # ⬇️ 关键修正：使用自定义函数 ⬇️
            "validate": validate_port_range,
            
            # 因为验证函数已经返回了错误信息，所以 "invalid_message" 现在是可选的。
            "name": "port",
        }
    ]

    results = prompt(questions=questions)
    print(f"\n太好了！你选择了 {results['framework']} 框架，并将在 {results['port']} 端口运行它。")

except KeyboardInterrupt:
    print("\n操作已取消。")