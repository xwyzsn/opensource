import json
import os
from collections import defaultdict
from typing import Tuple, Dict, List
from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
user_repo = json.loads(open("user_repo.json").read())

@app.get("/get_all_repo_owner")
def get_all_repo_owner():
    return os.listdir("./repos/")


@app.get("/get_all_repo_of_owner/{company}")
def get_all_repo_of_owner(company: str):
    return os.listdir(f"./repos/{company}")


@app.get("/get_details_of_repo/{company}/{repo}")
def get_details_of_repo(company: str, repo: str):
    return os.listdir(f"./repos/{company}/{repo}")

@app.get("/get_details_of_repo/{company}/{repo}/{file}")
def get_details_file_of_repo(company: str, repo: str,file:str):
    return json.loads(open(f"./repos/{company}/{repo}/{file}").read())

@app.get("/get_all_info_of_repo/{company}/{repo}")
def get_all_info_of_repo(company: str, repo: str):
    file_list = ["stars.json","technical_fork.json","activity_details.json","bus_factor_detail.json","active_dates_and_times.json"]
    repo = repo.removeprefix("repo:")
    out:Dict[str,Dict] = defaultdict(dict)
    for file in file_list:
        with open(f"./repos/{company}/{repo}/{file}") as f:
            res = json.loads(f.read())
            for key in res.keys():
                name = file.split('.')[0]
                out[key] = {**out[key],**{name:res[key]}}

    return out

@app.get("/get_user_repo_or/{repo}")
def get_user_repo_or(repo:str):
    repo = repo.lower()
    with open(f"labels.json", "r") as f:
        res:List[Dict[str,str]] = json.loads(f.read())
    out = []
    for item in res:
        name = item['n']
        item_type = item['t']
        open_rank = item['or']
        if item_type == 'r' and repo in name.lower():
            n = "repo:"+name.split('/')[-1]
            out.append({'n':n,'t':item_type,'or':open_rank})
    return out

@app.get("/get_all_user_repo_or")
def get_all_user_repo_or():
    with open(f"labels.json", "r") as f:
        res:List[Dict[str,str]] = json.loads(f.read())
    out = []
    nodes = set()
    links = []
    link_set = set()
    company = os.listdir("./repos/")
    category = set()
    for item in res:
        name = item['n']
        item_type = item['t']
        open_rank = item['or']
        owner = name.split('/')[0]
        if item_type == 'r' and owner in company:
            n = name
            links.append({'source':owner,'target':n})
            category.add(owner)
            nodes.add((owner,n,owner))
            # nodes.add(n)
    for node in nodes:
        if node[0] not in link_set:
            out.append({'name':node[0],'category':node[2]})
            link_set.add(node[0])
        if node[1] not in link_set:
            out.append({'name':node[1],'category':node[2]})
            link_set.add(node[1])
    cc = []
    for cate in category:
        cc.append({'name':cate})
    response = {'nodes':out,'links':links,'category':cc}
    return response


@app.get("/user_repo/{user}")
def get_user_repo(user:str):
    res = {}
    out = []
    repos = user_repo[user]
    for repo in repos:
        out.append({'name':repo,'category':'repo'})
    out.append({'name':user,'category':'user'})
    res['nodes'] = out
    res['links'] = [{'source':user,'target':repo} for repo in repos]
    res['category'] = [{'name':'user'},{'name':'repo'}]
    return res




if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True,workers=1)
