import sys
import json
from client import NeedlemanWunschAligner

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "align":
        aligner = NeedlemanWunschAligner()
        return aligner.align(params.get("seq1", ""), params.get("seq2", ""))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
