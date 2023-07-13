import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000",
})

export {api , axios}

export function setUserAllRepo(user){
    return api.get(`/get_user_repo_or/${user}`)
}