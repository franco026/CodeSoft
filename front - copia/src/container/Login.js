
import React ,{Fragment,useEffect}from 'react';
import {Link, Redirect} from 'react-router-dom';
import {useSelector, useDispatch} from 'react-redux';
import * as action from '../store/action/auth';
import reducer from '../store/reduce/auth';
const LoginUser = () => {    
    
    const token =  useSelector(state=> state.token)
    const dispatch = useDispatch() 

    const handleSubmit = (e) =>{
        e.preventDefault()
        const username = e.target.elements.username.value;
        const password = e.target.elements.password.value;
        dispatch(action.authLogin(username, password)) 
    }

    if (token!==null){
        return <Redirect to="/profile"/>
    }
    return ( 

         <Fragment>
             <h1>Login Form</h1>
            <form className="mb-5" onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="username">Username:</label>
                    <input className="form-control" name="username" required/>
                </div>
                <div className="form-group">
                    <label htmlFor="title">Password:</label>
                    <input type="password" className="form-control" name="password" required/>
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
        </Fragment>
     );
}
 
export default LoginUser;
