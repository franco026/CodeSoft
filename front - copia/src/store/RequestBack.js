import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default class BackService {

    constructor() { }
    //PQRS
    async getDoctores() {
        const url = `${API_URL}/ListDoctor/`;
        return axios.get(url)
            .then(res => res.data)
            .catch(error => console.log(error));
    }

    
}