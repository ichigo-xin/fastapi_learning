import time


def get_time(func):
    """输出方法执行时间."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time_seconds = end_time - start_time
        execution_time_minutes = execution_time_seconds / 60  # 将秒转换为分钟
        end_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
        print(f"{func.__name__} 执行时间: {execution_time_minutes:.2f} 分钟")
        print(f"{func.__name__} 执行结束时间: {end_time_str}")
        return result
    return wrapper

@get_time
def test():
    time.sleep(2)  # 模拟运行2s

test()  # 耗时：2.000000238418579秒
