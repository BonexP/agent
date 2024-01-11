# Agent
simple an agent to fetch static files.


## config

create `config.yaml` in folder and:
```yaml
---
key:
  "abcacb"

items:
  sspaipod: "https://sspai.typlog.io/feed/audio.xml"
  smzdm: "https://www.smzdm.com/"

```
the `key` defined here will be overwrited in `.env`.
`items` is pre-defined items which you can get quickly by another route(see below).
## usage
```bash
flask run
```
and then
if you have defined something in `config.yaml`, you can just:
`get 127.0.0.1:5000/pre?id=DEFINED_ID&key=YOURKEY`

otherwise,use this:
`get 127.0.0.1:5000/check_args?item=URL_ENCODED_IN_BASE64key=YOURKEY`
