import React, {Fragment, Select, useState} from 'react';
import {Link, Redirect} from 'react-router-dom';
import {useSelector, useDispatch} from 'react-redux';
import * as action from '../store/action/auth';
import {errorMessage} from '../store/action/index';
import BackService from '../store/RequestBack';
import { List } from 'antd/lib/form/Form';
import axios from 'axios'
import { map } from 'jquery';
import Axios from 'axios';

const solicitudBack = new BackService();


let listDoctores = []
let vard = []


const submitSub =async()=> {  
          
    solicitudBack.getDoctores()
    .then(res =>{
        listDoctores.push(res)
        
        localStorage.setItem('Doctores',JSON.stringify(listDoctores))
        //va = JSON.parse(localStorage.getItem('Doctores'))
        
        
    })


}

submitSub()
const RegisterPatient =()=> {
    
    const doctore = JSON.parse(localStorage.getItem('Doctores'))
    const error = useSelector(state => state.error)    
    const loading = useSelector(state => state.loading)    
    const token = useSelector(state => state.token)
    const dispatch = useDispatch() 
        if (error){
        console.log(error.message)
        dispatch(errorMessage(error.message, error.status))
    }
    const handleSubmit = (e) =>{
        e.preventDefault()
        const userName = e.target.elements.username.value;
        const email = e.target.elements.email.value;
        const password1 = e.target.elements.password1.value;
        const password2 = e.target.elements.password2.value;
        const first_name = e.target.elements.first_name.value;  
        const last_name = e.target.elements.last_name.value;
        const Doctor = e.target.elements.Doctor.value;
        dispatch(action.authSignUpPatient(userName, email, password1, password2, first_name, last_name, Doctor))
    }
    if (token!==null){
        return <Redirect to="/profile"/>
    }
    console.log(doctore)
    return ( 
        <Fragment>
        <h1>Register Form</h1>
        {
                loading ? 
                <div className="row">
                    <div className="col-5"></div>
                    <div className="col-2"><div className="loader"></div></div>
                    <div className="col-5"></div>
                </div>
                :
        <form onSubmit={handleSubmit}  className="mb-5">
                <div className="form-group">
                    <label htmlFor="username">Username:</label>
                    <input type="text" className="form-control" name="username" required/>
                </div>
                <div className="form-group">
                    <label htmlFor="email">Email:</label>
                    <input type="email" className="form-control" name="email" required/>
                </div>
                <div className="form-group">
                    <label htmlFor="password1">Password:</label>
                    <input type="password" className="form-control" name="password1" required/>
                </div>
                <div className="form-group">
                    <label htmlFor="password2">Confirm Password:</label>
                    <input type="password" className="form-control" name="password2" required/>
                </div>
                <div className="form-group">
                    <label htmlFor="first_name">Nombres:</label>
                    <input type="text" className="form-control" name="first_name" required/>
                </div>
                <div className="form-group">
                    <label htmlFor="last_name">Apellidos:</label>
                    <input type="text" className="form-control" name="last_name" required/>
                </div>

                <div className="form-group">
                    <label htmlFor="last_name">Doctor asignado:</label>
                    <select className="form-control" name="Doctor" required>
                        {doctore[0].map((elements) => (
                            <option value={elements.id} key={elements.id}>{elements.first_name+' '+elements.last_name}</option>
                        ))}
                    </select>
                </div>
                <button type="submit" className="mb-5 btn btn-success">Submit</button>
            </form>
        }
        </Fragment>
     );
}
 
export default RegisterPatient;