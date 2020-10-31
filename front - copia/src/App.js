import React,{Component} from 'react';
import { BrowserRouter as Router} from 'react-router-dom';
import BaseRouter from './Routes';
import 'antd/dist/antd.css';

import Home from './container/Home';

class App extends Component {
        render() {
                return (
                        <div>
                                <Router>
                                        <BaseRouter />
                                </Router>
                        </div>
                );
        }
}

export default App;

