"""MCP stdio server for Needleman-Wunsch Global Alignment."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import NeedlemanWunschAligner

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "needleman_wunsch_align",
                        "description": "Perform end-to-end global sequence alignment via Needleman-Wunsch DP",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "seq1": {"type": "string"},
                                "seq2": {"type": "string"},
                                "match_score": {"type": "integer", "default": 1},
                                "mismatch_penalty": {"type": "integer", "default": -1},
                                "gap_penalty": {"type": "integer", "default": -1}
                            },
                            "required": ["seq1", "seq2"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "needleman_wunsch_align":
            s1 = args.get("seq1", "")
            s2 = args.get("seq2", "")
            m = int(args.get("match_score", 1))
            mm = int(args.get("mismatch_penalty", -1))
            g = int(args.get("gap_penalty", -1))
            res = NeedlemanWunschAligner.align(s1, s2, m, mm, g)
            return {"jsonrpc": "2.0", "id": req_id, "result": res}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
