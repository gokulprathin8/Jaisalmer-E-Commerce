import axios from "axios";

export default axios.create({
  baseURL : process.env.RESTURL_SERVICE,
});