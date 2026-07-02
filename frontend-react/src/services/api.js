import axios from "axios";

const API = axios.create({
  baseURL: "https://darkpatternplatform.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});

export default API;