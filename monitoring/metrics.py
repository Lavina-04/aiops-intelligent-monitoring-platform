from prometheus_client import Counter, Histogram
from functools import wraps
import time

# ----------------------------
# PROMETHEUS METRICS
# ----------------------------

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total App Requests"
)

ERROR_COUNT = Counter(
    "app_errors_total",
    "Total App Errors"
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request Latency"
)

# ----------------------------
# LOCAL METRICS STORAGE
# ----------------------------

request_count = 0
error_count = 0
response_times = []


# ----------------------------
# REQUEST TRACKER
# ----------------------------

def track_request(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        global request_count
        global error_count

        start = time.time()

        request_count += 1
        REQUEST_COUNT.inc()

        response = func(*args, **kwargs)

        latency = (time.time() - start) * 1000

        response_times.append(latency)

        REQUEST_LATENCY.observe(latency / 1000)

        if isinstance(response, tuple):

            status_code = response[1]

            if status_code >= 400:
                error_count += 1
                ERROR_COUNT.inc()

        return response

    return wrapper


# ----------------------------
# DASHBOARD METRICS
# ----------------------------

def get_metrics():

    avg_latency = 0

    if response_times:
        avg_latency = sum(response_times) / len(response_times)

    uptime = 100

    if request_count > 0:
        uptime = (
            (request_count - error_count)
            / request_count
        ) * 100

    return {
        "requests": request_count,
        "errors": error_count,
        "avg_latency": round(avg_latency, 2),
        "uptime": round(uptime, 2)
    }