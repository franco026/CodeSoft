import { createStore, applyMiddleware, combineReducers, compose } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import reducer from './reduce/auth';

const middleware = [thunk];
const initialState = {
    token: null,
    error: null,
    loading: false,
    authenticate: null,
    usuario: null
}

function saveToLocalStorage(state) {
    try {
        const serializedState = JSON.stringify(state)
        localStorage.setItem('state', serializedState)
    } catch (e) {
        console.log(e)
    }
}

function loadFromLocalStorage() {
    try {

        const serializedState = localStorage.getItem('state')
        if (serializedState === null) return initialState
        return JSON.parse(serializedState)
    } catch (e) {
        console.log(e)
        return initialState
    }
}

const persistedState = loadFromLocalStorage()



const composeEnhances = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const store = createStore(reducer, composeEnhances(
    applyMiddleware(thunk)
));



store.subscribe(() => saveToLocalStorage(store.getState()))
export default store;