import React from 'react';
import { Link } from 'react-router-dom';

 

const home = () => (
    <div className='container'>
        <div className="jumbotron mt-5">
            <h1 className="display-4">Welcome to Auth System</h1>
            <p className="lead">This is a super cool authentication system with all kinds of functionalities.</p>
            <hr className="my-4" />
            <p>Go ahead and login!</p>
            <Link className="btn btn-primary btn-lg" to='/Login' role="button">Login</Link>
            <Link className="btn btn-primary btn-lg" to='/SingUp' role="button">SingUpDoctor</Link>
            <Link className="btn btn-primary btn-lg" to='/SingUpPatient' role="button">SingUpPatient</Link>
        </div>
    </div>
);

export default home;