import axios from "axios";

const fetcher = (endpoint: string) =>
  axios.get(`http://localhost:8000/${endpoint}`).then((res) => res.data);

export default fetcher;
