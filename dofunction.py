import requests
import base64
preOrderList={
  "afm1": "https://anchor.fm/s/40837440/podcast/rss",
  "scp": "https://sub.sharecentre.online/sub"
}

def get_reverse_p(ss):
  target=preOrderList[ss]
  r=requests.get(target)
  return r.text
def make_request(path):
    r=requests.get(f"https://rsshub.app{path}")
    return r.text
def main(args):
    name = args.get("name", "stranger")
    print(args)
    path=args["http"]["path"]
    if args.get("item") in preOrderList.keys():# and (args.get("keys") in data.keys):
      item_url_encoded=preOrderList[args.get("item")]
      item_url=base64.b64decode(item_url_encoded)
      return {"body":item_url,"headers":{"content-type":"text/html; charset=UTF-8"}}

    if args.get("rss"):
       return {"body":make_request(path),"headers":{"Content-Type":"application/xml; charset=utf-8","provider":"revp5rss"}}
    
    if args.get("pod") in preOrderList.keys():
      podid=preOrderList[args.get("pod")]
      r=requests.get(podid)
      return {"body":r.text,"header":"content-type: application/rss+xml; charset=utf-8 "}
    greeting = "Hello " + name + "!"+f"your request path {path}"
    print(greeting)
    return {"body": greeting,"header":"content-type: text/html; charset=UTF-8"}

