import axios from "axios";

const API = axios.create({
  baseURL: "https://darkpattern-api-zrwy.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});

export default API;