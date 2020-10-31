import axios from 'axios';
import * as actionType from '../action/types';
export const authStart = () =>{
    return {
        type:actionType.AUTH_START
    }
}  
export const authSuccess = (token) =>{
    return {
        type : actionType.AUTH_SUCCESS,
        token : token
    }
}  
export const authFail = ()=>{
    return {
        type:actionType.AUTH_FAIL,
    }
}
export const logout = () =>{
    localStorage.removeItem('token')
    localStorage.removeItem('expirationDate')
    localStorage.removeItem('userName')
    return {
        type:actionType.AUTH_LOGOUT
    }
}  
export const checkAuthTime = expirationTime =>{
    return dispatch=>{
        setTimeout(()=>{
            dispatch(logout())
        },expirationTime * 1000)
    }
}
export const authLogin = (username, password) =>{
    return dispatch => {
        dispatch(authStart());
        axios.post('http://localhost:8000/token-auth/',{
            headers: {
            'Content-Type': 'application/json'
          },
        username:username,
        password:password})
        .then(res=>{
            const token = res.data.token;
            const expirationDate = new Date(new Date().getTime()+3600 * 1000)
            localStorage.setItem('token',token)
            localStorage.setItem('expirationDate',expirationDate)
            dispatch(authSuccess(token))
            dispatch(checkAuthTime(3600))
            
        })
        .catch(err =>{
            dispatch(authFail())
            dispatch(errorMessage(err.response.data, err.response.status))
        })
    }
}
export const authSignUp = (username, email, password1, password2) =>{
    return dispatch => { 
        dispatch(authStart());
        let data = JSON.stringify({
            email:email,
            username:username,
            password:password1
        })
        axios.post('/accounts/users/',data,{
            headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(res=>{
            console.log(res)
            const token = res.data.token;
            const expirationDate = new Date(new Date().getTime()+3600 * 1000)
            localStorage.setItem('token',token)
            localStorage.setItem('expirationDate',expirationDate)
            localStorage.setItem('userName',res.data.username)
            dispatch(authSuccess(token))
            dispatch(checkAuthTime(3600))
        })
        .catch(err =>{
            dispatch(authFail())
            dispatch(errorMessage(err.response.data, err.response.status))
        })
    }
}
export const authCheckState = ()=>{
    return dispatch=>{      
        const token = localStorage.getItem('token')
        if (token === undefined){
            dispatch(logout())
        }
        else{
            const expirationDate = new Date(localStorage.getItem('expirationDate'))
            if (expirationDate<=new Date()){
                dispatch(logout())
            }
            else{
                dispatch(authSuccess(token))
                dispatch(checkAuthTime((expirationDate.getTime() - new Date().getTime()) /1000 ))
            }
        }
    }
}

export const errorMessage= (msg, status)=>{
    return{
        type:actionType.ERROR_LEAD,
        payload: {msg,status}
    }
}