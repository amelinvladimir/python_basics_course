import json

with open("big.json", "r", encoding="utf-8") as f:
    config = json.load(f)

warning = config["debug_info"]["warnings"][0]
print(warning)

warning = None
if config.get("debug_info") and isinstance(config["debug_info"], dict):
    debug_info = config["debug_info"]
    if debug_info.get("warnings") and isinstance(debug_info["warnings"], list) and len(debug_info["warnings"]) > 0:
        warning = debug_info["warnings"][0]
print(warning)

warning = None
warning = (
    config.get("debug_info")
    and isinstance(config["debug_info"], dict)
    and config.get("debug_info").get("warnings")
    and isinstance(config["debug_info"]["warnings"], list)
    and len(config["debug_info"]["warnings"]) > 0 
    and config["debug_info"]["warnings"][0]
) or None
print(warning)

warning = None
try:
    warning = config["debug_info"]["warnings"][0]
except (KeyError, IndexError, TypeError):
    warning = None
print(warning)