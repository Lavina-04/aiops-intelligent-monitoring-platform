from logs.logger import write_log
import time

request_count = 0
error_count = 0

response_times = []

start_time = time.time()

def track_request(func):

    def wrapper(*args, **kwargs):

        global request_count
        global error_count

        request_count += 1
        write_log(
          "REQUEST",
          "Incoming API request received"
        )

        start = time.time()

        response = func(*args, **kwargs)

        end = time.time()

        latency = round((end - start) * 1000, 2)

        response_times.append(latency)
        
        write_log(
        "METRIC",
        f"Request latency recorded: {latency} ms"
         )

        status_code = 200

        if isinstance(response, tuple):
            status_code = response[1]

        if status_code >= 500:
            error_count += 1
            write_log(
                 "ERROR",
                 f"Server returned status code {status_code}",
                 "CRITICAL"
            )

        print(f"""
        Requests : {request_count}
        Errors   : {error_count}
        Latency  : {latency} ms
        """)

        return response

    wrapper.__name__ = func.__name__

    return wrapper

def get_metrics():

    avg_latency = 0

    if response_times:
        avg_latency = round(sum(response_times) / len(response_times), 2)

    uptime_seconds = int(time.time() - start_time)

    uptime_percentage = 100

    if request_count > 0:
        uptime_percentage = round(
            ((request_count - error_count) / request_count) * 100,
            2
        )

    return {
        "requests": request_count,
        "errors": error_count,
        "avg_latency": avg_latency,
        "uptime": uptime_percentage,
    }