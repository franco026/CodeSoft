import React, {Fragment} from 'react';
import {Link, Redirect} from 'react-router-dom';
import {useSelector, useDispatch} from 'react-redux';
import * as action from '../store/action/auth';
import {errorMessage} from '../store/action/index';

const Register = () => {
    const error = useSelector(state=> state.error)
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
        dispatch(action.authSignUpDoctor(userName, email, password1, password2, first_name, last_name))
    }
    if (token!==null){
        return <Redirect to="/profile"/>
    }
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
        <form onSubmit={handleSubmit} className="mb-5">
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
                <button type="submit" className="mb-5 btn btn-success">Submit</button>
            </form>
        }
        </Fragment>
     );
}
 
export default Register;