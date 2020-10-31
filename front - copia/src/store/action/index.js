import * as actionType from '../../store/action/types';
import axios from 'axios';

export const errorMessage= (msg, status)=>{
    return{
        type:actionType.ERROR_LEAD,
        payload: {msg,status}
    }
}