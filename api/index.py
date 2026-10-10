from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 210.43,
    "uptime_pct": 97.723,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 138.61,
    "uptime_pct": 98.71,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 197.11,
    "uptime_pct": 98.082,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 136.59,
    "uptime_pct": 97.65,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 159.72,
    "uptime_pct": 99.328,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 148.84,
    "uptime_pct": 99.384,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 124.82,
    "uptime_pct": 97.189,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 147.02,
    "uptime_pct": 98.877,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 225.77,
    "uptime_pct": 99.05,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 142.67,
    "uptime_pct": 99.203,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 124.02,
    "uptime_pct": 98.838,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 137.51,
    "uptime_pct": 98.387,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 185.88,
    "uptime_pct": 98.34,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 166.65,
    "uptime_pct": 98.1,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 153.3,
    "uptime_pct": 97.248,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 172.97,
    "uptime_pct": 98.216,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 163.8,
    "uptime_pct": 97.242,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 109.03,
    "uptime_pct": 97.191,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 140.94,
    "uptime_pct": 98.307,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 126.07,
    "uptime_pct": 97.841,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 184.49,
    "uptime_pct": 97.482,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 177.44,
    "uptime_pct": 97.176,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 130.67,
    "uptime_pct": 99.045,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 206.86,
    "uptime_pct": 99.386,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 224.03,
    "uptime_pct": 97.528,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 104.39,
    "uptime_pct": 97.256,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 157.72,
    "uptime_pct": 97.919,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 159.77,
    "uptime_pct": 99.28,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 128.25,
    "uptime_pct": 97.575,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 143.5,
    "uptime_pct": 98.145,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 117.25,
    "uptime_pct": 98.029,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 192.14,
    "uptime_pct": 97.539,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 197.73,
    "uptime_pct": 99.242,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 143.81,
    "uptime_pct": 99.035,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 213.53,
    "uptime_pct": 97.585,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 183.95,
    "uptime_pct": 97.983,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
