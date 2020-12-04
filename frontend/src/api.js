import Cookies from "js-cookie";
import axios from "axios";

export default function (uri, method, payload) {
	// const base_url = 'http://localhost:8000/api'
	// depends on .env files
	const base_url = process.env.REACT_APP_PUBLIC_API_URL  || 'api';
	// const urlMapping={
	//     services: "http://localhost:8000/api/services/",
	//     appointments: "http://localhost:8000/api/appointments/",
	//     profesionals: "http://localhost:8000/api/profesionals/"
	// }
	return axios({
		method: method,
		headers: { Authorization: `Token ${Cookies.get("access_token")}` },
		url: `${base_url}/${uri}`,
		data: payload,
	}).then((response) => {
		// returning the data here allows the caller to get it through another .then(...) aeasñdañdlkañsdl
		// console.log(response.data)
		return response.data;
	});
}
